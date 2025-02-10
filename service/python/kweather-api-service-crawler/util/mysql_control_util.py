import pymysql
import config.server_config as config


def insert_pm_data(station_name, pm25data):
  conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER,
                         password=config.DB_PASSWORD, db=config.DB_SCHEMA, charset='utf8')

  try:
    curs = conn.cursor()
    sql = 'INSERT INTO craw_data(station_name, pm25data, created_date) VALUES (%s, %s, now())'
    curs.execute(sql, (station_name, pm25data))
    conn.commit()

  finally:
    conn.close()

def insert_finedust_data(datas):
  conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER,
                         password=config.DB_PASSWORD, db=config.DB_SCHEMA, charset='utf8')

  try:
    curs = conn.cursor()
    sql = 'INSERT INTO finedust(station_id, lat, lon, pm10, pm25, regdate) VALUES (%s, %s, %s, %s, %s, %s)'
    curs.execute(sql, (datas["station_id"], datas["lat"],
                       datas["lon"], datas["pm10"], datas["pm25"], datas["regdate"]))
    conn.commit()

  finally:
    conn.close()

def insert_point_data(datas):
  conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER,
                         password=config.DB_PASSWORD, db=config.DB_SCHEMA, charset='utf8')

  try:
    curs = conn.cursor()
    sql = 'INSERT INTO point_data(local_code, base_date, fcs_date, icon_no, temp, humidity, rain_prob, rain, snow, wind_dir, wind_speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE icon_no = %s, temp = %s, humidity = %s, rain_prob = %s, rain = %s, snow = %s, wind_dir = %s, wind_speed = %s'
    curs.execute(sql, (datas["localCode"], datas["TM_FC"], datas["TM_EF"], 
                  datas["WCOND"], datas["TEMP"], datas["HUMI"], 
                  datas["RAINP"], datas["RAIN"], datas["SNOW"], 
                  datas["WDIR"], datas["WSPD"], datas["WCOND"], 
                  datas["TEMP"], datas["HUMI"], datas["RAINP"], 
                  datas["RAIN"], datas["SNOW"], datas["WDIR"], datas["WSPD"]))
    conn.commit()

  finally:
    conn.close()
