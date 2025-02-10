import requests, time
from bs4 import BeautifulSoup
import util.mysql_control_util as db_con

def crawler_page(url):
  html = requests.get(url)
  return html.text

def crawler_parsing(url):
  html = requests.get(url)
  soup = BeautifulSoup(html.content, 'html.parser')
  now = time.localtime()
  time_str = "%04d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

  data_list = []
  for x in range(0, 14):
    p_name = str(soup.select(".info-box-text")[x].text)
    p_data = str(soup.select(".info-box-number")[x].text)

    data_list.append(
      {
        "dateTime" : time_str,
        "station_name" : p_name, 
        "data" : float(p_data.replace("초미세먼지 : ", "").replace(" ㎍/m³", ""))
      }
    )
    print(data_list)

  return data_list

def crawler_sche():
  html = requests.get("http://1.225.91.30/WEB/all")
  soup = BeautifulSoup(html.content, 'html.parser')

  for x in range(0, 14):
    p_name = str(soup.select(".info-box-text")[x].text)
    p_data = str(soup.select(".info-box-number")[x].text)
    db_con.insert_pm_data(p_name, p_data.replace("초미세먼지 : ", "").replace(" ㎍/m³", ""))
