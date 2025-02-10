import requests
import csv
import json
from haversine import haversine
import sys
from datetime import datetime
import config.server_config as config
import util.mysql_control_util as db_con


def api_data_call():
    try:
        response = requests.get(config.POINT_WEATHER_DATAURL)
        if response.status_code == 200:
            data = response.text
    except Exception as ex:
        print(ex)

    if response == None:
        print('POINT_WEATHER_DATAURL, remote data read Error!!!!')
        return
    try:
        jsonData = json.loads(response.text)
    except Exception as ex:
        print(ex)
        return

    return jsonData

def start():
    api_datas = api_data_call()
    for data in api_datas['data']:
        db_con.insert_point_data(data);
