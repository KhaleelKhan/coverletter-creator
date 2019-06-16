import unittest
from CoverletterCreator.textCreator import TextCreator
from lxml.etree import XML
import jinja2


class TestTextCreator(unittest.TestCase):
	def setUp(self):
		xml = XML("<root><personal_info><FIRSTNAME>Max</FIRSTNAME></personal_info></root>")
		self.text_creator = TextCreator(data=xml)

		with open('Text_template.txt', 'w')as f:
			f.write('{{FIRSTNAME}}')

	def tearDown(self):
		import os
		os.remove('Text_template.txt')

	def test_read_template(self):
		# Use a valid text template
		text_template = 'Text_template.txt'
		self.text_creator.read_template(template=text_template)
		# Check if jinja2 template is created
		self.assertIsInstance(self.text_creator.template, jinja2.Template)

	def test_read_template_raises_exection(self):
		# Use a invalid test template and check if exception thrown
		text_template = 'nonExistantFile.txt'
		self.assertRaises(FileNotFoundError, self.text_creator.read_template, text_template)

	def test_convert_to_dict(self):
		self.text_creator.convert_to_dict()
		# test if dict is created with element from xml
		self.assertIsInstance(self.text_creator.render_dict, dict)
		self.assertEqual(self.text_creator.render_dict["FIRSTNAME"], "Max")

	def test_render_template(self):
		text_template = 'Text_template.txt'
		self.text_creator.read_template(template=text_template)
		self.text_creator.convert_to_dict()
		self.text_creator.render_template()
		self.assertTrue(self.text_creator.renderer_template == 'Max')

	def test_compile_text(self):
		text_template = 'Text_template.txt'
		self.text_creator.read_template(template=text_template)
		self.text_creator.convert_to_dict()
		self.text_creator.render_template()
		self.text_creator.compile_text(textname='output.txt', outputDir='./', open_text=False)

		with open('output.txt', 'r') as f:
			test_string = f.read()
		self.assertEqual(test_string, 'Max')

		import os
		os.remove('output.txt')




if __name__ == '__main__':
	unittest.main()

