# Presentación del Proyecto: Plataforma de Recomendación de Hoteles

## Índice
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#Descripcion General">Descripción General</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Tecnologias Utilizadas">Tecnologias utilizadas</a></li>
    <li><a href="#Ingenieria de Datos">Ingenieria de Datos</a></li>
    <li><a href="#Analisis de Datos">Analisis de Datos</a></li>
    <li><a href="#Sistema de Recomendacion">Sistema de Recomendacion</a></li>
  </ol>
</details>

## Descripción General

Bienvenidos, inversionistas. Me complace presentarles nuestro proyecto de una plataforma web innovadora de recomendación de hoteles. Esta aplicación está diseñada para ofrecer a los usuarios experiencias de viaje personalizadas y convenientes, ayudándoles a encontrar los hoteles que mejor se adapten a sus necesidades y preferencias.

## Objetivo

La tecnologia avanza a pasos agigantados, y por ello el aprovechamiento de los datos en cuanto a lo que busca el cliente final termina siendo lo mas importante a la hora de poder conectar con el, debido a esto vimos una oportunidad de mejorar 


## Tecnologias Utilizadas

### 1. Google Cloud Platform (GCP) 
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://console.cloud.google.com/welcome)

- **Almacenamiento:** Utilizamos Cloud Storage para almacenar los datos en bruto y los resultados intermedios de nuestros procesos.
- **Orquestación:** Apache Airflow es nuestro orquestador principal para gestionar y programar los flujos de trabajo de la plataforma.
- **Análisis:** Utilizamos BigQuery para análisis de datos y generación de informes.

### 2. Firebase (Firestore) 
[![Firebase](https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/docs/firestore?hl=es-419)

- **Base de Datos:** Firestore actúa como nuestra base de datos principal, proporcionando un almacenamiento escalable y en tiempo real para la gestión de datos de usuarios y preferencias.

### 3. Locker para Análisis
[![Locker](https://img.shields.io/badge/Locker-333333?style=for-the-badge&logo=lock&logoColor=white)](https://cloud.google.com/looker?hl=es)

- **Herramienta de Análisis:** Hemos implementado Locker para el análisis de datos. Esta herramienta nos permite explorar y visualizar datos de manera eficiente, facilitando la toma de decisiones basada en datos.

## Ingeniería de Datos

Para garantizar la integridad y calidad de los datos, seguimos un enfoque robusto en ingeniería de datos:

1. **Almacenamiento en GCP:**

    [![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://console.cloud.google.com/welcome)
   
   - Los datos en bruto se almacenan en Cloud Storage, permitiendo una fácil escalabilidad y acceso.

2. **Procesamiento con Airflow:**

    [![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
   
   - Utilizamos Apache Airflow para orquestar y automatizar los flujos de trabajo de limpieza y transformación de datos.

3. **Firestore como Base de Datos:**

    [![Firestore](https://img.shields.io/badge/Cloud_Firestore-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/docs/firestore?hl=es-419)
   
   - Los datos limpios y procesados se almacenan eficientemente en Firestore para su posterior uso en la plataforma.

## Analisis de Datos

Nuestro enfoque de análisis se centra en obtener información valiosa y proporcionar insights para la toma de decisiones:

1. **Locker:**

    [![Locker](https://img.shields.io/badge/Locker-333333?style=for-the-badge&logo=lock&logoColor=withe)](https://cloud.google.com/looker?hl=es)
   
   - Utilizamos Locker para explorar visualmente datos y descubrir patrones significativos.

2. **BigQuery:**

    [![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/bigquery?utm_source=pmax&utm_medium=pmax&utm_campaign=FY24-Q1-usecasesproduct_dr&utm_content=latampaidmedia_LATAM_cloud-pmax_dr_image_gcp_gdn_usecasesproduct_BigQuery2_OPID-3878356_1707800&utmterm-&hl=es&gad_source=1&gclid=CjwKCAiA8YyuBhBSEiwA5R3-EwgthdMQs5bpqpE8wNeNWHFCNDLhrS2GoprtyEVvjtiXSO7ePt0ugRoCfu8QAvD_BwE)
   
   - Realizamos análisis avanzados en BigQuery para obtener información sobre tendencias de usuarios, demanda de hoteles y otros aspectos clave.

## Sistema de Recomendacion

Nuestra plataforma implementa un sistema de recomendación basado en la similitud del coseno para proporcionar sugerencias personalizadas:

1. **Tecnología de GCP:**

    [![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/recommender/docs/overview?hl=es-419)
   
   - Utilizamos las herramientas de aprendizaje automático de GCP para implementar un algoritmo de similitud del coseno.

2. **Datos en Firestore:**
   
   [![Firestore](https://img.shields.io/badge/Cloud_Firestore-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/docs/firestore?hl=es-419)

   - El sistema de recomendación utiliza los datos almacenados en Firestore, incluidas las preferencias y comportamientos pasados de los usuarios.

3. **Personalización:**
   
   - El sistema se adapta continuamente a los cambios en las preferencias del usuario, brindando recomendaciones más precisas con el tiempo.

En resumen, nuestra plataforma ofrece una experiencia de recomendación de hoteles única y personalizada, respaldada por tecnologías sólidas y un enfoque integral de ingeniería y análisis de datos. Estamos emocionados por el potencial de esta propuesta y esperamos colaborar con ustedes para llevar esta visión a la realidad. ¡Gracias!