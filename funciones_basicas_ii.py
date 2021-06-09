def countdown(p_desde):    
    v_result=[]
    for i in range(p_desde,-1,-1):
        result.append(i)
    return v_result    

def PrintAndReturn(p_lista):
    print(p_lista[0])
    return(p_lista[1])

def FirstPlusLen(p_lista):
    return(p_lista[0]+len(p_lista))

def gtSecond(p_lista):
    v_result=[]
    if len(p_lista)>1:
        for v_valor in p_lista:
            if(v_valor>p_lista[1]):
                v_result.append(v_valor)
        print(len(v_result))
        return v_result
    else:
        return False

def ThisLonThatVal(p_size,p_val):
    v_result=[]
    for v_indice in range(0,p_size):
        v_result.append(p_val)
    return v_result
#print(countdown(2))

#print(PrintAndReturn([1,2]))

#print(FirstPlusLen([1,2,3,4,5]))

#print(gtSecond([5,2,3,2,1,4]))

#print(gtSecond([5]))

#print(ThisLonThatVal(7,4))