import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def izveidot_savienojumu():
    conn = sqlite3.connect("citatu-db.db")
    conn.row_factory = sqlite3.Row
    return conn

def sanemt_citatu(citata_id):
    conn = izveidot_savienojumu()
    citats = conn.execute("SELECT * FROM citati WHERE id = ?", (citata_id,)).fetchone()
    conn.close()

    if citats is None:
        citats = {"autors": "Nezināms", "teksts": "Nezināms"}

    return citats


app = Flask(__name__)
app.config["SECRET_KEY"] = "Slepeni!"

@app.route("/")
def index():
    conn = izveidot_savienojumu()
    citati = conn.execute("SELECT * FROM citati").fetchall()
    conn.close()
    return render_template("index.html", citati = citati)

@app.route("/<int:citata_id>")
def citats(citata_id):
    citata_teksts = sanemt_citatu(citata_id)
    return render_template("citats.html", citata_teksts = citata_teksts)

@app.route("/pievienot", methods=("GET", "POST"))
def pievienot():
    if request.method == "POST":

        autors = request.form["autors"]
        teksts = request.form["teksts"]

        if not autors:
            flash("Ieraksti autoru!")

        else:
            conn = izveidot_savienojumu()
            conn.execute("INSERT INTO citati (autors, teksts) VALUES (?, ?)",
                            (autors, teksts))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))


    return render_template("pievienot.html")

@app.route("/<int:id>/labot", methods=("GET", "POST"))
def labot(id):
    citats = sanemt_citatu(id)
    if request.method == "POST":

        autors = request.form["autors"]
        teksts = request.form["teksts"]

        if not autors:
            flash("Ieraksti autoru!")

        else:
            conn = izveidot_savienojumu()
            conn.execute('UPDATE citati SET autors = ?, teksts = ?'
                         ' WHERE id = ?',
                         (autors, teksts, id))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("labot.html", citats = citats)

@app.route("/<int:id>/dzest", methods=('POST',))
def dzest(id):
    citats = sanemt_citatu(id)
    conn = izveidot_savienojumu()
    conn.execute('DELETE FROM citati WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash(f'{citats["autors"]} ir izdzēsts.')
    return redirect(url_for('index'))

@app.route("/meklet", methods=("GET", "POST"))
def meklet():
    if request.method == 'POST':
        meklejamais = request.form["teksts"]

        conn = izveidot_savienojumu()   
        vaicajums = f"SELECT * FROM citati WHERE teksts LIKE \"%{meklejamais}%\""
        citati = conn.execute(vaicajums).fetchall()
        conn.close()
        return render_template("index.html", citati = citati)


    return render_template("meklet.html")

if __name__ == "__main__":
    app.run(debug=True)