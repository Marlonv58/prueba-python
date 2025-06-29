from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.consulta import router as consulta_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(consulta_router, prefix="/consulta", tags=["consulta"])
