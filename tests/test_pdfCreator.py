import unittest
from CoverletterCreator.pdfCreator import PdfCreator
from lxml.etree import XML
import jinja2
import sys, os

from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)


class TestPdfCreator(unittest.TestCase):
	def setUp(self):
		xml = XML("<root><personal_info><FIRSTNAME>Max</FIRSTNAME></personal_info></root>")
		self.pdf_creator = PdfCreator(data=xml)

		with open('Latex_template.tex', 'w')as f:
			f.write('\\documentclass[11pt,a4paper]{article}\n\\begin{document}\n\\VAR{FIRSTNAME}\n\\end{document}')

	def tearDown(self):
		os.remove('Latex_template.tex')

	def test_read_template(self):
		# Use a valid text template
		pdf_template = 'Latex_template.tex'
		self.pdf_creator.read_template(template=pdf_template)
		# Check if jinja2 template is created
		self.assertIsInstance(self.pdf_creator.template, jinja2.Template)

	def test_read_template_raises_exection(self):
		# Use a invalid test template and check if exception thrown
		pdf_template = 'nonExistantFile.tex'
		self.assertRaises(jinja2.exceptions.TemplateNotFound, self.pdf_creator.read_template, pdf_template)

	def test_convert_to_dict(self):
		self.pdf_creator.convert_to_dict()
		# test if dict is created with element from xml
		self.assertIsInstance(self.pdf_creator.render_dict, dict)
		self.assertEqual(self.pdf_creator.render_dict["FIRSTNAME"], "Max")

	def test_render_template(self):
		pdf_template = 'Latex_template.tex'
		self.pdf_creator.read_template(template=pdf_template)
		self.pdf_creator.convert_to_dict()
		self.pdf_creator.render_template()
		self.assertTrue('Max' in self.pdf_creator.renderer_template)
		self.assertTrue('\\VAR{' not in self.pdf_creator.renderer_template)

	def test_compile_xelatex(self):
		pdf_template = 'Latex_template.tex'
		self.pdf_creator.read_template(template=pdf_template)
		self.pdf_creator.convert_to_dict()
		self.pdf_creator.render_template()
		output_dir = os.path.abspath('./')
		self.pdf_creator.compile_xelatex(compiler='pdflatex', pdfname='output.pdf', outputDir=output_dir, open_pdf=False)

		with open('coverletter.tex', 'r') as f:
			test_string = f.read()
		self.assertTrue('Max' in test_string)
		self.assertTrue(os.path.exists('output.pdf'))

		os.remove('output.pdf')
		os.remove('coverletter.tex')

if __name__ == '__main__':
	unittest.main()
