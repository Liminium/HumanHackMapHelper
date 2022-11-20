from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from operator import xor
import sys


class ToggleButton(QCheckBox):
    def __init__(self, parent: QWidget,
                 w: int = 52, h: int = 30,
                 off_color: tuple[int] = (65, 65, 72),
                 circle_color: tuple[int] = (225, 225, 225),
                 on_color: tuple[int] = (185, 147, 245), *,
                 blocked_on=False,
                 alt_on_color=(142, 79, 238),
                 alt_on_circle_color=(185, 185, 185),
                 blocked_off=False,
                 alt_off_color=(65, 65, 72),
                 alt_off_circle_color=(170, 170, 170)):

        super().__init__(parent=parent)

        # Создание размера
        self.setFixedSize(w, h)

        # Изменение курсора при наведении
        self.setCursor(Qt.PointingHandCursor)

        # Создание атрибутов экземпляра
        self.off_color = off_color
        self.circle_color = circle_color
        self.on_color = on_color

        self.main_off_color = off_color
        self.main_circle_color = circle_color
        self.main_on_color = on_color
        self.alt_on_color = alt_on_color
        self.alt_on_circle_color = alt_on_circle_color
        self.alt_off_circle_color = alt_off_circle_color
        self.alt_off_color = alt_off_color

        self.set_blocked_on(blocked_on)
        self.set_blocked_off(blocked_off)

    def set_ordinary(self) -> None:
        """Sets the button swappable"""
        self.setEnabled(True)
        self.on_color = self.main_on_color
        self.off_color = self.main_off_color
        self.circle_color = self.main_circle_color
        self.setCursor(Qt.PointingHandCursor)
        self.repaint()

    def set_blocked_on(self, blocked: bool) -> None:
        """Sets the button blocked `on`"""
        if blocked:
            self.setChecked(True)
            self.setEnabled(False)
            self.on_color = self.alt_on_color
            self.circle_color = self.alt_on_circle_color
            self.setCursor(Qt.ForbiddenCursor)
            self.repaint()

    def set_blocked_off(self, blocked: bool) -> None:
        """Sets the button blocked `off`"""
        if blocked:
            self.setChecked(False)
            self.setEnabled(False)
            self.off_color = self.alt_off_color
            self.circle_color = self.alt_off_circle_color
            self.setCursor(Qt.ForbiddenCursor)
            self.repaint()

    def hitButton(self, pos: QPoint):
        """Изменение хитбокса виджета"""
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        """Рисование виджета"""
        qp = QPainter(self)

        # Устанавливаем атрибут, чтобы сглаживать края
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        # Проверка на состояние, из-за чего и будет меняться его цвет и положение кружка внутри
        if self.isChecked():
            # Настройка кисточки
            qp.setBrush(QColor(*self.on_color))
            # Рисуем прямоугольник со скругленными краями
            qp.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

            # Рисование передвигающегося круга
            qp.setBrush(QColor(*self.circle_color))
            qp.drawEllipse(self.width() - 27, 3, 24, 24)
        else:
            # Настройка кисточки
            qp.setBrush(QColor(*self.off_color))
            # Рисуем прямоугольник со скругленными краями
            qp.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

            # Рисование передвигающегося круга
            qp.setBrush(QColor(*self.circle_color))
            qp.drawEllipse(3, 3, 24, 24)

        # Конец
        qp.end()


if __name__ == '__main__':

    class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.resize(300, 300)
            button = ToggleButton(self, blocked_off=True, blocked_on=True)
            button.move(100, 100)
            self.button = QCheckBox(self)
            print([self.button.objectName()])

    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec())