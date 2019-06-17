# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/progress.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        ProgressDialog.setObjectName("ProgressDialog")
        ProgressDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProgressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ProgressDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progress_bar = QtWidgets.QLabel(ProgressDialog)
        self.progress_bar.setText("")
        self.progress_bar.setPixmap(QtGui.QPixmap(":/animation/ajax-loader.gif"))
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar, 0, QtCore.Qt.AlignHCenter)
        self.log_display = QtWidgets.QPlainTextEdit(ProgressDialog)
        self.log_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.log_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_display.setReadOnly(True)
        self.log_display.setBackgroundVisible(False)
        self.log_display.setObjectName("log_display")
        self.verticalLayout.addWidget(self.log_display)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProgressDialog)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProgressDialog)
        self.buttonBox.accepted.connect(ProgressDialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(ProgressDialog)

    def retranslateUi(self, ProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressDialog.setWindowTitle(_translate("ProgressDialog", "Progress"))
        self.label.setText(_translate("ProgressDialog", "Please wait while PDF is compiled "))


import CoverletterCreator.ui.resources_rc
