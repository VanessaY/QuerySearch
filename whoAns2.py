import re
from bs4 import BeautifulSoup
import operator


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
                        #print 'hit'
                else:
                        source = source+ln
                
        sources.append(source)  
        return sources

def do_all(sources):
        bad_words = ['he', 'all', 'the', 'play', 'we', 'but', 'a', 'in', 'go', 'get', 'seem', 'see', 'log', 'ads', 'from',
                     'to', 'off', 'next', 'because', 'your', 'mine', 'url', 'be', 'of', 'just', 'have', 'that', 'as', 'be',
                     'do', 'at', 'time', 'day', 'place', 'say', 'work', 'tell', 'call', 'own', 'good', 'bad', 'big', 'small',
                     'high', 'able', 'same', 'by', 'this', 'will', 'one', 'every', 'an', 'not', 'or', 'would', 'there', 'their']
                     
        all_found = {}
        for src in sources:
               fd = findName(src)
               for k in fd.keys():
                       if k in all_found.keys():
                               all_found[k] = all_found[k]+fd[k]
                       else:
                               all_found.update({k:fd[k]})
                               '''
                               reason for commenting out:
                               Harbinger of Bugs and Bringer of Headaches
        for k in all_found.keys():
                st = k.split(' ')
                for st1 in st:
                        st2 = st1.lower()
                        if st2 in bad_words:
                                del all_found[k]
                               '''
        sret = sorted(all_found.items(), key=operator.itemgetter(1))
        ret = []
        for i in range(1,len(sret)+1):
                ind = len(sret)-i
                ret = ret+[sret[ind][0]]
        return ret

def aggregate(all_found):
        occurances = histogram(found)
        print occurances
        s = s.replace("'", " ")
        cap = re.findall('([A-Z][a-z]+[\s]([A-Z][a-z]+[\s]))', s)
        found = []
        for st in cap:
               found.append(st[0])
        occurances = histogram(found)
        return maxInDict(occurances, 25)

def findName(html_doc):
        soup = BeautifulSoup(html_doc)
        s=soup.get_text()
        s = s.replace('\n',' ')
        cap = re.findall('([A-Z][a-z]+[\s]([A-Z][a-z]+[\s]))', s)
        found = []
        for st in cap:
               found.append(st[0])
        occurances = histogram(found)
        return maxInDict(occurances, 25)


def maxInDict(d, n):
        ret = {}
        vals = d.values()
        if len(vals)==0:
                return ret
        mxt = max(vals)
        for i in range(0,min(n,len(vals))):
                mx = float(max(vals))
                #print mx/mxt
                ind = vals.index(mx)
                ky = d.keys()[ind]
                ret.update({ky:mx/mxt})

                del d[ky]
                vals = d.values()
        return ret

def histogram(L):
        d = {}
        for x in L:
               if x in d:
                   d[x] += 1
               else:
                   d[x] = 1
        return d

#sources = readSample('sample_html.txt')
#print do_all(sources)
