import unittest
from CoverletterCreator.pdfCreator import PdfCreator
from lxml.etree import XML
import jinja2


class TestPdfCreator(unittest.TestCase):
	def setUp(self):
		xml = XML("<root><personal_info><FIRSTNAME>Max</FIRSTNAME></personal_info></root>")
		self.pdf_creator = PdfCreator(data=xml)

		with open('Latex_template.tex', 'w')as f:
			f.write(r'\VAR{FIRSTNAME}')

	def tearDown(self):
		import os
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
		self.assertTrue(self.pdf_creator.renderer_template == 'Max')

	# Commented till Qt testing can be implemented
	# def test_compile_xelatex(self):
	# 	pdf_template = 'Latex_template.tex'
	# 	self.pdf_creator.read_template(template=pdf_template)
	# 	self.pdf_creator.convert_to_dict()
	# 	self.pdf_creator.render_template()
	# 	self.pdf_creator.compile_xelatex(compiler='xelatex', pdfname='output.pdf', outputDir='./', open_pdf=False)

if __name__ == '__main__':
	unittest.main()
