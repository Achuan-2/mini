import requests
import pandas as pd
import bs4
import os
from tqdm import tqdm
from lxml import etree
from bs4 import BeautifulSoup
"""
注意这个脚本是必须要有豆瓣登陆的cookie才能正常运行的，因为脚本会解析10+250=260个页面，会被豆瓣识别为异常访问，限制ip访问的
"""
def find_page_num(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find(
        'span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)

# 定义函数，用来处理User-Agent和Cookie


def ua_ck():
    '''
    网站需要登录才能采集，需要从Network里复制User-Agent和Cookie，Cookie要转化为字典，否则会采集失败！！！！！
    '''

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    cookies = 'll="108304"; bid=I4zqlTPs6Qg; douban-fav-remind=1; viewed="34432673"; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; dbcl2="191491114:SlSLE5NfS/M"; ck=6zCi'

    # Cookie转化为字典
    cookies = cookies.split('; ')
    cookies_dict = {}
    for i in cookies:
        cookies_dict[i.split('=')[0]] = i.split('=')[1]

    return user_agent, cookies_dict


def open_url(url):
    login = ua_ck()
    u_a = login[0]
    c_d = login[1]
    res = requests.get(url, headers=u_a, cookies=c_d)

    return res


def mkdir(path):
    flag = os.path.exists(path)
    if not flag:
        os.makedirs(path)


def download_pic(pic_url, filename):
    picture_response = requests.get(url=pic_url)
    with open(filename, 'wb') as f:
        f.write(picture_response.content)


def parse_movie(url):
    res = open_url(url)
    soup = BeautifulSoup(res.text, 'html.parser')  # 用 html.parser 来解析网页
    item = soup.find('div', id='content')
    movie_info = {}  # 新建字典，存放电影信息
    # 电影名称
    movie_info['电影名称'] = item.h1.span.text

    # 导演、类型、制片国家/地区、语言、上映时间、片长（部分电影这些信息不全，先全部采集，留待数据分析时处理）
    infos = item.find('div', id='info').text.replace(' ', '').split('\n')
    for i in infos:
        if ':' in i:
            movie_info[i.split(':')[0]] = i.split(':')[1]
        else:
            continue
    return movie_info


def parse_page(html, table):
    # 为电影图片生成一个文件夹
    movie_pic = "movie_pic"
    mkdir(movie_pic)

    # 开始解析
    xp = etree.HTML(html)
    lis = xp.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in lis:
        rank = li.xpath('div/div[1]/em/text()')[0]
        link = li.xpath('div/div[2]/div[1]/a/@href')[0]
        rating = li.xpath('div/div[2]/div[2]/div/span[2]/text()')[0]
        people = li.xpath('div/div[2]/div[2]/div/span[4]/text()')[0][:-3]
        try:
            quote = li.xpath('div/div[2]/div[2]/p[2]/span/text()')[0]
        except:
            quote = None
        movie_info = parse_movie(link)
        # line = [rank, rating] + \
        #     list(movie_info.values())[:-1]+[people, quote, link]
        movie_dict = {"排名": rank, "评分": rating}
        movie_dict.update(movie_info)
        movie_dict.update({"评分人数": people, "短评": quote, "豆瓣链接": link})

        table.append(movie_dict)

        # 下载图片
        # pic_url = li.xpath('div/div[1]/a/img/@src')[0]
        # download_pic(pic_url, f"{movie_pic}/{rank}-{title}_{rating}分.jpg")
    return table


def main():

    # 解析并生成excel表格
    table = []
    host = "https://movie.douban.com/top250"
    # page_num = find_page_num(open_url(host))
    page_num = 10
    for i in tqdm(range(page_num), desc='解析进度'):
        url = host + '/?start=' + str(25*i)
        res = open_url(url)
        html = res.text
        table = parse_page(html, table)
    df = pd.DataFrame(table)
    df.to_excel('movies/豆瓣Top250_raw.xlsx', index=False)


if __name__ == "__main__":
    main()
