import os
import cv2
import pandas as pd
import argparse


def main():


    description = """
    Function：
        获取文件夹下的所有视频文件的时长，输出excel表格
        参数
        -h : 帮助
        -i ： 指定输入文件夹
        -o ： 指定输出文件夹
        -m ： 
            1 ： 统计指定文件夹下的所有视频文件时长（包括子文件夹）
            2 ： 统计指定文件夹下的视频文件时长（不包括子文件夹）
    Example:
        # 显示帮助
        python calculate_video_duration.py -h
        # 统计指定文件夹下的所有视频文件时长（包括子文件夹）
        python calculate_video_duration.py -i  "F:\视频\01影视" -o "F:\视频\01影视" -m 1
        # 统计指定文件夹下的视频文件时长（不包括子文件夹）
        python calculate_video_duration.py -i  "F:\视频\01影视" -o "F:\视频\01影视" -m 2
    """

    end='*'.center(50,"*")
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter, epilog=f"{end}\n")
    parser.add_argument(
        '-i', '--input',type=str, help="input_dir: video folder to input", required=True)
    parser.add_argument(
        '-o', '--output',type=str, default='./',help="output_dir: where to output summary excel file", required=False)
    parser.add_argument(
        '-m', '--mode', type=str, default='1',help="whether to walk all file(include sub-folder),1:yes,2:not", required=False)


    
    args = parser.parse_args()  # 读入输入的参数，生成一个列表args
    input = args.input  # 接着对参数的任何操作，调用命名为xxx的参数方式为args.xxx
    output = args.output
    mode = args.mode

    # 如果输入的路径不存在，则报错
    if not os.path.exists(input):
        print("input path not exists")
        return

    # 选择模式
    if mode == '1':
        print("统计指定文件夹下的所有视频文件时长（包括子文件夹）")
        table = walk_videos(input)
    elif mode == '2':
        print("统计指定文件夹下的视频文件时长（不包括子文件夹）")
        table = get_videos(input)
    else:
        print("mode error")
    
    # 打印视频时长信息
    df = pd.DataFrame(table)
    print()
    print(df)

    # 保存为excel
    if output:
        mkdir(output)
        df.to_excel(os.path.join(output, 'video.xlsx'), index=False)


def walk_videos(filepath):
    """
    获取指定目录下以及目录下的所有子目录内的mp4文件的视频时长
    """
    table = []
    for path, dirs, files in os.walk(filepath):
        # 递归遍历当前py目录下的所有目录及文件，比如遍历到/a/aa/aaa/aaa.txt，则path='/a/aa/aaa/',dir=path路径下的所有文件夹名称，dir=path路径下的所有文件的名称
        # print(path)   # 当前所在路径
        # print(dirs)   # 当前所在路径下的所有目录名
        # print(files)   # 当前所在路径下的所有文件名
        for file_name in files:
            if is_video(file_name):
                file_path=os.path.join(path, file_name)
                duration = get_video_duration(file_path)
                row={"file_name":file_name,"duration":duration}
                table.append(row)
    return table


def get_videos(filepath):
    """
    获取指定目录下的mp4文件的视频时长
    """
    table = []
    for file_name in os.listdir(filepath):
            if is_video(file_name):
                file_path = os.path.join(filepath, file_name)
                duration = get_video_duration(file_path)
                row = {"file_name": file_name, "duration": duration}
                table.append(row)
    return table

def is_video(file_name):
    video_file_extensions = ('mp4','ts','mov','mov','wmv','flv','avi','mkv','mpeg','m4v','asf','f4v','rmvb' )

    if file_name.endswith((video_file_extensions)):
        return True


    
def get_video_duration(file_path):

    cap = cv2.VideoCapture(file_path)
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        rate = cap.get(5) # 获取帧率
        frame_num =cap.get(7) # 获取总帧数
        duration = frame_num/rate # 帧速率/视频总帧数 是时间,单位是秒
        return time_convert(duration)
    return -1


def time_convert(seconds):
    """
        将秒换成合适的时间，如果超过一分钟就换算成"分钟:秒",如果是小时，就换算成"小时:分钟:秒"单位换算
    """
    seconds=int(seconds)
    M, H = 60, 3600
    if seconds < M:
        return f'00:00:{zero_align(seconds)}'
    elif seconds < H:
        _M = int(seconds / M)
        _S = int(seconds % M)
        return f'00:{zero_align(_M)}:{zero_align(_S)}'
    else:
        _H = int(seconds/H)
        _M = int(seconds % H/M)
        _S = int(seconds % H % M)
        return f'{zero_align(_H)}:{zero_align(_M)}:{zero_align(_S)}'

def zero_align(num):
    """
        将数字转换成两位数字，如果是一位数字，就在前面加一个0
    """
    return f'0{num}' if num < 10 else str(num)


def mkdir(path):
    """
    创建文件夹
    """
    if not os.path.exists(path):
        os.makedirs(path)
if __name__ == "__main__":
    main()
