import re
from bs4 import BeautifulSoup


def findDate(data):
    results = []
    for d in data:
        soup = BeautifulSoup(d)
        s = soup.get_text()
        s = s.replace('\n',' ')
        dates = re.findall('\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) [0-3]?\d, [01]?[0-9]?[0-9]\d',s)
        results = []
        for i in dates:
            results.append(i[0])
            '''
        most = most_common(ans)
        results.append(most)
    answer = most_common(results)
    return answer
            '''
    return results

def most_common(lst):
    return max(set(lst), key=lst.count)
