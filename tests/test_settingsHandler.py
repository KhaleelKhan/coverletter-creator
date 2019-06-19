import os
import sys
from unittest import TestCase
from unittest import mock

from PyQt5.QtCore import QSettings
from PyQt5.QtTest import QTest

from CoverletterCreator.SettingsHandler import SettingsHandler
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)


class TestSettingsHandler(TestCase):
	def setUp(self):
		self.settings = QSettings("KhaleelKhan", "SettingsTestApp")
		self.settings.clear()
		self.form = SettingsHandler(settings=self.settings)
		self.form.show()

	def tearDown(self):
		self.form.close()
		del self.form

	def test_defaults(self):
		self.assertEqual(self.form.le_latex_tempate.text(), os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.assertEqual(self.form.le_text_template.text(), os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.assertEqual(self.form.le_latex_out_dir.text(), os.path.abspath('Latex/Output'))
		self.assertEqual(self.form.le_text_out_dir.text(), os.path.abspath('Text/Output'))
		self.assertTrue(self.form.cb_open_pdf_after.isChecked())
		self.assertTrue(self.form.cb_open_text_after.isChecked())
		self.assertTrue(self.form.cb_keep_tex.isChecked())
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')
		self.assertEqual(self.form.le_custom_latex.text(), '')
		self.assertFalse(self.form.le_custom_latex.isEnabled())

		self.assertTrue(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertTrue(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())
		self.assertTrue(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertTrue(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())

	def test_latex_compiler_changed(self):
		# reset value of combo box
		self.form.combo_latex_compiler.setCurrentText('xelatex')

		self.form.combo_latex_compiler.setCurrentText('custom')
		self.assertTrue(self.form.le_custom_latex.isEnabled())
		self.form.combo_latex_compiler.setCurrentText('xelatex')
		self.assertFalse(self.form.le_custom_latex.isEnabled())
		self.form.combo_latex_compiler.setCurrentText('pdflatex')
		self.assertFalse(self.form.le_custom_latex.isEnabled())


	def test_write_settings_to_config(self):
		# Write dummy values to variables
		self.form.latex_template = "latex_template_test_write_settings"
		self.form.text_template = "text_template_test_write_settings"
		self.form.latex_dir = "latex_out_dir_test_write_settings"
		self.form.text_dir = "text_out_dir_test_write_settings"
		self.form.open_pdf = True
		self.form.open_text = True
		self.form.keep_tex = True
		self.form.latex_compiler = "xelatex"
		self.form.latex_custom_command = "custom_command_test_write_settings"

		self.form.write_settings_to_config()

		# Read from config to verify
		self.settings.beginGroup("Templates")
		self.assertEqual(self.settings.value("latex"), "latex_template_test_write_settings")
		self.assertEqual(self.settings.value("text"), "text_template_test_write_settings")
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.assertEqual(self.settings.value("latex"), "latex_out_dir_test_write_settings")
		self.assertEqual(self.settings.value("text"), "text_out_dir_test_write_settings")
		self.settings.endGroup()

		self.settings.beginGroup("Misc")
		self.assertEqual(self.settings.value("open_pdf"), 'True')
		self.assertEqual(self.settings.value("open_text"), 'True')
		self.assertEqual(self.settings.value("keep_tex"), 'True')
		self.assertEqual(self.settings.value("latex_compiler"), "xelatex")
		self.assertEqual(self.settings.value("latex_custom_command"), "custom_command_test_write_settings")
		self.settings.endGroup()

		# Test for False
		self.form.open_pdf = False
		self.form.open_text = False
		self.form.keep_tex = False

		self.form.write_settings_to_config()

		self.settings.beginGroup("Misc")
		self.assertEqual(self.settings.value("open_pdf"), 'False')
		self.assertEqual(self.settings.value("open_text"), 'False')
		self.assertEqual(self.settings.value("keep_tex"), 'False')
		self.settings.endGroup()

	def test_read_settings_from_config(self):
		# Write dummy settings to config
		self.settings.beginGroup("Templates")
		self.settings.setValue("latex", "latex_template_test_read_settings")
		self.settings.setValue("text", "text_template_test_read_settings")
		self.settings.endGroup()

		self.settings.beginGroup("Outputs")
		self.settings.setValue("latex", "latex_dir_test_read_settings")
		self.settings.setValue("text", "text_dir_test_read_settings")
		self.settings.endGroup()

		self.settings.beginGroup("Misc")
		self.settings.setValue("open_pdf", "True")
		self.settings.setValue("open_text", "True")
		self.settings.setValue("keep_tex", "True")
		self.settings.setValue("latex_compiler", "xelatex")
		self.settings.setValue("latex_custom_command", "custom_command_test_read_settings")
		self.settings.endGroup()

		# Save to config
		self.settings.sync()

		self.form.read_settings_from_config()
		self.assertEqual(self.form.latex_template, "latex_template_test_read_settings")
		self.assertEqual(self.form.text_template, "text_template_test_read_settings")
		self.assertEqual(self.form.latex_dir, "latex_dir_test_read_settings")
		self.assertEqual(self.form.text_dir, "text_dir_test_read_settings")
		self.assertTrue(self.form.open_pdf)
		self.assertTrue(self.form.open_text)
		self.assertTrue(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'xelatex')
		self.assertEqual(self.form.latex_custom_command, "custom_command_test_read_settings")

		# Test for False

		self.settings.beginGroup("Misc")
		self.settings.setValue("open_pdf", "False")
		self.settings.setValue("open_text", "False")
		self.settings.setValue("keep_tex", "False")
		self.settings.setValue("latex_compiler", "custom")
		self.settings.setValue("latex_custom_command", "custom_command_test_read_settings")
		self.settings.endGroup()
		# Save to config
		self.settings.sync()

		self.form.read_settings_from_config()
		self.assertFalse(self.form.open_pdf)
		self.assertFalse(self.form.open_text)
		self.assertFalse(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'custom')
		self.assertEqual(self.form.latex_custom_command, "custom_command_test_read_settings")

	def test_get_latex_compiler(self):
		self.form.latex_compiler = 'custom'
		self.form.latex_custom_command = "test string"

		self.assertEqual(self.form.get_latex_compiler(), "test string")

		self.form.latex_compiler = 'xelatex'
		self.assertEqual(self.form.get_latex_compiler(), "xelatex")

		self.form.latex_compiler = 'pdflatex'
		self.assertEqual(self.form.get_latex_compiler(), "pdflatex")

	def test_invalid_combobox_setting(self):
		self.form.combo_latex_compiler.setCurrentText('xelatex')
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')

		self.form.combo_latex_compiler.setCurrentText('invalid')
		# Should still be same
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')


	def test_click_okay_button(self):
		self.reset_all_variables()
		self.reset_all_ui_elements()

		# Set ui elements
		self.form.le_latex_tempate.setText(os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.form.le_text_template.setText(os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.form.le_latex_out_dir.setText(os.path.abspath('Latex/Output'))
		self.form.le_text_out_dir.setText(os.path.abspath('Text/Output'))
		self.form.cb_open_pdf_after.setChecked(True)
		self.form.cb_open_text_after.setChecked(True)
		self.form.cb_keep_tex.setChecked(True)
		self.form.combo_latex_compiler.setCurrentText('custom')
		self.form.le_custom_latex.setText("test string")

		# Emulate click on OK button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Ok)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		self.assertEqual(self.form.latex_template, os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.assertEqual(self.form.text_template, os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.assertEqual(self.form.latex_dir, os.path.abspath('Latex/Output'))
		self.assertEqual(self.form.text_dir, os.path.abspath('Text/Output'))
		self.assertTrue(self.form.open_pdf)
		self.assertTrue(self.form.open_text)
		self.assertTrue(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'custom')
		self.assertEqual(self.form.latex_custom_command, "test string")

		# Test for False
		self.form.cb_open_pdf_after.setChecked(False)
		self.form.cb_open_text_after.setChecked(False)
		self.form.cb_keep_tex.setChecked(False)
		self.form.combo_latex_compiler.setCurrentText('xelatex')

		# Emulate click on OK button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Ok)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		self.assertFalse(self.form.open_pdf)
		self.assertFalse(self.form.open_text)
		self.assertFalse(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'xelatex')

	def test_click_apply_button(self):
		self.reset_all_variables()
		self.reset_all_ui_elements()

		# Set ui elements
		self.form.le_latex_tempate.setText(os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.form.le_text_template.setText(os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.form.le_latex_out_dir.setText(os.path.abspath('Latex/Output'))
		self.form.le_text_out_dir.setText(os.path.abspath('Text/Output'))
		self.form.cb_open_pdf_after.setChecked(True)
		self.form.cb_open_text_after.setChecked(True)
		self.form.cb_keep_tex.setChecked(True)
		self.form.combo_latex_compiler.setCurrentText('custom')
		self.form.le_custom_latex.setText("test string")

		# Emulate click on Apply button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Apply)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		self.assertEqual(self.form.latex_template, os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.assertEqual(self.form.text_template, os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.assertEqual(self.form.latex_dir, os.path.abspath('Latex/Output'))
		self.assertEqual(self.form.text_dir, os.path.abspath('Text/Output'))
		self.assertTrue(self.form.open_pdf)
		self.assertTrue(self.form.open_text)
		self.assertTrue(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'custom')
		self.assertEqual(self.form.latex_custom_command, "test string")

		# Test for False
		self.form.cb_open_pdf_after.setChecked(False)
		self.form.cb_open_text_after.setChecked(False)
		self.form.cb_keep_tex.setChecked(False)
		self.form.combo_latex_compiler.setCurrentText('xelatex')

		# Emulate click on Apply button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Apply)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		self.assertFalse(self.form.open_pdf)
		self.assertFalse(self.form.open_text)
		self.assertFalse(self.form.keep_tex)
		self.assertEqual(self.form.latex_compiler, 'xelatex')

	def test_click_cancel_button(self):
		self.reset_all_ui_elements()

		# Emulate click on Cancel button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Cancel)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		# Test if everything is still default
		self.assertEqual(self.form.le_latex_tempate.text(),
						 os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.assertEqual(self.form.le_text_template.text(), os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.assertEqual(self.form.le_latex_out_dir.text(), os.path.abspath('Latex/Output'))
		self.assertEqual(self.form.le_text_out_dir.text(), os.path.abspath('Text/Output'))
		self.assertTrue(self.form.cb_open_pdf_after.isChecked())
		self.assertTrue(self.form.cb_open_text_after.isChecked())
		self.assertTrue(self.form.cb_keep_tex.isChecked())
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')
		self.assertEqual(self.form.le_custom_latex.text(), '')

		# Test for False
		self.form.cb_open_pdf_after.setChecked(False)
		self.form.cb_open_text_after.setChecked(False)
		self.form.cb_keep_tex.setChecked(False)
		self.form.combo_latex_compiler.setCurrentText('xelatex')

		# Emulate click on Cancel button
		button = self.form.latex_buttonBox.button(self.form.latex_buttonBox.Cancel)
		QTest.mouseClick(button, QtCore.Qt.LeftButton)

		# still nothing should be changed
		self.assertTrue(self.form.cb_open_pdf_after.isChecked())
		self.assertTrue(self.form.cb_open_text_after.isChecked())
		self.assertTrue(self.form.cb_keep_tex.isChecked())
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')
		self.assertEqual(self.form.le_custom_latex.text(), '')

	def test_setting_window_closed(self):
		self.reset_all_ui_elements()

		# Emulate click on close button
		self.form.close()

		# Test if everything is still default
		self.assertEqual(self.form.le_latex_tempate.text(),
						 os.path.abspath('Latex/Templates/Awesome-CV/Latex_template.tex'))
		self.assertEqual(self.form.le_text_template.text(), os.path.abspath('Text/Templates/Simple/Text_template.txt'))
		self.assertEqual(self.form.le_latex_out_dir.text(), os.path.abspath('Latex/Output'))
		self.assertEqual(self.form.le_text_out_dir.text(), os.path.abspath('Text/Output'))
		self.assertTrue(self.form.cb_open_pdf_after.isChecked())
		self.assertTrue(self.form.cb_open_text_after.isChecked())
		self.assertTrue(self.form.cb_keep_tex.isChecked())
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')
		self.assertEqual(self.form.le_custom_latex.text(), '')

		# Test for False
		self.form.cb_open_pdf_after.setChecked(False)
		self.form.cb_open_text_after.setChecked(False)
		self.form.cb_keep_tex.setChecked(False)
		self.form.combo_latex_compiler.setCurrentText('xelatex')

		# Emulate click on close button
		self.form.close()

		# still nothing should be changed
		self.assertTrue(self.form.cb_open_pdf_after.isChecked())
		self.assertTrue(self.form.cb_open_text_after.isChecked())
		self.assertTrue(self.form.cb_keep_tex.isChecked())
		self.assertEqual(self.form.combo_latex_compiler.currentText(), 'xelatex')
		self.assertEqual(self.form.le_custom_latex.text(), '')


	@mock.patch('CoverletterCreator.SettingsHandler.os.path')
	def test_verify_path_field(self, mock_path):
		mock_path.exists.return_value = True

		self.form.verify_path_field('test_path_true', self.form.icon_latex_template)
		mock_path.exists.assert_called_with('test_path_true')

		self.assertTrue(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertTrue(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertTrue(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())
		self.assertTrue(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())

		mock_path.exists.return_value = False

		self.form.verify_path_field('test_path_false', self.form.icon_latex_template)
		mock_path.exists.assert_called_with('test_path_false')

		self.assertFalse(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertFalse(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Ok).isEnabled())
		self.assertFalse(self.form.latex_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())
		self.assertFalse(self.form.text_buttonBox.button(QtWidgets.QDialogButtonBox.Apply).isEnabled())

	@mock.patch('CoverletterCreator.SettingsHandler.QFileDialog', autospec=True)
	def test_open_latex_template(self, mock_opendialog):
		mock_opendialog.getOpenFileName.return_value = 'test_open_latex_template_filename', 'filetype'
		self.form.open_latex_template()
		self.assertTrue(mock_opendialog.getOpenFileName.called)
		self.assertEqual(os.path.abspath('test_open_latex_template_filename'), self.form.le_latex_tempate.text())

		# Simulate open dialog closed (canceled)
		mock_opendialog.getOpenFileName.return_value = '', ''
		self.form.open_latex_template()
		self.assertTrue(mock_opendialog.getOpenFileName.called)
		# no change
		self.assertEqual(os.path.abspath('test_open_latex_template_filename'), self.form.le_latex_tempate.text())

	@mock.patch('CoverletterCreator.SettingsHandler.QFileDialog', autospec=True)
	def test_open_latex_dir(self, mock_opendialog):
		mock_opendialog.getExistingDirectory.return_value = 'test_open_latex_dir_folder'
		self.form.open_latex_dir()
		self.assertTrue(mock_opendialog.getExistingDirectory.called)
		self.assertEqual(os.path.abspath('test_open_latex_dir_folder'), self.form.le_latex_out_dir.text())

		# Simulate open dialog closed (canceled)
		mock_opendialog.getExistingDirectory.return_value = ''
		self.form.open_latex_dir()
		self.assertTrue(mock_opendialog.getExistingDirectory.called)
		# no change
		self.assertEqual(os.path.abspath('test_open_latex_dir_folder'), self.form.le_latex_out_dir.text())

	@mock.patch('CoverletterCreator.SettingsHandler.QFileDialog', autospec=True)
	def test_open_text_template(self, mock_opendialog):
		mock_opendialog.getOpenFileName.return_value = 'test_open_text_template_filename', 'filetype'
		self.form.open_text_template()
		self.assertTrue(mock_opendialog.getOpenFileName.called)
		self.assertEqual(os.path.abspath('test_open_text_template_filename'), self.form.le_text_template.text())

		# Simulate open dialog closed (canceled)
		mock_opendialog.getOpenFileName.return_value = '', ''
		self.form.open_text_template()
		self.assertTrue(mock_opendialog.getOpenFileName.called)
		# no change
		self.assertEqual(os.path.abspath('test_open_text_template_filename'), self.form.le_text_template.text())

	@mock.patch('CoverletterCreator.SettingsHandler.QFileDialog', autospec=True)
	def test_open_text_dir(self, mock_opendialog):
		mock_opendialog.getExistingDirectory.return_value = 'test_open_text_dir_folder'
		self.form.open_text_dir()
		self.assertTrue(mock_opendialog.getExistingDirectory.called)
		self.assertEqual(os.path.abspath('test_open_text_dir_folder'), self.form.le_text_out_dir.text())

		# Simulate open dialog closed (canceled)
		mock_opendialog.getExistingDirectory.return_value = ''
		self.form.open_text_dir()
		self.assertTrue(mock_opendialog.getExistingDirectory.called)
		# no change
		self.assertEqual(os.path.abspath('test_open_text_dir_folder'), self.form.le_text_out_dir.text())


	def reset_all_variables(self):
		# Reset all variables

		self.form.latex_template = ""
		self.form.text_template = ""
		self.form.latex_dir = ""
		self.form.text_dir = ""
		self.form.open_pdf = False
		self.form.open_text = False
		self.form.keep_tex = False
		self.form.latex_compiler = ""
		self.form.latex_custom_command = ""

	def reset_all_ui_elements(self):
		self.form.le_latex_tempate.setText("")
		self.form.le_text_template.setText("")
		self.form.le_latex_out_dir.setText("")
		self.form.le_text_out_dir.setText("")
		self.form.cb_open_pdf_after.setChecked(True)
		self.form.cb_open_text_after.setChecked(True)
		self.form.cb_keep_tex.setChecked(True)
		self.form.combo_latex_compiler.setCurrentText("")
		self.form.le_custom_latex.setText("")


