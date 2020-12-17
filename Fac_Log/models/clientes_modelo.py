from pydantic import BaseModel

class BuscarClienteCedula(BaseModel):
    cedula: int