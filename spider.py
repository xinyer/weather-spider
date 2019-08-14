# -*- coding: utf-8 -*-
from weather import weather
import requests
from bs4 import BeautifulSoup

# w = weather('xian', "小雨", '8/14', 23, 12, '南', '2级')
# w.tostring()

url = 'http://www.weather.com.cn/textFC/hb.shtml'

res = requests.get(url)
res.encoding = 'utf-8'
html = res.text 
# print(html)
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
# print(tables)

weathers = []

for table in tables:
    trs = table.find_all('tr')
    
    dateTr = trs[0]
    firstTds = dateTr.find_all('td')
    date_day = firstTds[2].text
    date_night = firstTds[3].text
    # print("date_day:", date_day)
    # print("date_night:", date_night)
    
    for index in range(len(trs)):
        if index > 1:
            infos = trs[index].find_all('td')

            if index == 2:
                city = infos[0].find('a').text
                phenomenon_day = infos[2].text
                wind_day = infos[3].find_all('span')
                if len(wind_day) == 2:
                    wind_direct_day = wind_day[0].text
                    wind_power_day = wind_day[1].text
                else:
                    wind_direct_day = 'no data'
                    wind_power_day = 'no data'

                temperature_day = infos[4].text

                phenomenon_night = infos[5].text
                wind_night = infos[6].find_all('span')
                if len(wind_night) == 2:
                    wind_direct_night = wind_night[0].text
                    wind_power_night = wind_night[1].text
                else:
                    wind_direct_night = 'no data'
                    wind_power_night = 'no data'

                temperature_night = infos[7].text
            else:
                city = infos[0].find('a').text
                phenomenon_day = infos[1].text
                wind_day = infos[2].find_all('span')
                if len(wind_day) == 2:
                    wind_direct_day = wind_day[0].text
                    wind_power_day = wind_day[1].text
                else:
                    wind_direct_day = 'no data'
                    wind_power_day = 'no data'

                temperature_day = infos[3].text

                phenomenon_night = infos[4].text
                wind_night = infos[5].find_all('span')
                if len(wind_night) == 2:
                    wind_direct_night = wind_night[0].text
                    wind_power_night = wind_night[1].text
                else:
                    wind_direct_night = 'no data'
                    wind_power_night = 'no data'

                temperature_night = infos[6].text
            
            # print("city:", city)
            # print("phenomenon_day:", phenomenon_day)
            # print("wind_direct_day:", wind_direct_day)
            # print("wind_power_day:", wind_power_day)
            # print("temperature_day:", temperature_day)
            # print("phenomenon_night:", phenomenon_night)
            # print("wind_direct_night:", wind_direct_night)
            # print("wind_power_night:", wind_power_night)
            # print("temperature_night:", temperature_night)
            # print("----------------\n")
            weather_day = weather(city, date_day, phenomenon_day, temperature_day, wind_direct_day, wind_power_day)
            weathers.append(weather_day)
            weather_night = weather(city, date_night, phenomenon_night, temperature_night, wind_direct_night, wind_power_night)
            weathers.append(weather_night)
            pass

with open('weather.txt', 'w') as f:
    for weather in weathers:
        f.write(weather.city + " " +weather.date + " " +weather.phenomenon + " " + weather.temperature + " " +weather.wind_direction + "\n")
    pass
