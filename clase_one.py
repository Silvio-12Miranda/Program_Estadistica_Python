# Autor: Silvio Abimael
# Email: silviom727@gmail.;com
# Fecha: 12/02/22
#Este programa despliega los datos de un estudiante
def run():
    nombre='Silvio Abimael'
    edad=26
    universidad= 'UAEM'
    carrera='Fisica'
    print(f'Mi nombre es {nombre}, tengo {edad}, estudio en {universidad} la carrera de {carrera}')

# Esta funcion pide requiere ingrese ciertos datos que pedira para posterior ser mostrados

def repeticion():
    menu = """Escriba los datos que se le solicitan"""
    print(menu)
    nombre_p = input('¿cual es su nombre?: ')
    edad_p= int(input('¿cual es su edad?: '))
    carrera_p= input('¿que carrera estudia?: ')
    universidad_p= input('¿en que univeridad estudia?')

    resultado= print(f'Mi nombre es {nombre_p}, tengo {edad_p}, estudio en {universidad_p} la carrera de {carrera_p}')

# Algunos ejemplos de listas
def listas():
    lista=[1,2,3,4,5]
    tupla= (1,2,3,4,5)
    tupla= list(tupla)
    lista_cadena= ['silvio','abimael','miranda']
    print(f'{lista}, el tamaño de la lista es: {len(lista)}')

# Ejercicio de interes compuesto
def interes():
    menu= """
    Bienvenido a nuestra calculadora de interes compuesto
    Ingrese el numero de años:
    """
    t=int(input(menu))
    p=100
    n=12
    r=.08

    a = p*(1+(r/n))**(n*t)
    print(f'El resultado es: {a}')

# Uso de condicionales
def condicional():
    menor= int(input('ingrese un numero que sea menor a 10'))
    if menor< 10:
        print('si es menor a 10')
    else:
        print('no es menor a 10')

#Ciclo for 

def ciclo_for():
    for i in range(500,1001):
        if i%33 ==0:
            print(f'{i},')

# Matrices
def matrices():
    m1= [[8,14,-6],[12,7,4],[14,3,8]]
    print(m1)
    filas = len(m1)
    print('filas=',filas)
    columna= len(m1[0])
    print('columna=', columna)
    print(m1[0][1])
    for i in range(filas):
        print(m1[i])

# Suma de matrices 
def suma_matrices():
    m1=[[8,14,-6],[12,7,4],[-11,3,21],[14,3,8]]
    m2= [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    m3= [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m3[i][j]= m1[i][j]+m2[i][j]
    print('resultado')
    for k in m3:
        print(k)

def producto_matrices():
    m1= [[8,14,-6],[12,7,4],[-11,3,21],[14,3,8]]
    m2= [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

    if len(m1[0]) == len(m2):
        m3= []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(None)
        print(m3)



if __name__ == '__main__':
    #run()
    #repeticion()
    #listas()
    #interes()
    #condicional()
    #ciclo_for()
    #suma_matrices()
    producto_matrices()
