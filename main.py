#!/usr/bin/env python3

if __name__ == '__main__':

	import sys
	from CoverletterCreator import coverletter_creator
	from PyQt5 import QtCore

	QtCore.QCoreApplication.setOrganizationName("KhaleelKhan")
	QtCore.QCoreApplication.setApplicationName("Coverletter_Creator-dev")
	sys.exit(coverletter_creator.run())
