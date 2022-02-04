# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(380, 203)
        VentanaPrincipal.setStyleSheet(u"")
        self.Evaluar = QPushButton(VentanaPrincipal)
        self.Evaluar.setObjectName(u"Evaluar")
        self.Evaluar.setGeometry(QRect(10, 130, 121, 51))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.Evaluar.setFont(font)
        self.Evaluar.setCursor(QCursor(Qt.OpenHandCursor))
        self.Evaluar.setStyleSheet(u".QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
".QPushButton {border-radius: 8px;}\n"
"")
        self.CampoCadena = QLineEdit(VentanaPrincipal)
        self.CampoCadena.setObjectName(u"CampoCadena")
        self.CampoCadena.setGeometry(QRect(50, 60, 271, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(12)
        self.CampoCadena.setFont(font1)
        self.CampoCadena.setStyleSheet(u".QLineEdit {border-radius: 8px;}\n"
"")
        self.CampoCadena.setMaxLength(9)
        self.CampoCadena.setAlignment(Qt.AlignCenter)
        self.label = QLabel(VentanaPrincipal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 171, 16))
        self.label.setFont(font1)
        self.Limpiar = QPushButton(VentanaPrincipal)
        self.Limpiar.setObjectName(u"Limpiar")
        self.Limpiar.setGeometry(QRect(140, 130, 121, 51))
        self.Limpiar.setFont(font)
        self.Limpiar.setCursor(QCursor(Qt.OpenHandCursor))
        self.Limpiar.setStyleSheet(u".QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
".QPushButton {border-radius: 8px;}\n"
"")
        self.Diagrama = QPushButton(VentanaPrincipal)
        self.Diagrama.setObjectName(u"Diagrama")
        self.Diagrama.setGeometry(QRect(270, 130, 91, 51))
        self.Diagrama.setFont(font)
        self.Diagrama.setCursor(QCursor(Qt.OpenHandCursor))
        self.Diagrama.setStyleSheet(u".QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
".QPushButton {border-radius: 8px;}\n"
"")

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Lenguajes y automatas ", None))
        self.Evaluar.setText(QCoreApplication.translate("VentanaPrincipal", u"Evaluar", None))
        self.CampoCadena.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Ingresar cadena", None))
        self.label.setText(QCoreApplication.translate("VentanaPrincipal", u"INGRESAR MATRICULA", None))
        self.Limpiar.setText(QCoreApplication.translate("VentanaPrincipal", u"Limpiar", None))
        self.Diagrama.setText(QCoreApplication.translate("VentanaPrincipal", u"Diagrama", None))
    # retranslateUi

