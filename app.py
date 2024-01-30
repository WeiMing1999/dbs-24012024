from flask import Flask,request,render_template # Flask is the framework

app = Flask(__name__)#sign off 

@app.route("/" , methods=["GET","POST"])#decorator = @ run the decorator
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        return(render_template("index.html",result =(rate*-50.6)+90.2))
    else:
        return(render_template("index.html",result = "waiting for you to key in the exchange rate"))

if __name__ == "__main__":
    app.run()
