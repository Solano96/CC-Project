# Proyecto para la asignatura Cloud Computing

## Índice de contenidos

- [Descripción](#descripcin)
- [Arquitectura](#arquitectura)

<!-- /TOC -->

## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

Por simplicidad, todas las compras y ventas llevadas a cabo serán ejecutadas al precio del mercado en el momento de ejecutar la orden y estas ejecutarán inmediatamente después de su creación.

Esta aplicación tiene como objetivo, que los usuarios que la utilicen puedan invertir en bolsa con dinero ficticio y de esta forma puedan jugar en bolsa sin el riesgo de perder dinero real. Además, será de gran utilidad para principiantes que quieran aprender sin el peligro de perder sus ahorros.

## Arquitectura

La aplicación tendrá una arquitectura basada en microservicios, lo cual nos permitirá implementar los diferentes servicios de forma independiente y despleglarlos por separado.

A continuación se exponen las entidades del sistema y cada una de las cuales se corresponderá con un microservicio.

* `Portfolio`. Un portfolio en bolsa es una agrupación de activos financieros, en nuestro proyecto tan solo estará formado por el saldo disponible y las acciones compradas. Las funcionalidades de esta entidad son las siguientes:

	* Creación de un nuevo portfolio.
	* Dar de baja un portfolio.
	* Consultar el saldo disponible en un portfolio.
	* Modificar saldo de un portfolio.
	* Consultar acciones compradas en un porfolio.
	* Comprar acciones
	* Vender acciones.


* `Mercado`. Esta entidad está formada por el nombre del mercado y la información de la cotización del mercado, está incluye el precio de apertura, cierre, mínimo y máximo, además del volumen del periodo. También se incluye la fecha y hora en la que se actualizó las información. Las funcionalidades son las siguientes:

	* Añadir un nuevo mercado.
	* Eliminar mercado.
	* Consultar el precio de cierre/apertura/mínimo/máximo de un mercado.
	* Consultar el volumen de un mercado.
	* Consultar la hora de la última actualización de un mercado.
	* Actualizar información de la cotización de un mercado. Esta funcionalidad se ejecutará de manera interna cada minuto.

Para comunicarse con los microservicios se dispondrá de un API Gateway. Cada microservicio implementará un API Rest y además cada uno tendrá su propia base de datos.

En la siguiente ilustración podemos ver un diagrama de la arquitectura.

![](docs/img/architectureDiagram.png)


## Tecnologías

### Lenguaje de programación

El proyecto será realizado en el lenguaje de programación **Python**. Algunos de los motivos por los que he decidido utilizar este lenguaje son: la facilidad de implementación, el requerir menos código en comparación con otros lenguajes y el disponer de cierta experiencia en este lenguaje. Una de las ventajas que nos ofrece para este proyecto, es que nos va a permitir obtener de forma sencilla datos financieros de Yahoo Finance, mediante el uso de la biblioteca [**yfinance**](https://github.com/ranaroussi/yfinance), la cual nos facilitará la implementación del microservicio `Mercado`.

### Base de datos

Tanto para la base de datos del microservicio `Portfolio`, como para la del microservicio `Mercado`, se va a utilizar el sistema de base de datos [**MongoDB**](https://www.mongodb.com). Para poder interactuar con las bases de datos en MongoDB desde Python, se va a utilizar **PyMongo**.

### Framework

El framework que se utilizará para implementar las APIs Rest será **Flask**. Como ventajas de utilizar este framework se puede destacar el permitir desarrollar de forma ágil y además existe una gran documentación, lo cual facilitará el proceso de desarrollo.

### Servicios

Para para la implementación del servicio de log se utilizará la biblioteca **logging** de Python. Para el servicio de configuración distribuida como puede verse en el diagrama de la arquitectura se va a utilizar **etcd**, para el cual se hará uso de la librería [**python-etcd**](https://github.com/jplana/python-etcd).
