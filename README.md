![wink](imagenes/HotelWiseLogo.png)

# Análisis Exploratorio de Datos (EDA)

En este proyecto de análisis exploratorio de datos, exploramos un conjunto de datos para comprender su estructura, características y patrones.

## Descripción del Conjunto de Datos

El conjunto de datos utilizado en este análisis contiene información sobre comentarios que los usuarios de google dejan sobre los establecimientos a los que la app de Google_Maps evidencia que estuvieron, si estos usuarios dejan sus calificaciones y comentarios, tambien existe una metadata la cual contiene toda la informacion acerca de los establecimientos, la cual nos fue util para identificar a que establecimiento hacia referencia el usuario.

## Tecnologias Utilizadas

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
- [![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
- [![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
- [![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
- [![NLTK](https://img.shields.io/badge/NLTK-333?style=for-the-badge&logo=nltk&logoColor=white)](https://www.nltk.org/)


## Proceso de Análisis

El proceso de análisis se realizó en varios pasos:

1. **Carga de Datos**: Cargamos el conjunto de datos utilizando pandas.
2. **Exploración Inicial**: Realizamos una exploración inicial del conjunto de datos para comprender su estructura y características.
3. **Limpieza de Datos**: Llevamos a cabo tareas de limpieza de datos, incluyendo el manejo de valores faltantes, duplicados y valores atípicos.
4. **Análisis Estadístico**: Realizamos análisis estadísticos descriptivos para resumir las características del conjunto de datos.
5. **Visualización de Datos**: Utilizamos gráficos y visualizaciones para explorar las relaciones entre variables y descubrir patrones en los datos.
6. **Conclusiones**: Resumimos las principales conclusiones y hallazgos del análisis exploratorio de datos.

## Archivos

- [`EDA_preliminar_reviws.ipynb`](EDA_preliminar/EDA_preliminar_reviws.ipynb)
: Jupyter Notebook que contiene el código y la narrativa del análisis exploratorio de datos para los comentarios de los estados.
- [`EDA_preliminar_metadata.ipynb`](EDA_preliminar/EDA_preliminar_metadata.ipynb)
: Jupyter Notebook que contiene el código y la narrativa del análisis exploratorio de datos para los datos de los hotles.
- [`id_hoteles.csv`](CSV/id_hoteles.csv)
: Archivo CSV que contiene informacion sobre los id de los hoteles para poder hacer un filtro en las reviws y asi obtener unicamente los comentarios que necesito para el proyecto.
- [`hoteles.csv`](CSV/hoteles.csv)
: Archivo CSV que contiene informacion recolectada de la metadata filtrando por hoteles.
- [`hoteles_Alabama1.csv`](CSV/hoteles_Alabama1.csv)
: Archivo CSV que contiene informacion recolectada de los reviw de Alabama para un primer avistamiento de los datos.

