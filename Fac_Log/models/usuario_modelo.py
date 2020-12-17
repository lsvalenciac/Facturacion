from pydantic import BaseModel
class UserIn(BaseModel):
    cedula: int
    password: str

class UserStatus(BaseModel):
    autenticado: bool = False

