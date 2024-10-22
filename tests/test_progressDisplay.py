import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtTest import QTest

from CoverletterCreator.ProgressDisplay import ProgressDisplay

app = QtWidgets.QApplication(sys.argv)


class TestProgressDisplay(TestCase):
	def setUp(self):
		self.progress_display = ProgressDisplay('python', ['-h'])

	def test_show_dialog(self):
		self.progress_display.show()

	def test_defaults(self):
		self.assertEqual(self.progress_display.label.text(), "Please wait while PDF is compiled ")
		self.assertEqual(self.progress_display.log_display.toPlainText(), "")
		self.assertFalse(self.progress_display.buttonBox.isEnabled())

	def test_results_after_execution(self):
		self.progress_display.exec_()
		self.assertEqual(self.progress_display.label.text(), "Compilation Finished")
		self.assertNotEqual(self.progress_display.log_display.toPlainText(), "")
		self.assertTrue(self.progress_display.buttonBox.isEnabled())

		QTest.mouseClick(self.progress_display.buttonBox, QtCore.Qt.LeftButton)

	def tearDown(self):
		self.progress_display.close()
		del self.progress_display
