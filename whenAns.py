import re
from bs4 import BeautifulSoup
import operator

def readSample(path):
    sources = []
    source = ''
    f = open(path,'r')
    p = re.compile('stuff')
    print f.readline()
    for ln in f:
        if p.findall(ln):
            sources.append(source)
            source = ''
        else:
            source = source+ln
    sources.append(source)
    return sources

def do_all(sources):
    a = {}
    for s in sources:
        f = findDate(s)
        for k in f.keys():
            if k in a.keys():
                a[k] = a[k]+f[k]
            else:
                a.update({l:f[k]})
    newa = sorted(a.items(),key = operator.itemgetter(1))
    ans = []
    for i in range(1,len(newa)+1):
        index = len(newa)-i
        ans = ans + [newa[index][0]]
    return ans

def aggregate(all_found):
    occurances = histogram(found)
    print occurances

def findDate(html_doc):
    soup = BeautifulSoup(html_doc)
    s = soup.get_text()
    s = s.replace('\n',' ')
    date = re.findall('\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) [0-3]?\d, [0-9]?[0-9]?[0-9]?\d',s)
    found = []
    for st in date:
        found.append(st[0])
    occurances = histogram(found)
    return maxInDict(occurances, 25)

def maxInDict(d,n):
    ans = {}
    val = d.values()
    m = max(val)
    for i in range(0,n):
        mx = float(max(val))
        index = val.index(m)
        k = d.keys()[index]
        ans.update({k:mx/m})
        del d[k]
        val = d.values()
    return ans

def histogram(L):
    d = {}
    for x in L:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

sources = readSample('sample_html.txt')
print do_all(sources)
