
from flask import Flask, render_template, request

import google, bs4, whoAns2, whenAns2

app = Flask(__name__)

def get_stuff(query): 
    s = google.search (query, tld = 'com', lang = 'en', start=0, stop=10, pause=2.0)
    l = []
    for url in s:
        l.append(url)
    data = []
    for x in l:
        data.append(google.get_page(x))
    return data
    
@app.route("/")
def home():
    query = request.args.get("query", None)
    askbutton = request.args.get("askbutton", None)
    goback = request.args.get("goback", None)
    if askbutton == None:
        return render_template("home.html")
    elif askbutton == "Ask!":
        ##THIS IS LIST OF EACH RESULT'S PAGE (PROBABLY. HOPEFULLY)
        if (query == ""):
            return render_template("ohyou.html")
        data = get_stuff (query)
        if ("who" in query or "when" in query):
            if ("who" in query):
                results = whoAns2.do_all(data)
            elif ("when" in query):
                results = whenAns2.findDate(data)
        else:
            return render_template("oops.html")
        return render_template("ask.html", res = results)
    elif goback == "Return":
        return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
