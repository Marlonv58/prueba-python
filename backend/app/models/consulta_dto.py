from pydantic import BaseModel, Field

class ConsultaRequest(BaseModel):
    cliente_id: str
    pregunta: str

class ConsultaResponse(BaseModel):
    respuesta: str
    fuente: str = Field(..., min_length=3)