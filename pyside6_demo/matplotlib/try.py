import sys
from PySide6.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QComboBox, QSlider
import pandas as pd
import re
from PySide6.QtCore import Qt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setGeometry(400, 400, 900, 900)

        self.xComboBox = QComboBox(self)
        self.xComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.xLabel = QLabel("&X:")
        self.xLabel.setBuddy(self.xComboBox)

        self.yComboBox = QComboBox()
        self.yComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways", "Total fertility rate", "Life expectancy at birth"])
        self.yLabel = QLabel("Y:")
        self.yLabel.setBuddy(self.yComboBox)

        self.sComboBox = QComboBox()
        self.sComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.sLabel = QLabel("Size:")
        self.sLabel.setBuddy(self.sComboBox)

        self.cComboBox = QComboBox()
        self.cComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.cLabel = QLabel("Color:")
        self.cLabel.setBuddy(self.cComboBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.mySlider = QSlider(Qt.Horizontal, self)
        self.mySlider.setGeometry(30, 40, 200, 30)
        self.mySlider.valueChanged[int].connect(self.changeValue)

        button = QPushButton("Plot Current Attributes", self)
        button.pressed.connect(self.changeValue)

        grid = QVBoxLayout()
        grid.addWidget(self.xLabel)
        grid.addWidget(self.xComboBox)
        grid.addWidget(self.yLabel)
        grid.addWidget(self.yComboBox)
        grid.addWidget(self.sLabel)
        grid.addWidget(self.sComboBox)
        grid.addWidget(self.cLabel)
        grid.addWidget(self.cComboBox)
        grid.addWidget(self.canvas)
        grid.addWidget(self.mySlider)
        grid.addWidget(button)
        self.setLayout(grid)

    def changeValue(self, *args):
        # finding the content of current item in combo box
        x = self.xComboBox.currentText()
        y = self.yComboBox.currentText()
        s = self.sComboBox.currentText()
        c = self.cComboBox.currentText()

        #clear current figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        df = pd.read_csv("factbook.csv")

        #change column data from string to numeric
        non_decimal = re.compile(r'[^\d.]+')
        if (type(df[x][0])) == str:
            df[x] = df[x].apply(lambda x1: non_decimal.sub('',x1)).astype(float).astype(int)

        if (type(df[y][0])) == str:
            df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

        if (type(df[s][0])) == str:
            df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        if (type(df[c][0])) == str:
            df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        #change color column from continous to discrete
        df['new_c'] = (pd.cut(df[c], bins=5))

        #normalize the size data
        if len(args) == 0:
            df["s_new"] = df[s]/df[s].abs().max()
            df["s_new"] = df["s_new"] * 4
        else:
            df["s_new"] = df[s] / df[s].abs().max()
            df["s_new"] = df["s_new"] * args * 4

        #create scatter plot with new data
        b = ax.scatter(x=df[x], y=df[y], s = df["s_new"], c = df["new_c"].cat.codes)

        #create labels and title
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )

        #extract handles and labels for legend
        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        #create custom labels for size legend since automatic values will show normalized data
        num_labels = len(handles)
        labels_new = list(np.arange((min(df[s])), (max(df[s])), ((max(df[s]) - min(df[s]))/(num_labels-1))))
        labels_new = list(np.around(np.array(labels_new), 1))

        #get and adjust the position of the graoh
        box = ax.get_position()
        ax.set_position([box.x0, box.y0+ box.height * 0.15, box.width * 0.9, box.height*0.9])

        # create custom labels for color legend
        num_labels_c = len(b.legend_elements()[0])
        col_bins = pd.cut(df[c], bins=num_labels_c,precision=1)

        #color legend
        legend1 =ax.legend(b.legend_elements()[0],col_bins , title = c, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol = 5)
        ax.add_artist(legend1)

        #size legend with custom labels
        legend2 = ax.legend(handles, labels_new, loc = "center left", title=s,  bbox_to_anchor=(1, 0.5))
        ax.set(xlabel=x, ylabel =y, title=t )

        #draw new graph
        self.canvas.draw()

if __name__ == '__main__':
        # creating apyqt5 application
        app = QApplication(sys.argv)

        # creating a window object
        main = Window()

        # showing the window
        main.show()

        # loop
        sys.exit(app.exec_())