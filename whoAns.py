import re
from bs4 import BeautifulSoup


def readSample(path):
	sources = []
	source = ''
	f = open(path, 'r')
	p1 = re.compile('nexteliaportnoy')
	print f.readline()
	for ln in f:
		if p1.findall(ln):
			sources.append(source)
			source = ''
			print 'hit'
		else:
			source = source+ln
		
	sources.append(source)	
	return sources

def test(html_doc):
	#print html_doc
	soup = BeautifulSoup(html_doc)
	page = soup.find('p').getText()
	print page
	print soup.get_text()
	
sources = readSample('sample_html.txt')
html_doc = sources[0]
print html_doc[8999:9100]
test(html_doc)