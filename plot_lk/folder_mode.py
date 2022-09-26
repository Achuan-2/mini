"""
------批量画图程序-------

使用说明：
- 选择输入文件的文件夹和输出文件夹
- 通过修改PARAM_DICT字典的值，来设置画图参数
"""


from tkinter import *
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 这里设置批量画图
PARAM_DICT = {
    'time_start': 0,
    'time_end': 10,
    'y_min': 0,
    'y_max': 10,
    'channels': '1',
    'figsize': (16, 4),
    'panels_height': [1, 1, 0.4],
    'colors_dict': {
        'ch1': '#046cb0',
        'ch2': '#f72400',
        'ch3': '#000'
    },
    'x_tick_space': 1,
    'y_tick_space': 2,
    'x_label':'t (min)',
    'y_label':'Voltage (mV)',
    'grid': False

}

INPUT_PATH=''
OUTPUT_PATH=''


def main():
    menu=Menu()
    menu.mainloop()    
    file_list = list_file(OUTPUT_PATH, file_ext='.txt')
    for i, file in enumerate(file_list):
        print(f'Ploting {i+1}: {file}')
        plot_main(file, OUTPUT_PATH)


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("选择文件夹")
        self.geometry("500x150")
        self.input_label = Label(self, text="数据文件夹")
        self.input_label.grid(column=0, row=0)
        self.input_path = Label(self, text="文件夹")
        self.input_path.grid(column=1, row=0)
        self.btn = Button(self, text="选择", command=self.clicked1)
        self.btn.grid(column=2, row=0)
        self.output_label = Label(self, text="输出文件夹")
        self.output_label.grid(column=0, row=1)
        self.output_path = Label(self, text="文件夹")
        self.output_path.grid(column=1, row=1)
        self.btn2 = Button(self, text="选择", command=self.clicked2)
        self.btn2.grid(column=2, row=1)
        self.btn2 = Button(self, text="确认", command=self.destroy)
        self.btn2.grid(column=2, row=2)
        self.protocol('WM_DELETE_WINDOW', self.destroy)

    def clicked1(self):
        global INPUT_PATH
        INPUT_PATH = filedialog.askdirectory(initialdir=r"./",
                                             title="Choose Folder to Input Txt")
        self.input_path.configure(text=INPUT_PATH)

    def clicked2(self):
        global OUTPUT_PATH
        OUTPUT_PATH = filedialog.askdirectory(
            initialdir=r"./", title="Choose Folder to Output Plot")
        self.output_path.configure(text=OUTPUT_PATH)

# 只列出某一文件夹的文件
def list_file(filepath, file_ext=''):
    file_list = []
    for filename in os.listdir(filepath):
        f = os.path.join(filepath, filename)
        if os.path.isfile(f):
            if file_ext:
                if os.path.splitext(f)[1] == file_ext:
                    file_list.append(f)
            else:
                file_list.append(f)
    return file_list


def plot_main(file, output_path):
    df = pd.read_csv(file, sep='\t', skiprows=11, header=None, usecols=[
                     0, 1, 2, 3], names=['min', 'ch1', 'ch2', 'ch3'])
    fig = plot_graph(
        df,
        **PARAM_DICT
    )
    output_name = os.path.basename(file).split('.')[0]
    fig.savefig(f'{output_path}/{output_name}.png', dpi=200)


def plot_graph(df, time_start=0, time_end=60, y_min=3,
               y_max=9, channels='both', figsize=(8, 8), panels_height=[1, 1, 1],
               colors_dict={'ch1': '#046cb0', 'ch2': '#f72400', 'ch3': '#000'},
               x_tick_space=1,
               y_tick_space=1,
               x_label='t (min)',
               y_label='Voltage (mV)',
               grid=False):
    # settings
    channel_dict = {
        '1': (2, ['ch1', 'ch3']),
        '2': (2, ['ch2', 'ch3']),
        'both': (3, ['ch1', 'ch2', 'ch3']),
        '12': (3, ['ch1', 'ch2', 'ch3'])
    }
    x_major_locator = MultipleLocator(x_tick_space)
    y_major_locator = MultipleLocator(y_tick_space)

    panels, channel_li = channel_dict[channels]
    height_ratios = panels_height[0:panels-1]
    height_ratios.append(panels_height[-1])

    # deal with df_plot
    df_plot = df[(df["min"] > time_start) & (df["min"] < time_end)].copy()
    df_plot['ch3'] = df_plot['ch3'].astype('int64')*4

    # plot
    fig, axes = plt.subplots(panels, 1, figsize=figsize, sharex=False, sharey=False,
                             gridspec_kw={'height_ratios': height_ratios})

    for i, axi in enumerate(axes):
        if i < 3:
            axi.set_ylim(y_min, y_max)
            axi.set_xlabel(x_label, size=12, loc="right")
            axi.set_ylabel(y_label, size=12)

        axi.plot(df_plot['min'], df_plot[channel_li[i]],
                 color=colors_dict[channel_li[i]])
        axi.margins(0)
        axi.grid(grid)
        axi.xaxis.set_major_locator(x_major_locator)
        axi.yaxis.set_major_locator(y_major_locator)
    # axes[-1].margins(y=-0.2)
    axes[-1].axis('off')
    fig.tight_layout()
    fig = plt.gcf()
    fig.set_facecolor('white')
    # plt.show()
    return fig


if __name__ == "__main__":
    main()
