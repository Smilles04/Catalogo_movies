from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar Pelicula')
        print('e. Eliminar Catalogo de Pelicula')
        print('4. Salir')

        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agegar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_pelicula()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print("Salimos del programa")