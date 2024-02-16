import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json
from google.cloud import storage

class JsonTransformation(beam.DoFn):
    def process(self, element):
        file_name, json_content = element
        data = json.loads(json_content)
        # Realizar transformaciones en los datos
        # Eliminar columnas no deseadas
        if 'address' in data:
            del data['address']
        if 'description' in data:
            del data['description']
        if 'price' in data:
            del data['price']
        if 'hours' in data:
            del data['hours']
        if 'MISC' in data:
            del data['MISC']
        if 'state' in data:
            del data['state']
        if 'relative_results' in data:
            del data['relative_results']
        # Expandir contenido de la columna 'category'
        categories = data.get('category', [])
        for category in categories:
            # Filtrar filas que contienen 'hotel'
            if 'hotel' in category.lower():
                new_data = data.copy()
                new_data['category'] = category
                yield new_data

# Función para leer archivos JSON desde un bucket de GCS
def read_json_from_gcs(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_string()
    return content.decode('utf-8')

bucket_name = 'hw-b1'  
output_folder = 'meta-result/'

with beam.Pipeline(options=PipelineOptions()) as p:
    for i in range(1, 12):  # Iterar sobre los 11 archivos
        input_file = f'gs://{bucket_name}/meta-data/sitios/{i}.json'
        output_file = f'gs://{bucket_name}/{output_folder}{i}.parquet'
        
        (p | f'Read JSON {i}' >> beam.Create([read_json_from_gcs(bucket_name, f'{i}.json')])
           | f'Transform JSON {i}' >> beam.ParDo(JsonTransformation())
           | f'Remove Duplicates {i}' >> beam.Distinct()
           | f'Write Parquet {i}' >> beam.io.parquetio.WriteToParquet(output_file)
        )
