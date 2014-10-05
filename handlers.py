class Handlers(object):
	"""docstring for Handlers,base class to hand different conditions
		start hand start of  
		end hand end of 
	"""
	def __init__(self):
		super(Handlers, self).__init__()
	def callback(self,prefix,name,*arg):
		#print prefix+':'+name
		method=getattr(self,prefix+name,None)
		if callable(method):return method(*arg)
	def start(self,name):
		self.callback('start_',name)
	def end(self,name):
		self.callback('end_',name)
	def sub(self,name):
		def subsititution(match):
			res=self.callback('sub_',name,match)
			if res is None:return match.group(0)
			return res
		return subsititution

class HttpHandlers(Handlers):
	"""docstring for HttpHandlers"""
	def __init__(self,f):
		super(HttpHandlers, self).__init__()
		self.fileout=open(f,'w+')
	def start_document(self):
		self.fileout.writelines('<html><head><title>hello</title></head><body>')
		print '<html><head><title>hello</title></head><body>'
	def end_document(self):
		self.fileout.writelines('</body></html>')
		print '</body></html>'
	def start_paragraph(self):
		self.fileout.writelines('<p>')
		print '<p>'
	def end_paragraph(self):
		self.fileout.writelines('</p>')
		print '</p>'
	def start_heading(self):
		self.fileout.writelines('<h2>')
		print '<h2>'
	def end_heading(self):
		self.fileout.writelines('<h2>')
		print '</h2>'
	def start_list(self):
		self.fileout.writelines('<ul>')
		print '<ul>'
	def end_list(self):
		self.fileout.writelines('</ul>')
		print '</ul>'
	def start_listitem(self):
		self.fileout.writelines('<li>')
		print '<li>'
	def end_listitem(self):
		self.fileout.writelines('</li>')
		print '</li>'
	def start_title(self):
		self.fileout.writelines('<h1>')
		print '<h1>'
	def end_title(self):
		self.fileout.writelines('</h1>')
		print '</h1>'
	def sub_emphasis(self,match):
		return '<em>%s</em>' % match.group(1)
	def sub_url(self,match):
		return '<a href="%s">%s</a>' % (match.group(1),match.group(1))
	def sub_mail(self,match):
		return '<a href="mailto:%s">%s</a>' % (match.group(1),match.group(1))
	def feed(self,data):
		self.fileout.writelines(data)
		print data