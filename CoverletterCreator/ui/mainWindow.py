# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 466)
        MainWindow.setMinimumSize(QtCore.QSize(616, 466))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.tabPersonal = QtWidgets.QWidget()
        self.tabPersonal.setObjectName("tabPersonal")
        self.personalInfo_layout = QtWidgets.QFormLayout(self.tabPersonal)
        self.personalInfo_layout.setObjectName("personalInfo_layout")
        self.label = QtWidgets.QLabel(self.tabPersonal)
        self.label.setObjectName("label")
        self.personalInfo_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.FIRSTNAME = QtWidgets.QLineEdit(self.tabPersonal)
        self.FIRSTNAME.setObjectName("FIRSTNAME")
        self.personalInfo_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FIRSTNAME)
        self.label_2 = QtWidgets.QLabel(self.tabPersonal)
        self.label_2.setObjectName("label_2")
        self.personalInfo_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tabPersonal)
        self.label_3.setObjectName("label_3")
        self.personalInfo_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.LASTNAME = QtWidgets.QLineEdit(self.tabPersonal)
        self.LASTNAME.setObjectName("LASTNAME")
        self.personalInfo_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LASTNAME)
        self.label_4 = QtWidgets.QLabel(self.tabPersonal)
        self.label_4.setObjectName("label_4")
        self.personalInfo_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.tabPersonal)
        self.label_5.setObjectName("label_5")
        self.personalInfo_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tabPersonal)
        self.label_6.setObjectName("label_6")
        self.personalInfo_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.tabPersonal)
        self.label_7.setObjectName("label_7")
        self.personalInfo_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tabPersonal)
        self.label_8.setObjectName("label_8")
        self.personalInfo_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.MOBILE = QtWidgets.QLineEdit(self.tabPersonal)
        self.MOBILE.setObjectName("MOBILE")
        self.personalInfo_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.MOBILE)
        self.EMAIL = QtWidgets.QLineEdit(self.tabPersonal)
        self.EMAIL.setObjectName("EMAIL")
        self.personalInfo_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.EMAIL)
        self.HOMEPAGE = QtWidgets.QLineEdit(self.tabPersonal)
        self.HOMEPAGE.setObjectName("HOMEPAGE")
        self.personalInfo_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.HOMEPAGE)
        self.GITHUBNAME = QtWidgets.QLineEdit(self.tabPersonal)
        self.GITHUBNAME.setObjectName("GITHUBNAME")
        self.personalInfo_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.GITHUBNAME)
        self.LINKEDINNAME = QtWidgets.QLineEdit(self.tabPersonal)
        self.LINKEDINNAME.setObjectName("LINKEDINNAME")
        self.personalInfo_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.LINKEDINNAME)
        self.PERSONALADDRESS = QtWidgets.QPlainTextEdit(self.tabPersonal)
        self.PERSONALADDRESS.setObjectName("PERSONALADDRESS")
        self.personalInfo_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PERSONALADDRESS)
        self.mainTabWidget.addTab(self.tabPersonal, "")
        self.tabCompany = QtWidgets.QWidget()
        self.tabCompany.setObjectName("tabCompany")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabCompany)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.tabCompany)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.COMPANYNAME = QtWidgets.QLineEdit(self.tabCompany)
        self.COMPANYNAME.setObjectName("COMPANYNAME")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.COMPANYNAME)
        self.label_10 = QtWidgets.QLabel(self.tabCompany)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.COMPANYSHORTNAME = QtWidgets.QLineEdit(self.tabCompany)
        self.COMPANYSHORTNAME.setObjectName("COMPANYSHORTNAME")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.COMPANYSHORTNAME)
        self.label_11 = QtWidgets.QLabel(self.tabCompany)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.DEPARTMENT = QtWidgets.QLineEdit(self.tabCompany)
        self.DEPARTMENT.setObjectName("DEPARTMENT")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DEPARTMENT)
        self.label_12 = QtWidgets.QLabel(self.tabCompany)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.COMPANYADDRESS = QtWidgets.QPlainTextEdit(self.tabCompany)
        self.COMPANYADDRESS.setObjectName("COMPANYADDRESS")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.COMPANYADDRESS)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.line = QtWidgets.QFrame(self.tabCompany)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.tabCompany)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.LETTERTITLE = QtWidgets.QLineEdit(self.tabCompany)
        self.LETTERTITLE.setObjectName("LETTERTITLE")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LETTERTITLE)
        self.label_14 = QtWidgets.QLabel(self.tabCompany)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.tabCompany)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.JOBTITLE = QtWidgets.QLineEdit(self.tabCompany)
        self.JOBTITLE.setObjectName("JOBTITLE")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.JOBTITLE)
        self.JOBREFID = QtWidgets.QLineEdit(self.tabCompany)
        self.JOBREFID.setObjectName("JOBREFID")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.JOBREFID)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.line_2 = QtWidgets.QFrame(self.tabCompany)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.tabCompany)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)
        self.RECEIPIENTGENDER = QtWidgets.QComboBox(self.tabCompany)
        self.RECEIPIENTGENDER.setEditable(True)
        self.RECEIPIENTGENDER.setObjectName("RECEIPIENTGENDER")
        self.RECEIPIENTGENDER.addItem("")
        self.RECEIPIENTGENDER.addItem("")
        self.RECEIPIENTGENDER.addItem("")
        self.RECEIPIENTGENDER.addItem("")
        self.RECEIPIENTGENDER.addItem("")
        self.RECEIPIENTGENDER.addItem("")
        self.gridLayout.addWidget(self.RECEIPIENTGENDER, 0, 2, 1, 1)
        self.RECEIPIENTNAME = QtWidgets.QLineEdit(self.tabCompany)
        self.RECEIPIENTNAME.setObjectName("RECEIPIENTNAME")
        self.gridLayout.addWidget(self.RECEIPIENTNAME, 0, 3, 1, 1)
        self.RECEIPIENTSALUTATION = QtWidgets.QComboBox(self.tabCompany)
        self.RECEIPIENTSALUTATION.setEditable(True)
        self.RECEIPIENTSALUTATION.setObjectName("RECEIPIENTSALUTATION")
        self.RECEIPIENTSALUTATION.addItem("")
        self.RECEIPIENTSALUTATION.addItem("")
        self.gridLayout.addWidget(self.RECEIPIENTSALUTATION, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.mainTabWidget.addTab(self.tabCompany, "")
        self.tabAboutMe = QtWidgets.QWidget()
        self.tabAboutMe.setObjectName("tabAboutMe")
        self.verticalLayout_AboutMeTab = QtWidgets.QVBoxLayout(self.tabAboutMe)
        self.verticalLayout_AboutMeTab.setObjectName("verticalLayout_AboutMeTab")
        self.label_17 = QtWidgets.QLabel(self.tabAboutMe)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_AboutMeTab.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainTabWidget.addTab(self.tabAboutMe, "")
        self.tabWhyFirm = QtWidgets.QWidget()
        self.tabWhyFirm.setObjectName("tabWhyFirm")
        self.verticalLayout_WhyFirmTab = QtWidgets.QVBoxLayout(self.tabWhyFirm)
        self.verticalLayout_WhyFirmTab.setObjectName("verticalLayout_WhyFirmTab")
        self.label_18 = QtWidgets.QLabel(self.tabWhyFirm)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_WhyFirmTab.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainTabWidget.addTab(self.tabWhyFirm, "")
        self.tabWhyYou = QtWidgets.QWidget()
        self.tabWhyYou.setObjectName("tabWhyYou")
        self.verticalLayout_WhyYouTab = QtWidgets.QVBoxLayout(self.tabWhyYou)
        self.verticalLayout_WhyYouTab.setObjectName("verticalLayout_WhyYouTab")
        self.label_19 = QtWidgets.QLabel(self.tabWhyYou)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_WhyYouTab.addWidget(self.label_19, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainTabWidget.addTab(self.tabWhyYou, "")
        self.tabFinish = QtWidgets.QWidget()
        self.tabFinish.setObjectName("tabFinish")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabFinish)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.tabFinish)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_20 = QtWidgets.QLabel(self.tabFinish)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)
        self.ENCLOSINGPREFIX = QtWidgets.QLineEdit(self.tabFinish)
        self.ENCLOSINGPREFIX.setObjectName("ENCLOSINGPREFIX")
        self.gridLayout_2.addWidget(self.ENCLOSINGPREFIX, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.CLOSINGSALUTATION = QtWidgets.QLineEdit(self.tabFinish)
        self.CLOSINGSALUTATION.setObjectName("CLOSINGSALUTATION")
        self.gridLayout_2.addWidget(self.CLOSINGSALUTATION, 0, 1, 1, 2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CVATTACHED = QtWidgets.QCheckBox(self.tabFinish)
        self.CVATTACHED.setObjectName("CVATTACHED")
        self.verticalLayout_7.addWidget(self.CVATTACHED)
        self.TRANSCRIPTSATTACHED = QtWidgets.QCheckBox(self.tabFinish)
        self.TRANSCRIPTSATTACHED.setObjectName("TRANSCRIPTSATTACHED")
        self.verticalLayout_7.addWidget(self.TRANSCRIPTSATTACHED)
        self.CERTIFICATESATTACHED = QtWidgets.QCheckBox(self.tabFinish)
        self.CERTIFICATESATTACHED.setObjectName("CERTIFICATESATTACHED")
        self.verticalLayout_7.addWidget(self.CERTIFICATESATTACHED)
        self.REFLETTERSATTACHED = QtWidgets.QCheckBox(self.tabFinish)
        self.REFLETTERSATTACHED.setObjectName("REFLETTERSATTACHED")
        self.verticalLayout_7.addWidget(self.REFLETTERSATTACHED)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tabFinish)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PHOTOPATH = QtWidgets.QLineEdit(self.tabFinish)
        self.PHOTOPATH.setReadOnly(True)
        self.PHOTOPATH.setObjectName("PHOTOPATH")
        self.horizontalLayout_2.addWidget(self.PHOTOPATH, 0, QtCore.Qt.AlignTop)
        self.pb_browsePhoto = QtWidgets.QPushButton(self.tabFinish)
        self.pb_browsePhoto.setObjectName("pb_browsePhoto")
        self.horizontalLayout_2.addWidget(self.pb_browsePhoto, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.label_pic = QtWidgets.QLabel(self.tabFinish)
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.gridLayout_2.addWidget(self.label_pic, 2, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_generatePdf = QtWidgets.QPushButton(self.tabFinish)
        self.pb_generatePdf.setObjectName("pb_generatePdf")
        self.horizontalLayout.addWidget(self.pb_generatePdf)
        self.pb_generateText = QtWidgets.QPushButton(self.tabFinish)
        self.pb_generateText.setObjectName("pb_generateText")
        self.horizontalLayout.addWidget(self.pb_generateText)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.mainTabWidget.addTab(self.tabFinish, "")
        self.verticalLayout.addWidget(self.mainTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOutput = QtWidgets.QMenu(self.menubar)
        self.menuOutput.setObjectName("menuOutput")
        self.menuLatex = QtWidgets.QMenu(self.menuOutput)
        self.menuLatex.setObjectName("menuLatex")
        self.menuText = QtWidgets.QMenu(self.menuOutput)
        self.menuText.setObjectName("menuText")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSet_LatexTemplate = QtWidgets.QAction(MainWindow)
        self.actionSet_LatexTemplate.setObjectName("actionSet_LatexTemplate")
        self.actionSet_LatexOutputDirectory = QtWidgets.QAction(MainWindow)
        self.actionSet_LatexOutputDirectory.setObjectName("actionSet_LatexOutputDirectory")
        self.actionText_Template = QtWidgets.QAction(MainWindow)
        self.actionText_Template.setObjectName("actionText_Template")
        self.actionCompiler_2 = QtWidgets.QAction(MainWindow)
        self.actionCompiler_2.setObjectName("actionCompiler_2")
        self.actionSet_TextOutputDirectory = QtWidgets.QAction(MainWindow)
        self.actionSet_TextOutputDirectory.setObjectName("actionSet_TextOutputDirectory")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuLatex.addAction(self.actionSet_LatexTemplate)
        self.menuLatex.addAction(self.actionSet_LatexOutputDirectory)
        self.menuLatex.addAction(self.actionCompiler_2)
        self.menuText.addAction(self.actionText_Template)
        self.menuText.addAction(self.actionSet_TextOutputDirectory)
        self.menuOutput.addSeparator()
        self.menuOutput.addAction(self.menuLatex.menuAction())
        self.menuOutput.addAction(self.menuText.menuAction())
        self.menuOutput.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOutput.menuAction())

        self.retranslateUi(MainWindow)
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coverletter Creator"))
        self.label.setAccessibleName(_translate("MainWindow", "FIRSTNAME"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setAccessibleName(_translate("MainWindow", "LASTNAME"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setAccessibleName(_translate("MainWindow", "PERSONALADDRESS"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_4.setAccessibleName(_translate("MainWindow", "MOBILE"))
        self.label_4.setText(_translate("MainWindow", "Mobile"))
        self.label_5.setAccessibleName(_translate("MainWindow", "EMAIL"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.label_6.setAccessibleName(_translate("MainWindow", "HOMEPAGE"))
        self.label_6.setText(_translate("MainWindow", "Homepage"))
        self.label_7.setAccessibleName(_translate("MainWindow", "GITHUBNAME"))
        self.label_7.setText(_translate("MainWindow", "Github"))
        self.label_8.setAccessibleName(_translate("MainWindow", "LINKEDINNAME"))
        self.label_8.setText(_translate("MainWindow", "Linkedin"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabPersonal), _translate("MainWindow", "Personal Info"))
        self.label_9.setAccessibleName(_translate("MainWindow", "COMPANYNAME"))
        self.label_9.setText(_translate("MainWindow", "Company Name"))
        self.COMPANYNAME.setToolTip(_translate("MainWindow", "Full company name, for example: Intel Deutschland GmbH"))
        self.label_10.setAccessibleName(_translate("MainWindow", "COMPANYSHORTNAME"))
        self.label_10.setText(_translate("MainWindow", "Company Short Name"))
        self.COMPANYSHORTNAME.setToolTip(_translate("MainWindow", "Company Short name, for example: Intel"))
        self.label_11.setAccessibleName(_translate("MainWindow", "DEPARTMENT"))
        self.label_11.setText(_translate("MainWindow", "Department"))
        self.DEPARTMENT.setText(_translate("MainWindow", "Human Resources"))
        self.label_12.setAccessibleName(_translate("MainWindow", "COMPANYADDRESS"))
        self.label_12.setText(_translate("MainWindow", "Address"))
        self.label_13.setAccessibleName(_translate("MainWindow", "LETTERTITLE"))
        self.label_13.setText(_translate("MainWindow", "Letter Title"))
        self.LETTERTITLE.setText(_translate("MainWindow", "Job Application for"))
        self.label_14.setAccessibleName(_translate("MainWindow", "JOBTITLE"))
        self.label_14.setText(_translate("MainWindow", "Job Title"))
        self.label_15.setAccessibleName(_translate("MainWindow", "JOBREFID"))
        self.label_15.setText(_translate("MainWindow", "Job Referrence ID"))
        self.label_16.setAccessibleName(_translate("MainWindow", "RECEIPIENTNAME"))
        self.label_16.setText(_translate("MainWindow", "Recipient"))
        self.RECEIPIENTGENDER.setAccessibleName(_translate("MainWindow", "RECEIPIENTGENDER"))
        self.RECEIPIENTGENDER.setItemText(0, _translate("MainWindow", "Mr."))
        self.RECEIPIENTGENDER.setItemText(1, _translate("MainWindow", "Ms."))
        self.RECEIPIENTGENDER.setItemText(2, _translate("MainWindow", "Unknown"))
        self.RECEIPIENTGENDER.setItemText(3, _translate("MainWindow", "Mrs."))
        self.RECEIPIENTGENDER.setItemText(4, _translate("MainWindow", "Dr."))
        self.RECEIPIENTGENDER.setItemText(5, _translate("MainWindow", "Prof."))
        self.RECEIPIENTSALUTATION.setAccessibleName(_translate("MainWindow", "RECEIPIENTSALUTATION"))
        self.RECEIPIENTSALUTATION.setItemText(0, _translate("MainWindow", "Dear"))
        self.RECEIPIENTSALUTATION.setItemText(1, _translate("MainWindow", "Hello"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabCompany), _translate("MainWindow", "Company Info"))
        self.label_17.setAccessibleName(_translate("MainWindow", "TEXTABOUTME"))
        self.label_17.setText(_translate("MainWindow", "Give a short introduction about yourself"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabAboutMe), _translate("MainWindow", "About me"))
        self.label_18.setAccessibleName(_translate("MainWindow", "TEXTWHYTHISFIRM"))
        self.label_18.setText(_translate("MainWindow", "Why did you choose this particular firm?"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabWhyFirm), _translate("MainWindow", "Why this Firm?"))
        self.label_19.setAccessibleName(_translate("MainWindow", "TEXTWHYYOU"))
        self.label_19.setText(_translate("MainWindow", "Specify why you are the perfect fit for this job?"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabWhyYou), _translate("MainWindow", "Why You?"))
        self.label_21.setAccessibleName(_translate("MainWindow", "ENCLOSINGPREFIX"))
        self.label_21.setText(_translate("MainWindow", "Enclosing"))
        self.label_20.setAccessibleName(_translate("MainWindow", "CLOSINGSALUTATION"))
        self.label_20.setText(_translate("MainWindow", "Letter Closing"))
        self.ENCLOSINGPREFIX.setText(_translate("MainWindow", "Attached "))
        self.CLOSINGSALUTATION.setText(_translate("MainWindow", "Sincerely"))
        self.CVATTACHED.setAccessibleName(_translate("MainWindow", "CVATTACHED"))
        self.CVATTACHED.setText(_translate("MainWindow", "Curriculum Vitae"))
        self.TRANSCRIPTSATTACHED.setAccessibleName(_translate("MainWindow", "TRANSCRIPTSATTACHED"))
        self.TRANSCRIPTSATTACHED.setText(_translate("MainWindow", "Transcripts"))
        self.CERTIFICATESATTACHED.setAccessibleName(_translate("MainWindow", "CERTIFICATESATTACHED"))
        self.CERTIFICATESATTACHED.setText(_translate("MainWindow", "Certificates"))
        self.REFLETTERSATTACHED.setAccessibleName(_translate("MainWindow", "REFLETTERSATTACHED"))
        self.REFLETTERSATTACHED.setText(_translate("MainWindow", "Reference Letters"))
        self.label_22.setAccessibleName(_translate("MainWindow", "PHOTOPATH"))
        self.label_22.setText(_translate("MainWindow", "Photo"))
        self.pb_browsePhoto.setText(_translate("MainWindow", "..."))
        self.pb_generatePdf.setText(_translate("MainWindow", "Generate PDF"))
        self.pb_generateText.setText(_translate("MainWindow", "Generate Text"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tabFinish), _translate("MainWindow", "Finish"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOutput.setTitle(_translate("MainWindow", "Output"))
        self.menuLatex.setTitle(_translate("MainWindow", "Latex"))
        self.menuText.setTitle(_translate("MainWindow", "Text"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "F12"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSet_LatexTemplate.setText(_translate("MainWindow", "Set Template"))
        self.actionSet_LatexOutputDirectory.setText(_translate("MainWindow", "Set Output Directory"))
        self.actionText_Template.setText(_translate("MainWindow", "Set Template"))
        self.actionCompiler_2.setText(_translate("MainWindow", "Compiler"))
        self.actionSet_TextOutputDirectory.setText(_translate("MainWindow", "Set Output Directory"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
