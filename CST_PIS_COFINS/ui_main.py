# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 10, 641, 541))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(158,205,221);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"\n"
"color:rgb(158,205,221)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_file = QLineEdit(self.frame)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_file)

        self.btn_select = QPushButton(self.frame)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setMinimumSize(QSize(100, 31))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.btn_select.setFont(font1)
        self.btn_select.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_select.setMouseTracking(False)
        self.btn_select.setStyleSheet(u"QPushButton{color:#fff;background-color:rgb(158,205,221);border:solid\n"
"0px;font:75 16px;border-radius:7px}\n"
"QPushButton:hover{background-color:rgb(67,203,99)}")

        self.horizontalLayout.addWidget(self.btn_select)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"\n"
"color:rgb(158,205,221)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.txt_cfop = QLineEdit(self.frame)
        self.txt_cfop.setObjectName(u"txt_cfop")
        self.txt_cfop.setMaxLength(4)
        self.txt_cfop.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_cfop)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"\n"
"color:rgb(158,205,221)")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.txt_cst = QLineEdit(self.frame)
        self.txt_cst.setObjectName(u"txt_cst")
        self.txt_cst.setMaxLength(2)
        self.txt_cst.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.txt_cst)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.btn_correct = QPushButton(self.frame)
        self.btn_correct.setObjectName(u"btn_correct")
        self.btn_correct.setMinimumSize(QSize(0, 35))
        self.btn_correct.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_correct.setStyleSheet(u"QPushButton{color:#fff;background-color:rgb(158,205,221);border:solid\n"
"0px;font:75 16px;border-radius:7px}\n"
"QPushButton:hover{background-color:rgb(67,203,99)}")

        self.verticalLayout_4.addWidget(self.btn_correct)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CORRETOR DE EFD CONTRIBUICOES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selecione o arquivo de SPED", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o EFD Contribicoes", None))
        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Digite o CFOP", None))
        self.txt_cfop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digite o Novo CST", None))
        self.txt_cst.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.btn_correct.setText(QCoreApplication.translate("MainWindow", u"Corrigir", None))
    # retranslateUi

