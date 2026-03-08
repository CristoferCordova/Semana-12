import sys
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL ---")
    print("1. Añadir Libro")
    print("2. Quitar Libro")
    print("3. Registrar Usuario")
    print("4. Dar de Baja Usuario")
    print("5. Prestar Libro")
    print("6. Devolver Libro")
    print("7. Buscar Libros")
    print("8. Listar Libros Prestados a un Usuario")
    print("0. Salir")
    print("------------------------------------------------")

def main():
    servicio = BibliotecaServicio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                isbn = input("ISBN: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                servicio.añadir_libro(isbn, titulo, autor, categoria)

            elif opcion == '2':
                isbn = input("ISBN del libro a quitar: ")
                servicio.quitar_libro(isbn)

            elif opcion == '3':
                user_id = int(input("ID de Usuario (entero): "))
                nombre = input("Nombre: ")
                servicio.registrar_usuario(user_id, nombre)

            elif opcion == '4':
                user_id = int(input("ID de Usuario a dar de baja: "))
                servicio.dar_baja_usuario(user_id)

            elif opcion == '5':
                isbn = input("ISBN del libro: ")
                user_id = int(input("ID de Usuario: "))
                servicio.prestar_libro(isbn, user_id)

            elif opcion == '6':
                isbn = input("ISBN del libro: ")
                user_id = int(input("ID de Usuario: "))
                servicio.devolver_libro(isbn, user_id)

            elif opcion == '7':
                print("Criterios: 1(Título), 2(Autor), 3(Categoría)")
                crit_opt = input("Seleccione (1-3): ")
                criterios_map = {'1': 'titulo', '2': 'autor', '3': 'categoria'}
                
                if crit_opt in criterios_map:
                    valor = input("Texto a buscar: ")
                    servicio.buscar_libros(criterios_map[crit_opt], valor)
                else:
                    print("Criterio inválido.")

            elif opcion == '8':
                user_id = int(input("ID de Usuario: "))
                servicio.listar_libros_prestados_usuario(user_id)

            elif opcion == '0':
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Por favor ingrese un tipo de dato válido (ej. números para IDs).")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()