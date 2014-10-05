from parse import *
from handlers import *
import sys,os


def main():
	handler=HttpHandlers(sys.argv[2])
	files=open(sys.argv[1],'r+')
	parse=BasicTextParser(handler)
	parse.parse(files)

if __name__=='__main__':
	main()