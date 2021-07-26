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
from flask import Flask, request, render_template, jsonify

print('\n')
print('Poner en el navegador "http://localhost:5000/api/v1/weather/<ciudad>" donde ciudad puede ser Madrid, San_Francisco o New_York')
print('Tambien desde una consola python "request.get("http://localhost:5000/api/v1/weather/<ciudad>")", donde ciudad puede ser Madrid, San_Francisco o New_York')
print('Pulsar ctrl+c para cancelar')
print('\n')


if '__file__' in locals():
    wd = os.path.dirname(__file__)
    sys.path.append(wd)
    sep = '/'
else:
    wd = os.path.abspath('/working_folder/app/')
    wd = wd + '/'
    sys.path.append(wd)
    sep = '/'

### Conexion a la bbdd 
# 
user = 'jmortegac'
password = 'linux'
client = pymongo.MongoClient("mongodb+srv://jmortegac:linux@cluster0.nqnow.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("weather_database")
## Creacion de la app
#
app = Flask(__name__) 

@app.route('/api/v1/weather/<city>', methods=['GET'])
def api_weather_city(city):
    records = 'db.' + city + '_records'
    records = eval(records)
    results = list(records.find({}, {"_id": 0})) # Asi omitimos el _id que por defecto nos agrega mongo
    return jsonify(results)
    

###############################################################################################################
#         INFINITY LOOP LISTENING TO PORT 80 (port=int("80")) TO THE OUTSIDE WORLD (host="0.0.0.0") - START   #
###############################################################################################################
if __name__ == '__main__':
    app.run(
	host="0.0.0.0",
        port=int("5000")
    )
###############################################################################################################
#         INFINITY LOOP LISTENING TO PORT 80 (port=int("80")) TO THE OUTSIDE WORLD (host="0.0.0.0") - END     #
###############################################################################################################

## END ##     