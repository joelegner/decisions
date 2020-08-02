from PySide2 import QtWidgets
from PySide2 import QtCore
import random
import logging
import settings


class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Decisions %s" % settings.VERSION)

        # Add widgets
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.new_button = QtWidgets.QPushButton("Start a New Decision")
        self.open_button = QtWidgets.QPushButton("Open a Decision File")
        self.exit_button = QtWidgets.QPushButton("Exit")

        # Connect widgets to slots
        self.exit_button.clicked.connect(self.exit_button_click)

        # Layout widgets
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.new_button)
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.exit_button)
        self.setLayout(self.layout)

    def exit_button_click(self):
        self.close()
