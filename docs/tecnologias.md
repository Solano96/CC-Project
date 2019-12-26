## Tecnologías

### Lenguaje de programación

El proyecto será realizado en el lenguaje de programación **Python**. Algunos de los motivos por los que he decidido utilizar este lenguaje son: la facilidad de implementación, el requerir menos código en comparación con otros lenguajes y el disponer de cierta experiencia en este lenguaje. Una de las ventajas que nos ofrece para este proyecto, es que nos va a permitir obtener de forma sencilla datos financieros de Yahoo Finance, mediante el uso de la biblioteca [**yfinance**](https://github.com/ranaroussi/yfinance), la cual nos facilitará la implementación del microservicio `Mercado`.

### API Gateway

Para el API Gateway vamos a recurrir a [**Kong Gateway**](https://github.com/Kong/kong), un proyecto de código abierto muy popular para arquitecturas basadas en microservicios. Este se va a encargar del enrutamiento hacia los distintos microservicios

### Base de datos

Tanto para la base de datos del microservicio `Portfolio`, como para la del microservicio `Mercado`, se va a utilizar el sistema de base de datos [**MongoDB**](https://www.mongodb.com). Para poder interactuar con las bases de datos en MongoDB desde Python, se va a utilizar **PyMongo**.

### Framework

El framework que se utilizará para implementar las APIs Rest será **Flask**. Como ventajas de utilizar este framework se puede destacar el permitir desarrollar de forma ágil y además existe una gran documentación, lo cual facilitará el proceso de desarrollo.

### Servicios

Para para la implementación del servicio de log se utilizará la biblioteca **logging** de Python. Para el servicio de configuración distribuida como puede verse en el diagrama de la arquitectura se va a utilizar **etcd**, para el cual se hará uso de la librería [**python-etcd**](https://github.com/jplana/python-etcd).
