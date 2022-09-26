import requests
import pandas as pd
import bs4
import os
from tqdm import tqdm
from lxml import etree

"""
注意：这个脚本是只抓取TOP25010个页面，因此获得的豆瓣Top250_page.xlsx缺少编剧、演员等信息
"""

def find_page_num(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find(
        'span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)
# 定义函数，用来处理User-Agent和Cookie


def ua_ck():
    '''
    网站需要登录才能采集，需要从Network--Doc里复制User-Agent和Cookie，Cookie要转化为字典，否则会采集失败！！！！！
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


def parse_html(html, table):
    # 为电影图片生成一个文件夹
    movie_pic = "movie_pic"
    mkdir(movie_pic)
    # 开始解析
    xp = etree.HTML(html)
    lis = xp.xpath('//*[@id="content"]/div/div[1]/ol/li')

    columns = ['排名', '电影名称', '别名', '导演', '上映年份',
               '制作国家', '类型', '评分', '评价人数', '短评', '豆瓣链接']
    for li in lis:
        rank = li.xpath('div/div[1]/em/text()')[0]
        title = li.xpath('div/div[2]/div[1]/a/span[1]/text()')[0]
        try:
            title2 = li.xpath(
                'div/div[2]/div[1]/a/span[@class="title"][2]/text()')[0].replace("\xa0", "")
        except:

            title2 = li.xpath(
                'div/div[2]/div[1]/a/span[2]/text()')[0].replace("\xa0", "")
        else:
            title2 += li.xpath('div/div[2]/div[1]/a/span[@class="other"]/text()')[
                0].replace("\xa0", "")
        director = li.xpath('div/div[2]/div[2]/p[1]/text()')[
            0].strip().replace("\xa0\xa0\xa0", "\t").split("\t")[0][4:]
        info = li.xpath(
            'div/div[2]/div[2]/p[1]/text()')[1].strip().replace("\xa0", "").split("/")
        date, area, genre = info[0], info[1].replace(
            " ", ","), info[2].replace(" ", ",")
        rating = li.xpath('div/div[2]/div[2]/div/span[2]/text()')[0]
        people = li.xpath('div/div[2]/div[2]/div/span[4]/text()')[0][:-3]
        try:
            quote = li.xpath('div/div[2]/div[2]/p[2]/span/text()')[0]
        except:
            quote = None

        link = li.xpath('div/div[2]/div[1]/a/@href')[0]
        line = [rank, title, title2, director, date, area,
                genre, rating, people, quote, link]
        table.append(line)

        # 下载图片
        pic_url = li.xpath('div/div[1]/a/img/@src')[0]
        download_pic(pic_url, f"{movie_pic}/{rank}-{title}_{rating}分.jpg")
    return table


def main():

    # 解析并生成excel表格
    table = []
    host = "https://movie.douban.com/top250"
    page_num = find_page_num(open_url(host))
    for i in tqdm(range(page_num), desc='解析进度'):
        url = host + '/?start=' + str(25*i)
        res = open_url(url)
        html = res.text
        table = parse_html(html, table)
    columns = ['排名', '电影名称', '别名', '导演', '上映年份', '制作国家', '类型', '评分', '评分人数', '短评', '豆瓣链接']

    df = pd.DataFrame(table, columns=columns)
    df.to_excel('movies/豆瓣Top250_page.xlsx', index=False)


if __name__ == "__main__":
    main()
