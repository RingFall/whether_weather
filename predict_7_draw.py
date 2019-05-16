#! usr/bin/python3
#! -*- coding: utf-8 -*-
from pyecharts.charts import Bar
from pyecharts import options as opts
import sqlite3,sys

city = input("city:")

conn = sqlite3.connect('weather.db')
c = conn.cursor()
print("opened database successfully")

try:
    cursor = c.execute("SELECT * from week_weather where city='{}'".format(city))
    print("data selected successfully")
except:
    sys.exit("No information about {}, please run predict_7.py first~".format(city))

x = []
y1 = []
y2 = []
try:
    for row in cursor:
        x.append(row[2])
        h = row[4].split('/')[0]
        if h.find('℃'):
            high = int(h.split('℃')[0])
        else:
            high = int(h)
        try:
            low = int(row[4].split('/')[1].split('℃')[0])
        except:
            low = high
        y1.append(high)
        y2.append(low)
except:
    sys.exit("高低温信息缺失")

bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis("最高温度", y1)
bar.add_yaxis("最低温度", y2)
bar.set_global_opts(title_opts=opts.TitleOpts(title="{}七日高低温预测".format(city), subtitle="made by Ringfa1l"))
bar.render("result/{}_pre.html".format(city))
print("pic created successfully")

conn.close()