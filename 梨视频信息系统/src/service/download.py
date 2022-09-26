
"""
下载专区

    - 用户输入视频id，根据id找到对应的mp4视频下载地址，然后下载视频到项目的files目录。
    - 视频的文件名为：`视频id-年-月-日-时-分-秒.mp4`
    - 下载的过程中，输出已下载的百分比，示例代码如下：
"""
import re
import os
import time
from datetime import datetime
import requests
import config


def execute():
    print("欢迎来到下载专区")
    while True:
        video_id = input("请输入要下载的视频ID,如1747579(Q/q退出)：")
        if  video_id.upper() == 'Q':
            break
        match_group = re.match("\d{7}",  video_id.strip())
        if not match_group:
            print("ID格式错误，请重新输入")
            continue
        vide_url = get_mp4_url(video_id)
        if not vide_url:
            print("没有找到视频")
            continue
        download_mp4(video_id, vide_url)

def get_mp4_url(video_id):
    """ 根据视频ID或者视频链接"""
    with open(config.VIDEO_FILE_PATH,mode='r',encoding='utf-8') as file_object:
        for line in file_object:
            if video_id in line:
                data = line.strip().split(",")
                vid=data[0]
                url=data[2]
                if video_id == vid:
                    return url


def download_mp4(video_id, video_url):
    """ 下载视频 """
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    mkdir(os.path.join(config.BASE_DIR, 'files'))
    file_path = os.path.join(config.BASE_DIR, 'files',
                            "{}-{}.mp4".format(video_id, current_time))
    res = requests.get(url=video_url)
    print("正在下载中...")
    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])
    download_size = 0
    with open(file_path, mode='wb') as file_object:
        for chunk in res.iter_content(128):
            download_size += len(chunk)
            file_object.write(chunk)
            # 将缓冲区中的数据立刻写入文件，同时清空缓冲区
            file_object.flush()
            percent = "\r{}%".format(
                int(round(download_size / file_size, 2) * 100))
            print(percent, end="")
        file_object.close()
    print("\n下载完成")
    print("-"*50)
    res.close()


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)
