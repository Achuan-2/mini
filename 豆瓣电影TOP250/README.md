# 豆瓣电影Top250
阿巛的第一个爬虫项目

## 项目结构

- douban250_page.py 爬取豆瓣电影Top250页面的脚本
- douban250.py 爬取豆瓣电影Top250页面+每部电影页面的脚本
- data_anylysis.ipynb 数据处理和分析代码
- douban250_explore.ipynb 中间脚本文件（无用）
- movies/ 存放爬取和整理后的豆瓣电影信息表格
- movie_pic/ 存放豆瓣电影Top250中250部电影的封面图片
- anlysis/ 存放分析生成的图片和文件

## 爬虫部分

爬虫部分的脚本主要功能有两个
1. 解析豆瓣电影Top页面，获得250部电影的信息，汇总成表格
2. 把250部电影的封面图下载到[anlysis/](anlysis/)文件夹中
    ![20220125015630_2022-01-25](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20220125015630_2022-01-25.png)

douban250_page.py 是只对[豆瓣电影Top250页面](https://movie.douban.com/top250)进行解析，即只解析10个页面，得到的豆瓣Top250_page.xlsx没有编剧、演员信息
![豆瓣电影Top250页面](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20220125020703_2022-01-25.png "豆瓣电影Top250页面")
douban250.py 则除了解析豆瓣电影Top250页面，还会对每部电影进行解析，得到的豆瓣Top250.xlsx 汇总比较全面
![20220125020827_2022-01-25](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20220125020827_2022-01-25.png)
注意：由于脚本会解析10+250=260个页面，必须要有豆瓣登陆的cookie才能正常运行的，因为会被豆瓣识别为异常访问，限制ip访问的
获取豆瓣cookie见，
![20220125021416_2022-01-25](https://cdn.jsdelivr.net/gh/Achuan-2/PicBed@pic/assets/README/20220125021416_2022-01-25.png)
只需要按照上图的方法，将复制的cookie替换douban250.py中ua_ck()函数的cookies变量

## 分析部分见
[anlysis.md](anlysis.md)

