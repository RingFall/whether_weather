#! usr/bin/python3
#! -*- coding: utf-8 -*-
from pyecharts.charts import Line
from pyecharts import options as opts
import sqlite3,sys

city = input("请输入一个省会城市:")

conn = sqlite3.connect('weather.db')
c = conn.cursor()
print("opened database successfully")

try:
    cursor = c.execute("SELECT * from his_weather where city='{}'".format(city))
    print("data selected successfully")
except:
    sys.exit("No information about {}".format(city))

time = []
high = []
low = []

for row in cursor:
    time.append(row[2])
    high.append(row[3])
    low.append(row[4])

def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(time)
        .add_yaxis("月平均最高温度", high)
        .add_yaxis("月平均最低温度", low)
        .set_global_opts(title_opts=opts.TitleOpts(title="{}历史气温比较".format(city), subtitle="made by Ringfa1l"))
    )
    return c

line_base().render("result/{}_his_compare.html".format(city))
print("pic created successfully")

conn.close()