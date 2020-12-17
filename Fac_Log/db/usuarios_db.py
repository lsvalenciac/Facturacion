from pydantic import BaseModel
from typing import Optional
from db.clientes_db import ClienteDb


class UsuarioDb(ClienteDb):
    rol: int
    password: str



usuarios = {
    1: UsuarioDb(cedula=1, nombre="Maria", apellido="Moreno", telefono=687914, email="maria.moreno@laempresa.com", password= "khrie123", rol=1),
    2: UsuarioDb(cedula=2, nombre="Orlando", apellido="Melo", telefono=698754,email="orlando.melo@laempresa.com", password= "654789", rol=1),
    3: UsuarioDb(cedula=3, nombre="Carlos", apellido="Rojas", telefono=589745, email="carlos.rojas@laempresa.com", password= "123456", rol=2)
}


def lista_usuarios():
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuarios[usuario])
    return lista_usuarios


def obtener_usuario(cedula: int):
    if cedula in usuarios.keys():
        return usuarios[cedula]
    else:
        return None

""" def buscar_cliente(cedula):
    if cedula in clientes:
        return clientes[id]
    else:
        return None

def ingresar_cliente(cliente:Cliente):
    if cliente.cedula in clientes:
        return False
    else:
        clientes[cliente.cedula]= cliente
        return True """

