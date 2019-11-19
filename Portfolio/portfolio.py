
class PortfolioException(Exception):
    pass


class Portfolio:

    def __init__(self, dni, nombre, saldo_inicial):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.acciones = {}


    def consultar_saldo(self):
        """
        Método para consultar el saldo disponible
        :return: saldo disponible
        """
        return {'saldo': self.saldo}


    def incrementar_saldo(self, cantidad):
        """
        Incrementar el saldo de la cuenta
        :param cantidad: cantidad en la que el saldo va a incrementarse
        :return: saldo actualizado
        """
        self.saldo += cantidad
        return {'saldo': self.saldo}


    def decrementar_saldo(self, cantidad):
        """
        Decrementar el saldo de la cuenta
        :param cantidad: cantidad que se va a substraer al saldo
        :return: saldo actualizado
        """
        if self.saldo < cantidad:
            raise PortfolioException("Error: saldo inferior a la cantidad a substraer.")
        else:
            self.saldo -= cantidad

        return {'saldo': self.saldo}


    def consultar_acciones(self):
        """
        Método para consultar todas las acciones de las que se dispone
        :return: lista de mercados y número de acciones de dichos mercados
        """
        return self.acciones


    def consultar_acciones_mercado(self, nombre_mercado):
        """
        Método para consultar las acciones que se disponen de un mercado concreto
        :param nombre_mercado: nombre de un mercado
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.acciones:
            return {nombre_mercado: self.acciones[nombre_mercado]}
        else:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")


    def aniadir_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para incremetar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a incrementar
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.acciones:
            self.acciones[nombre_mercado] += num_acciones
        else:
            self.acciones[nombre_mercado] = num_acciones

        return {nombre_mercado: self.acciones[nombre_mercado]}


    def substraer_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para decrementar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a decrementar
        :return: número de acciones que se disponen del mercado <nombre_mercado>
        """
        if nombre_mercado in self.acciones:
            if num_acciones <= self.acciones[nombre_mercado]:
                self.acciones[nombre_mercado] -= num_acciones
            else:
                raise PortfolioException("Error: no se pueden susbtraer más acciones de las que se disponen.")
        else:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")

        return {nombre_mercado: self.acciones[nombre_mercado]}
