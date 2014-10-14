import re
from bs4 import BeautifulSoup
import collections

def findDate(data):
    results = []
    for d in data:
        soup = BeautifulSoup(d)
        s = soup.get_text()
        s = s.encode('utf-8')
        s = s.replace('\n',' ')
        a = re.compile(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) [0-3]?\d, [0-9]?[0-9]?[0-9]?\d')
        dates = a.findall(s)
        for i in dates:
            results.append(i)
    counter = collections.Counter(results)
    ans = counter.most_common()
    answer = []
    for ind in ans:
        answer.append(ind[0])
    return answer
