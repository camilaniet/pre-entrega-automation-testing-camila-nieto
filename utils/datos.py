import csv
import pathlib

def leer_csv_login(ruta_archivo):
    ruta = pathlib.Path(ruta_archivo)
    datos = []
    with open(ruta,newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            datos.append((fila["usuario"], fila["password"], fila["debe_funcionar"]))
    return datos