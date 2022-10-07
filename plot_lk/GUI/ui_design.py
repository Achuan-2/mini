# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, QRect)

from PySide6.QtWidgets import (QComboBox, QDoubleSpinBox, QHBoxLayout,
                               QLabel, QLayout, QLineEdit,
                               QMenuBar, QPushButton, QScrollArea, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget)

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


class myCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setMinimumSize(self, QSize(640, 780))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 689)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_file_button = QPushButton(self.centralwidget)
        self.input_file_button.setObjectName(u"input_file_button")
        self.input_file_button.setMouseTracking(False)
        self.input_file_button.setStyleSheet(
            u"QPushButton {background-color: #A3C1DA}")

        self.verticalLayout_2.addWidget(self.input_file_button)

        self.input_file = QLabel(self.centralwidget)
        self.input_file.setObjectName(u"input_file")

        self.verticalLayout_2.addWidget(self.input_file)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.channel_combox = QComboBox(self.centralwidget)
        self.channel_combox.setObjectName(u"channel_combox")

        self.horizontalLayout.addWidget(self.channel_combox)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.time_start = QDoubleSpinBox(self.centralwidget)
        self.time_start.setObjectName(u"time_start")

        self.horizontalLayout_2.addWidget(self.time_start)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.time_end = QDoubleSpinBox(self.centralwidget)
        self.time_end.setObjectName(u"time_end")

        self.horizontalLayout_2.addWidget(self.time_end)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.y_min = QDoubleSpinBox(self.centralwidget)
        self.y_min.setObjectName(u"y_min")

        self.horizontalLayout_3.addWidget(self.y_min)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.y_max = QDoubleSpinBox(self.centralwidget)
        self.y_max.setObjectName(u"y_max")

        self.horizontalLayout_3.addWidget(self.y_max)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.x_tick_space = QDoubleSpinBox(self.centralwidget)
        self.x_tick_space.setObjectName(u"x_tick_space")
        self.x_tick_space.setDecimals(1)

        self.horizontalLayout_4.addWidget(self.x_tick_space)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.y_tick_space = QDoubleSpinBox(self.centralwidget)
        self.y_tick_space.setObjectName(u"y_tick_space")
        self.y_tick_space.setDecimals(1)

        self.horizontalLayout_4.addWidget(self.y_tick_space)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.fig_width = QDoubleSpinBox(self.centralwidget)
        self.fig_width.setObjectName(u"fig_width")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.fig_width.sizePolicy().hasHeightForWidth())
        self.fig_width.setSizePolicy(sizePolicy1)
        self.fig_width.setDecimals(1)

        self.horizontalLayout_5.addWidget(self.fig_width)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.fig_height = QDoubleSpinBox(self.centralwidget)
        self.fig_height.setObjectName(u"fig_height")
        sizePolicy1.setHeightForWidth(
            self.fig_height.sizePolicy().hasHeightForWidth())
        self.fig_height.setSizePolicy(sizePolicy1)
        self.fig_height.setDecimals(1)

        self.horizontalLayout_5.addWidget(self.fig_height)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.xlabel = QLineEdit(self.centralwidget)
        self.xlabel.setObjectName(u"xlabel")

        self.horizontalLayout_5.addWidget(self.xlabel)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_5.addWidget(self.label_21)

        self.ylabel = QLineEdit(self.centralwidget)
        self.ylabel.setObjectName(u"ylabel")

        self.horizontalLayout_5.addWidget(self.ylabel)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.height1 = QDoubleSpinBox(self.centralwidget)
        self.height1.setObjectName(u"height1")
        self.height1.setDecimals(1)
        self.height1.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.height1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.color1 = QLabel(self.centralwidget)
        self.color1.setObjectName(u"color1")

        self.horizontalLayout_11.addWidget(self.color1)

        self.color_picker1 = QPushButton(self.centralwidget)
        self.color_picker1.setObjectName(u"color_picker1")

        self.horizontalLayout_11.addWidget(self.color_picker1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.height2 = QDoubleSpinBox(self.centralwidget)
        self.height2.setObjectName(u"height2")
        self.height2.setDecimals(1)
        self.height2.setValue(1.000000000000000)

        self.horizontalLayout_9.addWidget(self.height2)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)

        self.color2 = QLabel(self.centralwidget)
        self.color2.setObjectName(u"color2")

        self.horizontalLayout_12.addWidget(self.color2)

        self.color_picker2 = QPushButton(self.centralwidget)
        self.color_picker2.setObjectName(u"color_picker2")

        self.horizontalLayout_12.addWidget(self.color_picker2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_10.addWidget(self.label_20)

        self.height3 = QDoubleSpinBox(self.centralwidget)
        self.height3.setObjectName(u"height3")
        self.height3.setDecimals(1)
        self.height3.setValue(0.400000000000000)

        self.horizontalLayout_10.addWidget(self.height3)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)

        self.color3 = QLabel(self.centralwidget)
        self.color3.setObjectName(u"color3")

        self.horizontalLayout_13.addWidget(self.color3)

        self.color_picker3 = QPushButton(self.centralwidget)
        self.color_picker3.setObjectName(u"color_picker3")

        self.horizontalLayout_13.addWidget(self.color_picker3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.plot_button = QPushButton(self.centralwidget)
        self.plot_button.setObjectName(u"plot_button")

        self.horizontalLayout_14.addWidget(self.plot_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_14.addWidget(self.save_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)

        self.view = myCanvas()
        self.scrollArea.setWidget(self.view)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.toolbar = NavigationToolbar2QT(self.view, self.scrollArea)
        self.verticalLayout_2.addWidget(self.toolbar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 634, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.input_file_button.setText(
            QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.input_file.setText(QCoreApplication.translate(
            "MainWindow", u"Filename:", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Show Channels :", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Time Start :", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Time End :", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Ymin :", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Ymax :", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"X Tick Space :", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Y Tick Space :", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Figure Size:", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u" W=", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"H=", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"xlabel", None))
        self.xlabel.setText(QCoreApplication.translate(
            "MainWindow", u"t (min)", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow", u"ylabel", None))
        self.ylabel.setText(QCoreApplication.translate(
            "MainWindow", u"cm H2O", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Chanel1 :", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"height=", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"color=", None))
        self.color1.setText(QCoreApplication.translate(
            "MainWindow", u"#046cb0", None))
        self.color_picker1.setText(QCoreApplication.translate(
            "MainWindow", u"color picker", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"Chanel2 :", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"height=", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"color=", None))
        self.color2.setText(QCoreApplication.translate(
            "MainWindow", u"#f72400", None))
        self.color_picker2.setText(QCoreApplication.translate(
            "MainWindow", u"color picker", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"Chanel3 :", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"height=", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"color=", None))
        self.color3.setText(QCoreApplication.translate(
            "MainWindow", u"#000000", None))
        self.color_picker3.setText(QCoreApplication.translate(
            "MainWindow", u"color picker", None))
        self.plot_button.setText(
            QCoreApplication.translate("MainWindow", u"Plot", None))
        self.save_button.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi
