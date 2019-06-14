import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFileDialog

from CoverletterCreator.ui import settings


class SettingsHandler(QtWidgets.QMainWindow, settings.Ui_SettingsWindow):
	latex_compiler_list = ["xelatex", "pdfLatex"]

	def __init__(self, parent=None, settings=None):
		super(SettingsHandler, self).__init__(parent)
		self.setupUi(self)

		self.latex_template = 'Latex/Templates/Awesome-CV/Latex_template.tex'
		self.latex_dir = os.path.abspath('Latex/Output')
		self.text_template = 'Text/Templates/Simple/Text_template.txt'
		self.text_dir = os.path.abspath('Text/Output')
		self.open_pdf = True
		self.open_text = True
		self.keep_tex = True

		self.latex_compiler = "xelatex"
		self.latex_custom_command = ''


		if settings is None:
			self.settings = QSettings("KhaleelKhan", "Coverletter_Creator-dev")
		else:
			self.settings = settings

		self.pb_browse_latex_dir.clicked.connect(self.open_latex_dir)
		self.pb_browse_text_dir.clicked.connect(self.open_text_dir)
		self.pb_browse_latex_tempate.clicked.connect(self.open_latex_template)
		self.pb_browse_text_template.clicked.connect(self.open_text_template)

		self.combo_latex_compiler.addItems(self.latex_compiler_list)
		self.combo_latex_compiler.addItem("custom")
		self.combo_latex_compiler.currentTextChanged[str].connect(self.latex_compiler_changed)

		self.latex_buttonBox.clicked[QtWidgets.QAbstractButton].connect(lambda btn: self.handleButtonClick(btn, self.latex_buttonBox))
		self.text_buttonBox.clicked[QtWidgets.QAbstractButton].connect(lambda btn: self.handleButtonClick(btn, self.text_buttonBox))

		self.le_latex_tempate.textChanged[str].connect(lambda path: self.verify_path_field(path, self.icon_latex_template))
		self.le_text_template.textChanged[str].connect(lambda path: self.verify_path_field(path, self.icon_text_template))
		self.le_latex_out_dir.textChanged[str].connect(lambda path: self.verify_path_field(path, self.icon_latex_output))
		self.le_text_out_dir.textChanged[str].connect(lambda path: self.verify_path_field(path, self.icon_text_output))
		self.read_settings_from_config()

	def handleButtonClick(self, button, buttonbox):
		sb = buttonbox.standardButton(button)
		if sb == QtWidgets.QDialogButtonBox.Apply:
			self.save_fields()
		elif sb == QtWidgets.QDialogButtonBox.Ok:
			self.save_fields()
			self.write_settings_to_config()
			self.hide()
		elif sb == QtWidgets.QDialogButtonBox.Cancel:
			self.reset_fields()
			self.hide()

	def verify_path_field(self, path, icon_label):
		if os.path.exists(path):
			icon_label.setPixmap(QtGui.QPixmap(":/icons/okay.png"))
			self.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
			self.text_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
			self.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).setEnabled(True)
			self.text_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).setEnabled(True)

		else:
			icon_label.setPixmap(QtGui.QPixmap(":/icons/notokay.png"))
			self.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
			self.text_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
			self.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).setEnabled(False)
			self.text_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).setEnabled(False)


	def latex_compiler_changed(self, compiler):
		if compiler == 'custom':
			self.le_custom_latex.setEnabled(True)
		else:
			self.le_custom_latex.setEnabled(False)

	def reset_fields(self):
		self.le_latex_tempate.setText(self.latex_template)
		self.le_text_template.setText(self.text_template)
		self.le_latex_out_dir.setText(self.latex_dir)
		self.le_text_out_dir.setText(self.text_dir)
		self.cb_open_pdf_after.setChecked(self.open_pdf)
		self.cb_open_text_after.setChecked(self.open_text)
		self.cb_keep_tex.setChecked(self.keep_tex)

		index = self.combo_latex_compiler.findText(self.latex_compiler)
		if index >= 0:
			self.combo_latex_compiler.setCurrentIndex(index)

		self.le_custom_latex.setText(self.latex_custom_command)
		self.hide()

	def save_fields(self):
		self.latex_template = self.le_latex_tempate.text()
		self.text_template = self.le_text_template.text()
		self.latex_dir = self.le_latex_out_dir.text()
		self.text_dir = self.le_text_out_dir.text()
		self.open_pdf = self.cb_open_pdf_after.isChecked()
		self.open_text = self.cb_open_text_after.isChecked()
		self.keep_tex = self.cb_keep_tex.isChecked()
		self.latex_compiler = self.combo_latex_compiler.currentText()
		self.latex_custom_command = self.le_custom_latex.text()

	def write_settings_to_config(self):
		self.settings.beginGroup("Templates")
		self.settings.setValue("latex", str(self.latex_template))
		self.settings.setValue("text", str(self.text_template))
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.settings.setValue("latex", str(self.latex_dir))
		self.settings.setValue("text", str(self.text_dir))
		self.settings.endGroup()

		self.settings.beginGroup("Misc")
		self.settings.setValue("open_pdf", self.open_pdf)
		self.settings.setValue("open_text", self.open_text)
		self.settings.setValue("keep_tex", self.keep_tex)
		self.settings.setValue("latex_compiler", self.latex_compiler)
		self.settings.setValue("latex_custom_command", self.latex_custom_command)
		self.settings.endGroup()

		self.settings.sync()

	def read_settings_from_config(self):
		self.settings.beginGroup("Templates")
		self.latex_template = str(self.settings.value("latex", self.latex_template))
		self.text_template = str(self.settings.value("text", self.text_template))
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.latex_dir = str(self.settings.value("latex", self.latex_dir))
		self.text_dir = str(self.settings.value("text", self.text_dir))
		self.settings.endGroup()

		self.settings.beginGroup("Misc")
		self.open_pdf = self.settings.value("open_pdf", self.open_pdf) == 'true'
		self.open_text = self.settings.value("open_text", self.open_text) == 'true'
		self.keep_tex = self.settings.value("keep_tex", self.keep_tex) == 'true'
		self.latex_compiler = str(self.settings.value("latex_compiler", self.latex_compiler))
		self.latex_custom_command = str(self.settings.value("latex_custom_command", self.latex_custom_command))
		self.settings.endGroup()

		self.reset_fields()

	def get_latex_compiler(self):
		if self.latex_compiler == 'custom':
			return self.latex_custom_command
		else:
			return self.latex_compiler

	def open_latex_template(self):
		latex_template, _ = QFileDialog.getOpenFileName(self, "Open latex template", "./", "Latex Files (*.tex)")
		if latex_template:
			self.le_latex_tempate.setText(latex_template)

	def open_latex_dir(self):
		latex_dir = QFileDialog.getExistingDirectory(self, 'Latex output directory', './')
		if latex_dir:
			self.le_latex_out_dir.setText(os.path.abspath(latex_dir))

	def open_text_template(self):
		template, _ = QFileDialog.getOpenFileName(self, "Open text template", "./", "Text Files (*.txt)")
		if template:
			self.le_text_template.setText(template)

	def open_text_dir(self):
		text_dir = QFileDialog.getExistingDirectory(self, 'Text output directory', './')
		if text_dir:
			self.le_text_out_dir.setText(os.path.abspath(text_dir))

	def close(self):
		self.reset_fields()

def run():
	app = QtWidgets.QApplication(sys.argv)
	form = SettingsHandler()
	form.show()
	app.exec_()


if __name__ == "__main__":
	import sys
	run()