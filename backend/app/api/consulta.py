from fastapi import APIRouter
from app.models.consulta_dto import ConsultaRequest, ConsultaResponse
from app.core.procesador import procesar_pregunta

router = APIRouter()

@router.post("/", response_model=ConsultaResponse)
async def consultar(request: ConsultaRequest):
    return procesar_pregunta(request.cliente_id, request.pregunta)

@router.get("/clientes")
async def listar_clientes():
    import os
    base_path = "documentos"
    clientes = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    return clientes