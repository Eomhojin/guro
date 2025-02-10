from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

import util.craw_util as craw
import util.finedust_util as finedust
import util.point_weather_util as weather

sched = BackgroundScheduler()

def craw_job():
  print("craw_job : " + str(datetime.now()))
  craw.crawler_sche()

def findust_job():
  print("findust_job : " + str(datetime.now()))
  finedust.start()

def pot_job():
  print("pot_job : " + str(datetime.now()))
  weather.start()

def scheduler_init():
  sched.add_job(craw_job, 'cron', hour='0-23', minute='*/10', id="crawler_scheduler")
  sched.add_job(findust_job, 'cron', hour='0-23', minute='*/10', id="finedust_scheduler")
  sched.add_job(pot_job, 'cron', hour='0-23', minute='*/10', id="pot_scheduler")

  sched.start()
