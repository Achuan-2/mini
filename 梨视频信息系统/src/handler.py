from sympy import print_rcode
from src.service import init,download, search, page


def run():
    print("欢迎来到梨视频系统")
    func_dict = {
        '0': {'title': "初始系统", 'func': init.execute},
        '1': {'title': "分页看新闻", 'func': page.execute},
        '2': {'title': "搜索专区", 'func': search.execute},
        '3': {'title': "下载专区", 'func': download.execute},
    }


    tips = ";".join(["{}.{}".format(k, v['title']) for k, v in func_dict.items()])

    while True:
        print("\n"+"="*50)
        print(tips)
        print("="*50,end="\n\n")
        choice = input("请输入序号(Q/q退出)：").strip()
        if choice.upper() == 'Q':
            break
        data_dict = func_dict.get(choice)
        if not data_dict:
            print("序号不存在，请重新输入！")
            continue

        data_dict['func']()
        if choice == '0':
            # 一旦初始化后，就不能再次初始化
            func_dict.pop('0')
            tips = ";".join(["{}.{}".format(k, v['title'])
                            for k, v in func_dict.items()])
