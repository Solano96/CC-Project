
class PortfolioException(Exception):
    pass


class Portfolio:

    def __init__(self, dni, nombre, saldo_inicial):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.acciones = []


    def consultar_saldo(self):
        """
        Método para consultar el saldo disponible
        :return: saldo disponible
        """
        return self.saldo


    def incrementar_saldo(self, cantidad):
        """
        Incrementar el saldo de la cuenta
        :param cantidad: cantidad en la que el saldo va a incrementarse
        :return: saldo actualizado
        """
        self.saldo += cantidad
        return self.saldo


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

        return self.saldo


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
        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")
        else:
            return self.acciones[indice_acciones]


    def aniadir_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para incremetar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a incrementar
        """
        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            self.acciones.append({
                'mercado': nombre_mercado,
                'acciones': num_acciones
            })
        else:
            self.acciones[indice_acciones]['acciones'] += num_acciones


    def substraer_acciones_mercado(self, nombre_mercado, num_acciones):
        """
        Método para decrementar las acciones de un mercado
        :param nombre_mercado: nombre de un mercado
        :param num_acciones: número de acciones a decrementar
        """
        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")
        elif self.acciones[indice_acciones]['acciones'] < num_acciones:
            raise PortfolioException("Error: no se pueden susbtraer más acciones de las que se disponen.")
        else:
            self.acciones[indice_acciones]['acciones'] -= num_acciones


    def __buscar_mercado(self, nombre_mercado):
        """
        Método privado para encontrar el índice de un mercado en acciones
        :param nombre_mercado: nombre de un mercado
        :return: índice del mercado en la lista de acciones
        """
        for i in range(len(self.acciones)):
            if self.acciones[i]['mercado'] == nombre_mercado:
                return i
        return None
