import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPolygon, QColor, QBrush, QPen
from random import randint
from ui import Ui_Form
from numpy import random

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("")
        self.ui.Draw__.clicked.connect(self.drawf)
        self.qp = QPainter()
        self.flag = False
        self.coords = self.width()//2, self.height()//2

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, a0):
        if self.flag:
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.flag = False

    def draw(self):
        a = randint(20, 200)
        color = tuple(map(int,random.random(size=3) * 255))
        x,y = self.coords[0] - a//2 ,self.coords[1] - a//2
        self.qp.setPen(QPen(QColor(*color)))
        self.qp.setBrush(QBrush(QColor(*color)))
        self.qp.drawEllipse(x,y, a, a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = MyWidget()
    f.show()
    sys.exit(app.exec())