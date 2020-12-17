from pydantic import BaseModel
from typing import Optional

class ClienteDb(BaseModel):
    cedula:int
    nombre: str
    apellido:str
    telefono: int
    email: Optional[str]=None
    direccion: Optional[str]=None


clientes = {

    1: ClienteDb(cedula=1, nombre="Laura", apellido="Valencia", telefono=1234, email="por@example.com"),
    2: ClienteDb(cedula=2, nombre="Ana", apellido="Perez", telefono=7534,email="por456@example.com"),
    3: ClienteDb(cedula=3, nombre="Marcos", apellido="Avila", telefono=9876, email="por123@example.com")
}

def lista_clientes():
    lista_clientes = []
    for cliente in clientes:
        lista_clientes.append(clientes[cliente])
    return lista_clientes

def buscar_cliente(cedula: int):
    if cedula in clientes.keys():
        return clientes[cedula]
    else:
        return None

def ingresar_cliente(cliente:ClienteDb):
    if cliente.cedula in clientes:
        return False
    else:
        clientes[cliente.cedula]= cliente
        return True

