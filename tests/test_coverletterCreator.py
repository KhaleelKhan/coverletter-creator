import sys
from unittest import TestCase, mock

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

from CoverletterCreator.coverletter_creator import CoverletterCreator

app = QtWidgets.QApplication(sys.argv)
app.setOrganizationName("KhaleelKhan")
app.setApplicationName("Coverletter_Creator-unittest")


class TestCoverletterCreator(TestCase):
	def setUp(self):
		# Start app fresh
		self.qsettings = QSettings()
		self.qsettings.clear()
		self.cc = CoverletterCreator()
		self.cc.show()

	def tearDown(self):
		self.cc.file_dirty = False  # To not trigger "are you sure?" popup
		self.cc.close()

	def test_check_mandatory_fields(self):
		self.cc.FIRSTNAME.setText("test")
		self.cc.FIRSTNAME.setText("")
		self.assertFalse(self.cc.pb_generatePdf.isEnabled())
		self.assertFalse(self.cc.pb_generateText.isEnabled())

	'''
	def test_label_clicked(self):
		self.fail()

	def test_checkbox_clicked(self):
		self.fail()

	def test_combobox_clicked(self):
		self.fail()

	def test_setWindowTitleUnsaved(self):
		self.fail()

	def test_setWindowTitleSaved(self):
		self.fail()

	def test_new_project(self):
		self.fail()

	def test_reset_all_fields(self):
		self.fail()

	def test_save_project(self):
		self.fail()

	def test_generate_root(self):
		self.fail()

	def test_saveas_project(self):
		self.fail()

	def test_open_project(self):
		self.fail()

	def test_load_file(self):
		self.fail()
	'''

	@mock.patch('CoverletterCreator.coverletter_creator.QFileDialog', autospec=True)
	@mock.patch('CoverletterCreator.coverletter_creator.QtWidgets.QMessageBox.information')
	def test_browse_and_get_photo(self, mock_error, mock_opendialog):
		from PyQt5 import QtGui
		# Valid photo path
		mock_opendialog.getOpenFileName.return_value = 'Latex/Resources/profile.png', 'file_type'
		self.cc.label_pic.clear()
		self.cc.browse_photo()
		self.assertEqual("Latex/Resources/profile.png", self.cc.PHOTOPATH.text())
		self.assertIsInstance(self.cc.label_pic.pixmap(), QtGui.QPixmap)

		# invalid photo path
		mock_opendialog.getOpenFileName.return_value = 'invalid.png', 'file_type'
		self.cc.browse_photo()
		# ensure no change on set path
		self.assertEqual("Latex/Resources/profile.png", self.cc.PHOTOPATH.text())
		assert mock_error.called

	@mock.patch('CoverletterCreator.coverletter_creator.PdfCreator')
	@mock.patch('CoverletterCreator.coverletter_creator.QtWidgets.QMessageBox.critical')
	def test_generate_pdf(self, mock_error, mock_pdfcreator):
		self.cc.settings.latex_template = "test_generate_latex_template"
		self.cc.settings.latex_dir = "test_generate_latex_dir"
		self.cc.settings.open_pdf = True
		self.cc.generate_pdf()

		assert mock_pdfcreator.called
		assert mock_pdfcreator().read_template.called
		mock_pdfcreator().read_template.assert_called_with(template="test_generate_latex_template")
		assert mock_pdfcreator().convert_to_dict.called
		assert mock_pdfcreator().render_template.called
		assert mock_pdfcreator().compile_xelatex.called

		mock_pdfcreator().compile_xelatex.side_effect = FileNotFoundError
		self.cc.generate_pdf()
		assert mock_error.called

	@mock.patch('CoverletterCreator.coverletter_creator.TextCreator')
	@mock.patch('CoverletterCreator.coverletter_creator.QtWidgets.QMessageBox.critical')
	def test_generate_text(self, mock_error, mock_textcreator):
		self.cc.settings.text_template = "test_generate_text_template"
		self.cc.settings.text_dir = "test_generate_text_dir"
		self.cc.settings.open_text = True
		self.cc.generate_text()

		assert mock_textcreator.called
		assert mock_textcreator().read_template.called
		mock_textcreator().read_template.assert_called_with(template="test_generate_text_template")
		assert mock_textcreator().convert_to_dict.called
		assert mock_textcreator().render_template.called
		assert mock_textcreator().compile_text.called
		mock_textcreator().compile_text.assert_called_with(open_text=True, outputDir='test_generate_text_dir',
														   textname=mock.ANY)

		mock_textcreator().read_template.side_effect = FileNotFoundError
		self.cc.generate_text()
		assert mock_error.called

	def test_writeSettings(self):
		self.cc.filename = "test_writeSettings_filename"
		# Set file not modified
		self.cc.file_dirty = False
		self.cc.writeSettings()
		self.qsettings.beginGroup("Project")
		self.assertEqual("test_writeSettings_filename", self.qsettings.value("filename"))
		self.qsettings.endGroup()

		self.cc.filename = "test_writeSettings_filename_modified"
		# Set file modified
		self.cc.file_dirty = True
		self.cc.writeSettings()
		self.qsettings.beginGroup("Project")
		# Settings not changed because file has not been saved
		self.assertEqual("test_writeSettings_filename", self.qsettings.value("filename"))
		self.qsettings.endGroup()

	def test_readSettings(self):
		self.qsettings.beginGroup("Project")
		self.qsettings.setValue("filename", "test_readSettings_filename")
		self.qsettings.endGroup()

		self.cc.readSettings()
		self.assertEqual("test_readSettings_filename", self.cc.filename)
