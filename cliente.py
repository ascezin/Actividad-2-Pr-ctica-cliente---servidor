import requests
from requests.auth import HTTPBasicAuth  # Importa la autenticación básica
def obtener_usuarios():
    response = requests.get('http://localhost:5000/usuarios', auth=HTTPBasicAuth('Jesus', 'contraseña2'))  
    if response.status_code == 200:
        usuarios = response.json()
        print("Usuarios encontrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print("Error al obtener usuarios")


def crear_usuario(nombre):
    #Realizar peticion POST al servidor para agregar el usuario
    response = requests.post('http://localhost:5000/usuarios', json={"nombre": nombre}, auth=HTTPBasicAuth('Jesus', 'contraseña2'))
    
    if response.status_code == 200:
        print("Usuario agregado correctamente:", response.json())
    else:
        print("Error al crear el usuario:", response.status_code)
        try:
            print("Respuesta JSON:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Contenido de la respuesta no JSON:", response.text)
        
def buscar_usuario(id):
    response = requests.get('http://localhost:5000/usuarios', auth=HTTPBasicAuth('Jesus', 'contraseña2')) 
    contar = 0
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            if id == usuario['id']:
                id = usuario['id']
                nombre = usuario['nombre']
                contar += 1
        if contar == 1:
            print(f"El usuario con id: {id} si existe y se llama {nombre}")
        else:
            print(f"El usuario con id: {id} no existe")            
    else:
        print("Error al obtener usuarios")
        
def eliminar_usuario(id):
    response = requests.delete(f'http://localhost:5000/usuarios/{id}', auth=HTTPBasicAuth('Jesus', 'contraseña2'))
    if response.status_code == 200:
        print("Usuario eliminado correctamente.")
    else:
        print("Error al eliminar el usuario:", response.status_code)
        try:
            print("Respuesta JSON:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Contenido de la respuesta no JSON:", response.text)

if __name__ == '__main__':
    obtener_usuarios()
    crear_usuario("David") 
    crear_usuario("Dayanna")
    obtener_usuarios()
    buscar_usuario(1)
    eliminar_usuario(1)
    obtener_usuarios()