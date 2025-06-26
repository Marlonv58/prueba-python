from app.infrastructure.lector_txt import buscar_respuesta_en_documentos

import time

def simular_llm_respuesta(pregunta: str) -> str:
    
    time.sleep(1)
    return f"(Simulado) El modelo IA respondió algo sobre: '{pregunta}'."

def procesar_pregunta(cliente_id: str, pregunta: str):
    respuesta, fuente = buscar_respuesta_en_documentos(cliente_id, pregunta)
    
    
    if "No se encontró" in respuesta:
        respuesta = simular_llm_respuesta(pregunta)
        fuente = "modelo IA simulado"

    return {
        "respuesta": respuesta,
        "fuente": fuente
    }