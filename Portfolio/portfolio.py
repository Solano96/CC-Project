class PortfolioException(Exception):
    pass

class Portfolio:

    def __init__(self, dni, nombre, saldo_inicial):
        self.dni = dni
        self.name = name
        self.saldo = saldo_inicial
        self.acciones = []

    def consultar_saldo(self):
        return self.saldo

    def incrementar_saldo(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def decrementar_saldo(self, cantidad):

        if saldo < cantidad:
            raise PortfolioException("Error: saldo inferior a la cantidad a substraer.")

    def consultar_acciones(self):
        return self.acciones

    def consultar_acciones_mercado(self, nombre_mercado):

        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")
        else:
            return self.acciones[indice_acciones]

    def aniadir_acciones_mercado(self, nombre_mercado, num_acciones):

        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            acciones.append([nombre_mercado, num_acciones])
        else:
            acciones[indice_acciones][1] += num_acciones

    def substraer_acciones_mercado(self, nombre_mercado, num_acciones):

        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")
        elif self.acciones[indice_acciones][1] < num_acciones:
            raise PortfolioException("Error: no se pueden susbtraer más acciones de las que se disponen.")
        else:
            self.acciones[indice_acciones][1] -= num_acciones            

    def __buscar_mercado(self, nombre_mercado):
        for i in range(len(self.acciones)):
            if self.acciones[i][0] == nombre_mercado:
                return i
        return None
