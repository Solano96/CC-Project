## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

Por simplicidad todas las compras y ventas llevadas a cabo, serán ejecutadas al precio del mercado en el momento de ejecutar la orden y estas ejecutarán inmediatamente después de su creación.

Esta aplicación tiene como objetivo que los usuarios que la utilicen puedan invertir en bolsa con dinero ficticio y de esta forma puedan jugar en bolsa, sin el riesgo de perder dinero real. Además será de gran utilidad para principiantes que quieran aprender, sin el peligro de perder sus ahorros.

## Arquitectura

La aplicación tendrá una arquitectura basada en microservicios, lo cual nos permitirá implementar los diferentes servicios de forma independiente y despleglarlos por separado.

A continuación se exponen las entidades del sistema y cada una de las cuales se corresponderá con un microservicio.

* **Portfolio.** Un portfolio en bolsa es una agrupación de activos financieros, en nuestro proyecto tan solo estará formado por el saldo disponible y las acciones compradas. Las funcionalidades de esta entidad son las siguientes:

	* Consultar el saldo disponible.
	* Modificar saldo.
	* Consultar acciones compradas.
	* Comprar acciones.
	* Añadir acciones.

* **Mercado**. Esta entidad está formada por el nombre del mercado y la información de la cotización del mercado, está incluye el precio de apertura, cierre, mínimo y máximo, además del volumen del periodo. También se incluye la fecha y hora en la que se actualizó las información. Las funcionalidades son las siguientes:

	* Consultar el precio de cierre/apertura/mínimo/máximo.
	* Consultar la hora de la última actualización.
	* Actualizar información de la cotización. Esta funcionalidad se ejecutará de manera interna cada minuto.

![](img/architectureDiagram.png)
