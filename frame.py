# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.xcolor = QtWidgets.QLabel(Dialog)
        self.xcolor.setGeometry(QtCore.QRect(10, 254, 91, 31))
        self.xcolor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(91, 91, 91);")
        self.xcolor.setAlignment(QtCore.Qt.AlignCenter)
        self.xcolor.setObjectName("xcolor")
        self.img_preview = QtWidgets.QLabel(Dialog)
        self.img_preview.setGeometry(QtCore.QRect(10, 10, 211, 231))
        self.img_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_preview.setText("")
        self.img_preview.setObjectName("img_preview")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(295, 246, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.line_h = QtWidgets.QFrame(Dialog)
        self.line_h.setGeometry(QtCore.QRect(10, 140, 211, 20))
        self.line_h.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_h.setLineWidth(1)
        self.line_h.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h.setObjectName("line_h")
        self.line_v = QtWidgets.QFrame(Dialog)
        self.line_v.setGeometry(QtCore.QRect(110, 10, 16, 231))
        self.line_v.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_v.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v.setObjectName("line_v")
        self.color_preview = QtWidgets.QLabel(Dialog)
        self.color_preview.setGeometry(QtCore.QRect(114, 146, 8, 8))
        self.color_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_preview.setText("")
        self.color_preview.setObjectName("color_preview")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "xcolorpick"))
        self.xcolor.setText(_translate("Dialog", "#FFFFFF"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
