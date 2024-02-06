# Proyecto de Machine Learning con AutoML de Google en HotelWise

Este es un proyecto de Machine Learning que utiliza AutoML de Google para entrenar y desplegar modelos de aprendizaje automático.

## Descripción del Proyecto

El proyecto tiene como objetivo desarrollar modelos de aprendizaje automático utilizando AutoML de Google utilizando las bases de datos de Google y Yelp para hacer recomendaciones de hoteles.

## Flujo de Trabajo

Diagrama de Gantt
<p align="center">
    <img src="HotelWiseML/screenshots/Gantt_Proyecto_Grupal_HenryDS.png">
</p>

## Stack Tecnológico

- **Google Cloud Platform (GCP)**:
  - Utilizaremos Google Cloud Platform para acceder a los servicios de AutoML y alojar nuestro proyecto.

- **AutoML de Google**:
  - Utilizaremos AutoML de Google para entrenar y desplegar nuestros modelos de aprendizaje automático. 
 
  Dentro de esta plataforma podremos utilizar las siguientes funciones y bibliotecas para implementar los modelos de recomendación:
    - BigQuery ML:
        BigQuery ML es una función dentro de Google BigQuery que permite a los usuarios crear y ejecutar modelos de aprendizaje automático directamente dentro del almacén de datos en la nube de BigQuery. Permite a los analistas y científicos de datos construir y desplegar modelos de machine learning usando SQL estándar, sin necesidad de mover datos a otro lugar. BigQuery ML admite varios tipos de modelos, como modelos de regresión, clasificación y clustering, y es adecuado para problemas de predicción y análisis de datos a gran escala.
    - TensorFlow Recommenders:
        TensorFlow Recommenders es una biblioteca de TensorFlow diseñada específicamente para construir y desplegar sistemas de recomendación utilizando modelos de aprendizaje profundo. Proporciona una variedad de algoritmos y herramientas que simplifican el proceso de construcción y entrenamiento de modelos de recomendación personalizados. TensorFlow Recommenders es especialmente útil para proyectos que requieren modelos avanzados de recomendación, como sistemas de recomendación de productos en línea, recomendaciones de contenido y sistemas de filtrado colaborativo.
    - AI Platform de Google Cloud:
        Google Cloud AI Platform es un servicio integral de Google Cloud diseñado para ayudar a las organizaciones a construir, entrenar, implementar y administrar modelos de machine learning a escala. Ofrece una variedad de servicios y herramientas que facilitan el desarrollo de modelos de machine learning, incluyendo TensorFlow, scikit-learn y otros frameworks populares. AI Platform proporciona capacidades de procesamiento escalable, administración de recursos, monitoreo de modelos y herramientas de colaboración para equipos de científicos de datos y desarrolladores de machine learning.
    - Cloud Functions:
        Google Cloud Functions es un servicio de computación sin servidor que permite a los desarrolladores ejecutar código en respuesta a eventos en la nube sin necesidad de aprovisionar o administrar servidores. Permite a los desarrolladores crear funciones pequeñas y modulares que se ejecutan de forma independiente en la nube, escalando automáticamente según la demanda. Cloud Functions es adecuado para implementar lógica empresarial, procesamiento de eventos, integraciones de sistemas y tareas de automatización en la nube de Google.

  Los modelos que pueden implementrse serán:

    - Vecinos más cercanos (Nearest Neighbors):
        Este es un enfoque simple que recomienda elementos similares a los que un usuario ha interactuado anteriormente. Se basa en encontrar elementos similares en función de la distancia entre ellos en un espacio de características.
    - Filtro colaborativo (Collaborative Filtering):
        Este enfoque recomienda elementos basados en la información de preferencias de otros usuarios. Puede ser basado en usuario (User-Based Collaborative Filtering) o basado en elemento (Item-Based Collaborative Filtering).
    - Modelos de factorización matricial (Matrix Factorization Models):
        Estos modelos descomponen la matriz de interacciones usuario-elemento en matrices de características latentes para usuarios y elementos. Algunos ejemplos incluyen SVD (Descomposición de Valor Singular), Factorización QR, y Factorización de Matriz No Negativa (NMF).
    - Modelos de factorización profunda (Deep Factorization Models):
        Estos modelos utilizan redes neuronales profundas para aprender representaciones latentes de usuarios y elementos, lo que puede mejorar la calidad de las recomendaciones. Ejemplos incluyen Autoencoders y Redes Neuronales Convolucionales (CNN) para recomendaciones de imágenes.
    - Modelos de contenido (Content-Based Models):
        Estos modelos recomiendan elementos similares a los que un usuario ha interactuado anteriormente en función de características de los elementos, como metadatos o atributos. Utilizan técnicas de aprendizaje automático para calcular la similitud entre elementos.
    - Modelos de aprendizaje por refuerzo (Reinforcement Learning Models):
        Estos modelos recomiendan elementos basados en interacciones de usuario en tiempo real y el objetivo de maximizar una recompensa a largo plazo. Pueden ser útiles en entornos donde las interacciones de los usuarios tienen un impacto dinámico en las recomendaciones.

- **Python**:
  - Utilizaremos Python como lenguaje de programación principal para desarrollar y ejecutar nuestro código.

- **Bibliotecas de Python**:
  - Las Bibliotecas de aprendizaje automático serán utilizadas según sea necesario para el desarrollo de modelos que se eligirán para trabajar con AutoML.

- **Entorno de Desarrollo**:
  - Visual Studio Code para escribir y ejecutar nuestro código Python.

- **Git y GitHub**:
  - Utilizaremos Git y GitHub para el control de versiones del código y la colaboración en equipo.

## Requisitos de Instalación

- Instalar Python: [Python.org](https://www.python.org/downloads/)
- Configurar Google Cloud Platform: [Google Cloud Platform](https://cloud.google.com/)
- Modelos a instalar...

## Instalación

Asegúrate de tener Python instalado. Recomiendo usar un entorno virtual para instalar las dependencias del proyecto.

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual para trabajar 
3. Instala las dependencias necesarias utilizando el gestor de paquetes de tu elección (por ejemplo, npm o pip).

### Procedimiento

```bash
git clone https://github.com/jgutierrezladino/HotelWise/tree/HotelWiseML

pip install -r requirements.txt

...

```
## Contribución

¡Estamos abiertos a contribuciones! Si tienes ideas de mejora, problemas que reportar o características nuevas que te gustaría añadir, no dudes en abrir una solicitud de extracción o un problema en este repositorio.

## Créditos

- Desarrollado por (Equipo).
- Logotipo diseñado por (Diseñador).

## Licencia

Este proyecto está bajo las Licencias:

- [Licencia GPL 3.0](LICENSE-GPL).
- [Licencia MIT](LICENSE-MIT).
- [Licencia Apache 2.0](LICENSE-APACHE).

## Contacto

Si tienes alguna pregunta, comentario o problema con la página web de HotReviews, no dudes en ponerte en contacto con nosotros en [mdallanegra@icloud.com](mailto:mdallanegra@icloud.com).

## Enlaces adicionales

- [Documentación completa del proyecto](/HotelWiseML)
- [Repositorio de código fuente](https://github.com/jgutierrezladino/HotelWise/tree/HotelWiseML)
- [Sitio web en vivo](https://www.soyhenry.com)