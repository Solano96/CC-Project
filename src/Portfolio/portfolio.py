from Portfolio.portfolioException import PortfolioException
import requests

class Portfolio:

    def __init__(self, portfolio_db, dni):
        self.portfolio_db = portfolio_db
        result = self.portfolio_db.get_user_portfolio(dni)

        if len(result) > 0:
            self.user_portfolio = result[0]
        else:
            raise PortfolioException("Error: DNI no encontrado.")


    def consultar_datos_usuario(self):
        """
        Método para consultar los datos del usuario
        :return: dni y nombre
        """
        return {'dni': self.user_portfolio['dni'], 'nombre': self.user_portfolio['nombre']}


    def consultar_saldo(self):
        """
        Método para consultar el saldo disponible
        :return: saldo disponible
        """
        return {'saldo': self.user_portfolio['saldo']}


    def incrementar_saldo(self, cantidad):
        """
        Incrementar el saldo de la cuenta
        :param cantidad: cantidad en la que el saldo va a incrementarse
        :return: saldo actualizado
        """
        self.user_portfolio['saldo'] += cantidad
        self.portfolio_db.update_user_portfolio(self.user_portfolio)
        return {'saldo': self.user_portfolio['saldo']}


    def decrementar_saldo(self, cantidad):
        """
        Decrementar el saldo de la cuenta
        :param cantidad: cantidad que se va a substraer al saldo
        :return: saldo actualizado
        """
        if self.user_portfolio['saldo'] < cantidad:
            raise PortfolioException("Error: saldo inferior a la cantidad a substraer.")
        else:
            self.user_portfolio['saldo'] -= cantidad
            self.portfolio_db.update_user_portfolio(self.user_portfolio)

        return {'saldo': self.user_portfolio['saldo']}


    def consultar_acciones(self):
        """
        Método para consultar todas las acciones de las que se dispone
        :return: lista de mercados y número de acciones de dichos mercados
        """
        return {'acciones': self.user_portfolio['acciones']}


    def consultar_acciones_mercado(self, nombre_mercado):
        """
        Método para consultar las acciones que se disponen de un mercado concreto
        :param nombre_mercado: nombre de un mercado
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.user_portfolio['acciones']:
            return {nombre_mercado: self.user_portfolio['acciones'][nombre_mercado]}
        else:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")


    def __aniadir_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para incremetar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a incrementar
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.user_portfolio['acciones']:
            self.user_portfolio['acciones'][nombre_mercado] += num_acciones
        else:
            self.user_portfolio['acciones'][nombre_mercado] = num_acciones

        self.portfolio_db.update_user_portfolio(self.user_portfolio)


    def __substraer_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para decrementar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a decrementar
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.user_portfolio['acciones']:
            if num_acciones <= self.user_portfolio['acciones'][nombre_mercado]:
                self.user_portfolio['acciones'][nombre_mercado] -= num_acciones
            else:
                raise PortfolioException("Error: no se pueden susbtraer más acciones de las que se disponen.")
        else:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")

        self.portfolio_db.update_user_portfolio(self.user_portfolio)


    def comprar_acciones_mercado(self, nombre_mercado, num_acciones):
        # r = client.get(url+'/quote/realtime/'+nombre_mercado)
        # price = num_acciones*r.json()['regularMarketOpen']

        price = num_acciones*10
        self.decrementar_saldo(price)
        self.__aniadir_acciones_mercado(nombre_mercado, num_acciones)

        return self.consultar_acciones_mercado(nombre_mercado)


    def vender_acciones_mercado(self, nombre_mercado, num_acciones):
        # r = client.get(url+'/quote/realtime/'+nombre_mercado)
        # price = num_acciones*r.json()['regularMarketOpen']

        price = num_acciones*10
        self.incrementar_saldo(price)
        self.__substraer_acciones_mercado(nombre_mercado, num_acciones)

        return self.consultar_acciones_mercado(nombre_mercado)
