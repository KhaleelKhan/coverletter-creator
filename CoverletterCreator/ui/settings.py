# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setting_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_list.sizePolicy().hasHeightForWidth())
        self.setting_list.setSizePolicy(sizePolicy)
        self.setting_list.setProperty("showDropIndicator", False)
        self.setting_list.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.setting_list.setObjectName("setting_list")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.setting_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.setting_list.addItem(item)
        self.horizontalLayout.addWidget(self.setting_list)
        self.mainWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainWidget.setObjectName("mainWidget")
        self.Latex_settings = QtWidgets.QWidget()
        self.Latex_settings.setObjectName("Latex_settings")
        self.mainWidget.addWidget(self.Latex_settings)
        self.Text_settings = QtWidgets.QWidget()
        self.Text_settings.setObjectName("Text_settings")
        self.mainWidget.addWidget(self.Text_settings)
        self.horizontalLayout.addWidget(self.mainWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.setting_list.isSortingEnabled()
        self.setting_list.setSortingEnabled(False)
        item = self.setting_list.item(0)
        item.setText(_translate("MainWindow", "Latex"))
        item = self.setting_list.item(1)
        item.setText(_translate("MainWindow", "Text"))
        self.setting_list.setSortingEnabled(__sortingEnabled)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
