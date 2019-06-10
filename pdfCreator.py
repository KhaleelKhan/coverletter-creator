import os

import jinja2

latex_jinja_env = jinja2.Environment(
	block_start_string='\BLOCK{',
	block_end_string='}',
	variable_start_string='\VAR{',
	variable_end_string='}',
	comment_start_string='\#{',
	comment_end_string='}',
	line_statement_prefix='%%',
	line_comment_prefix='%#',
	trim_blocks=True,
	autoescape=False,
	loader=jinja2.FileSystemLoader(os.path.abspath('/'))
)


class PdfCreator():
	def __init__(self, data, parent=None):
		super(PdfCreator, self).__init__()
		self.lxml_data = data

	def read_template(self, template):
		# TODO: test if template file exists
		self.template = latex_jinja_env.get_template(os.path.realpath(template))

	def render_template(self):
		self.renderer_template = self.template.render(self.render_dict)

	def convert_to_dict(self):
		temp_dict = {}
		for element in self.lxml_data.iter():
			if element.text is not None:
				temp_dict[str(element.tag)] = str(element.text).replace('\n', r'\\')
		self.render_dict = temp_dict

	def compile_xelatex(self, pdfname, outputDir, photo):
		"""
		Genertates the pdf from string
		"""

		import subprocess
		import os
		import tempfile
		import shutil

		current = os.getcwd()
		temp = tempfile.mkdtemp()
		shutil.copy(photo, temp)
		os.chdir(temp)

		f = open('coverletter.tex', 'w')
		f.write(self.renderer_template)
		f.close()

		proc = subprocess.Popen(['xelatex', '-interaction=nonstopmode', 'coverletter.tex'])
		proc.communicate()

		os.rename('coverletter.pdf', pdfname)
		shutil.copy(pdfname, outputDir)
		shutil.copy('coverletter.tex', outputDir)
		shutil.rmtree(temp)
		os.chdir(current)


if __name__ == "__main__":
	pdfcreator = PdfCreator()
	pdfcreator.read_template()
	pdfcreator.render_template()
	pdfcreator.compile_xelatex(pdfname='coverletter.pdf')
