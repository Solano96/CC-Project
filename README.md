# CC-Project-Trading
Proyecto para la asignatura Cloud Computing

## Descripción

En este proyecto se va a crear una aplicación en la nube para simulación en la bolsa de valores. Esta aplicación permitirá crear ordenes de compra y venta en el mercado y poder llevar un registro de la cartera del usuario.

Por simplicidad todas las compras y ventas llevadas a cabo, serán ejecutadas al precio de cierre del mercado en el momento de ejecutar la orden.

## Arquitectura

La aplicación estará basada en microservicios. Los microservicios considerados serán los siguientes:

* **Gestión de usuarios.** Este microservicio se encargará de la gestión de los usuarios, realizando funcionalidades como el registro de nuevos usuarios o el inicio de sesión.

* **Gestión de la cuenta.** Este microservicio gestionará la cuenta del usuario, guardando información como el dinero en la cuenta o las acciones que posee el usuario.

* **Gestión de cotizaciones.** Este microservicio es responsable de obtener información acerca de las cotizaciones de los mercados.

* **Gestión de ordenes.** Este microservicio se encargá de la gestión de las ordenes de compra y venta. Se tendrá que comunicar con el microservicio de gestión de la cuenta para comprobar si el usuario tiene suficiente dinero para ejecutar la orden de compra y además para actualizar la cartera del usuario tras ejecutar una orden de compra o venta. Se comunicará también con el microservicio de gestión de cotizaciones para consultar el precio de cierre del mercado sobre el cual se va a llevar a cabo la orden.


![](docs/img/architectureDiagram.png)

#### Bases de datos

Se dispondrá de una base de datos para cada microservicio, excepto para el de gestión de cotizaciones. Las bases de datos serán las siguientes:

* Base de datos para la gestión de usuarios. En esta base de datos se almacenarán los nombres de usuarios y las contraseñas asociadas.

* Base de datos para la gestión de la cuenta. En esta base de datos se almacenará información sobre la cartera de los usuarios y las acciones de las que disponen.

* Base de datos para la gestión de ordenes. En esta base de datos se almacenará un historial de todas las ordenes de compra o venta llevadas a cabo por el usuario, así como las ordenes fallidas.

## Tecnologías

Respecto a las tecnologías que usaremos para las bases de datos, se considerará el uso de una base de datos relacional para la gestión de usuarios, como por ejemplo el sistema de gestión de base de datos MySQL. Para las bases de datos correspondientes a la gestión de la cuenta y la gestión de ordenes se optará por el uso de una base de datos no relacional, como puede ser el caso de MongoDB. 

## Licencia

Este proyecto está bajo la licencia [*GNU General Public License v3.0*](https://github.com/Solano96/CC-Project-Trading/blob/master/LICENSE).
