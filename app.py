from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("query", None)
    askbutton = request.args.get("askbutton", None)
    goback = request.args.get("goback", None)
    if askbutton == None:
        return render_template("home.html")
    elif askbutton == "Ask!":
        return render_template("ask.html")
    elif goback == "Return":
        return render_template("home.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run()
