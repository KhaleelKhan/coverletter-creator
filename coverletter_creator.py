import sys
import mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class CoverletterCreator(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
	def __init__(self, parent=None):
		super(CoverletterCreator, self).__init__(parent)
		self.setupUi(self)

		self.actionSave.triggered.connect(self.save_project)
		self.actionSave_As.triggered.connect(self.saveas_project)
		self.actionOpen.triggered.connect(self.open_project)

		self.filename = ""

	def save_project(self):
		try:
			open(self.filename, 'w')
		except OSError:
			self.filename = self.saveas_project()

			open(self.filename, 'w+')

	def saveas_project(self):
		filename, _ =QFileDialog.getSaveFileName(self, "Save Project","./","XML Files (*.xml)")
		return filename + ".xml"

	def open_project(self):
		filename, _ = QFileDialog.getOpenFileName(self, "Open Project","./","XML Files (*.xml)")
		self.filename = filename + ".xml"

def main():
	app = QtWidgets.QApplication(sys.argv)
	form = CoverletterCreator()
	form.show()
	app.exec_()


if __name__ == "__main__":
	main()
