Este proyecto consiste en una aplicación web que permite a usuarios realizar consultas de texto en documentos previamente cargados por cliente. La búsqueda se simula como si fuera asistida por un modelo de lenguaje (LLM), pero sin usar un modelo real.

---

## Funcionalidad

- Selección del cliente
- Ingreso de pregunta textual
- Respuesta basada en documentos `.txt` por cliente
- Simulación de respuesta IA si no se encuentra una coincidencia
- Validaciones de entrada y control de errores
- Separación clara por capas (Clean Architecture)
- Listo para despliegue con Docker

---

## Stack Tecnológico

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: [Angular](https://angular.io/)
- **Contenedores**: Docker + Docker Compose

---

## Cómo ejecutar localmente (con Docker)

1. Asegúrate de tener Docker y Docker Compose instalados.
2. En la raíz del proyecto, ejecuta:

```bash
docker-compose up --build
```

3. Abre:

- Frontend: http://localhost:4200
- Backend (Swagger): http://localhost:8000/docs

## Estructura del proyecto y documentos

prueba-python/
├── backend/
│ ├── app/
│ │ ├── api/  
│ │ │ └── consulta.py
│ │ ├── core/  
│ │ │ └── procesador.py
│ │ ├── infrastructure/  
│ │ │ └── lector_txt.py
│ │ └── models/  
│ │ └── consulta_dto.py
│ ├── documentos/
│ │ └── cliente1/
│ │ └── archivo1.txt  
│ ├── Dockerfile  
│ ├── main.py  
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── app/
│ │ │ ├── consulta/  
│ │ │ │ ├── consulta.component.html
│ │ │ │ ├── consulta.component.scss
│ │ │ │ └── consulta.component.ts
│ │ │ └── servicios/  
│ │ │ └── consulta.service.ts
│ │ ├── app-routing.module.ts
│ │ ├── app.module.ts
│ │ └── styles.scss
│ └── Dockerfile  
│
├── docker-compose.yml  
└── README.md

Cada archivo .txt puede contener múltiples frases o párrafos.
El sistema buscará coincidencias exactas de palabras dentro de ellos.

## Logica de consulta

El usuario selecciona un cliente y escribe una pregunta.

El backend recorre los documentos del cliente y busca coincidencias exactas por palabra usando expresiones regulares.

Si no encuentra nada relevante, simula una llamada a un modelo IA con sleep() y devuelve una respuesta genérica.

Esta lógica puede ser fácilmente extendida a usar OpenAI, LLaMA, o HuggingFace models con una simple integración.

## Como agregar clientes y documentos

se puede crear tantos clientes y agregar documentos como se desee.
Crea una carpeta dentro de backend/documentos con el nombre del cliente
ejemplo:

```bash
backend/documentos/cliente2/
```

agrega dentro de este cliente el archivo .txt con información para consultar

## Arquitectura: Clean Architecture

Se eligió aplicar Clean Architecture para asegurar un diseño desacoplado, testable y mantenible. Esta decisión permite escalar el sistema fácilmente, por ejemplo, integrando una base de datos, autenticación o incluso un modelo de lenguaje real sin afectar la lógica de negocio.

Separación de capas
Dominio / caso de uso → core/procesador.py
Contiene la lógica pura de cómo procesar una pregunta, sin importar de dónde vienen los datos ni cómo se exponen.

Adaptador entrante → api/consulta.py
Es quien recibe las peticiones HTTP y delega al core.

Adaptador saliente → infrastructure/lector_txt.py
Permite cambiar fácilmente la fuente de documentos (por ejemplo, una base de datos o servicio externo) sin tocar la lógica de negocio.

Modelos / DTOs → models/consulta_dto.py
Aseguran validación y documentación automática con FastAPI/Pydantic.

## Posibilidades de extensión

- Integración real con modelos de lenguaje (OpenAI, Cohere, LLaMA)
- Autenticación JWT por cliente
- Panel de administración de documentos
- Registro de métricas y logs (p. ej. con Elastic + Kibana)
- Exportación de logs de consulta por cliente

## comentarios personales

Basado en la reunion que tuvimos tome desiciones como el usar python, usé fast api porque a diferencia de django que es un poco mas robusto para una api rapida me parece mas apropiado; si el proyecto escalase o se necesitara algo mas robusto hubiese usado django, use angular en el front por lo que hablamos en la reunion y contenedores docker que me parece lo mejor para desplegar localmente, usé clean architecture porque es con la que mas experiencia tengo y me es mas comodo, sin embargo si se necesita se puede revisar la otra opcion de arquitetura.
