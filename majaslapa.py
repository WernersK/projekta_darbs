from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")	
def pirma():
    return "Labdien, tauta!"

@app.route("/<name>")
def otra(name):
    return f"Labdien, {name}!"
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/par")
def par():
    return render_template("par.html")

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)

