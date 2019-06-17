import os
import sys

import jinja2

from CoverletterCreator.ProgressDisplay import ProgressDisplay
from CoverletterCreator.SettingsHandler import SettingsHandler

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


class PdfCreator:
	"""
	This class handles latex rendering and generating pdf.

	"""
	def __init__(self, data, parent=None):
		"""
		Initialise PdfCreator

		:param data: lxml root data
		:type data: lxml.etree
		:param parent: Optional parent for gui creation.
		:type parent: QtWidgets.QMainWindow
		"""
		super(PdfCreator, self).__init__()
		self.lxml_data = data
		self.parent = parent

	def read_template(self, template):
		"""
		Generates jinja2 template from text file.

		:param template: Path to template file
		:type template: str
		"""
		self.template = latex_jinja_env.get_template(os.path.realpath(template))

	def render_template(self):
		"""
		Render template using jinja renderer.

		"""
		self.renderer_template = self.template.render(self.render_dict)

	def convert_to_dict(self):
		"""
		Convert xml data to dict, dict is used while rendering wih jinja.

		"""
		temp_dict = {}
		for element in self.lxml_data.iter():
			if element.text is not None:
				temp_dict[str(element.tag)] = str(element.text).replace('\n', r'\\')
		self.render_dict = temp_dict
		self.render_dict['PHOTOPATH'] = os.path.abspath(self.render_dict['PHOTOPATH'])

	def compile_xelatex(self, compiler, pdfname, outputDir, open_pdf=True, keep_tex=True):
		"""
		Generates the pdf from string.

		:param compiler: Which latex compiler to use.
		:type compiler: str
		:param pdfname: Name of the output file.
		:type pdfname: str
		:param outputDir: Output Directory.
		:type outputDir: str
		:param photo: Optional photo path.
		:type photo: str
		:param open_pdf: Open text file after saving?
		:type open_pdf: Bool
		:param keep_tex: Keep .tex file after pdf compilation?
		:type keep_tex: Bool
		"""

		import subprocess
		import os
		import tempfile
		import shutil

		current = os.getcwd()
		temp = tempfile.mkdtemp()
		os.chdir(temp)

		f = open('coverletter.tex', 'w')
		f.write(self.renderer_template)
		f.close()

		if compiler in SettingsHandler.latex_compiler_list:
			args = ['-interaction=nonstopmode', 'coverletter.tex']
		else:
			args = ['-halt-on-error', 'coverletter.tex']

		# Start a dialog window which handles log display and execution.
		progress_display = ProgressDisplay(parent=self.parent, executable=compiler, arguments=args)
		progress_display.exec_()  # This blocks the other windows, which is expected. self closing.
		# Reshow dialog window but in non-blocking mode
		progress_display.show()

		try:
			os.rename('coverletter.pdf', pdfname)
			shutil.copy(pdfname, outputDir)
			if keep_tex:
				shutil.copy('coverletter.tex', outputDir)
		except FileNotFoundError:
			raise FileNotFoundError
		shutil.rmtree(temp)
		os.chdir(current)

		if open_pdf:
			if sys.platform.startswith('linux'):
				subprocess.call(["xdg-open", os.path.join(outputDir, pdfname)])
			else:
				os.startfile(os.path.join(outputDir, pdfname))
