class PortfolioException(Exception):
    pass

class Portfolio:

    def __init__(self, dni, nombre, saldo_inicial):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.acciones = []

    def consultar_saldo(self):
        return self.saldo

    def incrementar_saldo(self, cantidad):
        self.saldo += cantidad

    def decrementar_saldo(self, cantidad):
        if self.saldo < cantidad:
            raise PortfolioException("Error: saldo inferior a la cantidad a substraer.")
        else:
            self.saldo -= cantidad

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
            self.acciones.append({
                'mercado': nombre_mercado,
                'acciones': num_acciones
            })
        else:
            self.acciones[indice_acciones]['acciones'] += num_acciones

    def substraer_acciones_mercado(self, nombre_mercado, num_acciones):
        indice_acciones = self.__buscar_mercado(nombre_mercado)

        if indice_acciones is None:
            raise PortfolioException("Error: No hay acciones compradas de este mercado.")
        elif self.acciones[indice_acciones]['acciones'] < num_acciones:
            raise PortfolioException("Error: no se pueden susbtraer más acciones de las que se disponen.")
        else:
            self.acciones[indice_acciones]['acciones'] -= num_acciones

    def __buscar_mercado(self, nombre_mercado):
        for i in range(len(self.acciones)):
            if self.acciones[i]['mercado'] == nombre_mercado:
                return i
        return None
