# Utiliza una imagen de Python como base
FROM python:3.10.12-alpine3.17

ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en /app
WORKDIR /app/

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . /app/

# Expone el puerto 8000 para que se pueda acceder desde fuera del contenedor
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación Django en el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
