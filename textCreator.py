import os

import jinja2


class TextCreator():
	def __init__(self, data, parent=None):
		super(TextCreator, self).__init__()
		self.lxml_data = data

	def read_template(self, template):
		# TODO: test if template file exists
		with open(os.path.realpath(template), 'r') as f:
			template_str = f.read()
			self.template = jinja2.Template(template_str)

	def render_template(self):
		self.renderer_template = self.template.render(self.render_dict)

	def convert_to_dict(self):
		temp_dict = {}
		for element in self.lxml_data.iter():
			if element.text is not None:
				temp_dict[str(element.tag)] = str(element.text)
		self.render_dict = temp_dict

	def compile_text(self, textname, outputDir):
		"""
		Genertates the text from string
		"""

		import os

		outputFile = os.path.join(outputDir, textname)
		with open(outputFile, 'w') as f:
			f.write(self.renderer_template)



if __name__ == "__main__":
	textcreator = TextCreator()
	textcreator.read_template()
	textcreator.render_template()