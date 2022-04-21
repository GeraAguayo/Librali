print("* * * Soy Grecia y te ayudare a buscar un libro que te guste * * *")
print("\n")
#Decidir entre realistas o ficticios
print("¿Que tipo de textos prefiere?")
print("1 -  Realistas")
print("2 - Ficticios")
opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

if opcion == 1:
    print("¿Que tipo de textos prefiere?")
    print("1 - Relacionados con historia")
    print("2 - Novelas")
    print("3 - Textos científicos")
    opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))
    #Textos relacionados con historia
    if opcion == 1:
        print("¿Que tipos de textos realacionados con historia te parecen mas interesantes?")
        print("1 - La biografía de una persona")
        print("2 - De hechos históricos en general")
        print("3 - Historias realcionados con la guerra y sucesos bélicos")
        opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

        if opcion == 1:
            print("Recomendacion biografías personas")

        elif opcion == 2:
            print("Recomendación hechos históricos en general")
            
        elif opcion == 3:
            print("Recomendación hechos históricos relacionados con la guerra ")

        else:
            print("Se ha introducido una opcion invalida")
        
    #Novelas
    elif opcion == 2:
        print("¿Que tipo de novela te parece más interesante?")
        print("1- Juvenil")
        print("2- Romantica")
        opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

        if opcion == 1:
            print("Recomendacin novelas juveniles")
        
        elif opcion == 2:
            print("Recomendacion novela romantica")

        else:
            print("La opcion introducida es invalida")

    #Textos cientificos
    elif opcion == 3:
        print("¿Que texto científico te pareces más interesante?")
        print("1- Relacionado con biología")
        print("2- Relacionado con física")
        print("3- Relacionado con astronomía")
        opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

        if opcion == 1:
            print("Recomendacion libros biologia")
        
        elif opcion == 2:
            print("Recomendacion libros fisica")
        
        elif opcion == 3:
            print("Recomendacion libros atronomia")

        else:
            print("La opcion introducida no es valida")

    else:
        print("Ha ingresado una opcion invalida")
#Textos ficticios
elif opcion == 2:
    print("¿Que tipo de texto le atrae más?")
    print("1- De terror")
    print("2- De fantasía")
    print("3- De ciencia ficción")
    opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

    if opcion == 1:
        print("Recomendacion libros de terror")

    elif opcion == 2:
        print("¿Y que le gustaria de fantasía?")
        print("1- Cuentos")
        print("2- Travesías")
        opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

        if opcion == 1:
            print("Recomendacion cuentos")
        
        elif opcion == 2:
            print("Recomendacion libros de travesisas")

        else:
            print("Opcion introducida invalida")

    elif opcion == 3:
        print("¿Que tipo de ciencia ficción le interesa más?")
        print("1- Relacionado con tecnología")
        print("2- Relacionados con viajes espaciales")
        print("3- Relacionados con mundos postapocalipticos")
        opcion = int(input("Escriba el numero correspondiente a su opcion elegida: "))

        if opcion == 1:
            print("Recomendacion libro tecnologia")

        elif opcion == 2:
            print("Recomendacion libros viajes espaciales")
        
        elif opcion == 3:
            print("Recomendacion libros postapocaliptivos")
        
        else:
            print("Opcion introducida invalida")
else:
    print("Introduzca una opcion valida")
