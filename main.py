#!/usr/bin/env python3

if __name__ == '__main__':

	import sys
	from CoverletterCreator.coverletter_creator import CoverletterCreator
	from PyQt5 import QtWidgets

	app = QtWidgets.QApplication(sys.argv)
	app.setOrganizationName("KhaleelKhan")
	app.setApplicationName("Coverletter_Creator-dev")
	form = CoverletterCreator()
	form.show()
	app.exec_()
	sys.exit()
