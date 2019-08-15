# -*- coding: utf-8 -*-
from weather import weather
import requests
from bs4 import BeautifulSoup
import os
from db import saveDb

weathers = []

def load_weather(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text 

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        trs = table.find_all('tr')
        
        dateTr = trs[0]
        firstTds = dateTr.find_all('td')
        date_day = firstTds[2].text
        date_night = firstTds[3].text
        province = ''
        
        for index in range(len(trs)):
            if index > 1:
                infos = trs[index].find_all('td')
                if index == 2:
                    province = infos[0].find('a').text
                    city = infos[1].find('a').text
                    phenomenon_day = infos[2].text
                    wind_day = infos[3].find_all('span')
                    if len(wind_day) == 2:
                        wind_direct_day = wind_day[0].text
                        wind_power_day = wind_day[1].text
                    else:
                        wind_direct_day = '-'
                        wind_power_day = '-'

                    temperature_day = infos[4].text

                    phenomenon_night = infos[5].text
                    wind_night = infos[6].find_all('span')
                    if len(wind_night) == 2:
                        wind_direct_night = wind_night[0].text
                        wind_power_night = wind_night[1].text
                    else:
                        wind_direct_night = '-'
                        wind_power_night = '-'

                    temperature_night = infos[7].text
                else:
                    city = infos[0].find('a').text
                    phenomenon_day = infos[1].text
                    wind_day = infos[2].find_all('span')
                    if len(wind_day) == 2:
                        wind_direct_day = wind_day[0].text
                        wind_power_day = wind_day[1].text
                    else:
                        wind_direct_day = '-'
                        wind_power_day = '-'

                    temperature_day = infos[3].text

                    phenomenon_night = infos[4].text
                    wind_night = infos[5].find_all('span')
                    if len(wind_night) == 2:
                        wind_direct_night = wind_night[0].text
                        wind_power_night = wind_night[1].text
                    else:
                        wind_direct_night = '-'
                        wind_power_night = '-'

                    temperature_night = infos[6].text
                
                weather_day = weather(province, city, date_day, phenomenon_day, temperature_day, wind_direct_day, wind_power_day)
                if phenomenon_day != '-':
                    weathers.append(weather_day)
                    pass
                
                weather_night = weather(province, city, date_night, phenomenon_night, temperature_night, wind_direct_night, wind_power_night)
                if phenomenon_night != '-':
                    weathers.append(weather_night)
                    pass

                pass

# 华北天气
url_hb = 'http://www.weather.com.cn/textFC/hb.shtml'
load_weather(url_hb)

# 东北天气
url_db = 'http://www.weather.com.cn/textFC/db.shtml'
load_weather(url_db)

# 华东天气
url_hd = 'http://www.weather.com.cn/textFC/hd.shtml'
load_weather(url_hd)

# 华中天气
url_hz = 'http://www.weather.com.cn/textFC/hz.shtml'
load_weather(url_hz)

# 华南天气
url_hn = 'http://www.weather.com.cn/textFC/hn.shtml'
load_weather(url_hn)

# 西北天气
url_xb = 'http://www.weather.com.cn/textFC/xb.shtml'
load_weather(url_xb)

# 西南天气
url_xn = 'http://www.weather.com.cn/textFC/xn.shtml'
load_weather(url_xn)

path = 'weather.txt'
if os.path.exists(path):
    os.remove(path)

with open(path, 'w') as f:
    for w in weathers:
        f.write(w.province + " " + w.city + " " + w.date + " " + w.phenomenon + " " + w.temperature + " " + w.wind_direction + " " + w.wind_power + "\n")
    pass
pass

saveDb(weathers)

# 港澳台天气
# url_gat = 'http://www.weather.com.cn/textFC/gat.shtml'
# load_weather(url_gat)