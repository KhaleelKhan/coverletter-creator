from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFileDialog

from CoverletterCreator.ui import progress
from PyQt5 import QtCore



class ProgressDisplay(QtWidgets.QDialog, progress.Ui_ProgressDialog):
	def __init__(self, executable, arguments, parent=None):
		super(ProgressDisplay, self).__init__(parent)
		self.setupUi(self)
		movie = QtGui.QMovie(":/animation/ajax-loader.gif")
		self.progress_bar.setMovie(movie)
		movie.start()

		# QProcess object for external app
		self.process = QtCore.QProcess(self)
		# QProcess emits `readyRead` when there is data to be read
		self.process.readyRead.connect(self.dataReady)

		# Just to prevent accidentally running multiple times
		# Disable the button when process starts, and enable it when it finishes
		self.process.started.connect(lambda: self.buttonBox.setEnabled(False))
		self.process.finished.connect(self.processFinished)

		self.process.start(executable, arguments)

	def dataReady(self):
		cursor = self.log_display.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(str(self.process.readAll(), 'utf-8'))
		self.log_display.ensureCursorVisible()

	def processFinished(self):
		self.buttonBox.setEnabled(True)
		self.label.setText("Compilation Finished")
		self.progress_bar.movie().stop()
		self.close()



def run():
	app = QtWidgets.QApplication(sys.argv)
	form = ProgressDisplay('ping',['-c 3','127.0.0.1'])
	form.show()
	app.exec_()


if __name__ == "__main__":
	import sys
	run()