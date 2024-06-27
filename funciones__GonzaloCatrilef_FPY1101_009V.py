import os

books = []
prestamos = []
# PROGIT-XIO-2021



def registro():
    os.system('cls')
    print('\n\t ** Registrar Libro')

    title = input('Titulo del Libro\t:\t')
    author = input('Autor del Libro\t:\t\t')
    anio = int(input('Año de Publicación\t:\t'))
    sku_id = input('Ingrese SKU\t:\t\t') 
    
    if title == '' or author == '' or anio <= 0 or sku_id == '':
        print('Todos los campos son obligatorios. Vuelva a ingresar los datos. ')
    else:
        print('Libro Registrado Exitosamente. ')

    book = {
        'titulo': title,
        'author': author,
        'año': anio,
        'sku' : sku_id,
    }

    books.append(book)

def prestar(): 
    os.system('cls')
    print('\n\t ** Prestar Libro')

    user = input('\nIngrese Nombre de Usuario:  ')
    sku = input('Ingrese SKU del Libro: ')
    date = input('Ingrese Fecha Solicitud: ')

    if sku in books:
        print ('El libro se encuentra prestado.')
    else:
        os.system('date')
        print('date')
    prestamo = {
        'user': user,
        'sku' : sku,
        'date' : date
    }

    prestamos.append(prestamo)

def lista():
    os.system('cls')
    print('\n\t ** Listas de Libros')

    print('\n \tTitulo\t\t\t\tAutor\t\t\tAño de Publicacion\t\t\tSKU')
    for i in books:
        print(f"{i['titulo']}\t\t{i['author']}\t\t\t{i['año']}\t\t\t\t{i['sku']}\n")

def imprimir():
    os.system('cls')
    print('\n\t ** Imprimir Libro')

    with open('reporte_prestamos.txt','w') as archivo:
        print(f"\nUsuario\t\t\t\t Titulo\t\t\t\t Fecha Prestamo")
        for prestados in prestamos:
          archivo.write(f"{prestados['user']}\t\t\t{prestados['sku']}\t\t\t{prestados['date']}\n")
          print(f"{prestados['user']}\t\t\t{prestados['sku']}\t\t\t{prestados['date']}\n")


def dev_datos():
    os.system('cls')
    print('Gracias por visitarnos... Nos vemos! ')

    nombre = 'Gonzalo Catrilef'
    rut = '18365610-4'

    dev = {
        'nombre': nombre,
        'rut' : rut
    }

    print(f"Desarrollado por {dev['nombre']}\nRun : {dev['rut']}")


def menu ():
    while True:
        print('\t\t***  Menu  ***\n1.Registrar Libro\n2.Prestar Libro\n3.Lista todos los Libros\n4.Imprimir Reporte de Prestamos.\n5. Salir')
        try:
            op = int(input('Ingrese una opción [ 1 - 5 ] :   '))

            if ( op == 1):
                registro()
            elif ( op == 2):    
                prestar()
            elif ( op == 3):
                lista()
            elif ( op == 4):
                imprimir()
            elif ( op == 5):
                dev_datos()
                break
            else:
                print('\nSeleccione una Opción valida...!!')
        except ValueError as ve: 
            print(f'Error {ve}. Favor vuelva a ingresar una opción. ')