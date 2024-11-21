from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth  # Importa la autenticación básica

app = Flask(__name__)

auth = HTTPBasicAuth()  # Inicializa la autenticación básica

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
    ]
}


# Diccionario de usuarios 
usuarios = {
    "Karen": "contraseña1",
    "Jesus": "contraseña2"
}

# Callback para verificar el nombre de usuario y la contraseña
@auth.verify_password
def verificar_usuario(username, password):
    if username in usuarios and usuarios[username] == password:
        return username
    return None

# Ruta para obtener los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(base_datos["usuarios"])

# Ruta para crear el nuevo usuario
@app.route('/usuarios', methods=['POST'])

#Definos la funcion para crear usuarios
def crear_usuario():
    #Obtenemos el metodo Post enviado desde el cliente.py
    datos = request.get_json()
    if "nombre" not in datos or not datos["nombre"] or len(datos["nombre"]) < 2:
        return jsonify({"error": "El campo 'nombre' debe contener al menos un carácter."}), 400
    
    #Creamos la estructura del usuario, id y nombre
    nuevo_usuario = {
        "id": len(base_datos["usuarios"]) + 1,
        "nombre": datos["nombre"]
    }
    #Agregamos el nuevo usuario a la base_datos simulada
    base_datos["usuarios"].append(nuevo_usuario)
    return jsonify(nuevo_usuario), 200

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    for usuario in base_datos["usuarios"]:
        if usuario["id"] == id:
            base_datos["usuarios"].remove(usuario)
            return jsonify({"mensaje": "Usuario eliminado"}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000)