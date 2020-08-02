from PySide2 import QtWidgets
from PySide2 import QtCore
import random
import logging


class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.label = QtWidgets.QLabel(
            "<font color=red size=40>Hello World!</font>")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        logging.info("Randomizing the label")
        self.text.setText(random.choice(self.hello))
