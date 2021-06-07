
#saludo= 'Saludos desde un archivo Python'
#print(saludo)

#nombre='Patricio'
#edad=43

#print('Mi nombre es '+ nombre+' y mi edad es '+str(edad))

#def cubo(num):
#    x=10
#    x+=1
#    print(x)
#    return num*num*num

#print(cubo(3))

ciudades=['Iquique','Los Angeles','Chillán','Guayaquil','Lima']

for ciudad in ciudades:
    if ciudad[0]=='L':
        continue
    print(ciudad)

i=1
while i < 1000:
    print(i)
    i+=3

while True:
    nombre= input('Ingrese un nombre(o 0 para salir)')
    if (nombre=="0"):
        break
    print('Hola ',nombre)

def a():
    print(5)
x = a()
print(x)