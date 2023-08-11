from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/kape'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from utils.db import db  # Importa db aquí

db.init_app(app)  # Configura db con la aplicación

app.register_blueprint(auth)