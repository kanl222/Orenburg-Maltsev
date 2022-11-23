import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPolygon, QColor, QBrush, QPen
from random import randint
from PyQt5 import uic  # Импортируем uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.Draw__.clicked.connect(self.drawf)
        self.setWindowTitle("")
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
        red = 255
        green = 255
        blue = 0
        x,y = self.coords[0] - a ,self.coords[1] - a
        self.qp.setPen(QPen(QColor(red, green, blue)))
        self.qp.setBrush(QBrush(QColor(red, green, blue)))
        self.qp.drawEllipse(x,y, a, a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = MyWidget()
    f.show()
    sys.exit(app.exec())