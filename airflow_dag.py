from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.providers.google.transfers.local_to_gcs import LocalFilesystemToGCSOperator
import polars as pl
from ptransform import eliminar_columnas, explode_columna, eliminar_duplicados, filtrar_por_categoria
import json
from airflow.models import Variable

# Obtener el valor de la variable 'project_id'
gcp_project_id = Variable.get('project_id')

# Obtener el valor de la variable 'bucket'
gcp_bucket = Variable.get('bucket')


# Configuración del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mi_dag',
    default_args=default_args,
    description='DAG para manipulación de datos en GCS con Polars',
    schedule_interval=timedelta(days=1),
)

# Tarea 1: Descargar archivo JSON desde GCS y cargar como DataFrame de Polars
def descargar_y_cargar_df(**kwargs):
    # Descargar archivo JSON
    download_gcs_task = GCSToLocalFilesystemOperator(
        task_id='download_gcs_file',
        bucket_name='your_gcs_bucket',
        object_name='your_json_file.json',
        filename='/tmp/input_file.json',
    )
    download_gcs_task.execute(context=kwargs)

    # Leer el archivo JSON y cargar como DataFrame de Polars
    with open('/tmp/input_file.json', 'r') as file:
        data = json.load(file)
    df = pl.DataFrame(data)

    return df

descargar_y_cargar_df_task = PythonOperator(
    task_id='descargar_y_cargar_df',
    python_callable=descargar_y_cargar_df,
    provide_context=True,
    dag=dag,
)

# Tarea 2: Realizar Transformaciones
def realizar_transformaciones(df: pl.DataFrame) -> pl.DataFrame:
    df_paso1 = eliminar_columnas(df)
    df_paso2 = explode_columna(df_paso1, 'category')
    df_paso3 = eliminar_duplicados(df_paso2, 'name')
    df_resultante = filtrar_por_categoria(df_paso3, 'category', 'hotel')

    return df_resultante

realizar_transformaciones_task = PythonOperator(
    task_id='realizar_transformaciones',
    python_callable=realizar_transformaciones,
    provide_context=True,
    dag=dag,
)

# Tarea 3: Subir archivo Parquet a GCS
def subir_df_a_gcs(df: pl.DataFrame, **kwargs):
    output_file_path = '/tmp/output_file.parquet'

    # Guardar el DataFrame resultante como archivo Parquet
    df.write_parquet(output_file_path)

    # Subir archivo Parquet a GCS
    upload_gcs_task = LocalFilesystemToGCSOperator(
        task_id='upload_gcs_file',
        src=output_file_path,
        dst='your_gcs_bucket/your_output_parquet_file.parquet',
        bucket_name='your_gcs_bucket',
    )
    upload_gcs_task.execute(context=kwargs)

subir_df_a_gcs_task = PythonOperator(
    task_id='subir_df_a_gcs',
    python_callable=subir_df_a_gcs,
    provide_context=True,
    dag=dag,
)

def insert_into_cloud_sql(**kwargs):
    # Recuperar el DataFrame de XCom
    df = kwargs['ti'].xcom_pull(key='my_dataframe')

    # Conectar a la base de datos de Cloud SQL
    db_user = 'YOUR_DB_USER'
    db_password = 'YOUR_DB_PASSWORD'
    db_name = 'YOUR_DB_NAME'
    db_socket_dir = '/cloudsql'
    cloud_sql_connection_name = 'YOUR_PROJECT_ID:YOUR_REGION:YOUR_INSTANCE_NAME'
    connection_string = f"mysql+mysqldb://{db_user}:{db_password}@/{db_name}?unix_socket={db_socket_dir}/{cloud_sql_connection_name}"

    # Crear una conexión a la base de datos
    engine = create_engine(connection_string)

    # Insertar el DataFrame en la tabla de la base de datos
    table_name = 'YOUR_TABLE_NAME'
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


# Configuración de dependencias entre tareas
descargar_y_cargar_df_task >> realizar_transformaciones_task >> subir_df_a_gcs_task
