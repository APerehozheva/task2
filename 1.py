import sys
import random
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Design(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(100, 100, 1200, 600)
        self.setWindowTitle('Случайные окружности')
        btn = QPushButton('Рисовать', self)
        btn.resize(500, 50)
        btn.move(10, 10)
        btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        cnt = randint(5, 25)
        a = [i for i in range(1, 256)]
        qp.setBrush(QColor(random.choice(a), random.choice(a), random.choice(a)))
        for i in range(cnt):
            x, y = randint(0, self.width()), randint(0, self.height())
            d = randint(10, 55)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Design()
    ex.show()
    sys.exit(app.exec())