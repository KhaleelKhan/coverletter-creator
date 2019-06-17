import os
import subprocess
import sys

import jinja2


class TextCreator:
	"""
	This class handles text rendering and saving to file.

	"""

	def __init__(self, data):
		"""
		Initialise TextCreator

		:param data: lxml root data
		:type data: lxml.etree
		"""
		super(TextCreator, self).__init__()
		self.lxml_data = data

	def read_template(self, template):
		"""
		Generates jinja2 template from text file.

		:param template: Path to template file
		:type template: str
		"""
		with open(os.path.realpath(template), 'r') as f:
			template_str = f.read()
			self.template = jinja2.Template(template_str)

	def render_template(self):
		"""
		Render template using jinja renderer.

		"""
		self.rendered_template = self.template.render(self.render_dict)

	def convert_to_dict(self):
		"""
		Convert xml data to dict, dict is used while rendering wih jinja.

		"""
		temp_dict = {}
		for element in self.lxml_data.iter():
			if element.text is not None:
				temp_dict[str(element.tag)] = str(element.text)
		self.render_dict = temp_dict

	def compile_text(self, textname, outputDir, open_text=True):
		"""
		Generates the text from string.

		:param textname: Name of the output file.
		:type textname: str
		:param outputDir: Output Directory.
		:type outputDir: str
		:param open_text: Open text file after saving?
		:type open_text: Bool
		"""

		outputFile = os.path.join(outputDir, textname)
		with open(outputFile, 'w+') as f:
			f.write(self.rendered_template)

		if open_text:
			if sys.platform.startswith('linux'):
				subprocess.call(["xdg-open", outputFile])
			else:
				os.startfile(os.path.join(outputDir, outputFile))

