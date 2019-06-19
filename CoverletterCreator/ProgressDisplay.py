from PyQt5 import QtCore, QtGui, QtWidgets

from CoverletterCreator.ui import progress


class ProgressDisplay(QtWidgets.QDialog, progress.Ui_ProgressDialog):
	"""
	This class handles execution of command while showing the log in a dialog window.
	"""
	def __init__(self, executable, arguments, parent=None):
		"""
		Initialising ProgressDisplay.

		:param executable: Executable command to run.
		:type executable: str
		:param arguments: List of arguments passed to Qprocess
		:type arguments: list of str
		:param parent: Optional Qwidget parent
		:type parent: Qwidget
		"""
		super(ProgressDisplay, self).__init__(parent)
		self.setupUi(self)

		# start the progress animation
		movie = QtGui.QMovie(":/animation/ajax-loader.gif")
		self.progress_bar.setMovie(movie)
		movie.start()

		self.executable = executable
		self.arguments = arguments

		# QProcess object for external app
		self.process = QtCore.QProcess(self)
		# QProcess emits `readyRead` when there is data to be read
		self.process.readyRead.connect(self.dataReady)

		# Disable the button when process starts, and enable it when it finishes
		self.process.started.connect(lambda: self.buttonBox.setEnabled(False))
		self.process.finished.connect(self.processFinished)

		self.process.start(self.executable, self.arguments)

	def dataReady(self):
		"""
		Called by Qprocess on readyData. Adds output of Qprocess to PlainTextEdit.

		"""
		cursor = self.log_display.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(str(self.process.readAll(), 'utf-8'))
		self.log_display.ensureCursorVisible()

	def processFinished(self):
		"""
		Called in Qprocess finished. Stop movie and display "finished".
		Also enables Ok button for closing this dialog.

		"""
		self.buttonBox.setEnabled(True)
		self.label.setText("Compilation Finished")
		self.progress_bar.movie().stop()
		self.close()

	def __del__(self):
		# If QApplication is closed attempt to kill the process
		self.process.terminate()
		# Wait for Xms and then elevate the situation to terminate
		if not self.process.waitForFinished(10000):
			self.process.kill()


if __name__ == "__main__":
	pass
