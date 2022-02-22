# Autor: Silvio Miranda
# Correo: silviom727@gmail.com
# Este programa calcula el IMC de 'n' cantidad de personas.


def calc_imc():
    p=[68,70,80]
    e=[165,175,185]
    imc= []

    for i in p:
        for j in e:
            imc.append()
    print(imc)


def datos_p(name,weight,height):
    
    nombre= []
    pesos= []
    estaturas= []
   
    nombre.append(name)
    pesos.append(weight)
    estaturas.append(height)
    
    #return print(f'\nSon correctos los datos: \n\nNombre:{nombre[0]}\nPeso: {pesos[0]} kg\nEstatura: {estaturas[0]} cm')
    

def run():
    menu = """  
    Bienvenido a la calculadora IMC
    
    Ingrese el numero de personas a las cuales desea calcular su IMC: 
    """
    men = int(input(menu))
    
    for i in range(men):
        name= input('Ingrese su nombre: ')
        weight= int(input('Ingrese su peso en kg: '))
        height= int(input('Ingrese su estatura en cm: '))
        datos_p(name,weight,height)

if __name__ == '__main__':
    calc_imc()
