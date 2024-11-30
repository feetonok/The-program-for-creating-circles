import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QWidget


class CirclesGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

        uic.loadUi('UI.ui', self)

        self.GenerateButton.clicked.connect(self.generate_circles)

    def generate_circles(self):
        x = randint(0, self.width())
        y = randint(0, self.height())
        radius = randint(10, 50)
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("black"), 2, Qt.PenStyle.SolidLine)
        brush = QBrush(QColor('yellow'))

        for circle in self.circles:
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cirgen = CirclesGenerator()
    cirgen.show()
    sys.exit(app.exec())
