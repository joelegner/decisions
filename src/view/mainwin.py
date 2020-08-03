from PySide2 import QtWidgets
from PySide2 import QtCore
import random
import logging
import settings
from model import Decision
from model import open_decision_file


class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.cur_filename = ""
        self.saved = False
        self.changed = False
        self.decision = self.new_decision()

        self.setWindowTitle("Decisions %s" % settings.VERSION)

        # Add widgets
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.new_button = QtWidgets.QPushButton("&New Decision")
        self.open_button = QtWidgets.QPushButton("&Open Decision File")
        self.exit_button = QtWidgets.QPushButton("&Quit")
        self.exit_button.setText("&Quit")

        self.recent_files_listview = QtWidgets.QListView()

        # Connect widgets to slots
        self.open_button.clicked.connect(self.open_button_click)
        self.exit_button.clicked.connect(self.exit_button_click)

        # Layout widgets
        self.leftside = QtWidgets.QVBoxLayout()
        self.leftside.addWidget(self.new_button)
        self.leftside.addWidget(self.open_button)
        self.leftside.addWidget(self.exit_button)

        self.rightside = QtWidgets.QVBoxLayout()
        self.rightside.addWidget(QtWidgets.QLabel(
            "Double Click to Open Recent File"))
        self.rightside.addWidget(self.recent_files_listview)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.leftside)
        self.layout.addLayout(self.rightside)
        self.setLayout(self.layout)

    def exit_button_click(self):
        QtWidgets.QApplication.quit()

    def open_button_click(self):
        if self.changed and not self.saved:
            print("TODO: Prompt to save unsaved changes")
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Image", "%", "Decision Files (*.dec)")
        if len(fileName):
            decision = open_decision_file(fileName[0])
            if decision is not None:
                print("TODO: Update main window to view decision")

    def new_decision(self):
        if self.changed and not self.saved:
            print("TODO: Prompt to save unsaved changes")
        self.decision = Decision()
        return self.decision
