"""
下载梨视频的：视频ID，视频标题，视频URL地址 并写入到本次 video.csv 文件中。
"""
import requests
import config
from bs4 import BeautifulSoup


def execute():
    print("开始初始化...")
    download_video()
    print()
    print("下载完成！")
    print("-"*50)



def download_video():
    file_object = open(config.VIDEO_FILE_PATH, mode='w', encoding='utf-8')
    count = 0
    while True:
        res = requests.get(
            url="https://www.pearvideo.com/category_loading.jsp?reqType=14&categoryId=&start={}".format(
                count)
        )
        bs = BeautifulSoup(res.text, 'lxml')
        a_list = bs.find_all("a", attrs={'class': "vervideo-lilink"})
        for tag in a_list:
            title = tag.find(
                'div', attrs={'class': "vervideo-title"}).text.strip()
            video_id = tag.get('href').split('_')[-1]
            try:
                mp4_url = get_mp4_url(video_id)
            except:
                continue
            row = "{},{},{}\n".format(video_id, title, mp4_url)
            file_object.write(row)
            file_object.flush()
            count += 1
            message = "\r已下载{}个".format(count)
            print(message, end="")
            if count == config.TOTAL_COUNT:
                return 1
    file_object.close()
    

def get_mp4_url(video_id):
    data = requests.get(
        url="https://www.pearvideo.com/videoStatus.jsp?contId={}".format(
            video_id),
        headers={
            "Referer": "https://www.pearvideo.com/video_{}".format(video_id),
        }
    )
    response = data.json()
    image_url = response['videoInfo']['video_image']
    video_url = response['videoInfo']['videos']['srcUrl']
    middle = image_url.rsplit('/', 1)[-1].rsplit('-', 1)[0]
    before, after = video_url.rsplit('/', 1)
    suffix = after.split('-', 1)[-1]
    url = "{}/{}-{}".format(before, middle, suffix)
    return url


if __name__ == '__main__':
    download_video()
