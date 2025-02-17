# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(540, 302)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.setting_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_list.sizePolicy().hasHeightForWidth())
        self.setting_list.setSizePolicy(sizePolicy)
        self.setting_list.setMaximumSize(QtCore.QSize(120, 16777215))
        self.setting_list.setLineWidth(1)
        self.setting_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setting_list.setProperty("showDropIndicator", False)
        self.setting_list.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.setting_list.setAlternatingRowColors(True)
        self.setting_list.setObjectName("setting_list")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.setting_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.setting_list.addItem(item)
        self.verticalLayout_4.addWidget(self.setting_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.mainWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.Latex_settings = QtWidgets.QWidget()
        self.Latex_settings.setObjectName("Latex_settings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Latex_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.Latex_settings)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.le_latex_tempate = QtWidgets.QLineEdit(self.Latex_settings)
        self.le_latex_tempate.setObjectName("le_latex_tempate")
        self.horizontalLayout_2.addWidget(self.le_latex_tempate)
        self.pb_browse_latex_tempate = QtWidgets.QPushButton(self.Latex_settings)
        self.pb_browse_latex_tempate.setObjectName("pb_browse_latex_tempate")
        self.horizontalLayout_2.addWidget(self.pb_browse_latex_tempate, 0, QtCore.Qt.AlignRight)
        self.icon_latex_template = QtWidgets.QLabel(self.Latex_settings)
        self.icon_latex_template.setMaximumSize(QtCore.QSize(16, 16))
        self.icon_latex_template.setToolTip("")
        self.icon_latex_template.setStatusTip("")
        self.icon_latex_template.setText("")
        self.icon_latex_template.setPixmap(QtGui.QPixmap(":/icons/notokay.png"))
        self.icon_latex_template.setScaledContents(True)
        self.icon_latex_template.setObjectName("icon_latex_template")
        self.horizontalLayout_2.addWidget(self.icon_latex_template)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.Latex_settings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_latex_out_dir = QtWidgets.QLineEdit(self.Latex_settings)
        self.le_latex_out_dir.setObjectName("le_latex_out_dir")
        self.horizontalLayout_3.addWidget(self.le_latex_out_dir)
        self.pb_browse_latex_dir = QtWidgets.QPushButton(self.Latex_settings)
        self.pb_browse_latex_dir.setObjectName("pb_browse_latex_dir")
        self.horizontalLayout_3.addWidget(self.pb_browse_latex_dir, 0, QtCore.Qt.AlignRight)
        self.icon_latex_output = QtWidgets.QLabel(self.Latex_settings)
        self.icon_latex_output.setMaximumSize(QtCore.QSize(16, 16))
        self.icon_latex_output.setText("")
        self.icon_latex_output.setPixmap(QtGui.QPixmap(":/icons/notokay.png"))
        self.icon_latex_output.setScaledContents(True)
        self.icon_latex_output.setObjectName("icon_latex_output")
        self.horizontalLayout_3.addWidget(self.icon_latex_output)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cb_keep_tex = QtWidgets.QCheckBox(self.Latex_settings)
        self.cb_keep_tex.setObjectName("cb_keep_tex")
        self.verticalLayout.addWidget(self.cb_keep_tex)
        self.line = QtWidgets.QFrame(self.Latex_settings)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.groupBox = QtWidgets.QGroupBox(self.Latex_settings)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.combo_latex_compiler = QtWidgets.QComboBox(self.groupBox)
        self.combo_latex_compiler.setObjectName("combo_latex_compiler")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_latex_compiler)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.le_custom_latex = QtWidgets.QLineEdit(self.groupBox)
        self.le_custom_latex.setEnabled(False)
        self.le_custom_latex.setClearButtonEnabled(False)
        self.le_custom_latex.setObjectName("le_custom_latex")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_custom_latex)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.cb_open_pdf_after = QtWidgets.QCheckBox(self.groupBox)
        self.cb_open_pdf_after.setObjectName("cb_open_pdf_after")
        self.verticalLayout_2.addWidget(self.cb_open_pdf_after)
        self.verticalLayout.addWidget(self.groupBox)
        self.latex_buttonBox = QtWidgets.QDialogButtonBox(self.Latex_settings)
        self.latex_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.latex_buttonBox.setObjectName("latex_buttonBox")
        self.verticalLayout.addWidget(self.latex_buttonBox)
        self.mainWidget.addWidget(self.Latex_settings)
        self.Text_settings = QtWidgets.QWidget()
        self.Text_settings.setObjectName("Text_settings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Text_settings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.Text_settings)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.le_text_template = QtWidgets.QLineEdit(self.Text_settings)
        self.le_text_template.setObjectName("le_text_template")
        self.horizontalLayout_5.addWidget(self.le_text_template)
        self.pb_browse_text_template = QtWidgets.QPushButton(self.Text_settings)
        self.pb_browse_text_template.setObjectName("pb_browse_text_template")
        self.horizontalLayout_5.addWidget(self.pb_browse_text_template, 0, QtCore.Qt.AlignRight)
        self.icon_text_template = QtWidgets.QLabel(self.Text_settings)
        self.icon_text_template.setMaximumSize(QtCore.QSize(16, 16))
        self.icon_text_template.setToolTip("")
        self.icon_text_template.setStatusTip("")
        self.icon_text_template.setText("")
        self.icon_text_template.setPixmap(QtGui.QPixmap(":/icons/notokay.png"))
        self.icon_text_template.setScaledContents(True)
        self.icon_text_template.setObjectName("icon_text_template")
        self.horizontalLayout_5.addWidget(self.icon_text_template)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.Text_settings)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.le_text_out_dir = QtWidgets.QLineEdit(self.Text_settings)
        self.le_text_out_dir.setObjectName("le_text_out_dir")
        self.horizontalLayout_4.addWidget(self.le_text_out_dir)
        self.pb_browse_text_dir = QtWidgets.QPushButton(self.Text_settings)
        self.pb_browse_text_dir.setObjectName("pb_browse_text_dir")
        self.horizontalLayout_4.addWidget(self.pb_browse_text_dir, 0, QtCore.Qt.AlignRight)
        self.icon_text_output = QtWidgets.QLabel(self.Text_settings)
        self.icon_text_output.setMaximumSize(QtCore.QSize(16, 16))
        self.icon_text_output.setText("")
        self.icon_text_output.setPixmap(QtGui.QPixmap(":/icons/notokay.png"))
        self.icon_text_output.setScaledContents(True)
        self.icon_text_output.setObjectName("icon_text_output")
        self.horizontalLayout_4.addWidget(self.icon_text_output)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.cb_open_text_after = QtWidgets.QCheckBox(self.Text_settings)
        self.cb_open_text_after.setObjectName("cb_open_text_after")
        self.verticalLayout_3.addWidget(self.cb_open_text_after)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.text_buttonBox = QtWidgets.QDialogButtonBox(self.Text_settings)
        self.text_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.text_buttonBox.setObjectName("text_buttonBox")
        self.verticalLayout_3.addWidget(self.text_buttonBox)
        self.mainWidget.addWidget(self.Text_settings)
        self.horizontalLayout.addWidget(self.mainWidget)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        self.mainWidget.setCurrentIndex(1)
        self.setting_list.currentRowChanged['int'].connect(self.mainWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        __sortingEnabled = self.setting_list.isSortingEnabled()
        self.setting_list.setSortingEnabled(False)
        item = self.setting_list.item(0)
        item.setText(_translate("SettingsWindow", "Latex"))
        item = self.setting_list.item(1)
        item.setText(_translate("SettingsWindow", "Text"))
        self.setting_list.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("SettingsWindow", "Template File"))
        self.pb_browse_latex_tempate.setText(_translate("SettingsWindow", "..."))
        self.icon_latex_template.setWhatsThis(_translate("SettingsWindow", "Folder does not exist"))
        self.label_2.setText(_translate("SettingsWindow", "Output Directory"))
        self.pb_browse_latex_dir.setText(_translate("SettingsWindow", "..."))
        self.icon_latex_output.setWhatsThis(_translate("SettingsWindow", "Folder does not exist"))
        self.cb_keep_tex.setText(_translate("SettingsWindow", "Keep .tex file"))
        self.groupBox.setTitle(_translate("SettingsWindow", "Compiler Options"))
        self.label_5.setText(_translate("SettingsWindow", "Latex compiler"))
        self.label_6.setText(_translate("SettingsWindow", "Custom Command"))
        self.cb_open_pdf_after.setText(_translate("SettingsWindow", "Open pdf file after compilation"))
        self.label_9.setText(_translate("SettingsWindow", "Template File"))
        self.pb_browse_text_template.setText(_translate("SettingsWindow", "..."))
        self.icon_text_template.setWhatsThis(_translate("SettingsWindow", "Folder does not exist"))
        self.label_7.setText(_translate("SettingsWindow", "Output Directory"))
        self.pb_browse_text_dir.setText(_translate("SettingsWindow", "..."))
        self.icon_text_output.setWhatsThis(_translate("SettingsWindow", "Folder does not exist"))
        self.cb_open_text_after.setText(_translate("SettingsWindow", "Open text file after compiling"))


import CoverletterCreator.ui.resources_rc
