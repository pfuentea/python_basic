import random
def randInt(p_min=0,p_max=100):
    if p_min<p_max or p_max>0 :
        num = random.random() * (p_max-p_min) + p_min
        return round(num)

def getCarton():
    carton=[]
    while True:
        bolita = randInt(1,36)
        if bolita in carton:
            continue
        carton.append(bolita)
        if len(carton)==6:
            break
    return carton

def Loto():
    while True:
        eleccion =input('Ingrese 1 para jugar, sino saldrá del juego: ')
        if eleccion != '1':
                break
        carton_usuario= getCarton()
        carton_casa = getCarton()
        aciertos=0
        print('Su carton es:',carton_usuario)
        print('Los numeros sorteados son:',carton_casa)
        for bolita in carton_usuario:
            if bolita in carton_casa:
                aciertos+=1
        print('Acerto:',aciertos)
    print('Gracias por jugar al loto')


#print(randInt(10,30))

Loto()
