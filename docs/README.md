## Índice de contenidos

- [Descripción](#descripcin)
- [Arquitectura](#arquitectura)

<!-- /TOC -->

## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

Por simplicidad todas las compras y ventas llevadas a cabo, serán ejecutadas al precio del mercado en el momento de ejecutar la orden y estas ejecutarán inmediatamente después de su creación.

Esta aplicación tiene como objetivo que los usuarios que la utilicen puedan invertir en bolsa con dinero ficticio y de esta forma puedan jugar en bolsa, sin el riesgo de perder dinero real. Además será de gran utilidad para principiantes que quieran aprender, sin el peligro de perder sus ahorros.

## Arquitectura

La aplicación tendrá una arquitectura basada en microservicios, lo cual nos permitirá implementar los diferentes servicios de forma independiente y despleglarlos por separado.

A continuación se exponen las entidades del sistema y cada una de las cuales se corresponderá con un microservicio.

* **Portfolio.** Un portfolio en bolsa es una agrupación de activos financieros, en nuestro proyecto tan solo estará formado por el saldo disponible y las acciones compradas. Las funcionalidades de esta entidad son las siguientes:

	* Creación de un nuevo portfolio.
	* Dar de baja un portfolio.
	* Consultar el saldo disponible en un portfolio.
	* Modificar saldo de un portfolio.
	* Consultar acciones compradas en un porfolio.
	* Comprar acciones para añadir nuevas acciones a un portfolio.
	* Vender acciones de un portfolio.


* **Mercado**. Esta entidad está formada por el nombre del mercado y la información de la cotización del mercado, está incluye el precio de apertura, cierre, mínimo y máximo, además del volumen del periodo. También se incluye la fecha y hora en la que se actualizó las información. Las funcionalidades son las siguientes:

	* Añadir un nuevo mercado.
	* Eliminar mercado.
	* Consultar el precio de cierre/apertura/mínimo/máximo de un mercado.
	* Consultar el volumen de un mercado.
	* Consultar la hora de la última actualización de un mercado.
	* Actualizar información de la cotización de un mercado. Esta funcionalidad se ejecutará de manera interna cada minuto.

En la siguiente ilustración podemos ver un diagrama de la arquitectura.

![](img/architectureDiagram.png)
