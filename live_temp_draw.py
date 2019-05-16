#! usr/bin/python3
#! -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Geo, Map
from pyecharts.globals import ChartType, SymbolType
import sqlite3, sys


conn = sqlite3.connect('weather.db')
c = conn.cursor()
print("opened database successfully")

try:
    cursor = c.execute("SELECT * from live_weather")
    print("data selected successfully")
except:
    sys.exit("No information")

city = []
temp = []
for row in cursor:
    city.append(row[2])
    temp.append(row[3])

print(city)
print(temp)


def geo_base() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("省会温度", [list(z) for z in zip(city, temp)])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=30),
            title_opts=opts.TitleOpts(title="省会城市实时温度", subtitle="made by Ringfa1l"),
        )
    )
    return c

geo_base().render("result/live_temp.html")
print("pic created successfully")

conn.close()