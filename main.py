import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class DrawYellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter(self)
        self.paint_circle(qp)

    def paint_circle(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(150, 150, randint(10, 100), randint(10, 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dc = DrawYellowCircle()
    dc.show()
    app.exec_()
