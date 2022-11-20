from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

import icons


class TimeHereDialog(QDialog):
    def __init__(self, time_here: str):
        super().__init__()
        uic.loadUi("time_here/time_here.ui", self)

        self.title_app_name.setText(f'Welcome, Your {time_here} time here!')

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.title.mouseMoveEvent = self.move_window

        self.close_window_system.clicked.connect(lambda: self.close())
        self.donate_button.clicked.connect(self.donate)  # todo

        self.your_time_here_label.setText(f"Your {time_here} time here")

        self.shadow = QGraphicsDropShadowEffect(self.frame)
        self.shadow.setBlurRadius(16)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.setGraphicsEffect(self.shadow)

    def donate(self) -> None:
        """Donate button"""
        ...

    def move_window(self, event) -> None:
        """Function making window able to be moved"""
        if "drag_position" in self.__dict__:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.drag_position)
                self.drag_position = event.globalPos()
                event.accept()

    def mousePressEvent(self, event) -> None:
        """Event activating when a mouse button getting pressed"""
        self.drag_position = event.globalPos()


