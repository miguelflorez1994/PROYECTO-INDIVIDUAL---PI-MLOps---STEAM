#código para que jale: uvicorn app:main --reload


import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

@app.get("/")
def index():
    return {
        "Mensaje de bienvenida": [
            "Proyecto Individual 1 - Sistema Recomendacion STEAM",
            "Desarrollado por: Miguel Flórez Betancourt"
        ]
    }

# Devuelve la cantidad de items y porcentaje de contenido Free por año para la empresa desarrolladora ingresada como
# parametro.
@app.get("/developer/{desarrollador}")
def developer(desarrollador : str):

    df_dev = pd.read_parquet('def_developer.parquet')

    if desarrollador in df_dev['developer'].values:

        dev = df_dev[df_dev['developer']==desarrollador]
        dev['free']=dev['price'].apply(lambda x: 1 if x == 0 else 0)
        dev['tot']=1
        dev = dev.groupby(['developer','year']).agg({'free': 'sum','tot':'count'}).reset_index()
        dev['percentage']=((dev['free']/dev['tot'])*100).round(2)
        dev.drop(columns=['developer','free'],inplace=True)
        dev.rename(columns={'year':'Año','tot':'Cantidad de items','percentage':'Contenido Free (%)'},inplace=True)

        # Usar Jinja2 para renderizar la tabla dentro de una plantilla HTML
        template = Template("""
        <html>
        <head><title>Tabla de Datos</title></head>
        <body>
        {{ table_html | safe }}
        </body>
        </html>
        """)

        # Renderizar la plantilla con los datos
        html_content = template.render(table_html=dev.to_html())

        return HTMLResponse(content=html_content)
        #return dev.to_dict(orient='records')
    
    else:

        return f'El desarrollador {desarrollador} no se encuentra en los registros'

#ca,bops

# Devuelve el usuario que acumula más horas jugadas para el género ingresado como parametro y una lista de la 
# acumulación de horas jugadas por año de lanzamiento.
@app.get("/UserForGenre/{genero}")
def UserForGenre(genero : str):
    df_user_gen = pd.read_parquet('def_userforgenre.parquet')

    df_gen = df_user_gen[df_user_gen['genres'].apply(lambda x: genero in x)]
    tot = df_gen.groupby(['user_id']).agg({'playtime_forever': 'sum'}).reset_index()
    
    if tot.size > 0:

        u_most = tot.sort_values(by='playtime_forever',ascending=False).iloc[0,0]

        df_user = df_gen[df_gen['user_id']==u_most]

        df_user = df_user.groupby(['year']).agg({'playtime_forever': 'sum'}).reset_index()

        df_user.rename(columns={'year':'Año','playtime_forever':'Horas'},inplace=True)
        res_dict = df_user.to_dict(orient='records')

        return {f"Usuario con más horas jugadas para Genero '{genero}'" : u_most, 
                "Horas jugadas":res_dict}
    
    else:

        return f"No hay registros de horas de juego para Genero '{genero}'"

