import sys
from random import randint
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QWidget
from UI import Ui_RandomCircles


class CirclesGenerator(QWidget, Ui_RandomCircles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.GenerateButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = randint(0, self.width())
        y = randint(0, self.height())
        radius = randint(10, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("black"), 2, Qt.PenStyle.SolidLine)

        for circle in self.circles:
            painter.setPen(pen)
            painter.setBrush(QBrush(circle[3]))
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cirgen = CirclesGenerator()
    cirgen.show()
    sys.exit(app.exec())
