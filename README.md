# Presentación del Proyecto: Plataforma de Recomendación de Hoteles

## Descripción General

Bienvenidos, inversionistas. Me complace presentarles nuestro proyecto de una plataforma web innovadora de recomendación de hoteles. Esta aplicación está diseñada para ofrecer a los usuarios experiencias de viaje personalizadas y convenientes, ayudándoles a encontrar los hoteles que mejor se adapten a sus necesidades y preferencias.

## Tecnologías Utilizadas

### 1. Google Cloud Platform (GCP)

- **Almacenamiento:** Utilizamos Cloud Storage para almacenar los datos en bruto y los resultados intermedios de nuestros procesos.
- **Orquestación:** Apache Airflow es nuestro orquestador principal para gestionar y programar los flujos de trabajo de la plataforma.
- **Análisis:** Utilizamos BigQuery para análisis de datos y generación de informes.

### 2. Firebase (Firestore)

- **Base de Datos:** Firestore actúa como nuestra base de datos principal, proporcionando un almacenamiento escalable y en tiempo real para la gestión de datos de usuarios y preferencias.

### 3. Locker para Análisis

- **Herramienta de Análisis:** Hemos implementado Locker para el análisis de datos. Esta herramienta nos permite explorar y visualizar datos de manera eficiente, facilitando la toma de decisiones basada en datos.

## Ingeniería de Datos

Para garantizar la integridad y calidad de los datos, seguimos un enfoque robusto en ingeniería de datos:

1. **Almacenamiento en GCP:**
   
   - Los datos en bruto se almacenan en Cloud Storage, permitiendo una fácil escalabilidad y acceso.

2. **Procesamiento con Airflow:**
   
   - Utilizamos Apache Airflow para orquestar y automatizar los flujos de trabajo de limpieza y transformación de datos.

3. **Firestore como Base de Datos:**
   
   - Los datos limpios y procesados se almacenan eficientemente en Firestore para su posterior uso en la plataforma.

## Análisis de Datos

Nuestro enfoque de análisis se centra en obtener información valiosa y proporcionar insights para la toma de decisiones:

1. **Locker:**
   
   - Utilizamos Locker para explorar visualmente datos y descubrir patrones significativos.

2. **BigQuery:**
   
   - Realizamos análisis avanzados en BigQuery para obtener información sobre tendencias de usuarios, demanda de hoteles y otros aspectos clave.

## Sistema de Recomendación

Nuestra plataforma implementa un sistema de recomendación basado en la similitud del coseno para proporcionar sugerencias personalizadas:

1. **Tecnología de GCP:**
   
   - Utilizamos las herramientas de aprendizaje automático de GCP para implementar un algoritmo de similitud del coseno.

2. **Datos en Firestore:**
   
   - El sistema de recomendación utiliza los datos almacenados en Firestore, incluidas las preferencias y comportamientos pasados de los usuarios.

3. **Personalización:**
   
   - El sistema se adapta continuamente a los cambios en las preferencias del usuario, brindando recomendaciones más precisas con el tiempo.

En resumen, nuestra plataforma ofrece una experiencia de recomendación de hoteles única y personalizada, respaldada por tecnologías sólidas y un enfoque integral de ingeniería y análisis de datos. Estamos emocionados por el potencial de esta propuesta y esperamos colaborar con ustedes para llevar esta visión a la realidad. ¡Gracias!
