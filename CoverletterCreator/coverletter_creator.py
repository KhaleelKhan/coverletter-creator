#!/usr/bin/env python3

import functools
import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFileDialog
from lxml.etree import Element, tostring, XML, XMLSyntaxError

from CoverletterCreator.SettingsHandler import SettingsHandler
from CoverletterCreator.SpellTextEdit import SpellTextEdit
from CoverletterCreator.pdfCreator import PdfCreator
from CoverletterCreator.textCreator import TextCreator
from CoverletterCreator.ui import mainWindow


class CoverletterCreator(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(CoverletterCreator, self).__init__(parent)
		self.setupUi(self)

		self.mainTitle = "Coverletter Creator"
		self.config = QSettings("KhaleelKhan", "Coverletter_Creator")
		self.settings = SettingsHandler(parent=self, settings=self.config)

		self.clipboard = QtWidgets.QApplication.clipboard()

		self.actionNew.triggered.connect(self.new_project)
		self.actionSave.triggered.connect(self.save_project)
		self.actionSave_As.triggered.connect(self.saveas_project)
		self.actionOpen.triggered.connect(self.open_project)
		self.actionExit.triggered.connect(self.close)
		self.actionSettings.triggered.connect(self.settings.show)


		# Set default values
		self.filename = "untitled.xml"
		self.file_dirty = False

		self.readSettings()
		self.load_file(self.filename)

		self.pb_browsePhoto.clicked.connect(self.browse_photo)
		self.pb_generatePdf.clicked.connect(self.generate_pdf)
		self.pb_generateText.clicked.connect(self.generate_text)

		self.connect_all_fields()
		self.connect_mandatory_fields()

		# Connect all labels to click handler
		for child in self.centralwidget.findChildren(QtWidgets.QLabel):
			child.mousePressEvent = functools.partial(self.label_clicked, source=child)
		for child in self.centralwidget.findChildren(QtWidgets.QCheckBox):
			child.mousePressEvent = functools.partial(self.checkbox_clicked, source=child)
		self.RECEIPIENTGENDER.mousePressEvent = functools.partial(self.combobox_clicked, source=self.RECEIPIENTGENDER)
		self.RECEIPIENTSALUTATION.mousePressEvent = functools.partial(self.combobox_clicked, source=self.RECEIPIENTSALUTATION)

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

	def label_clicked(self, event, source):
		var_code = source.accessibleName()
		self.clipboard.setText(str(var_code))
		event.accept()

	def checkbox_clicked(self, event, source):
		var_code = source.accessibleName()
		self.clipboard.setText(str(var_code))
		source.toggle()

	def combobox_clicked(self, event, source):
		var_code = source.accessibleName()
		self.clipboard.setText(str(var_code))
		source.showPopup()

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
		RECEIPIENTSALUTATION.text = str(self.RECEIPIENTSALUTATION.currentText())
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
			self.load_file(filename)

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

		except XMLSyntaxError:
			QtWidgets.QMessageBox.critical(self, "XML Read Failed",
										   "Cannot read xml file %s. \n\nMake sure the xml file is not blank " % filename)


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

	def generate_pdf(self):
		pdfcreator = PdfCreator(data=self.generate_root(), parent=self)
		pdfcreator.read_template(template=self.settings.latex_template)
		pdfcreator.convert_to_dict()
		pdfcreator.render_template()
		filename = self.COMPANYSHORTNAME.text() + '_' + self.JOBREFID.text() + '_Coverletter'
		filename = "".join(i for i in filename if i not in ".\/:*?<>|").replace(r' ', '_')

		self.pb_generatePdf.setEnabled(False)
		try:
			pdfcreator.compile_xelatex(compiler=self.settings.get_latex_compiler(), pdfname=filename+".pdf",
									outputDir=self.settings.latex_dir,
									open_pdf=self.settings.open_pdf, keep_tex=self.settings.keep_tex)
		except FileNotFoundError as e:
			QtWidgets.QMessageBox.critical(self, "PDF Compilation Failed", "Cannot complete command %s." + str(e) % self.settings.get_latex_compiler())
		self.pb_generatePdf.setEnabled(True)

	def generate_text(self):
		textcreator = TextCreator(data=self.generate_root())
		try:
			textcreator.read_template(template=self.settings.text_template)
		except FileNotFoundError as e:
			QtWidgets.QMessageBox.critical(self, "Error", "Cannot find template file %s.\n" + str(e) % self.settings.text_template)
		textcreator.convert_to_dict()
		textcreator.render_template()
		filename = self.COMPANYSHORTNAME.text() + '_' + self.JOBREFID.text() + '_Coverletter'
		filename = "".join(i for i in filename if i not in ".\/:    *?<>|").replace(r' ', '_')
		self.pb_generateText.setEnabled(False)
		textcreator.compile_text(textname=filename+".txt", outputDir=self.settings.text_dir, open_text=self.settings.open_text)
		self.pb_generateText.setEnabled(True)

	def writeSettings(self):
		self.config.beginGroup("MainWindow")
		self.config.setValue("size", self.size())
		self.config.setValue("pos", self.pos())
		self.config.endGroup()

		if not self.file_dirty:
			self.config.beginGroup("Project")
			self.config.setValue("filename", str(self.filename))
			self.config.endGroup()

		self.config.sync()

	def readSettings(self):
		self.config.beginGroup("MainWindow")
		self.resize(self.config.value("size", QtCore.QSize(616, 466)))
		self.move(self.config.value("pos", QtCore.QPoint(200, 200)))
		self.config.endGroup()

		self.config.beginGroup("Project")
		self.filename = str(self.config.value("filename", self.filename))
		self.config.endGroup()

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
