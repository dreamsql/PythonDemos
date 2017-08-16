import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	def __init__(self, txt):
		self.text = txt
		self.words = RE_WORD.findall(txt)

	def __getitem__(self, index):
		return self.words[index]

	def __len__(self):
		return len(self.words)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)


	
