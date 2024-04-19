# EXERCISE 2

class CuentaPersona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.ingresos = {}
        self.gastos = {}

    def total_ingresos(self):
        return sum(self.ingresos.values())

    def total_gastos(self):
        return sum(self.gastos.values())

    def informacion_cuenta(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Total de Ingresos: {self.total_ingresos()}, Total de Gastos: {self.total_gastos()}"

    def agregar_ingreso(self, descripcion, monto):
        if descripcion in self.ingresos:
            self.ingresos[descripcion] += monto
        else:
            self.ingresos[descripcion] = monto

    def agregar_gasto(self, descripcion, monto):
        if descripcion in self.gastos:
            self.gastos[descripcion] += monto
        else:
            self.gastos[descripcion] = monto

    def saldo_cuenta(self):
        return self.total_ingresos() - self.total_gastos()


# Ejemplo de uso
persona = CuentaPersona("Juan", "Pérez")
persona.agregar_ingreso("Salario", 5000)
persona.agregar_ingreso("Bono", 1000)
persona.agregar_gasto("Alquiler", 1500)
persona.agregar_gasto("Comida", 500)

print(persona.informacion_cuenta())
print("Saldo de la Cuenta:", persona.saldo_cuenta())
