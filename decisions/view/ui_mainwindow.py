# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowXuYaVx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(674, 397)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_edit_decision_name = QLineEdit(self.centralwidget)
        self.line_edit_decision_name.setObjectName(u"line_edit_decision_name")
        self.line_edit_decision_name.setMinimumSize(QSize(500, 0))
        font = QFont()
        font.setPointSize(16)
        self.line_edit_decision_name.setFont(font)
        self.line_edit_decision_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.line_edit_decision_name, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableCriteria = QTableWidget(self.centralwidget)
        self.tableCriteria.setObjectName(u"tableCriteria")
        self.tableCriteria.setMinimumSize(QSize(0, 200))
        self.tableCriteria.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.tableCriteria)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_criteria_button = QPushButton(self.centralwidget)
        self.add_criteria_button.setObjectName(u"add_criteria_button")

        self.horizontalLayout_2.addWidget(self.add_criteria_button)

        self.delete_criteria_button = QPushButton(self.centralwidget)
        self.delete_criteria_button.setObjectName(u"delete_criteria_button")

        self.horizontalLayout_2.addWidget(self.delete_criteria_button)

        self.rate_criteria_button = QPushButton(self.centralwidget)
        self.rate_criteria_button.setObjectName(u"rate_criteria_button")

        self.horizontalLayout_2.addWidget(self.rate_criteria_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableAlternatives = QTableWidget(self.centralwidget)
        self.tableAlternatives.setObjectName(u"tableAlternatives")
        self.tableAlternatives.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.tableAlternatives)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_alternative_button = QPushButton(self.centralwidget)
        self.add_alternative_button.setObjectName(u"add_alternative_button")

        self.horizontalLayout_3.addWidget(self.add_alternative_button)

        self.delete_alternative_button = QPushButton(self.centralwidget)
        self.delete_alternative_button.setObjectName(u"delete_alternative_button")

        self.horizontalLayout_3.addWidget(self.delete_alternative_button)

        self.rate_alternatives_button = QPushButton(self.centralwidget)
        self.rate_alternatives_button.setObjectName(u"rate_alternatives_button")

        self.horizontalLayout_3.addWidget(self.rate_alternatives_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 674, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_edit_decision_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Decision Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Criteria", None))
        self.add_criteria_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delete_criteria_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.rate_criteria_button.setText(QCoreApplication.translate("MainWindow", u"Rate Criteria", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Alternatives:", None))
        self.add_alternative_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delete_alternative_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.rate_alternatives_button.setText(QCoreApplication.translate("MainWindow", u"Rate Alternatives", None))
    # retranslateUi

