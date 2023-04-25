from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektam.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    vardsuzvards = db.Column(db.String(150))
    password = db.Column(db.String(150))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/guide')
def guide():
    return render_template("guide.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Pievienošanās veiksmīga!', category='success')
            else:
                flash('Nepareiza parole, mēģini vēlreiz!', category='error')
        else:
            flash('E-pasts neeksistē', category='error')

    return render_template("login.html", boolean=True)

@app.route('/logout')
def logout():
    return render_template("exit.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        vardsuzvards = request.form.get('vardsuzvards')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-pasts jau ir aizņemts', category='error')
        elif len(email) < 4:
            flash('E-Pastam jābūt garākam par 3 simboliem.', category='error')
        elif len(vardsuzvards) < 2:
            flash('Vārdam un uzvārdam jābūt garākam par 1 simboliem.', category='error')
        elif password1 != password2:
            flash('Paroles nesakrīt', category='error')
        elif len(password1) < 7:
            flash('Parolei jābūt garākam par 7 simboliem.', category='error')
        else:
            new_user = User(email=email, vardsuzvards=vardsuzvards, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Konts veiksmīgi izveidots!', category='success')
            return redirect(url_for('home'))
            
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)