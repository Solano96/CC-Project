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

Para ver mas detalles sobre el uso de Docker puedo consultar el siguiente [enlace](https://solano96.github.io/CC-Project-Trading/docs/docker).

## Heroku

Podemos comprobar que la imagen está desplegada en Heroku accediendo al siguiente enlace:

https://cc-project-trading.herokuapp.com

Para desplegar heroku se han seguido los pasos explicados en esta [guía](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml). Mencionar que Heroku usa por defecto un puerto como variable de entorno, debido a ello hemos puesto el puerto en el dockerfile como variable de entorno. Adicionalmente he creado una base de datos en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) y posteriormente he añadido a Heroku la URI de dicha base de datos como variable de entorno, para lo cual he utilizado el comando `heroku config:set <VAR>=<VALUE>`.

## Base de datos

Para la base de datos se ha utilizado el sistema de base de datos MongoDB. Para hacer uso de la base de datos MongoDB podemos elegir entre 3 opciones, las cuales vamos a describir en los siguientes apartados.

#### Base de datos local

Esta primera opción cosiste en instalar MongoDB en local y hacer uso de la base de datos instalada en nuestro propio equipo. Para la instalación de MongoDB en Ubuntu 18.04, podemos seguir los pasos de instalación que se encuentran en esta guía [instalación MongoDB](https://www.digitalocean.com/community/tutorials/como-instalar-mongodb-en-ubuntu-18-04-es).

#### Base de datos con Docker

Para esta opción podemos hacer uso del fichero docker-compose.yml, con el cual podemos ejecutar múltiples contenedores, en nuestro caso uno creado a partir del Dockerfile y otro a partir de una imagen con MongoDB. La imagen de MongoDB nos permitirá que el contenedor con nuestro microservicio pueda hacer uso del nuevo contenedor creado a partir de la imagen de MongoDB, para poder acceder a la base de datos.

#### Base de datos Atlas

Para poder hacer uso de la base de datos remota que nos proporciona [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), deberemos crearnos una cuenta en su página web. Tras registrarnos deberemos de crear un usuario de la base de datos y después crear una base de datos con dicho usuario. Por último para poder acceder a esta base de datos, deberemos obtener el uri accediento a Clusters > Connect > Connect your application, y copiar la cadena de texto que nos proporciona. Esta cadena deberemos usarla para la variable de entorno DB_URI y nos permitirá conectarnos a la base de datos remota que hemos creado.

## Evaluación de prestaciones
