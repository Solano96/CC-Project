# Proyecto para la asignatura Cloud Computing

## Índice de contenidos

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Índice de contenidos](#ndice-de-contenidos)
- [Descripción](#descripcin)
- [Arquitectura](#arquitectura)
	- [Microservicios](#microservicios)
	- [Bases de datos](#bases-de-datos)
- [Tecnologías](#tecnologas)
- [Licencia](#licencia)

<!-- /TOC -->

## Descripción

En este proyecto se va a crear una aplicación desplegable en la nube, que sirva de simulador de bolsa.  Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

Por simplicidad todas las compras y ventas llevadas a cabo, serán ejecutadas al precio del mercado en el momento de ejecutar la orden y estas ejecutarán inmediatamente después de su creación.

Esta aplicación tiene como objetivo que los usuarios que la utilicen puedan invertir en bolsa con dinero ficticio y de esta forma puedan jugar en bolsa, sin el riesgo de perder dinero real. Además será de gran utilidad para principiantes que quieran aprender, sin el peligro de perder sus ahorros.

## Arquitectura

La aplicación tendrá una arquitectura basada en microservicios, lo cual nos permitirá implementar los diferentes servicios de forma independiente y despleglarlos por separado.

### Microservicios

Los microservicios considerados serán los siguientes:

* **Gestión de usuarios.** Este microservicio se encargará de la gestión de los usuarios, realizando funcionalidades como el registro de nuevos usuarios o el inicio de sesión. Algunas de las funcionalidades de este microservicio son las siguientes:

	1. Dar de alta usuarios.
	2. Dar de baja usuarios.
	3. Inicio de sesión.

* **Gestión de la cuenta.** Este microservicio gestionará la cuenta del usuario. Entre las funcionalidades de este servicio podemos encontrar las siguientes:

	1. Consultar saldo de la cuenta.
	2. Consultar acciones compradas.
	3. Modificar saldo.
	4. Modificar acciones compradas.

* **Gestión de cotizaciones.** Este microservicio es responsable de obtener información acerca de las cotizaciones de los mercados. Algunas de las funcionalidades de este servicio son:

	1. Consultar precio actual del mercado.
	2. Consultar información del mercado.
	3. Obtener señales basadas en indicadores técnicos.

* **Gestión de ordenes.** Este microservicio se encargá de la gestión de las ordenes de compra y venta. Se tendrá que comunicar con el microservicio de gestión de la cuenta para comprobar si el usuario tiene suficiente dinero para ejecutar la orden de compra y además para actualizar la cartera del usuario tras ejecutar una orden de compra o venta. Se comunicará también con el microservicio de gestión de cotizaciones para consultar el precio de cierre del mercado sobre el cual se va a llevar a cabo la orden.

	1. Crear orden de compra.
	2. Crear orden de venta.


### Bases de datos

Se dispondrá de una base de datos para cada microservicio, excepto para el de gestión de cotizaciones. Las bases de datos serán las siguientes:

* Base de datos para la gestión de usuarios. En esta base de datos se almacenarán los nombres de usuarios y las contraseñas asociadas.

* Base de datos para la gestión de la cuenta. En esta base de datos se almacenará información sobre la cartera de los usuarios y las acciones de las que disponen.

* Base de datos para la gestión de ordenes. En esta base de datos se almacenará un historial de todas las ordenes de compra o venta llevadas a cabo por el usuario, así como las ordenes fallidas.

En la siguiente ilustración podemos ver un diagrama de la arquitectura.

![](docs/img/architectureDiagram.png)

En el diagrama podemos ver que el cliente se comunicará con los microservicios mediante un API Gateway que enrutará las peticiones de los clientes a los servicios. Se puede apreciar también que hay un sistema de registro centralizado, al igual que el almacén de configuración etcd.

## Tecnologías

Para la implementación del API Gateway se utilizará el lenguaje de programación Go. Los microservicios serán implementados en Ruby con el framework Sinatra, a excepción del microservicio de gestión de cotizaciones el cual se implementará en Python con el framework Flask. La comunicación entre los microservicios se hará de forma asíncrona basada en mensajes, utilizando  RabbitMQ como broker de mensajería.

Respecto a las tecnologías que usaremos para las bases de datos, se considerará el uso de una base de datos relacional para la gestión de usuarios, en concreto se va a utilizar el sistema de gestión de base de datos PostgreSQL. Para las bases de datos correspondientes a la gestión de la cuenta y la gestión de ordenes se optará por el uso de una base de datos no relacional, en este caso se ha optado por MongoDB.

## Licencia

Este proyecto está bajo la licencia [*GNU General Public License v3.0*](https://github.com/Solano96/CC-Project-Trading/blob/master/LICENSE).
