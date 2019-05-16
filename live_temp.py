#! usr/bin/python3
#! -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sqlite3

dic1 = ['河北省', '山西省', '辽宁省','吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '广东省', '湖南省', '湖北省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区']
dic2 = ['石家庄', '太原', '沈阳', '长春', '哈尔滨', '南京', '杭州', '合肥', '福州', '南昌', '济南', '郑州', '广州', '长沙', '武汉', '海口', '成都', '贵阳', '昆明', '西安', '兰州', '西宁', '台北', '呼和浩特', '南宁', '拉萨', '银川', '乌鲁木齐']
dic3 = ['53698', '53772', '54342', '54161', '50953', '58238', '58457', '58321', '58847', '58606', '54823', '57083', '59287', '57687', '57494', '59758', '56294', '57816', '56778', '57036', '52889', '52866', '71294', '53463', '59431', '55591', '53614','51463']
dic4 = ['shijiazhuang', 'taiyuan', 'shenyang', 'changchun', 'haerbin', 'nanjing', 'hangzhou', 'hefei', 'fuzhou', 'nanchang', 'jinan', 'zhengzhou', 'guangzhou', 'changsha', 'wuhan', 'haikou', 'chengdu', 'guiyang', 'kunming', 'xian', 'lanzhou', 'xining', 'taibei', 'huhehaote', 'nanning', 'lasa', 'yinchuan', 'wulumuqi']

result = []
for i in range(dic1.__len__()):
    url = 'http://tianqi.eastday.com/{}/{}.html'.format(dic4[i],dic3[i])
    res = requests.get(url)
    bs = BeautifulSoup(res.text,"html.parser")
    data = bs.select("div.tempBox > span")
    temp = int(data[0].text)
    result.append([dic1[i],dic2[i],temp])

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
try:
    cursor.execute("drop table live_weather;")
    print("delete old data")
except:
    pass
cursor.execute('''create table live_weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province char(100),
    city char(100),
    temp int
    );''')
print("create new table")
for result1 in result:
    print(result1)
    insertsql = "insert into live_weather (province,city,temp) VALUES ('%s','%s','%d')"
    cursor.execute(insertsql % (result1[0],result1[1],result1[2]))
 
conn.commit()
cursor.close()
conn.close()