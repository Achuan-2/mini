"""
搜索专区
    - 用户输入关键字，根据关键词筛选出所有匹配成功的短视频资讯。
    - 支持的搜索两种搜索格式：
      - `id=1747579`，筛选出id等于1747579的视频（video.csv的第一列）。
      - `key=文本`，模糊搜索，筛选包含关键字的所有新闻（video.csv的第二列）。
"""
import re
import config


def execute():
    print("欢迎搜索专区")
    while True:
        text = input(
            "请输入搜索条件，支持 [ id=视频id（如id=1747579） 或 key=文本（如key=北京 ]（Q/q退出）：")
        if text.upper() == "Q":
            break
        match_object = re.match("(id|key)=(\w+)", text.strip())
        if not match_object:
            print("输入格式错误，请重新输入")
            continue
        name, value = match_object.groups()  # 这里的groups()返回的是所有组
        mapping = {
            "id": search_by_id,
            "key": search_by_text,
        }
        data_list = mapping[name](value)
        if not data_list:
            print("没有找到匹配的视频")
        show_table(data_list)
        print("-"*50)

def search_by_id(value):
    """ 根据ID精确搜索"""
    data_list=[]
    with open(config.VIDEO_FILE_PATH,mode='r',encoding='utf-8') as file_object:
        for line in file_object:
            line = line.strip()
            if value == line.split(',')[0]:
                data_list.append(line)
                break
        return data_list

def search_by_text(value):
    """ 根据文本模糊搜索 """
    data_list = []
    with open(config.VIDEO_FILE_PATH, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            line=line.strip()
            # 这里其实没有用正则，如果是我写的话，我可能就全部读取，然后用re.findall()了
            if value in line.split(',')[1]:
                data_list.append(line)
        return data_list

def show_table(data_list):
    """ 展示 """
    for num, line in enumerate(data_list, 1):
        row_list = line.split(',')
        print(num, row_list[1])


