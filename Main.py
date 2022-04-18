#Secuencia inicial en donde se preguntan los datos del usuario    
print("Hola!, soy Venus y te ayudare con tus estadisticas de lectura")
print("Hagamos unas preguntas para conocernos")
nombre = input("¿Como te llamas?")
generosFav = input("¿Que generos te gusta leer más?")
opcion = input("¿Estas leyendo un libro por el momento? S/N")
opcion = opcion.lower()
#Determina si esta leyendo algo o no, si si esta leyendo algo pide los datos del libro,
#si no, recomienda un libro
if opcion ==  "s":
    print("Interesante!, dejame saber un poco más de ese libro")
    nombreLibro = input("¿Como se llama el libro?: ")
    autorLibro = input("¿Quien lo escribió?: ")
    paginasTotal = float(input("¿Cuantas paginas tiene en total?: "))
    paginasLeidas = float(input("¿Cuantas paginas has leido hasta el momento?: "))
    print("")
    print("Wow, esas estadisticas son muy impresionantes!")
    estaLeyendo = f"Actualmente leyendo : {nombreLibro}"
elif opcion == "n":
    estaLeyendo = "Actualmente no esta leyendo"
    #Implementar a Grecia
    print("Por el momento nuestros prgramadores no han resuelto esto, vuelve pronto!")
else:
    print("Se ha intoducido una opcion invalida, vuelva a intentarlo")

#Ficha de datos del usuario    
print("")
print("||| Ficha de usuario")
print(f"||| Nombre: {nombre}")
print(f"||| Generos favoritos: {generosFav}")
print(f"||| Estatus actual: {estaLeyendo}")
