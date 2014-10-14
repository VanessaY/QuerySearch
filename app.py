
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
    more = request.args.get("more", None)
    if askbutton == "Ask!":
        ##THIS IS LIST OF EACH RESULT'S PAGE (PROBABLY. HOPEFULLY)
        if (query == ""):
            return render_template("ohyou.html")
        data = get_stuff (query)
        if ("who" in query or "when" in query):
            if ("who" in query):
                results = whoAns2.do_all(data)
            elif ("when" in query):
                results = whenAns2.findDate(data)
                results = results[1:]
        else:
            return render_template("oops.html")
<<<<<<< HEAD
        j = "<ul class = 'list-unstyled'>"
        k = 0
        for a in results:
            if k < 5:
                j = j + "<li>" + a + "</li>"
                k = k + 1
        j = j + "</ul>"
        hidden = '<input type="hidden" name="query" value="' + query + '">'
        more_button = '<input type="submit" class="btn btn-danger btn-primary btn-small" type="button" name="more" value="More Results">'
        print hidden
        return render_template("gdi.html").format(j, more_button, hidden)
    elif more == "More Results":
        data = get_stuff (query)
        if ("who" in query or "when" in query):
            if ("who" in query):
                results = whoAns2.do_all(data)
            elif ("when" in query):
                results = whenAns2.findDate(data)
        j = "<ul class = 'list-unstyled'>"
        for a in results:
            j = j + "<li>" + a + "</li>"
        j = j + "</ul>"
        return render_template("gdi.html").format(j, "",  "")
=======
<<<<<<< HEAD
        return render_template("ask.html", res = results)
=======
        i = "<ul class = 'list-unstyled'>"
        for a in results:
            i = i + "<li>" + a + "</li>"
        i = i + "</ul>"
        print 'cool beans'
        return render_template("gdi.html").format(i)
>>>>>>> 6864dd416c76ba114898e33ca0e4623c95126630
>>>>>>> FETCH_HEAD
    elif goback == "Return":
        return render_template("home.html")
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
