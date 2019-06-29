#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# credit: https://nachtimwald.com/2009/08/22/qplaintextedit-with-in-line-spell-check/

__license__ = 'MIT'
__copyright__ = '2009, John Schember '
__docformat__ = 'restructuredtext en'

import os
import re
import sys

from PyQt5.QtCore import QEvent, QStandardPaths, Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QSyntaxHighlighter, QTextCharFormat, QTextCursor
from PyQt5.QtWidgets import QAction, QApplication, QMenu, QPlainTextEdit
from spellchecker import SpellChecker


class SpellTextEdit(QPlainTextEdit):

    def __init__(self, *args):
        QPlainTextEdit.__init__(self, *args)

        # Path for custom dict
        custom_dict_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
		custom_dict_filename = 'customWords.txt'
        self.custom_dict = os.path.join(custom_dict_path, custom_dict_filename)
        os.makedirs(os.path.dirname(self.custom_dict), exist_ok=True)

        # Default dictionary based on the local locale.
		self.spell = SpellChecker()
		if os.path.exists(self.custom_dict):
			self.spell.word_frequency.load_text_file(self.custom_dict)

        self.highlighter = Highlighter(self.document())
		self.highlighter.setDict(self.spell)


    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            # Rewrite the mouse event to a left button event so the cursor is
            # moved to the location of the pointer.
            event = QMouseEvent(QEvent.MouseButtonPress, event.pos(),
                Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
        QPlainTextEdit.mousePressEvent(self, event)

    def contextMenuEvent(self, event):
        popup_menu = self.createStandardContextMenu()

        # Select the word under the cursor.
        cursor = self.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        self.setTextCursor(cursor)

        # Check if the selected word is misspelled and offer spelling
        # suggestions if it is.
        if self.textCursor().hasSelection():
            text = str(self.textCursor().selectedText())
			if text not in self.spell:
                spell_menu = QMenu('Spelling Suggestions')
				for word in self.spell.candidates(text):
                    action = SpellAction(word, spell_menu)
                    action.correct.connect(self.correctWord)
                    spell_menu.addAction(action)
                spell_menu.addSeparator()
                action = spell_menu.addAction('Add to Dictionary')
                action.triggered.connect(lambda: self.addWord(text))
                # Only add the spelling suggests to the menu if there are
                # suggestions.
                if len(spell_menu.actions()) != 0:
                    popup_menu.insertSeparator(popup_menu.actions()[0])
                    popup_menu.insertMenu(popup_menu.actions()[0], spell_menu)

        popup_menu.exec_(event.globalPos())

    def correctWord(self, word):
        '''
        Replaces the selected text with word.
        '''
        cursor = self.textCursor()
        cursor.beginEditBlock()

        cursor.removeSelectedText()
        cursor.insertText(word)

        cursor.endEditBlock()

    def addWord(self, word):
		self.spell.word_frequency.add(word)
		self.highlighter.setDict(self.spell)
        self.highlighter.rehighlight()

		# Save custom word
		with open(self.custom_dict, 'a+') as f:
			f.write(word + " ")

class Highlighter(QSyntaxHighlighter):

    WORDS = u'(?iu)[\w\']+'

    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)

        self.dict = None

    def setDict(self, dict):
        self.dict = dict

    def highlightBlock(self, text):
        if not self.dict:
            return

        text = str(text)

        format = QTextCharFormat()
        format.setUnderlineColor(Qt.red)
        format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)

        for word_object in re.finditer(self.WORDS, text):
			if word_object.group() not in self.dict:
                self.setFormat(word_object.start(),
                    word_object.end() - word_object.start(), format)


class SpellAction(QAction):

    '''
    A special QAction that returns the text in a signal.
    '''

    correct = pyqtSignal(str)

    def __init__(self, *args):
        QAction.__init__(self, *args)

        self.triggered.connect(lambda x: self.correct.emit(
            str(self.text())))


def main(args=sys.argv):
    app = QApplication(args)

    spellEdit = SpellTextEdit()
    spellEdit.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())