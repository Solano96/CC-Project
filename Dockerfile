FROM python:3.6-slim

# Información del desarrollador
LABEL maintainer="Francisco Solano <fransol0728@correo.ugr.es>"

# Directorio de trabajo
WORKDIR /src/

# Copiamos los archivos necesarios
COPY src/ src/ requirements.txt ./

# Instalamos las dependencias
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Puerto donde va a escuchar el servidor
EXPOSE ${PORT}

# Levantamos el servidor
CMD gunicorn server:app --bind 0.0.0.0:${PORT}
