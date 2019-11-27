## OPERACIONES BASICAS CON STRINGS

# len(cadena) muestra el numero de caracteres
unacadena = "hola mundo"
print (len(unacadena))

# index(cadena) muestra la ubicacion del primer caracter que cumple 
print (unacadena.index("l"))

# cadena[valor:valor]  imprime un rango de caracteres
print(unacadena[3:7])

# upper() y lower() para cambiar la cadena mayusculas o minusculas
print( unacadena.upper() )
print( unacadena.lower() )

# split() separa cadenas con un determinado caracater
afewwords = unacadena.split()
print (afewwords)

