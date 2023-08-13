from app import app
from utils.db import db
from models.user_back import User
from datetime import datetime
import bcrypt

def create_users():
    with app.app_context():
        # Asegurarse de que la tabla 'user' se cree si no existe
        db.create_all()

        num_users = int(input("Ingrese el número de usuarios que desea crear: "))

        for i in range(num_users):
            print(f"Ingrese los detalles del usuario {i + 1}:")
            
            nombre_usuario = input("Nombre de usuario: ")
            while not nombre_usuario:
                print("El nombre de usuario no puede estar en blanco.")
                nombre_usuario = input("Nombre de usuario: ")
                
            correo = input("Correo electrónico: ")
            while not correo:
                print("El correo del usuario no puede estar en blanco.")
                correo = input("Correo electrónico: ")
    
            contrasena = input("Contrasenia: ")
            while not contrasena:
                print("El usuario debe tener una contrasenia.")
                contrasena = input("Contrasenia: ")
    
            fecha_registro = datetime.now()
            
            user = User(nombre_usuario=nombre_usuario, correo=correo, contrasena=contrasena, fecha_registro=fecha_registro)
            db.session.add(user)
            
        # Realizar la operación de commit fuera del bucle
        db.session.commit()

        print(f"Se han creado {num_users} usuarios.")

if __name__ == '__main__':
    create_users()