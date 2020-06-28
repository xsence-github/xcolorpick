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
        Dialog.resize(500, 320)
        Dialog.setMinimumSize(QtCore.QSize(500, 320))
        Dialog.setMaximumSize(QtCore.QSize(500, 320))
        self.xcolor = QtWidgets.QLabel(Dialog)
        self.xcolor.setGeometry(QtCore.QRect(10, 276, 90, 30))
        self.xcolor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(91, 91, 91);")
        self.xcolor.setAlignment(QtCore.Qt.AlignCenter)
        self.xcolor.setObjectName("xcolor")
        self.img_preview = QtWidgets.QLabel(Dialog)
        self.img_preview.setGeometry(QtCore.QRect(10, 10, 256, 256))
        self.img_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_preview.setText("")
        self.img_preview.setObjectName("img_preview")
        self.btn_clear = QtWidgets.QPushButton(Dialog)
        self.btn_clear.setGeometry(QtCore.QRect(274, 276, 90, 29))
        self.btn_clear.setObjectName("btn_clear")
        self.line_h = QtWidgets.QFrame(Dialog)
        self.line_h.setGeometry(QtCore.QRect(11, 135, 256, 1))
        self.line_h.setStyleSheet("color: rgb(0, 85, 255);")
        self.line_h.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_h.setLineWidth(1)
        self.line_h.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h.setObjectName("line_h")
        self.line_v = QtWidgets.QFrame(Dialog)
        self.line_v.setGeometry(QtCore.QRect(135, 11, 1, 256))
        self.line_v.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_v.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v.setObjectName("line_v")
        self.color_preview = QtWidgets.QLabel(Dialog)
        self.color_preview.setGeometry(QtCore.QRect(131, 131, 9, 9))
        self.color_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_preview.setText("")
        self.color_preview.setObjectName("color_preview")
        self.color_list = QtWidgets.QTableWidget(Dialog)
        self.color_list.setGeometry(QtCore.QRect(275, 10, 215, 256))
        self.color_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.color_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.color_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.color_list.setProperty("showDropIndicator", False)
        self.color_list.setDragDropOverwriteMode(False)
        self.color_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.color_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.color_list.setRowCount(0)
        self.color_list.setColumnCount(2)
        self.color_list.setObjectName("color_list")
        item = QtWidgets.QTableWidgetItem()
        self.color_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.color_list.setHorizontalHeaderItem(1, item)
        self.color_list.horizontalHeader().setVisible(False)
        self.color_list.horizontalHeader().setCascadingSectionResizes(True)
        self.color_list.horizontalHeader().setDefaultSectionSize(50)
        self.color_list.horizontalHeader().setHighlightSections(False)
        self.color_list.horizontalHeader().setStretchLastSection(True)
        self.color_list.verticalHeader().setVisible(False)
        self.btn_copy = QtWidgets.QPushButton(Dialog)
        self.btn_copy.setGeometry(QtCore.QRect(400, 276, 90, 29))
        self.btn_copy.setObjectName("btn_copy")
        self.label_tip = QtWidgets.QLabel(Dialog)
        self.label_tip.setGeometry(QtCore.QRect(110, 276, 161, 30))
        self.label_tip.setObjectName("label_tip")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "xcolorpick"))
        self.xcolor.setText(_translate("Dialog", "#FFFFFF"))
        self.btn_clear.setText(_translate("Dialog", "Reset"))
        item = self.color_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "list_preview"))
        item = self.color_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "list_value"))
        self.btn_copy.setText(_translate("Dialog", "Copy"))
        self.label_tip.setText(_translate("Dialog", "Alt+s: pick color"))
