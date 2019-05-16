## 题目

> Made By RingFa1l_08163337

> E. 利用爬虫采集天气信息
>
> 天气数据存到数据库里；
>
> 数据可视化分析统计：各省会当日高低温、与去年同期比较、多日高低温预报、天气警报等（不必全做出来）。

> 项目/作业报告：题目，设计思路，开发环境配置，运行使用方法，运行效果截图，运行效果分析总结——缺陷、改进方法；
>
> 源代码；数据（数据库、文件、图片等形式）；可执行程序（可选）。 

### 开发环境配置

- Python 3.6.1
- SQLite 3.28.0
- beautifulsoup4 4.6.0
- requests 2.19.1

### 设计思路

#### 1.爬取数据存入数据库

- 使用requests库获取页面
- 使用BeautifulSoup库解析html
- 使用weather.db存储数据

#### 2.数据可视化分析统计

- 使用pyecharts库画图

#### 七天预报功能

数据来源：www.weather.com.cn 

#### 各省会实时温度功能

数据来源：tianqi.eastday.com

#### 历史数据比较功能

数据来源：tianqi.eastday.com

### 运行使用方法和截图

- 先在目录下新建weather.db数据库

- 运行predict_7.py，按提示输入城市，输入错误会提示

  [![EH9YsH.md.png](https://s2.ax1x.com/2019/05/16/EH9YsH.md.png)](https://imgchr.com/i/EH9YsH)

- 运行predict_7_draw.py，按提示输入城市，画出的柱形图在result目录下

  [![EH9UeA.md.png](https://s2.ax1x.com/2019/05/16/EH9UeA.md.png)](https://imgchr.com/i/EH9UeA)

- 运行live_temp.py

  [![EH94YV.md.png](https://s2.ax1x.com/2019/05/16/EH94YV.md.png)](https://imgchr.com/i/EH94YV)

- 运行live_temp_draw.py，画出地图，html格式时移动鼠标可显示省市信息和具体温度值

  [![EH9OT1.md.png](https://s2.ax1x.com/2019/05/16/EH9OT1.md.png)](https://imgchr.com/i/EH9OT1)

- 运行history.py，输入省会城市

  ![EHFim4.png](https://s2.ax1x.com/2019/05/16/EHFim4.png)

  ![EHkn5n.png](https://s2.ax1x.com/2019/05/16/EHkn5n.png)

- 运行history_draw.py，画出历史比较折线图

  [![EHk3KU.md.png](https://s2.ax1x.com/2019/05/16/EHk3KU.md.png)](https://imgchr.com/i/EHk3KU)

### 运行效果分析总结

|       脚本        |    缺陷     |       解决方法       |
| :-------------: | :-------: | :--------------: |
|  predict_7.py   |  用户输入不可信  |  加入是否是可查询城市的判断   |
| history_draw.py | 输入不是省会城市  | 加入数据库中是否有相关信息的判断 |
|   history.py    | 网站提供两种格式  |   分别进行不同的解析程序    |
|        *        |  网站数据缺失   |    加入判断并给用户提示    |
|        *        | 可视化结果难以区分 |   通过格式化创建特定文件名   |

~~哇最后转成exe惹，pyinstaller居然没坑窝，感动qvq~~  打脸了，画图程序无限报错x，还是直接用那几个脚本叭