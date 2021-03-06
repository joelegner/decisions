from PySide2 import QtWidgets
from PySide2 import QtCore
import random
import logging
import settings
from model import Decision
from model import connection_from_filename
from .ui_mainwindow import Ui_MainWindow
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from .ui_mainwindow import Ui_MainWindow


def get(url, qsargs=None, timeout=5.0):
    """Get something

:param qsargs: ARguments
:type qsargs: string
:rtype: None
"""

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._initialize()


    def _initialize(self):
        self.ui.add_criteria_button.clicked.connect(self.add_criteria)

        # Initialize criteria table
        tc = self.ui.tableCriteria
        tc.setColumnCount(3)
        tc.setHorizontalHeaderLabels(("ID", "Name", "Weight"))
        tc.horizontalHeader().setStretchLastSection(True)
        tc.horizontalHeader().setStretchLastSection(True) 
        tc.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


    def add_criteria(self):
        logging.info("Add criteria button clicked.")
        tc = self.ui.tableCriteria
        item = tc.insertRow(tc.rowCount())
        new_row_id = tc.rowCount()

        tc.setItem(new_row_id-1,0, QtWidgets.QTableWidgetItem(f"{new_row_id}"))
        
        

# class MainWin(Ui_MainWindow):
#     def __init__(self):
#         super().__init__()

#         self.conn = None

#         self.cur_filename = ""
#         self.saved = False
#         self.changed = False
#         self.decision = self.new_decision()

#         # self.setWindowTitle("Decisions %s" % settings.VERSION)

#         # # Add widgets
#         # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#         # self.new_button = QtWidgets.QPushButton("&New Decision")
#         # self.open_button = QtWidgets.QPushButton("&Open Decision File")
#         # self.exit_button = QtWidgets.QPushButton("&Quit")
#         # self.exit_button.setText("&Quit")

#         # self.recent_files_listview = QtWidgets.QListView()

#         # # Connect widgets to slots
#         # self.open_button.clicked.connect(self.open_button_click)
#         # self.exit_button.clicked.connect(self.exit_button_click)
#         # self.new_button.clicked.connect(self.new_button_click)

#         # # Layout widgets
#         # self.leftside = QtWidgets.QVBoxLayout()
#         # self.leftside.addWidget(self.new_button)
#         # self.leftside.addWidget(self.open_button)
#         # self.leftside.addWidget(self.exit_button)

#         # self.rightside = QtWidgets.QVBoxLayout()
#         # self.rightside.addWidget(QtWidgets.QLabel(
#         #     "Double Click to Open Recent File"))
#         # self.rightside.addWidget(self.recent_files_listview)

#         # self.layout = QtWidgets.QHBoxLayout()
#         # self.layout.addLayout(self.leftside)
#         # self.layout.addLayout(self.rightside)
#         # self.setLayout(self.layout)

#     def exit_button_click(self):
#         QtWidgets.QApplication.quit()

#     def open_button_click(self):
#         if self.changed and not self.saved:
#             print("TODO: Prompt to save unsaved changes")
#         fileName = QtWidgets.QFileDialog.getOpenFileName(
#             self, "Open Decision", "%", "Decision Files (*.dec)")
#         if len(fileName[0]):
#             if self.conn is not None:
#                 del self.conn
#             self.conn = connection_from_filename(fileName[0])
#             if self.decision is not None:
#                 self.setWindowTitle("%s" % self.decision.name)
#                 logging.info("Loaded decision %s from %s" %
#                              (self.decision, fileName))
#                 print("TODO: Update main window to view decision")

#     def new_decision(self):
#         if self.changed and not self.saved:
#             print("TODO: Prompt to save unsaved changes")
#         self.decision = Decision()
#         return self.decision


#     def new_button_click(self):
#         text, ok = QtWidgets.QInputDialog().getText(self, "New Decision",
#             "Decision Title:", QtWidgets.QLineEdit.Normal,
#             "Untitled Decision")
#         if ok and text:
#             self.decision = Decision(name=text)
#             return self.decision
#         else:
#             return None
