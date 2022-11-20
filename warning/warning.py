from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import icons


class WarningDialog(QDialog):
    def __init__(self, title: str, message: str, icon: str, *, choice: bool = False):
        super().__init__()
        uic.loadUi(r"warning\warning.ui", self)

        self.response = None

        self.title.setText(title)
        self.message.setText(message)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.title.mouseMoveEvent = self.move_window

        self.close_window_system.clicked.connect(lambda: self.close())
        self.btn_ok.clicked.connect(self.press_accept)
        self.btn_cancel.clicked.connect(self.press_cancel)

        self.icon.setPixmap(QPixmap(icon).scaled(40, 40))

        self.shadow = QGraphicsDropShadowEffect(self.frame)
        self.shadow.setBlurRadius(16)
        self.shadow.setYOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.setGraphicsEffect(self.shadow)

        self.btn_cancel.hide()
        if choice:
            self.btn_cancel.show()

    def press_accept(self):
        self.response = True
        self.close()

    def press_cancel(self):
        self.response = False
        self.close()

    def move_window(self, event):
        """Function making window able to be moved"""
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.drag_postion)
            self.drag_postion = event.globalPos()
            event.accept()

    def mousePressEvent(self, event) -> None:
        """Event activating when a mouse button getting pressed"""
        self.drag_postion = event.globalPos()
