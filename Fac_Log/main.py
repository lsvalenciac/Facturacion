from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from db import clientes_db
from db import usuarios_db
from models.clientes_modelo import *
from models.usuario_modelo import UserIn, UserStatus

from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://factapp4vi.herokuapp.com"
]
app.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

userstatus = UserStatus()

def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

#Petición a una ruta
@app.get("/clientes/lista/")
#Asincrona, la función no se ejecuta constantemente con las demas funciones 
async def enlistar_clientes():
    #Devuelve el codigo http 200
    return  clientes_db.lista_clientes()

@app.post("/clientes/agregar/")
async def agregar_cliente(cliente: clientes_db.ClienteDb):

    operacion_exitosa = clientes_db.ingresar_cliente(cliente)
    if operacion_exitosa:
        return {"mensaje":"Cliente creado"}
    else:
        raise HTTPException(status_code=400, detail="Cliente existente")


@app.post("/clientes/buscar/")
async def buscar_clientes(cliente: BuscarClienteCedula):
    operacion_exitosa = clientes_db.buscar_cliente(cliente.cedula)
    if operacion_exitosa:
        return operacion_exitosa
    else:
        raise HTTPException(status_code=400, detail="Cliente no existe")


