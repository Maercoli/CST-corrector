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
        MainWindow.resize(633, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 591, 121))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(158,205,221);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_correct = QPushButton(self.frame)
        self.btn_correct.setObjectName(u"btn_correct")
        self.btn_correct.setGeometry(QRect(10, 450, 591, 35))
        self.btn_correct.setMinimumSize(QSize(0, 35))
        self.btn_correct.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_correct.setStyleSheet(u"QPushButton{color:#fff;background-color:rgb(158,205,221);border:solid\n"
"0px;font:75 16px;border-radius:7px}\n"
"QPushButton:hover{background-color:rgb(67,203,99)}")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 591, 61))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color:rgb(158,205,221)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.layoutWidget)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_select = QPushButton(self.layoutWidget)
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

        self.horizontalLayout_3.addWidget(self.btn_select)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 240, 591, 51))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(158,205,221)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.txt_cfop = QLineEdit(self.layoutWidget1)
        self.txt_cfop.setObjectName(u"txt_cfop")
        self.txt_cfop.setMaxLength(4)
        self.txt_cfop.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_cfop)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 320, 591, 51))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(158,205,221)")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.txt_cst_icms = QLineEdit(self.layoutWidget2)
        self.txt_cst_icms.setObjectName(u"txt_cst_icms")
        self.txt_cst_icms.setMaxLength(3)
        self.txt_cst_icms.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_cst_icms)

        self.layoutWidget3 = QWidget(self.frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 400, 591, 44))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:rgb(158,205,221)")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.txt_cst_ipi = QLineEdit(self.layoutWidget3)
        self.txt_cst_ipi.setObjectName(u"txt_cst_ipi")
        self.txt_cst_ipi.setMaxLength(2)
        self.txt_cst_ipi.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.txt_cst_ipi)


        self.verticalLayout_5.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Corretor de CST-ICMS & CST-IPI", None))
        self.btn_correct.setText(QCoreApplication.translate("MainWindow", u"Corrigir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selecione o arquivo de SPED", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o EFD Contribicoes", None))
        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Digite o CFOP", None))
        self.txt_cfop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digite o NOVO CST-ICMS", None))
        self.txt_cst_icms.setPlaceholderText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Digite o NOVO CST-IPI", None))
        self.txt_cst_ipi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
    # retranslateUi

