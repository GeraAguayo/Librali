from Usuario import *
from Libro import *

def crearUsuario():
    print("Hola!, soy Venus y estoy aquí para ser tu compañera de lecturas!")
    print("Hagamos unas preguntas para conocernos mejor")
    print("----------------------------------------------------------------")
    nombreUsr = input("¿Cual es tu nombre?: ")
    generoFav = input("¿Cual es tu genero favorito?: ")
    estadoActual = input("¿Estas leyendo algo por ahora? Escribe si o no: ")
    estadoActual.lower()
    #Se determina es estado actual del usr (leyendo o no)
    if estadoActual == "si":
        estadoActual = True
    elif estadoActual == "no":
        estadoActual = False
    else:
        print("Se ha introducido una opcion incorrecta, intentelo de nuevo")
        crearUsuario()

    #Se crea el usuario con los datos
    nombreUsr = Usuario(nombreUsr,generoFav,estadoActual)
    nombreUsr.mostrarDatosUsr()



