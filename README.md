# Proyecto para la asignatura Cloud Computing

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Build Status](https://travis-ci.com/Solano96/CC-Project-Trading.svg?branch=master)](https://github.com/Solano96/CC-Project-Trading)
[![codecov](https://codecov.io/gh/Solano96/CC-Project-Trading/branch/master/graph/badge.svg)](https://codecov.io/gh/Solano96/CC-Project-Trading)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](http://cc-project-trading.herokuapp.com/)

## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

## Arquitectura

La aplicación tendrá una arquitectura basada en microservicios. Para ver una descripción de la arquitectura en detalle se puede consultar el siguiente [enlace](https://solano96.github.io/CC-Project-Trading/docs/arquitectura).

## Tecnologías

El proyecto será realizado en el lenguaje de programación **Python**, para ver más información acerca de las tecnologías puede consultar el siguiente [enlace](https://solano96.github.io/CC-Project-Trading/docs/tecnologias).

## Herramientas de construcción

```
buildtool: tasks.py
```

Como herramienta de construcción se ha añadido el fichero [tasks.py](https://github.com/Solano96/CC-Project-Trading/blob/master/tasks.py), para el cual es necesario instalar el paquete de python invoke, esto se puede lograr con el siguiente comando:

```
$ pip install invoke
```

Una vez tengamos instalado dicho paquete, podremos hacer uso de las tareas definidas en el fichero tasks.py, para ello bastará con escribir el comando:

```
$ invoke <nombre-tarea>
```

Las tareas que se han definido son las siguientes:

* **install**: esta tarea se encarga de instalar todas las dependencias del proyecto, haciendo uso del fichero requirements.txt, en el cual se encuentran las librerías correspondientes, junto a la versión que se va a instalar.

* **test**: esta tarea se encarga de ejecutar los tests unitarios. Para ejecutar dichos tests se ha hecho uso de la librería [pytest](https://docs.pytest.org/en/latest/).

* **coverage**: esta tarea se encarga de ejecutar los tests de cobertura, haciendo uso del plugin [pytest-cov](https://pypi.org/project/pytest-cov/).

* **clean**: esta tarea se encarga de limpiar los archivos que se generan al ejecutar los test unitarios y los de cobertura.

* **start**: esta tarea se encarga de levantar el servidor. Como parámetros se pueden especificar el host, el puerto y el uri de la base de datos. Ejemplo:

	```
	$ invoke start --host=0.0.0.0 --port=9000 --db=0.0.0.0:27017
	```

* **stop**: esta tarea se encarga de parar el servidor.

## Integración continua

Se han utilizado dos herramientas de integración continua **Travis-CI** y **Github Actions**, cuya documentación puede encontrarse en este [enlace](https://solano96.github.io/CC-Project-Trading/docs/integracion_continua).


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


## Heroku

Podemos comprobar que la imagen está desplegada en Heroku accediendo al siguiente enlace:

https://cc-project-trading.herokuapp.com

Para desplegar heroku se han seguido los pasos explicados en esta [guía](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml). Mencionar que Heroku usa por defecto un puerto como variable de entorno, debido a ello hemos puesto el puerto en el dockerfile como variable de entorno. Adicionalmente he creado una base de datos en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) y posteriormente he añadido a Heroku la URI de dicha base de datos como variable de entorno, para lo cual he utilizado el comando `heroku config:set <VAR>=<VALUE>`.
