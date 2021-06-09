x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
#print(x)
students[0]['last_name']='Bryant'
#print(students[0]['last_name'])
sports_directory['soccer'][0]='Andres'
#print(sports_directory['soccer'][0])
z[0]['y']=30
#print(z[0]['y'])

def iterateDictionary(some_list):
    coma=', '
    for item in some_list:
        salida=''
        for llave in item:
            salida+=llave+' - '+item[llave]+coma
            if coma == ', ':
                coma=''
            else:
                coma=', '
        print(salida)
        

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        for llave in item:
            if llave==key_name:
                print(item[llave])

def printInfo(some_dict):
    for item in some_dict:
        parte_1=item.upper()
        cantidad=len(some_dict[item])
        print(cantidad,':',parte_1)
        for elemento in some_dict[item]:
            print(elemento)
        print()


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#iterateDictionary(students) 

#iterateDictionary2 ('last_name', students)
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)