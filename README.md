# Proyecto para la asignatura Cloud Computing

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Build Status](https://travis-ci.com/Solano96/CC-Project-Trading.svg?branch=master)](https://github.com/Solano96/CC-Project-Trading)
[![codecov](https://codecov.io/gh/Solano96/CC-Project-Trading/branch/master/graph/badge.svg)](https://codecov.io/gh/Solano96/CC-Project-Trading)

## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

* **Arquitectura**

	La aplicación tendrá una arquitectura basada en microservicios. Para ver una descripción de la arquitectura en detalle se puede consultar el siguiente [enlace](https://solano96.github.io/CC-Project-Trading/#arquitectura).

* **Tecnologías**

	El proyecto será realizado en el lenguaje de programación **Python**, para ver más información acerca de las tecnologías puede consultar el siguiente [enlace](https://solano96.github.io/CC-Project-Trading/#tecnologías).

## Herramientas de construcción

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


## Integración continua

Se han utilizado dos herramientas de integración continua. Estas son las siguientes:

* **Travis-CI**: ejecuta los tests unitarios y de cobertura sobre el sistema operativo Linux, para las versiones de Python 3.6, 3.6.8, 3.7 y 3.8 (el motivo de que la versión minima sea la 3.6 es debido a errores de ejecución en versiones anteriores con el paquete *yfinance*).  Tras finalizar la ejecución de los tests, se envían los resultados del test de cobertura a [codecov](https://codecov.io/gh/Solano96/CC-Project-Trading). En el fichero [.travis.yml](https://github.com/Solano96/CC-Project-Trading/blob/master/.travis.yml) se puede consultar la configuración descrita.

* **Github Actions**: ejecuta los test unitarios y de cobertura en la última versión de Ubuntu, para las versiones de Python 3.6, 3.7 y 3.8. En el caso de *Github Actions*, no se envían los resultados del test de cobertura a codecov. En el fichero [pythonapp.yml](https://github.com/Solano96/CC-Project-Trading/blob/master/.github/workflows/pythonapp.yml) se puede consultar la configuración descrita.
