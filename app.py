
from flask import Flask, render_template, request

import google, bs4, whoAns

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
        data = get_stuff (query)
        results = whoAns.do_all (data)
        s = "<ul>"
        for a in results:
            s = s + "<li>" + a + "</li>"
        s = s + "</ul>"
        print 'cool beans'
        return render_template("gdi.html")%s
    elif goback == "Return":
        return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
