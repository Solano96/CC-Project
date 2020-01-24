## Docker

La imagen de nuestro contenedor docker puede encontrarse en el siguiente enlace:

Contenedor: https://hub.docker.com/r/fcosolano96/cc-project-trading

### Comparación de imágenes

Las imágenes base utilizadas han sido las siguientes: python:3.8, python:3.8-slim, python:3.7-slim-stretch y python:3.8-alpine. Todos los dockerfiles utilizados para la construcción de dichas imágenes son idénticos a diferencia evidentemente de la línea en la que espedificamos la imagen base. También mencionar que en la imagen de alpine se ha debido de incluir la siguiente línea adicional `RUN apk --update add --no-cache g++` necesaria para poder instalar ciertos paquetes con pip.

#### Tamaño de las imágenes

En primer lugar vamos a comparar los tamaños de las imágenes. Lo primero que apreciamos es la gran diferencia de tamaño entre la versión de python original y la versión slim la cual ocupa mucho menos debido a que solo contiene los paquetes mínimos necesarios para ejecutar python.

```shell
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
image-python-alpine         latest              1e2e8701fb2f        2 minutes ago       614MB
image-python-slim-stretch   latest              0843ebfeae3a        25 minutes ago      303MB
image-python-slim           latest              786c70f2b0ea        27 minutes ago      347MB
image-python                latest              f4258a4f5fd9        29 minutes ago      1.09GB
```

Debido al gran tamaño de la imagen de python original, vamos a optar por no usarla, ya que por ejemplo las versiones slim, nos van a servir para nuestro proyecto y ocupan mucho menos.

#### Prueba de rendimiento

En segundo lugar vamos a evaluar el rendimiento del servidor, para ello vamos a utilizar Apache Benchmark, el cual nos va a permitir conocer cuantas peticiones por segundo acepta nuestro servidor. Para la prueba se ha ejecutado el siguiente comando:

```
ab -n 10000 -c 10 http://localhost:8000/
```

En dicho comando estamos especificando que vamos a realizar 10000 con una concurrencia de 10.

Los resultados son los que se muestran en la siguiente tabla:

```shell
CONTAINER                   REQUEST PER SECOND   TIMER PER REQUEST            
image-python-alpine         1102.32              9.072 ms
image-python-slim-stretch   1090.07              9.174 ms
image-python-slim           1154.94              8.658 ms
image-python                1195.66              8.364 ms
```

### Imagen base elegida

Observando los resultados anteriores la imagen base que elegimos finalmente es python:3.8-slim que a pesar de que ocupa algo más que python:3.7-slim-stretch, podemos apreciar que es algo mejor en cuanto al rendimiento obteniendo una cifra de 1154 peticiones por segundo. Para ver más detalles sobre la imagen que finalmente se ha construido se puede consulta el fichero [dockerfile](https://github.com/Solano96/CC-Project-Trading/blob/master/Dockerfile).

### Docker-compose

Se ha incluido el fichero [docker-compose.yml](https://github.com/Solano96/CC-Project-Trading/blob/master/docker-compose.yml) al proyecto, gracias al cual vamos a poder ejecutar multiples contenedores, en este caso el contenedor con nuestro proyecto y otro adicional para la base de datos con MongoDB. El motivo de este fichero es el de permitir que nuestro proyecto ejecutado en docker pueda acceder a la base de datos de mongoDB.

Para iniciar y ejecutar toda nuestra aplicación con docker-compose tan solo debemos de ejecutar el comando `docker-compose up`. Para detener la ejecución ejecutaremos el comando `docker-compose down`.

Para el uso de docker-compose se han seguido los pasos explicado en este [enlace](https://docs.docker.com/compose/) de la página oficial de docker.
