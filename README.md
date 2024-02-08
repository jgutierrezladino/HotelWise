<div style="text-align: center;">
    <img src="_src/logo/HotelWiseLogo.png" alt="wink">
</div>

# Proyecto de Data Analytics: HotelWise

---

---

# **Introducción**

Nuestro servicio 'HotelWise' se destaca por brindar una experiencia de usuario excepcional y de primer nivel, superando la mera comparación de opciones de alojamiento. A diferencia de plataformas similares, nos especializamos en ofrecer una cuidadosa selección de hoteles de alta calidad, respaldados por reseñas auténticas y detalladas. Además, contamos con información confiable sobre zonas seguras para garantizar la tranquilidad de nuestros usuarios.

---

# **Objetivo Principal**

Presentar una plataforma web que realice recomendaciones de hoteles, mediante machine learning utilizando las comodidades y zona geografica preferidas por el usuario, donde el tiempo de muestra de la recomendación sea menor a 30 segundos, utilizando herramientas en la nube con un tiempo de implementación no mayor a 6 semanas.

---

## **Objetivos Específicos**

Crear dos bases de datos una para filtrar las zonas utilizando Cloud SQL y para el modelo de machine learning con Firestore (Firebase)

Crear Analisis de datos con looker para medir rendimiento de la plataforma y mostrar indicadores clave para convencer al usuario de la recomendación del hotel

Crear un modelo de recomendación utilizando Tensorflow para la generación de valor obtenido de los datos al usuario

Crear una plataforma web intuitiva y eficiente al momento de realizar recomendaciones al usuario.

---

## **KPI's plataforma**

Tiempo de obtención de datos de Cloud SQL

Tiempo de obtención de datos de Firestore

Tiempo de proceso de ML

---

## **KPI's Usuario**

Porcentaje de similitud de amenidades del hotel con relacion a las amenidades preferidas del usuario

Distancia del punto o zona de interes del usuario

Porcentaje de reseñas positivas sobre las amenidades del hotel

Indice de seguridad de la zona del hotel

demanda por meses o epoca

---

## Stack Tecnológico

GCP: Cloud Storage, Composer, Cloud SQL, Looker, Tensorflow.

Python: Polars, Pandas, Seaborn, Matplotlib, Django.

Firebase: Firestore, Hosting, Autenticación.

Java:

Github:

Marktext

---

## Alcance del proyecto

El proyecto parte con la base de datos ubicada en el pais de Estados Unidos, abarcara  de 51 Estados, donde se sentrará la atención principalmente en el rendimiento del tiempo de retorno de información y el valor otorgado por la analitica para el convencimiento del Usuario al momento de la elección del Hotel recomendado.

La ejecución de este constará de 6 semanas donde se utilizaran sprints para la divición de tareas a realizar y metas a cumplir, donde en el primer sprint semana 1 y 2 se definen los objetivos, metodologias, tecnologias, tareas y roles. La Semana 3 y 4 se realizará la extracción, disposición y analisis de datos; y por ultimo la semana 5 y 6 el desarrollo del sistema de recomendación mediante machine learning. En paralelo a las semanas 3, 4, 5 y 6 se llevara a cabo el diseño y pespliegue de la web.

El mismo será escalable gracias a que se implementará un flujo de extraccion y disposición de datos automatizado, por lo que permitirá en un futuro ir agregando paises junto con su divición política.

---

### *Integración de Tecnologías*

La integración de GCP y Firebase para una solución completa para el almacenamiento, procesamiento, análisis, visualización y recomendación de hotele. Esta combinación nos proporciona las herramientas necesarias para obtener información significativa a partir de nuestros datos, permitir a los ususarios tomar decisiones informadas.
