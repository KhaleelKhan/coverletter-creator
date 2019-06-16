import os
import sys

import jinja2

from CoverletterCreator.SettingsHandler import SettingsHandler
from CoverletterCreator.ProgressDisplay import ProgressDisplay

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
		self.parent = parent

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

	def compile_xelatex(self, compiler, pdfname, outputDir, photo=None, open_pdf=True, keep_tex=True):
		"""
		Genertates the pdf from string
		"""

		import subprocess
		import os
		import tempfile
		import shutil

		current = os.getcwd()
		temp = tempfile.mkdtemp()
		if photo is not None:
			shutil.copy(photo, temp)
		os.chdir(temp)

		f = open('coverletter.tex', 'w')
		f.write(self.renderer_template)
		f.close()

		if compiler in SettingsHandler.latex_compiler_list:
			args = ['-interaction=nonstopmode', 'coverletter.tex']
		else:
			args = ['coverletter.tex']
		progress_display = ProgressDisplay(parent=self.parent, executable=compiler, arguments=args)
		progress_display.exec_()
		progress_display.show()

		try:
			os.rename('coverletter.pdf', pdfname)
			shutil.copy(pdfname, outputDir)
			if keep_tex:
				shutil.copy('coverletter.tex', outputDir)
			shutil.rmtree(temp)
			os.chdir(current)
		except FileNotFoundError:
			raise FileNotFoundError

		if open_pdf:
			if sys.platform.startswith('linux'):
				subprocess.call(["xdg-open", os.path.join(outputDir, pdfname)])
			else:
				os.startfile(os.path.join(outputDir, pdfname))
