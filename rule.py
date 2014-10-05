class Rule(object):
	"""docstring for Rule"""
	def __init__(self):
		super(Rule, self).__init__()
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True

class HeadingRule(Rule):
	"""docstring for HeadingRule"""
	type="heading"
	def __init__(self):
		super(HeadingRule, self).__init__()
	def condition(self,block):
		return not '\n' in block and len(block)<70 and not block[-1]==':'
class TitleRule(HeadingRule):
	"""docstring for TitleRule"""
	type="title"
	first=True
	def __init__(self):
		super(TitleRule, self).__init__()
	def condition(self,block):
		if not self.first:
			return self.first
		self.first=False
		return HeadingRule.condition(self,block)

class ListItemRule(Rule):
	"""docstring for ListItemRule"""
	type="listitem"
	def __init__(self):
		super(ListItemRule, self).__init__()
	def condition(self,block):
		return block[0]=="-"
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block[1:])
		handler.end(self.type)
		return True		

class ListRule(ListItemRule):
	"""docstring for ListRule"""
	type="list"
	inline=False
	def __init__(self):
		super(ListRule, self).__init__()
	def condition(self,block):
		return True
	def action(self,block,handler):
		if not self.inline and ListItemRule.condition(self,block):
			handler.start(self.type)
			self.inline=True
		elif self.inline and not ListItemRule.condition(self,block):
			handler.end(self.type)
			self.inline=False
		return False

class ParagraphRule(Rule):
	"""docstring for ParagraphRule"""
	type="paragraph"
	def __init__(self):
		super(ParagraphRule, self).__init__()
	def condition(self,block):
		return True
		
		
