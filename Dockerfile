FROM python:3.7-slim-stretch

# Información del desarrollador
LABEL maintainer="Francisco Solano <fransol0728@correo.ugr.es>"

# Directorio de trabajo
WORKDIR /src/

# Copiamos los archivos necesarios
COPY src/ requirements.txt ./

# Instalamos las dependencias necesarias para el proyecto
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Definimos como argumentos el puerto por donde va a escuchar el servidor
# y la uri de la base de datos
ARG PORT
ARG DB_URI

# Variables de entorno
ENV PORT=${PORT}
ENV DB_URI=${DB_URI}

# Puerto donde va a escuchar el servidor
EXPOSE ${PORT}

# Levantamos el servidor
CMD gunicorn --workers=9 --worker-class eventlet server:app --bind 0.0.0.0:${PORT}
