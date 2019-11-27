## Manejo de las Condiciones
"""
    valor = 2
    valor == 2 -- condicion que se cumple
    valor == 3 -- condicion que no se cumple
    valor < 3  -- condicion que si se cumple
"""

numero = 2 
if numero > 3 :
    print ("numero es menor a 3")

nombre = "alfred"
age = 24
if nombre == "alfed" and age == 24:
    print ("Tu nombre es correcto y tu edad tambien")

# Operador in
arraynombres = ["alfred", "Jose"]
if nombre in arraynombres:
    print ("su nombre puede ser cualquira") 

# If anidados
numero2 = 2 
if numero2 > 3 :
    print ("numero es menor a 3")
elif numero2 == 1:
    print ("numero es igual que uno")
else:
    print ("numero es mayor a 3")


    