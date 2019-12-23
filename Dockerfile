FROM python:3.6-slim

# Información del desarrollador
LABEL maintainer="Francisco Solano <fransol0728@correo.ugr.es>"

# Directorio de trabajo
WORKDIR /

# Copiamos los archivos necesarios
COPY src/ src/ requirements.txt ./

# Instalamos las dependencias
RUN pip install -r requirements.txt
