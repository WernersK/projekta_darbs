from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("exit.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        vardsuzvards = request.form.get('vardsuzvards')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('E-Pastam jābūt garākam par 3 simboliem.', category='error')
        elif len(vardsuzvards) < 2:
            flash('Vārdam un uzvārdam jābūt garākam par 1 simboliem.', category='error')
        elif password1 != password2:
            flash('Paroles nesakrīt', category='error')
        elif len(password1) < 7:
            flash('Parolei jābūt garākam par 7 simboliem.', category='error')
        else:
            flash('Konts veiksmīgi izveidots!', category='success')
            
    return render_template("signup.html")

@auth.route('/search')
def search():
    return render_template("home.html")