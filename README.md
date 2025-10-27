# Amelia API

Backend desarrollado con FastAPI en Python.

## Características

- FastAPI framework
- Endpoint de status: `/ameliastatus`
- Dockerizado para fácil despliegue

## Uso con Docker

### Construir la imagen
```bash
docker build -t amelia-api .
```

### Ejecutar el contenedor
```bash
docker run -p 8000:8000 amelia-api
```

### Acceder a la API
- API: http://localhost:8000
- Status: http://localhost:8000/ameliastatus
- Documentación: http://localhost:8000/docs

## Desarrollo Local

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar el servidor
```bash
uvicorn main:app --reload
```
