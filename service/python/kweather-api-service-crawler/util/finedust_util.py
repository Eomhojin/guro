import requests
import csv
import json
from haversine import haversine
import sys
from datetime import datetime
import config.server_config as config
import util.mysql_control_util as db_con

def calcDistance(a, b):
    return haversine(a, b, unit='km')

def idw_interploation(datas):
    sd = 0.0
    v = {
        "pm10": 0.0,
        "pm25": 0.0
    }

    for i in range(len(datas)):
        data = datas[i]
        d = data['d']
        sd += 1/(d*d)
        d2 = d*d
        v['pm10'] += data['pm10'] / d2
        v['pm25'] += data['pm25'] / d2

    for key in v:
        v[key] = v[key]/sd

    return v


def calcData(points):
    dicString = loadRemoteData()
    if dicString == None:
        print('FINEDUST_DATAURL, remote data read Error!!!!')
        return

    try:
        jsonData = json.loads(dicString)
    except Exception as ex:
        print(ex)
        return

    dots = jsonData['data']

    finedustData = []
    for point in points:
        start = point['latlon']
        stations = []

        for dot in dots:
            dest = (dot['latlng']['lat'], dot['latlng']['lon'])
            distnace = calcDistance(start, dest)
            if distnace < 5:
                stations.append(
                    {"serial": dot["serial"], "d": distnace, "pm10": dot["pm10"], "pm25": dot["pm25"]})
                stations = sorted(
                    stations, key=lambda k: k["d"], reverse=False)[0:5]

        fData = idw_interploation(stations)

        finedustData.append({
            "station_id": point["station_id"],
            "lat": point['latlon'][0],
            "lon": point['latlon'][1],
            "pm10": fData["pm10"],
            "pm25": fData["pm25"],
            "regdate": f"{datetime.now().strftime('%Y-%m-%d %H')}:{int(datetime.now().minute/10)}0"
        })

    return finedustData


def loadRemoteData():
    data = None
    try:
        response = requests.get(config.FINEDUST_DATAURL)
        print(response)
        if response.status_code == 200:
            data = response.text
    except Exception as ex:
        print(ex)

    return data


def start():
    with open('./data/grid.csv', newline='') as csvFile:
        datas = csv.reader(csvFile, delimiter=',')
        points = []
        for data in datas:
            points.append({
                "station_id": data[0],
                "latlon": (float(data[2]), float(data[1])),
            })

        finedustData = calcData(points)
    for data in finedustData:        
      db_con.insert_finedust_data(data)
    
