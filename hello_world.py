# 1. TAREA: imprimir "Hola mundo"
print( "Hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print( "Hola", name )	# con una coma
print( "Hola "+ name )	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( "Hola",name  )	# con una coma
print( "Hola "+str(name) )	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} y {}".format(fave_food1,fave_food2) ) # con .format()
print( f"Me encanta comer {fave_food1} y {fave_food2}" ) # con una cadena f
#2a
mi_nombre="Patricio"
print ("Hola",mi_nombre)
#2b
print ("Hola "+mi_nombre)
#3a
num=4
print ("Hola",num)
#3b
print ("Hola "+ str(num))
#4a
food_one="Carbonada"
food_two="Charquican"
print ("Me encanta comer {} y {}".format(food_one,food_two))
#4b
print (f"Me encanta comer {food_one} y {food_two}")


