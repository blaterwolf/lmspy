from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class PasswordEdit(QLineEdit):
    """
    A LineEdit with icons to show/hide password entries
    """
    CSS = """QLineEdit {
        border-radius: 0px;
        height: 30px;
        margin: 0px 0px 0px 0px;
    }
    """

    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        # Set styles
        # self.setStyleSheet(self.CSS)

        self.visibleIcon = QIcon("./icons/eye_off_32x32.png")
        self.hiddenIcon = QIcon("./icons/eye_on_32x32.png")

        self.setEchoMode(QLineEdit.EchoMode.Password)
        self.togglepasswordAction = self.addAction(
            self.visibleIcon, QLineEdit.ActionPosition.TrailingPosition)
        self.togglepasswordAction.triggered.connect(
            self.on_toggle_password_Action)
        self.password_shown = False

    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)
