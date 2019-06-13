#!/usr/bin/env python3

import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFileDialog
from lxml.etree import Element, tostring, XML

from CoverletterCreator.SpellTextEdit import SpellTextEdit
from CoverletterCreator.pdfCreator import PdfCreator
from CoverletterCreator.textCreator import TextCreator
from CoverletterCreator.ui import mainWindow


class CoverletterCreator(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(CoverletterCreator, self).__init__(parent)
		self.setupUi(self)

		self.mainTitle = "Coverletter Creator"
		self.settings = QSettings("KhaleelKhan", "Coverletter_Creator")

		# Create text editors with spell-check
		self.TEXTABOUTME = SpellTextEdit(self.tabAboutMe)
		self.TEXTABOUTME.setObjectName("TEXTABOUTME")
		self.verticalLayout_AboutMeTab.addWidget(self.TEXTABOUTME)

		self.TEXTWHYTHISFIRM = SpellTextEdit(self.tabWhyFirm)
		self.TEXTWHYTHISFIRM.setObjectName("TEXTWHYTHISFIRM")
		self.verticalLayout_WhyFirmTab.addWidget(self.TEXTWHYTHISFIRM)

		self.TEXTWHYYOU = SpellTextEdit(self.tabWhyYou)
		self.TEXTWHYYOU.setObjectName("TEXTWHYYOU")
		self.verticalLayout_WhyYouTab.addWidget(self.TEXTWHYYOU)

		self.actionNew.triggered.connect(self.new_project)
		self.actionSave.triggered.connect(self.save_project)
		self.actionSave_As.triggered.connect(self.saveas_project)
		self.actionOpen.triggered.connect(self.open_project)
		self.actionExit.triggered.connect(self.close)
		self.actionSet_LatexTemplate.triggered.connect(self.get_latex_template)
		self.actionSet_LatexOutputDirectory.triggered.connect(self.get_latex_dir)
		self.actionText_Template.triggered.connect(self.get_text_template)
		self.actionSet_TextOutputDirectory.triggered.connect(self.get_text_dir)

		# Set default values
		self.filename = "untitled.xml"
		self.file_dirty = False
		self.latex_template = 'Latex/Templates/Awesome-CV/Latex_template.tex'
		self.latex_dir = os.path.abspath('Latex/Output')
		self.text_template = 'Text/Templates/Simple/Text_template.txt'
		self.text_dir = os.path.abspath('Text/Output')

		self.readSettings()
		self.load_file(self.filename)

		self.pb_browsePhoto.clicked.connect(self.browse_photo)
		self.pb_generatePdf.clicked.connect(self.generate_pdf)
		self.pb_generateText.clicked.connect(self.generate_text)

		self.connect_all_fields()
		self.connect_mandatory_fields()

		self.COMPANYNAME.editingFinished.connect(lambda: self.COMPANYSHORTNAME.setText(self.COMPANYNAME.text()))

	def connect_all_fields(self):
		for child in self.centralwidget.findChildren(QtWidgets.QLineEdit):
			child.textChanged.connect(self.setWindowTitleUnsaved)
		for child in self.centralwidget.findChildren(QtWidgets.QPlainTextEdit):
			child.textChanged.connect(self.setWindowTitleUnsaved)
		for child in self.centralwidget.findChildren(QtWidgets.QCheckBox):
			child.clicked.connect(self.setWindowTitleUnsaved)
		for child in self.centralwidget.findChildren(SpellTextEdit):
			child.textChanged.connect(self.setWindowTitleUnsaved)
		for child in self.centralwidget.findChildren(QtWidgets.QComboBox):
			#self.cb_recipientSalutation.currentIndexChanged()
			child.currentIndexChanged.connect(self.setWindowTitleUnsaved)

	def connect_mandatory_fields(self):
		mandatory_fields_list = [self.FIRSTNAME, self.LASTNAME, self.MOBILE, self.EMAIL, self.COMPANYNAME]
		for textBox in mandatory_fields_list:
			textBox.textChanged[str].connect(lambda: self.pb_generatePdf.setEnabled(textBox.text() != ""))

		for textBox in mandatory_fields_list:
			textBox.textChanged[str].connect(lambda: self.pb_generateText.setEnabled(textBox.text() != ""))


	def setWindowTitleUnsaved(self):
		self.file_dirty = True
		_, fname = os.path.split(self.filename)
		self.setWindowTitle(self.mainTitle + " - " + fname + "*")

	def setWindowTitleSaved(self):
		self.file_dirty = False
		_, fname = os.path.split(self.filename)
		self.setWindowTitle(self.mainTitle + " - " + fname)

	def new_project(self):
		filename, _ = QFileDialog.getSaveFileName(self, "New Project", "./", "XML Files (*.xml)")
		if filename:
			if ".xml" not in filename:
				filename = filename + '.xml'

			self.reset_all_fields()
			self.filename = filename
			self.setWindowTitleUnsaved()
		else:
			return

	def reset_all_fields(self):
		for child in self.centralwidget.findChildren(QtWidgets.QLineEdit):
			child.clear()
		for child in self.centralwidget.findChildren(QtWidgets.QPlainTextEdit):
			child.clear()
		for child in self.centralwidget.findChildren(QtWidgets.QCheckBox):
			child.setChecked(False)
		for child in self.centralwidget.findChildren(SpellTextEdit):
			child.clear()
		for child in self.centralwidget.findChildren(SpellTextEdit):
			child.clear()
		self.label_pic.clear()

	def save_project(self):
		try:
			open(self.filename, 'w')
		except OSError:
			filename, _ = QFileDialog.getSaveFileName(self, "Save Project", "./", "XML Files (*.xml)")
			if filename:
				self.filename = filename
			else:
				return
		self.root = self.generate_root()

		if ".xml" not in self.filename:
			self.filename = self.filename + '.xml'
		with open(self.filename, 'wb') as f:
			f.write(tostring(self.root, pretty_print=True))

		self.setWindowTitleSaved()

	def generate_root(self):
		root = Element('root')

		personal_info = Element('personal_info')
		root.append(personal_info)
		for qW in [self.FIRSTNAME, self.LASTNAME, self.MOBILE, self.EMAIL, self.HOMEPAGE, self.GITHUBNAME, self.LINKEDINNAME	]:
			child = Element(qW.objectName())
			child.text = qW.text()
			personal_info.append(child)

		personal_address = Element('PERSONALADDRESS')
		personal_address.text = self.PERSONALADDRESS.toPlainText()
		personal_info.append(personal_address)

		company_info = Element('company_info')
		root.append(company_info)
		for qW in [self.COMPANYNAME, self.COMPANYSHORTNAME, self.DEPARTMENT, self.LETTERTITLE, self.JOBTITLE, self.JOBREFID, self.RECEIPIENTNAME]:
			child = Element(qW.objectName())
			child.text = qW.text()
			company_info.append(child)

		company_address = Element('COMPANYADDRESS')
		company_address.text = self.COMPANYADDRESS.toPlainText()
		company_info.append(company_address)

		RECEIPIENTGENDER = Element('RECEIPIENTGENDER')
		RECEIPIENTGENDER.text = str(self.RECEIPIENTGENDER.currentText())
		company_info.append(RECEIPIENTGENDER)

		RECEIPIENTSALUTATION = Element('RECEIPIENTSALUTATION')
		RECEIPIENTSALUTATION.text = str(self.cb_recipientSalutation.currentText())
		company_info.append(RECEIPIENTSALUTATION)

		about_me = Element('TEXTABOUTME')
		about_me.text = self.TEXTABOUTME.toPlainText()
		root.append(about_me)

		WhyFirm = Element('TEXTWHYTHISFIRM')
		WhyFirm.text = self.TEXTWHYTHISFIRM.toPlainText()
		root.append(WhyFirm)

		whyYou = Element('TEXTWHYYOU')
		whyYou.text = self.TEXTWHYYOU.toPlainText()
		root.append(whyYou)

		misc = Element('misc')
		root.append(misc)
		for qW in [self.CLOSINGSALUTATION, self.ENCLOSINGPREFIX, self.PHOTOPATH]:
			child = Element(qW.objectName())
			child.text = qW.text()
			misc.append(child)
		for qW in [self.CERTIFICATESATTACHED, self.CVATTACHED, self.REFLETTERSATTACHED, self.TRANSCRIPTSATTACHED, ]:
			child = Element(qW.objectName())
			child.text = str(qW.isChecked())
			misc.append(child)

		return root


	def saveas_project(self):
		filename, _ = QFileDialog.getSaveFileName(self, "Save Project As","./","XML Files (*.xml)")

		if filename:
			if ".xml" not in filename:
				filename = filename + '.xml'
			with open(filename, 'wb') as f:
				f.write(tostring(self.generate_root(), pretty_print=True))

	def open_project(self):
		filename, _ = QFileDialog.getOpenFileName(self, "Open Project","./","XML Files (*.xml)")
		if not filename:
			return

		if ".xml" not in filename:
			filename = filename + '.xml'

		self.load_file(filename)

	def load_file(self, filename):
		try:
			with open(filename, 'r') as f:
				self.root = XML(f.read())#.replace("\n", ""))

			for element in self.root.iter():
				widget = self.findChild(QtWidgets.QLineEdit, str(element.tag))
				if widget is not None and element.text is not None:
					widget.setText(str(element.text))
				else:
					widget = self.findChild(QtWidgets.QPlainTextEdit, str(element.tag))
					if widget is not None and element.text is not None:
						widget.setPlainText(str(element.text))
					else:
						widget = self.findChild(QtWidgets.QComboBox, str(element.tag))
						if widget is not None and element.text is not None:
							index = widget.findText(element.text, QtCore.Qt.MatchFixedString)
							if index >= 0:
								widget.setCurrentIndex(index)
							elif str(element.text).isdigit():
								widget.setCurrentIndex(int(element.text))
							else:
								widget.setCurrentText(str(element.text))
						else:
							widget = self.findChild(QtWidgets.QCheckBox, str(element.tag))
							if widget is not None and element.text is not None:
								widget.setChecked(str(element.text) == 'True')
							else:
								widget = self.findChild(SpellTextEdit, str(element.tag))
								if widget is not None and element.text is not None:
									widget.setChecked(str(element.text) == 'True')

			self.filename = filename
			self.get_photo(self.PHOTOPATH.text())
			self.setWindowTitleSaved()

		except FileNotFoundError:
			self.setWindowTitleUnsaved()
			self.file_dirty = False
			print("Warning: File not found!")

	def browse_photo(self):
		fname, _ = QFileDialog.getOpenFileName(self, 'Open profile photo',
											   './', "Image files (*.jpg *.png)")
		if fname:
			image = QtGui.QImage(fname)
			if image.isNull():
				QtWidgets.QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fname)
				return
			self.get_photo(fname)

	def get_photo(self, fname):
		image = QtGui.QImage(fname)
		if image.isNull():
			QtWidgets.QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fname)
			return
		self.PHOTOPATH.setText(fname)
		self.label_pic.setPixmap(
			QtGui.QPixmap(fname).scaled(160, 160, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))

	def get_latex_template(self):
		latex_template, _ = QFileDialog.getOpenFileName(self, "Open latex template", "./", "Latex Files (*.tex)")
		if latex_template:
			self.latex_template = latex_template

	def get_latex_dir(self):
		latex_dir = QFileDialog.getExistingDirectory(self, 'Latex output directory', './')
		if latex_dir:
			self.latex_dir = os.path.abspath(latex_dir)

	def get_text_template(self):
		template, _ = QFileDialog.getOpenFileName(self, "Open text template", "./", "Text Files (*.txt)")
		if template:
			self.text_template = template

	def get_text_dir(self):
		text_dir = QFileDialog.getExistingDirectory(self, 'Text output directory', './')
		if text_dir:
			self.text_dir = os.path.abspath(text_dir)

	def generate_pdf(self):
		pdfcreator = PdfCreator(data=self.generate_root())
		pdfcreator.read_template(template=self.latex_template)
		pdfcreator.convert_to_dict()
		pdfcreator.render_template()
		filename = self.COMPANYSHORTNAME.text() + '_' + self.JOBREFID.text() + '_Coverletter'
		filename = "".join(i for i in filename if i not in ".\/:*?<>|").replace(r' ', '_')
		pdfcreator.compile_xelatex(pdfname=filename+".pdf", outputDir=self.latex_dir,
									photo=self.PHOTOPATH.text())

	def generate_text(self):
		textcreator = TextCreator(data=self.generate_root())
		textcreator.read_template(template=self.text_template)
		textcreator.convert_to_dict()
		textcreator.render_template()
		filename = self.COMPANYSHORTNAME.text() + '_' + self.JOBREFID.text() + '_Coverletter'
		filename = "".join(i for i in filename if i not in ".\/:*?<>|").replace(r' ', '_')
		textcreator.compile_text(textname=filename+".txt", outputDir=self.text_dir)

	def writeSettings(self):
		self.settings.beginGroup("MainWindow")
		self.settings.setValue("size", self.size())
		self.settings.setValue("pos", self.pos())
		self.settings.endGroup()

		self.settings.beginGroup("Templates")
		self.settings.setValue("latex", str(self.latex_template))
		self.settings.setValue("text", str(self.text_template))
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.settings.setValue("latex", str(self.latex_dir))
		self.settings.setValue("text", str(self.text_dir))
		self.settings.endGroup()

		if not self.file_dirty:
			self.settings.beginGroup("Project")
			self.settings.setValue("filename", str(self.filename))
			self.settings.endGroup()

		self.settings.sync()

	def readSettings(self):
		self.settings.beginGroup("MainWindow")
		self.resize(self.settings.value("size", QtCore.QSize(616, 466)))
		self.move(self.settings.value("pos", QtCore.QPoint(200, 200)))
		self.settings.endGroup()

		self.settings.beginGroup("Templates")
		self.latex_template = str(self.settings.value("latex", self.latex_template))
		self.text_template = str(self.settings.value("text", self.text_template))
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.latex_dir = str(self.settings.value("latex", self.latex_dir))
		self.text_dir = str(self.settings.value("text", self.text_dir))
		self.settings.endGroup()

		self.settings.beginGroup("Project")
		self.filename = str(self.settings.value("filename", self.filename))
		self.settings.endGroup()


	# event : QCloseEvent
	def closeEvent(self, event):
		if self.file_dirty :
			choice = QtWidgets.QMessageBox.question(self, 'Project not saved',
												"Save Project before exit?",
												QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
			if choice == QtWidgets.QMessageBox.Yes:
				self.save_project()
				self.writeSettings()
				event.accept()
				sys.exit()
			elif choice == QtWidgets.QMessageBox.Cancel:
				event.ignore()
			else:
				self.writeSettings()
				event.accept()
				sys.exit()
		else:
			self.writeSettings()
			event.accept()
			sys.exit()


def run():
	app = QtWidgets.QApplication(sys.argv)
	form = CoverletterCreator()
	form.show()
	app.exec_()


if __name__ == "__main__":
	run()
