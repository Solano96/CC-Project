# Dockerfile para el microservicio Mercado
FROM python:3.6-slim-stretch

# Información del desarrollador
LABEL maintainer="Francisco Solano <fransol0728@correo.ugr.es>"

# Directorio de trabajo
WORKDIR /src

# Copiamos los archivos .py del directorio actual
COPY ./*.py ./Mercado/

# Instalamos las dependencias necesarias para el proyecto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir fix-yahoo-finance==0.1.30 Flask==1.1.1 dnspython==1.16.0 gunicorn==20.0.4 eventlet==0.25

# Definimos como argumento el puerto por donde va a escuchar el servidor
ARG PORT_MARKET

# Variables de entorno
ENV PORT_MARKET=${PORT_MARKET}

# Puerto donde va a escuchar el servidor
EXPOSE ${PORT_MARKET}

# Levantamos el microservicio mercado
CMD gunicorn --workers=9 --worker-class eventlet Mercado.server:app --bind 0.0.0.0:${PORT_MARKET}
