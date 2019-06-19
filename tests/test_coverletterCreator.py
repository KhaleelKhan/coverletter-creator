import sys
from unittest import TestCase
from unittest import mock
from PyQt5 import QtWidgets, QtCore

from CoverletterCreator.coverletter_creator import CoverletterCreator

app = QtWidgets.QApplication(sys.argv)
app.setOrganizationName("KhaleelKhan")
app.setApplicationName("Coverletter_Creator-unittest")

class TestCoverletterCreator(TestCase):
	def setUp(self):
		self.cc = CoverletterCreator()
		self.cc.show()

	def tearDown(self):
		self.cc.close()

	def test_connect_all_fields(self):
		self.fail()

	def test_connect_mandatory_fields(self):
		self.fail()

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

	def test_browse_photo(self):
		self.fail()

	def test_get_photo(self):
		self.fail()

	def test_generate_pdf(self):
		self.fail()

	def test_generate_text(self):
		self.fail()

	def test_writeSettings(self):
		self.fail()

	def test_readSettings(self):
		self.fail()

	def test_closeEvent(self):
		self.fail()
