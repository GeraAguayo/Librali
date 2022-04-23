class Usuario:
    def __init__(self,nombreUsr,generosFav,estadoActual):
        self.nombreUsr = nombreUsr
        self.generosFav = generosFav
        self.estadoActual = estadoActual
        #Determinar si el usr esta leyendo o no
        if estadoActual == True:
            estadoActual == "Leyendo"
        else:
            estadoActual == "Por el momento no esta leyendo"

    
    
    def mostrarDatosUsr(self):
        print("Los datos del usuario son:")
        print(f"Nombre: {self.nombreUsr}")
        print(f"Generos favoritos: {self.generosFav}")
        print(f"Estado actual: {self.estadoActual}")