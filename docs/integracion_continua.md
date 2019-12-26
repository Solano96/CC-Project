## Integración continua

Se han utilizado dos herramientas de integración continua. Estas son las siguientes:

* **Travis-CI**: ejecuta los tests unitarios y de cobertura sobre el sistema operativo Linux, para las versiones de Python 3.6, 3.6.8, 3.7 y 3.8 (el motivo de que la versión minima sea la 3.6 es debido a errores de ejecución en versiones anteriores con el paquete *yfinance*).  Tras finalizar la ejecución de los tests, se envían los resultados del test de cobertura a [codecov](https://codecov.io/gh/Solano96/CC-Project-Trading). En el fichero [.travis.yml](https://github.com/Solano96/CC-Project-Trading/blob/master/.travis.yml) se puede consultar la configuración descrita.

* **Github Actions**: ejecuta los test unitarios y de cobertura en la última versión de Ubuntu, para las versiones de Python 3.6, 3.7 y 3.8. En el caso de *Github Actions*, no se envían los resultados del test de cobertura a codecov. En el fichero [pythonapp.yml](https://github.com/Solano96/CC-Project-Trading/blob/master/.github/workflows/pythonapp.yml) se puede consultar la configuración descrita.
