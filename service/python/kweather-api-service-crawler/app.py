from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
import config.server_config as server
import py_eureka_client.eureka_client as eureka_client
import util.craw_util as craw
import util.point_weather_util as weather
import service.craw_scheduler as scheduler

app = Flask(__name__)
api = Api(app)
CORS(app)

eureka_client.init(eureka_server=server.EUREKA_SERVER,
                   app_name=server.SERVICE_NAME,
                   instance_host=server.SERVICE_HOST,
                   instance_port=server.SERVICE_PORT)

@app.route("/craw/url", methods=['GET'])
def get_crawling_url():
  return craw.crawler_page('http://1.225.91.30/WEB/all')

@app.route("/craw/get_data", methods=['GET'])
def post_crawling_data():
  params = request.get_json()
  response_data = craw.crawler_parsing(params['url'])
  return {"data" : response_data}

if __name__ == "__main__": 
  scheduler.scheduler_init()
  app.run(host=server.SERVICE_HOST, port=server.SERVICE_PORT, debug=True)
