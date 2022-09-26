
"""
分页看新闻（每页显示10条），提示用户输入页码，根据页码显示指定页面的数据。
    - 提示用户输入页码，根据页码显示指定页面的数据。
    - 当用户输入的页码不存在时，默认显示第1页

"""

import config


def execute():
    """ 分页看新闻 """

    # 0.计算页码最大值
    max_page_num, remain = divmod(config.TOTAL_COUNT, config.PER_PER_COUNT)
    if remain:
        max_page_num += 1
    print(f"分页看新闻：每页显示10条，共{max_page_num}页")
    while True:
        # 1.获取页码
        num = input("请输入页码(Q/q退出)：")
        if num.upper() == 'Q':
            break
        if not num.isdecimal():
            print("请输入数字！")
            continue
        num = int(num)
        if num < 1 or num > max_page_num:
            print("已超过页数范围！")
            num = 1
        page_string = f"第{num}页/共{max_page_num}页"
        print(page_string)
        # 2.获取数据
        data_list = get_page_data(num, config.PER_PER_COUNT)
        show_table(num, config.PER_PER_COUNT, data_list)
        print("-"*50)


def get_page_data(page_num, per_page_count):
    """ 根据页码获取要展示的数据列表
    :param page_num:页码
    :param per_page_count:每页数据条数
    :return:数据列表
    """
    start_index = (page_num-1)*per_page_count
    end_index = page_num*per_page_count
    data_list = []
    read_row_count =0
    with open(config.VIDEO_FILE_PATH, mode='r',encoding='utf-8') as file_object:
        for line in file_object:
            if start_index <= read_row_count < end_index:
                data_list.append(line.strip())
            if read_row_count >= end_index:
                break
            read_row_count += 1
    return data_list

def show_table(page_num, per_page_count, data_list):
    """ 在页面展示分页信息（输出）
    :param page_num:页码
    :param per_page_count:每页数据条数
    :param data_list:
    :return:
    """
    index= (page_num-1)*per_page_count+1
    for num,line in enumerate(data_list,index):
        title = line.split(',')[1]
        print(num,title)


