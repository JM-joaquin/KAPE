from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, nombre_usuario, correo, contrasena, fecha_registro):
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro