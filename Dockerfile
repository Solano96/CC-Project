FROM python:3.7-slim-stretch

# Información del desarrollador
LABEL maintainer="Francisco Solano <fransol0728@correo.ugr.es>"

# Directorio de trabajo
WORKDIR /src

# Copiamos el fichero de dependencias
COPY requirements.txt ./
# Copiamos los archivos de la carpeta Portfolio
COPY src/Portfolio ./Portfolio/

RUN ls

# Instalamos las dependencias necesarias para el proyecto
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Definimos como argumentos el puerto por donde va a escuchar el servidor
# y la uri de la base de datos
ARG PORT_PORTFOLIO
ARG DB_URI

# Variables de entorno
ENV PORT_PORTFOLIO=${PORT_PORTFOLIO}
ENV DB_URI=${DB_URI}
ENV DB_NAME_PORTFOLIO='Portfolio'

# Puerto donde va a escuchar el servidor
EXPOSE ${PORT_PORTFOLIO}

# Levantamos el servidor
CMD gunicorn --workers=9 --worker-class eventlet Portfolio.server:app --bind 0.0.0.0:${PORT_PORTFOLIO}
