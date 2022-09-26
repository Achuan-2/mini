
import requests
import os

COLOR = {
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'green': '\033[92m',
    'cyan': '\033[96m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'end': '\033[0m',
}

DB = {
    "1": {
        "area": "花瓣网图片专区",
        "data_dict": {
            "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
            "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
            "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
            "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
        },
        "ext": "png",
        "selected": set()
    },
    "2": {
        "area": "抖音短视频专区",
        "data_dict": {
            "1": {"title": "东北F4模仿秀",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
            "2": {"title": "卡特扣篮",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
            "3": {"title": "罗斯mvp",
                  'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
        },
        "ext": "mp4",
        "selected": set()
    },
    "3": {
        "area": "NBA锦集专区",
        "data_dict": {
            "1": {"title": "威少奇才首秀三双",
                  "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
            "2": {"title": "塔图姆三分准绝杀",
                  "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}
        },
        "ext": "mp4",
        "selected": set()
    },
}



def color(text, color):
    return f"{COLOR[color]}{text}{COLOR['end']}"
def download(file_path, url):
    file = os.path.basename(file_path)
    dir = os.path.dirname(file_path)
    if dir == '':
        dir ='当前'
    try:
        res = requests.get(
            url=url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
            }
        )
    except:
        print(color(f'下载 {file} 失败'),'red')
        return False
    else:
        with open(file_path, mode='wb') as f:
            f.write(res.content)
        print("已下载 "+color(file, 'blue')+" 至 "+color(dir, 'blue')+"文件夹")
        return True

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def handler(area_info):

    while True:
        # 进入专区提醒
        summary = color(f"\n欢迎进入{area_info['area']}", 'magenta')
        print(summary)
        ####打印可下载信息####
        text_list = []
        for num, item in area_info['data_dict'].items():
            if num in area_info['selected']:
                continue
            if type(item) == tuple:
                data = f"{num}.{item[0]}"
            else:
                data = f"{num}.{item['title']}"
            text_list.append(data)
        if text_list:
            text="; ".join(text_list)
            print(color(f"可下载列表：{text}",'cyan'))
        else:
            print(color("无可下载选项。已全部下载",'yellow'))

        ####选择下载项####
        index = input(color("请输入要选择的序号(Q/q退出）：",'green'))
        # 输入Q/q返回上一步
        if index.upper() == "Q":
            return
        # 已下载序号不能重复选择
        if index in area_info['selected']:
            print(color("已下载，无法再继续下载，请重新选择！",'red'))
            continue
        group =area_info['data_dict'].get(index)
        if not group:
            print(color("序号不存在，请重新选择",'red'))
            continue

        ####下载####
        mkdir(area_info['area'])
        if type(group) == tuple:
            title, url = group
        else:
            title, url = group['title'], group['url']
        ext = area_info['ext']
        file_path = f"{area_info['area']}/{title}.{ext}"
        flag=download(file_path, url)
        # 已下载集合添加索引
        if flag:
            area_info['selected'].add(index)



def main():

    print(COLOR['blue']+"欢迎来到资源下载器软件".center(20,'！')+COLOR['end'])

    while True:
        print('\n'+"专区列表".center(20, '*'))
        print("""
        1.花瓣网图片专区
        2.抖音短视频专区
        3.NBA锦集专区
        """)
        print("*".center(24, '*'))
        choice = input(COLOR['green']+"请输入你要进入的专区编号（Q/q退出）:"+COLOR['end'])
        if choice.upper() == "Q":
            break
        area_info=DB.get(choice)
        if not area_info:
            print(COLOR['red']+"输入有误"+COLOR['end'])
            continue
        else:
            handler(area_info)
if __name__ == '__main__':
    main()
