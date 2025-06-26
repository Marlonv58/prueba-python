import os
import re

def buscar_respuesta_en_documentos(cliente_id: str, pregunta: str):
    base_path = f"documentos/{cliente_id}"
    if not os.path.exists(base_path):
        return "Cliente no encontrado", ""

    if len(pregunta.strip()) < 3:
        return "La pregunta debe tener al menos 3 caracteres.", ""

    for file in os.listdir(base_path):
        if file.endswith(".txt"):
            with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
                contenido = f.read()
                
                pattern = r'\b' + re.escape(pregunta.strip().lower()) + r'\b'
                if re.search(pattern, contenido.lower()):
                    return f"{contenido[:100]}...", file

    return "No se encontró una respuesta relacionada.", ""