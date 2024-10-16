## PI_1-MLOps Juegos Steam - Modelo de recomendación

Repositorio correspondiente al primer proyecto individual de la cohorte 25 de data science en HENRY

### Descripción del Proyecto:

Este proyecto tiene como objetivo simular un entorno de trabajo real como ingenieros de datos, realizando trabajos para la plataforma de juegos Steam. Se debe desarrollar un `Producto Mínimo Viable (MVP)`. Este MVP incluirá una `API` implementada, junto con un modelo de `Machine Learning` que realizará un análisis de sentimientos basado en los comentarios de los usuarios y proporcionará un sistema de recomendación de videojuegos para la plataforma.

### Datos:

El proyecto se basa en tres archivos de tipo JSON:

+ **output_steam_games.json**: Contiene información detallada sobre los juegos, incluyendo nombre, desarrollador, género y etiquetas.

+ **australian_users_items.json**: Proporciona información sobre los juegos utilizados por los usuarios y la cantidad de tiempo que cada usuario ha dedicado a un juego.

+ **australian_users_reviews.json**: Contiene los comentarios de los usuarios sobre los juegos, así como sus recomendaciones y la fecha de los mismos.


### Tareas desarrolladas:

#### ETL (Extracción, Transformación y Carga)


En esta etapa del proyecto, se procedió a la extracción de los datos de los dataframes iniciales con el objetivo de familiarizarse con su contenido e iniciar el proceso de depuración. Siguiendo las pautas establecidas en el enunciado, se eliminaron todos aquellos elementos que pudieran dificultar la comprensión e interpretación de los datos, con la finalidad de alcanzar los objetivos planteados.

Tras culminar el proceso de limpieza de datos, se construyeron los conjuntos de datos necesarios para la etapa subsiguiente, optimizándolos mediante el formato parquet.

#### EDA (Análisis Exploratorio de Datos)

Durante esta etapa del proyecto, se llevó a cabo el análisis de los tres conjuntos de datos después del proceso ETL, con el objetivo de lograr una visualización más clara de cada variable categórica y numérica.


#### Creación de funciones

En esta fase del proyecto, después de depurar la información, se seleccionaron los conjuntos de datos necesarios para abordar cada función específica. Este enfoque se llevó a cabo con el objetivo de lograr una optimización significativa y mejorar los tiempos computacionales asociados a cada tarea.

Las funciones creadas son las siguientes: 

* **`UserForGenre`**: Esta función recibe un género y devuelve el usuario con mayor tiempo de juego en un diccionario donde la clave es el año y el valor la acumulación de tiempo de juego para cada uno.

* **`Developer`**: Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. <b

#### Modelado Machine Learning

En esta etapa del proyecto, se utilizan los conjuntos de datos obtenidos durante las fases de ETL y EDA. Se centra particularmente en el conjunto de datos llamado modelo_item, el cual incluye columnas que contienen información sobre los géneros de videojuegos, los títulos y sus identificaciones. 

### Conclusiones 

A lo largo de este proyecto, hemos aplicado los conocimientos adquiridos en HENRY para construir un MVP que responde a las demandas de un mercado en constante evolución. Nuestro trabajo, que abarca desde la ingeniería de datos hasta el modelado predictivo, ha sido un viaje de aprendizaje continuo. Aunque hemos logrado cumplir con los objetivos iniciales, hemos identificado oportunidades para mejorar la eficiencia de nuestros procesos. Las limitaciones de almacenamiento actuales nos han obligado a adoptar soluciones creativas y a priorizar las funcionalidades más críticas. Sin embargo, esta experiencia nos ha enseñado a adaptarnos a entornos cambiantes y a buscar soluciones innovadoras.


## Autor
Miguel Flórez Betancourt 
