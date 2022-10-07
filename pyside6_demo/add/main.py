"""
https://gitee.com/laorange/DemoPyside6/tree/master
"""


import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import  QRunnable, Slot, Signal, QObject, QThreadPool
# PySide6-uic demo.ui -o ui_demo.py
from ui_demo import Ui_MainWindow
from utils.add import add

class WorkerSignals(QObject):
    result = Signal(str)
    progressBar = Signal(int)


class Worker(QRunnable):
    def __init__(self, a,b,time_cost,windows,*args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.a=a
        self.b=b
        self.time_cost=time_cost
        self.windows=windows
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
            for index,_ in enumerate(range(self.time_cost)):
                progress = index*100//self.time_cost
                # self.ui.progressBar.setValue(progress)
                self.signals.progressBar.emit(progress)
                time.sleep(1)
        except:
             self.signals.result.emit("Error")
        else:
            self.signals.progressBar.emit(100)
            result = str(add(self.a,self.b))
            self.signals.result.emit(result)
            self.windows.ui.inputA.setValue(self.a)
            self.windows.ui.inputB.setValue(self.b)



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        self.bind()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" %
              self.threadpool.maxThreadCount())
    
    def bind(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        self.ui.pushButton.clicked.connect(self.handle_click)
    def set_progress_bar(self, progress:int):
        self.ui.progressBar.setValue(progress)
    def set_result(self, result:str):
        self.ui.result.setText(result)
    def handle_click(self):
        a = self.ui.inputA.value()
        b = self.ui.inputB.value()
        time_cost = self.ui.timeCost.value()

        task = Worker(a,b,time_cost,self)
        task.signals.progressBar.connect(self.set_progress_bar)
        task.signals.result.connect(self.set_result)
        self.threadpool.start(task)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
