from flask import Blueprint, render_template, request, redirect, jsonify, url_for
from models.user_back import User
import bcrypt

auth = Blueprint('auth', __name__)

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

@auth.route("/")
def home():
    return render_template('login.html')

@auth.route('/inicio')
def Index():
    return render_template('index.html')

@auth.route("/auth/login", methods=['POST'])
def auth_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    

    user = User.query.filter_by(nombre_usuario=username).first()

    if user and check_password(user.contrasena, password):
        return redirect(url_for('auth.Index'))
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401