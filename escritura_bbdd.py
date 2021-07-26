# -*- coding: utf-8 -*-

import sys
if sys.platform == 'win32':
    path = ''
    print ('\n#### Windows System ####')
    system = sys.platform
else:
    path = ''
    print ('\n#### Linux System ####')
    system = sys.platform

print ('#####################################')
print ('#####################################')
print ('\n### Importing Libraries... ###')

import os
import pandas as pd
import numpy as np
import requests as rq
import csv
import json
import glob
import pymongo
import dns

if '__file__' in locals():
    wd = os.path.dirname(__file__)
    print(wd)
    sys.path.append(wd)
    sep = '/'
else:
    wd = os.path.abspath('/working_folder/')
    wd = wd + '/'
    sys.path.append(wd)
    sep = '/'

def escritura_bbdd(): 
    ### Obtenemos lista de ficheros ###
    #
    lista_ficheros = glob.glob(wd + '*.csv')
    
    ### Conexion a la bbdd 
    # 
    user = 'jmortegac'
    password = 'linux'
    client = pymongo.MongoClient("mongodb+srv://jmortegac:linux@cluster0.nqnow.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database("weather_database")
    
    for item in lista_ficheros:
        item_str = item.split(sep)[-1]
        item_str = item_str.split('.')[0]
        item_str = item_str.split('consolidated_weather_')[-1]
        item_str = item_str + '_records'
        df = pd.read_csv(f'{item}')
        df_json = df.to_json(orient="records")
        df_json = json.loads(df_json)
        exec('records = db.' + item_str)
        #exec('records.remove()')
        exec('records.insert(df_json)')
    print('Se han leído los .csv y se han subido como documentos a la base de datos MongoDB Atlas')
    return

if __name__ == '__main__':
    escritura_bbdd()
