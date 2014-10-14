import re
from bs4 import BeautifulSoup

def findDate(data):
    results = []
    for d in data:
        ans = []
        soup = BeautifulSoup(d)
        s = soup.get_text()
        s = s.replace('\n')
        a = re.compile('\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) [0-3]?\d, [0-9]?[0-9]?[0-9]?\d')
        result = a.findall(d)
        for i in result:
            ans.append(i)
        most = most_common(ans)
        results.append(most)
    answer = most_common(results)
    return answer


def most_common(lst):
    return max(lst, key=lst.count)
