from PySide6.QtCore import Signal, QObject


class MySignal(QObject):
    setweatherResult = Signal(str)
    # setProgressBar = Signal(int)


my_signal = MySignal()
