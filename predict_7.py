#! usr/bin/python3
#! -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sqlite3
import json
import sys

def city2code(city_name):
	with open('city_code.json', 'r') as f:
		data = json.load(f)
	f.close()
	try:
		return data[city_name]
	except:
		sys.exit('no city {} information'.format(city_name))

city = input("city:")
city_code = city2code(city)
url = "http://www.weather.com.cn/weather/{}.shtml".format(city_code)
res = requests.get(url)
res.encoding = 'utf-8'
bs = BeautifulSoup(res.text,"html.parser")
date = bs.select("li.sky > h1")
desc = bs.select("li.sky > p.wea")
temp = bs.select("li.sky > p.tem")
dir = bs.select("li > p.win > em")
level = bs.select("li > p.win > i")

result = []
for i in range(date.__len__()):
    date1 = date[i].text
    desc1 = desc[i].text
    temp1 = temp[i].stripped_strings
    temp1 = "".join(temp1)
    dir1 = dir[i]
    dir2 = dir1.select("span")
    if len(dir2) == 1:
        direction = "无持续风向"
    else:
        direction = dir2[0].get("title")+"-"+dir2[1].get("title")
    level1 = level[i].text
    result.append([city,date1,desc1,temp1,direction,level1])

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
try:
    cursor.execute("delete from week_weather where city='{}'".format(city))
    print("delete old data")
except:
    cursor.execute('''create table week_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city char(100),
        date char(100),
        desc char(100),
        temp char(100),
        direction char(100),
        level char(100)
        );''')
    print("create new table")
for result1 in result:
    print(result1)
    insertsql = "insert into week_weather (city,date,desc,temp,direction,level) VALUES ('%s','%s','%s','%s','%s','%s')"
    cursor.execute(insertsql % (result1[0],result1[1],result1[2],result1[3],result1[4],result1[5]))
 
conn.commit()
cursor.close()
conn.close()