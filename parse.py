from handlers import *
import sys,re
from rule import *
from util import *

class Parser(object):
	"""docstring for Parser"""
	def __init__(self, handler):
		super(Parser, self).__init__()
		self.handler=handler
		self.rules=[]
		self.filters=[]
	def addRule(self,rule):
		self.rules.append(rule)
	def addFilter(self,pattern,name):
		def filter(block,handler):
			return re.sub(pattern,handler.sub(name),block)
		self.filters.append(filter)

	def parse(self,file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block=filter(block,self.handler)
			for rule in self.rules:
				if (rule.condition(block)):
					flag=rule.action(block,self.handler)
					if flag:break
		self.handler.end('document')

class BasicTextParser(Parser):
	def __init__(self,handler):
		super(BasicTextParser,self).__init__(handler)
		emphasisP=re.compile(r'\*(.+?)\*')
		emailP=re.compile(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)')
		urlP=re.compile(r'(http://[\.a-zA-Z/]+)')
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())
		self.addFilter(emphasisP,'emphasis')
		self.addFilter(emailP,'mail')
		self.addFilter(urlP,'url')