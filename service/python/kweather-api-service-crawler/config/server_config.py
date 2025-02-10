# MSA Config
SERVICE_NAME = 'kweather-python-crawling-app'
SERVICE_PORT = 8003
SERVICE_HOST = '127.0.0.1'
EUREKA_SERVER = 'http://localhost:8081/eureka/'

# DB Config
DB_HOST = '220.95.232.80' #'kiotmysqlrw.kweather.co.kr'
DB_USER = 'root'
DB_PASSWORD = 'Dnpejelql1!'
DB_SCHEMA = 'guro_open'

# K-WEATHER, DATA-CENTER
FINEDUST_DATAURL = 'https://datacenter.kweather.co.kr/api/collection/list/airmap/lightly?type=dot'
POINT_WEATHER_DATAURL = 'https://kwapi.kweather.co.kr/v1/kma/forecast/guro?auth=a3dlYXRoZXItYXBwLWF1dGg='
