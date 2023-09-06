from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)
app.secret_key = 'first-flaskapp-das'

#Ruta default
@app.route("/", methods=['GET','POST'])
def default():
    return redirect(url_for('login'))

#Ruta login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Checar si el usuario empieza con mayuscula
        if not username[0].isupper():
            flash('El usuario debe comenzar con una letra mayúscula.', 'danger')
            return render_template('login.html')

        # Checar si la clave contiene letras y numeros
        if not (any(chars.isdigit() for chars in password) and any(chars.isalpha() for chars in password)):
            flash('La contraseña debe contener letras y números.', 'danger')
            return render_template('login.html')

        # Checar usuario y clave, esto se puede reemplazar con una funcion de ORM para usuarios multiples
        if username == "Admin" and password == "Password1792":
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash('Error en valores. Favor de  checar su usuario y clave', 'danger')

    return render_template('login.html')


#Pagina de Inicio
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['user'])


#Funcion de Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
