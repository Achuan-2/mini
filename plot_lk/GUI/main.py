
import os
import json
import pandas as pd
from functools import partial
from ui_design import Ui_MainWindow

from matplotlib.pyplot import MultipleLocator
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QMessageBox
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool


class ReadData():
    def __init__(self, input_file):
        self.filepath = input_file
        self.df = pd.read_csv(input_file,
                              sep='\t',
                              skiprows=11, header=None, usecols=[0, 1, 2, 3], names=['min', 'ch1', 'ch2', 'ch3'])
        self.time_start = round(self.df['min'].min(), 2)
        self.time_end = round(self.df['min'].max(), 2)
        self.y_min = 0
        self.y_max = self.get_ymax()

    def get_ymax(self):
        a = round(self.df['ch1'].max(), 2)
        b = round(self.df['ch2'].max(), 2)
        c = a if a > b else b
        return c

class WorkerSignals(QObject):
    fileloader = Signal(str)


class Worker(QRunnable):
    def __init__(self, input_file,windows, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.input_file = input_file
        self.windows = windows
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            self.windows.data = ReadData(self.input_file)
        except:
            self.signals.fileloader.emit('Error')
        else:
            self.signals.fileloader.emit(self.input_file)

class Worker2(QRunnable):
    def __init__(self,windows, parameters):
        super(Worker2, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.windows = windows
        self.parameters= parameters

    @Slot()
    def run(self):
            self.windows.plot_graph(**self.parameters)
            self.windows.ui.plot_button.setText('Plot')
            self.windows.ui.plot_button.setEnabled(True)
            self.windows.ui.save_button.setEnabled(True)


class MainWindow(QMainWindow):
    def __init__(self):
        # setup
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Plotting Tools for Kai Li")
        self.setup()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())
        # bind methods
        
        self.ui.input_file_button.clicked.connect(self.file_choose)
        self.ui.plot_button.clicked.connect(self.plot)
        self.ui.save_button.clicked.connect(self.save_plot)
        self.ui.color_picker1.clicked.connect(
            partial(self.color_picker, self.ui.color1))
        self.ui.color_picker2.clicked.connect(
            partial(self.color_picker, self.ui.color2))
        self.ui.color_picker3.clicked.connect(
            partial(self.color_picker, self.ui.color3))

    def setup(self):
        self.view = self.ui.view
        self.data = None
        self.ui.channel_combox.addItem('1', userData='1')
        self.ui.channel_combox.addItem('2', userData='2')
        self.ui.channel_combox.addItem('1&2', userData='both')
        self.ui.channel_combox.setCurrentText('1&2')
        self.ui.time_start.setValue(0)
        self.ui.time_end.setValue(90)
        self.ui.y_min.setValue(0)
        self.ui.y_max.setValue(10)
        self.ui.x_tick_space.setValue(5)
        self.ui.y_tick_space.setValue(1)
        self.ui.plot_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)
        # if config file exists, load it
        if os.path.exists('config.json'):
            self.loadConfig()
        else:
            self.ui.fig_height.setValue(6.3)
            self.ui.fig_width.setValue(6.3)
            self.ui.height1.setValue(1)
            self.ui.height2.setValue(1)
            self.ui.height3.setValue(0.4)
            self.ui.color1.setText('#212121')
            self.ui.color1.setStyleSheet(
                'QLabel {background-color: #212121;color:#FFF}')
            self.ui.color2.setText('#ea2000')
            self.ui.color2.setStyleSheet(
                'QLabel {background-color: #ea2000;color:#FFF}')
            self.ui.color3.setText('#3449ff')
            self.ui.color3.setStyleSheet(
                'QLabel {background-color: #3449ff;color:#FFF}')

    def loadConfig(self):
        with open('config.json', 'r') as f:
            config_dict = json.load(f)
        self.ui.fig_width.setValue(config_dict['figsize'][0])
        self.ui.fig_height.setValue(config_dict['figsize'][1])
        self.ui.xlabel.setText(config_dict['x_label'])
        self.ui.ylabel.setText(config_dict['y_label'])
        self.ui.height1.setValue(config_dict['panels_height'][0])
        self.ui.height2.setValue(config_dict['panels_height'][1])
        self.ui.height3.setValue(config_dict['panels_height'][2])
        self.ui.color1.setText(config_dict['colors_dict']['ch1'])
        self.ui.color1.setStyleSheet(
            'QLabel {background-color: '+config_dict['colors_dict']['ch1']+';color:#FFF}')
        self.ui.color2.setText(config_dict['colors_dict']['ch2'])
        self.ui.color2.setStyleSheet(
            'QLabel {background-color: '+config_dict['colors_dict']['ch2']+';color:#FFF}')
        self.ui.color3.setText(config_dict['colors_dict']['ch3'])
        self.ui.color3.setStyleSheet(
            'QLabel {background-color: '+config_dict['colors_dict']['ch3']+';color:#FFF}')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.saveConfig()
            event.accept()
        else:
            event.ignore()

    def saveConfig(self):
        config_dict = {
            'figsize': (self.ui.fig_width.value(), self.ui.fig_height.value()),
            'x_label': self.ui.xlabel.text(),
            'y_label': self.ui.ylabel.text(),
            'panels_height': [self.ui.height1.value(), self.ui.height2.value(), self.ui.height3.value()],
            'colors_dict': {
                'ch1': self.ui.color1.text(),
                'ch2': self.ui.color2.text(),
                'ch3': self.ui.color3.text()
            }
        }
        with open('config.json', 'w') as f:
            json.dump(config_dict, f, indent=4)

    def color_picker(self, color_label):
        color = QColorDialog.getColor()
        color_label.setText(color.name())
        color_label.setStyleSheet(
            'QLabel {background-color: '+color.name()+';color:#FFF}')

    def loadFileSet(self, input_file):
        self.ui.time_start.setValue(self.data.time_start)
        self.ui.time_end.setValue(self.data.time_end)
        # self.ui.time_end.setMaximum(self.data.time_end)
        self.ui.y_min.setValue(0)
        self.ui.y_max.setValue(self.data.y_max)
        self.ui.x_tick_space.setValue(
            (self.data.time_end-self.data.time_start)//5 if ((self.data.time_end-self.data.time_start) // 5) > 1 else 1)
        self.ui.y_tick_space.setValue(
            self.data.y_max//5 if (self.data.y_max // 5) > 1 else 1)
        self.ui.input_file.setText("Filename："+input_file)
        self.ui.plot_button.setEnabled(True)
        self.ui.save_button.setEnabled(True)

    def file_choose(self):
        self.ui.plot_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)
        input_file = QFileDialog.getOpenFileName(
            QMainWindow(), "Choose File")[0]
        if input_file:
            self.ui.input_file.setText("Loading File...")
            task = Worker(input_file,self)
            task.signals.fileloader.connect(self.loadFileSet)
            self.threadpool.start(task)
        else:
            return None

    def plot(self):
        para_dict = self.get_plot_parameters()
        self.ui.plot_button.setText('Plot...')
        self.ui.plot_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)

        task2 = Worker2(self,para_dict)
        self.threadpool.start(task2)

    def get_plot_parameters(self):
        time_start = self.ui.time_start.value()
        time_end = self.ui.time_end.value()
        y_min = self.ui.y_min.value()
        y_max = self.ui.y_max.value()
        channels = self.ui.channel_combox.currentData()
        x_tick_space = self.ui.x_tick_space.value()
        y_tick_space = self.ui.y_tick_space.value()
        fig_height = self.ui.fig_height.value()
        fig_width = self.ui.fig_width.value()
        height1 = self.ui.height1.value()
        height2 = self.ui.height2.value()
        height3 = self.ui.height3.value()
        color1 = self.ui.color1.text()
        color2 = self.ui.color2.text()
        color3 = self.ui.color3.text()
        xlabel = self.ui.xlabel.text()
        ylabel = self.ui.ylabel.text()
        parameters_dict = {
            'time_start': time_start,
            'time_end': time_end,
            'y_min': y_min,
            'y_max': y_max,
            'channels': channels,
            'figsize': (fig_width, fig_height),
            'panels_height': [height1, height2, height3],
            'colors_dict': {
                'ch1': color1,
                'ch2': color2,
                'ch3': color3
            },
            'x_tick_space': x_tick_space,
            'y_tick_space': y_tick_space,
            'x_label': xlabel,
            'y_label': ylabel
        }
        return parameters_dict

    def plot_graph(self, time_start=0, time_end=60, y_min=0,
                   y_max=10, channels='both', figsize=(8, 8), panels_height=[1, 1, 1],
                   colors_dict={'ch1': '#046cb0',
                                'ch2': '#f72400', 'ch3': '#000'},
                   x_tick_space=1,
                   y_tick_space=1,
                   x_label='t (min)',
                   y_label='cm H2O',
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
        try:
            df_plot = self.data.df[(self.data.df["min"] > time_start) & (
                self.data.df["min"] < time_end)].copy()
        except:
            df_plot = self.data.df
        df_plot['ch3'] = df_plot['ch3'].astype('int64')*4

        # plot
        # self.view.setMinimumSize(QSize(*figsize))
        self.view.figure.set_size_inches(*figsize)
        self.view.figure.clf()
        axes = self.view.figure.subplots(panels, 1,
                                         gridspec_kw={'height_ratios': height_ratios})

        for i, axi in enumerate(axes):
            if i < 3:
                axi.set_xlim(time_start, time_end)
                axi.set_ylim(y_min, y_max)
                axi.set_xlabel(x_label, size=12, loc="right")
                axi.set_ylabel(y_label, size=12)

            axi.plot(df_plot['min'], df_plot[channel_li[i]],
                     color=colors_dict[channel_li[i]])
            axi.margins(0)
            axi.grid(grid)
            axi.xaxis.set_major_locator(x_major_locator)
            axi.yaxis.set_major_locator(y_major_locator)
        axes[-1].axis('off')
        self.view.figure.tight_layout()
        self.view.draw()
        del df_plot

    def save_plot(self):
        file_name, _ = QFileDialog.getSaveFileName(QMainWindow(
        ), "保存图片", "", "PNG(*.png);;JPG(*.jpg);;BMP(*.bmp);;TIFF(*.tif);;PDF(*.pdf)")
        if file_name:
            self.view.figure.savefig(file_name, dpi=200)





if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    # window.showFullScreen()
    window.showMaximized()
    app.exec()  # 避免程序执行到这一行后直接退出
