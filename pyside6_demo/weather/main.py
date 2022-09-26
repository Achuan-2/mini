"""
https://zhuanlan.zhihu.com/p/521255429
"""

import json
import sys
import time
import urllib.request

from PySide6 import QtCore
from PySide6.QtWidgets import (QPushButton, QApplication,
                               QComboBox, QLabel, QWidget, QTextEdit, QGridLayout)
from threading import Thread
from signal import my_signal
class Window(QWidget):
    cityList = {
        101020100: '上海',
        101230303: '霞浦',
        101230201: '厦门',
        101230501: '泉州',
        101200101: '武汉',
        101190101: '南京',
        101270101: '成都',
        101180101: '郑州',
        101040100: '重庆',
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle('查询天气')
        self.resize(350, 300)

        city = QLabel('选择城市')
        weather = QLabel('天气')

        self.cityCombo = QComboBox()
        [self.cityCombo.addItem(self.cityList[i], userData=i)
         for i in self.cityList.keys()]

        self.button = QPushButton('查询天气')
        self.weatherResult = QTextEdit()

        grid = QGridLayout()
        # grid.setColumnMinimumWidth(0, self.width()//4)
        grid.setSpacing(10)

        grid.addWidget(city, 1, 0)
        grid.addWidget(self.cityCombo, 1, 1)
        grid.addWidget(self.button, 2, 1)
        grid.addWidget(weather, 3, 0)
        grid.addWidget(self.weatherResult, 3, 1, 5, 1)
        self.setLayout(grid)

        self.cityCombo.textActivated[str].connect(self.onActivated)
        self.button.clicked.connect(self.onClick)
        my_signal.setweatherResult.connect(self.set_weather_result)
    def set_weather_result(self, text:str):
        self.weatherResult.setText(text)
    def onActivated(self, text):
        # 选择城市后，weatherResult显示城市名称
        self.weatherResult.setText(text)


    @QtCore.Slot()
    def onClick(self):
        cityId = self.cityCombo.currentData()
        print('button clicked', self.cityList[cityId])
        self.button.setEnabled(False)
        self.weatherResult.setText(f'查询 [{self.cityList[cityId]}] 的天气...')
        task = Thread(target=self.getData, args=(cityId,))
        task.start()


    def getData(self, cityId):
        try:
            url = f"http://t.weather.sojson.com/api/weather/city/{cityId}"
            print('start downloading... ', url)
            response = urllib.request.urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            weatherdata = f"City: {data['cityInfo']['parent']} {data['cityInfo']['city']}\nUdateTime: {data['time']}\n"
            d = data['data']['forecast'][0]
            weatherdata += '\n'.join([str(k) + ': ' + str(v)
                                    for k, v in d.items() if k not in ['date', 'ymd', 'aqi']])
            time.sleep(3)
            print('downloaded, data len:', len(str(data)))
            # self.weatherResult.setText(weatherdata)
            my_signal.setweatherResult.emit(weatherdata)
        except Exception as e:
            # self.weatherResult.setText('ERROR when getting data')
            my_signal.setweatherResult.emit('ERROR when getting data')
            print(e)
        # self.cityCombo.setItemText(self.cityCombo.currentIndex(), self.cityList[cityId])
        self.cityCombo.setCurrentText(self.cityList[cityId])
        self.button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
