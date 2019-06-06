#!/usr/bin/env python3

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from lxml.etree import Element, tostring, XML

import mainWindow
from pdfCreator import PdfCreator


class CoverletterCreator(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(CoverletterCreator, self).__init__(parent)
		self.setupUi(self)

		self.actionSave.triggered.connect(self.save_project)
		self.actionSave_As.triggered.connect(self.saveas_project)
		self.actionOpen.triggered.connect(self.open_project)

		self.filename = ""

		self.pb_generatePdf.clicked.connect(self.generate_pdf)

	def save_project(self):
		try:
			open(self.filename, 'w')
		except OSError:
			self.filename, _ = QFileDialog.getSaveFileName(self, "Save Project", "./", "XML Files (*.xml)")

		self.root = self.generate_root()

		if ".xml" not in self.filename:
			self.filename = self.filename + '.xml'
		with open(self.filename, 'wb') as f:
			f.write(tostring(self.root, pretty_print=True))

	def generate_root(self):
		root = Element('root')

		personal_info = Element('personal_info')
		root.append(personal_info)
		for qW in [self.le_firstName, self.le_lastName, self.le_mobile, self.le_email, self.le_homepage, self.le_githubName, self.le_LinkedinName	]:
			child = Element(qW.objectName())
			child.text = qW.text()
			personal_info.append(child)

		personal_address = Element('te_personalAddress')
		personal_address.text = self.te_personalAddress.toPlainText()
		personal_info.append(personal_address)

		company_info = Element('company_info')
		root.append(company_info)
		for qW in [self.le_companyName, self.le_companyShortName, self.le_department, self.le_Lettertitle, self.le_jobTitle, self.le_jobRefId, self.le_RecepientName]:
			child = Element(qW.objectName())
			child.text = qW.text()
			company_info.append(child)

		company_address = Element('te_companyAddress')
		company_address.text = self.te_companyAddress.toPlainText()
		company_info.append(company_address)

		receipientGender = Element('receipientGender')
		receipientGender.text = str(self.receipientGender.currentIndex())
		company_info.append(receipientGender)

		about_me = Element('te_aboutMe')
		about_me.text = self.te_aboutMe.toPlainText()
		root.append(about_me)

		WhyFirm = Element('te_WhyFirm')
		WhyFirm.text = self.te_WhyFirm.toPlainText()
		root.append(WhyFirm)

		whyYou = Element('te_whyYou')
		whyYou.text = self.te_whyYou.toPlainText()
		root.append(whyYou)

		misc = Element('misc')
		root.append(misc)
		for qW in [self.le_closing, self.le_enclosing]:
			child = Element(qW.objectName())
			child.text = qW.text()
			misc.append(child)
		for qW in [self.cb_certificates, self.cb_CV, self.cb_referenceLetters, self.cb_Transcripts, ]:
			child = Element(qW.objectName())
			child.text = str(qW.isChecked())
			misc.append(child)

		return root


	def saveas_project(self):
		filename, _ = QFileDialog.getSaveFileName(self, "Save Project As","./","XML Files (*.xml)")

		if ".xml" not in filename:
			filename = filename + '.xml'
		with open(filename, 'wb') as f:
			f.write(tostring(self.generate_root(), pretty_print=True))

	def open_project(self):
		filename, _ = QFileDialog.getOpenFileName(self, "Open Project","./","XML Files (*.xml)")
		if ".xml" not in filename:
			filename = filename + '.xml'

		with open(filename,'r') as f:
			self.root = XML(f.read())#.replace("\n", ""))

		for element in self.root.iter():
			widget = self.findChild(QtWidgets.QLineEdit, str(element.tag))
			if widget is not None and element.text is not None:
				widget.setText(str(element.text))
			else:
				widget = self.findChild(QtWidgets.QTextEdit, str(element.tag))
				if widget is not None and element.text is not None:
					widget.setText(str(element.text))
				else:
					widget = self.findChild(QtWidgets.QComboBox, str(element.tag))
					if widget is not None and element.text is not None:
						widget.setCurrentIndex(int(element.text))
					else:
						widget = self.findChild(QtWidgets.QCheckBox, str(element.tag))
						if widget is not None and element.text is not None:
							widget.setChecked(str(element.text) == 'True')

		self.filename = filename

	def generate_pdf(self):
		pdfcreator = PdfCreator(data=self.generate_root())
		pdfcreator.read_template()
		pdfcreator.convert_to_dict()
		pdfcreator.render_template()
		pdfcreator.compile_xelatex(pdfname='coverletter.pdf')

	def generate_text(self):
		# TODO: implement text coverletter creation
		None


def main():
	app = QtWidgets.QApplication(sys.argv)
	form = CoverletterCreator()
	form.show()
	app.exec_()


if __name__ == "__main__":
	main()
