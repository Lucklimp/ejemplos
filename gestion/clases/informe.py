from GESTION.DAL.db import conexion
from pandas.plotting import table
import pandas as pd
import matplotlib.pyplot as plt
def obtener_datos(): 
    conex = conexion() 
    consulta = "SELECT * FROM empleados,departamento, proyectos, registro tiempo" # Ajusta esta consulta según tus necesidades 
    df = pd.read_sql(consulta, conex) 
    conexion.close() 
    return df

def generar_informe_excel(): 
    df = obtener_datos() 
    df.to_excel('informe_departamento.xlsx', index=False) 
    print("Informe Excel generado en 'informe_departamento.xlsx'")

# Generar una tabla con datos del DataFrame
def generar_informes_pdf():
    df = obtener_datos() 
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax.axis('tight')
    ax.axis('off') 
    tbl = table(ax, df, loc='center', cellLoc='center', colWidths=[0.1]*len(df.columns)) 
    fig.savefig('temp_table.png', bbox_inches='tight')

