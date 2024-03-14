import matplotlib.pyplot as plt

class FinCal:
    def __init__(self):
        interes = input("Ingrese el tipo de interés (simple/compuesto): ")
        
        if interes == "simple":
            self.simple()
        elif interes == "compuesto":
            self.compuesto()
        else:
            print("Escoge un tipo de interés valido: simple o compuesto.")   

    def simple(self):
        monto_inicial = float(input("Ingrese el monto inicial: "))
        interes = float(input("Ingrese el interés (%): "))
        tiempo = int(input("Ingrese el tiempo: "))

        registros = []
        for t in range(tiempo+1):
            token = monto_inicial * (1 + interes/100 * t)
            registros.append(token)

        graph = input("¿Desea graficar? (si/no): ")
        if graph == "si":
            plt.figure()
            plt.title("Interés Simple")
            plt.xlabel("Tiempo")
            plt.ylabel("$")
            plt.plot(range(tiempo+1), registros, label="Interés Simple")
            plt.show()
            
        print("El monto final es:", token)

    def compuesto(self):
        monto_inicial = float(input("Ingrese el monto inicial: "))
        interes = float(input("Ingrese el interés (%): "))
        tiempo = int(input("Ingrese el tiempo: "))

        registros = []
        for t in range(tiempo+1):
            token = monto_inicial * (1 + interes/100)**t
            registros.append(token)

        graph = input("¿Desea graficar? (si/no): ")
        if graph == "si":
            plt.figure()
            plt.title("Interés Compuesto")
            plt.xlabel("Tiempo")
            plt.ylabel("$")
            plt.plot(range(tiempo+1), registros, label="Interés Compuesto")
            plt.show()
            
        print("El monto final es:", token)

app = FinCal()
