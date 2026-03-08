# Tarea: Clase BibliotecaServicio (servicio)
# Esta clase gestiona la lógica: administración de colecciones de libros, usuarios y préstamos.

# Importaciones necesarias de la capa de modelos
from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    """
    Servicio principal que gestiona la lógica del negocio de la biblioteca digital.
    Cumple con la separación de responsabilidades entre modelos y servicios.
    """

    def __init__(self):
    
        # Utilizar DICCIONARIO para almacenar los libros disponibles.
        # Clave: ISBN, Valor: Objeto Libro.
        # Decisión de diseño: Los diccionarios permiten búsquedas O(1) extremadamente rápidas por clave única (ISBN).
        self.__libros_disponibles = {} 

        
        self.__usuarios_registrados = {} 

    # --- Gestión de Libros ---

    #  Funcionalidad: Añadir libros.
    def añadir_libro(self, isbn: str, titulo: str, autor: str, categoria: str) -> bool:
        """Crea un nuevo libro y lo añade al diccionario de disponibles."""
        if isbn in self.__libros_disponibles:
            print(f"Error: Ya existe un libro con el ISBN {isbn}.")
            return False
        
        #  Creación de objetos.
        nuevo_libro = Libro(isbn, titulo, autor, categoria)
        # Uso adecuado de colecciones (diccionario).
        self.__libros_disponibles[isbn] = nuevo_libro
        print(f"Libro '{titulo}' añadido correctamente.")
        return True

    # Funcionalidad: Quitar libros.
    def quitar_libro(self, isbn: str) -> bool:
        """Elimina un libro del sistema si existe y no está prestado."""
        if isbn in self.__libros_disponibles:
            libro_eliminado = self.__libros_disponibles.pop(isbn)
            print(f"Libro '{libro_eliminado.get_titulo()}' eliminado correctamente.")
            return True
        else:
            # Si no está en disponibles, podría estar prestado
            print(f"Error: El libro con ISBN {isbn} no está disponible o no existe.")
            return False

    # --- Gestión de Usuarios ---

    # Funcionalidad: Registrar usuarios.
    def registrar_usuario(self, user_id: int, nombre: str) -> bool:
        """Registra un nuevo usuario asegurando ID único."""
        #  Garantizamos ID único usando el diccionario (como un set de claves).
        if user_id in self.__usuarios_registrados:
            print(f"Error: Ya existe un usuario registrado con el ID {user_id}.")
            return False
        
        # Registro de usuarios.
        nuevo_usuario = Usuario(user_id, nombre)
        self.__usuarios_registrados[user_id] = nuevo_usuario
        print(f"Usuario '{nombre}' registrado correctamente.")
        return True

    #  Funcionalidad: Dar de baja usuarios.
    def dar_baja_usuario(self, user_id: int) -> bool:
        """Elimina un usuario del sistema si no tiene préstamos activos."""
        if user_id in self.__usuarios_registrados:
            usuario = self.__usuarios_registrados[user_id]
            # Verificación de lógica de negocio: no se puede dar de baja si tiene libros
            if len(usuario.get_libros_prestados()) > 0:
                print(f"Error: El usuario {usuario.get_nombre()} tiene préstamos activos. Debe devolver los libros primero.")
                return False
            
            self.__usuarios_registrados.pop(user_id)
            print(f"Usuario '{usuario.get_nombre()}' dado de baja correctamente.")
            return True
        else:
            print(f"Error: El usuario con ID {user_id} no existe.")
            return False

    # --- Préstamos y Devoluciones ---

    # Funcionalidad: Prestar libros.
    def prestar_libro(self, isbn: str, user_id: int) -> bool:
        """Gestiona el préstamo de un libro disponible a un usuario registrado."""
        # Validar existencia de libro y usuario
        if isbn not in self.__libros_disponibles:
            print(f"Error: El libro con ISBN {isbn} no está disponible.")
            return False
        if user_id not in self.__usuarios_registrados:
            print(f"Error: El usuario con ID {user_id} no está registrado.")
            return False
        
        # Recuperar objetos
        libro_objeto = self.__libros_disponibles[isbn]
        usuario_objeto = self.__usuarios_registrados[user_id]
        
        # Lógica del préstamo: mover libro de la biblioteca al usuario
        #  Se quita del diccionario de disponibles.
        self.__libros_disponibles.pop(isbn)
        #  Se añade a la lista de préstamos del usuario.
        usuario_objeto.añadir_libro_prestado(libro_objeto)
        print(f"Libro '{libro_objeto.get_titulo()}' prestado con éxito a {usuario_objeto.get_nombre()}.")
        return True

    #  Funcionalidad: Devolver libros.
    def devolver_libro(self, isbn: str, user_id: int) -> bool:
        """Gestiona la devolución de un libro por parte de un usuario."""
        if user_id not in self.__usuarios_registrados:
            print(f"Error: El usuario con ID {user_id} no está registrado.")
            return False
        
        usuario_objeto = self.__usuarios_registrados[user_id]
        
        # Lógica de devolución: mover libro del usuario a la biblioteca
        #  El usuario busca y elimina de su lista.
        libro_devuelto = usuario_objeto.devolver_libro_prestado(isbn)
        
        if libro_devuelto:
            # Se añade de vuelta al diccionario de disponibles.
            self.__libros_disponibles[isbn] = libro_devuelto
            print(f"Libro '{libro_devuelto.get_titulo()}' devuelto con éxito por {usuario_objeto.get_nombre()}.")
            return True
        else:
            print(f"Error: El usuario {usuario_objeto.get_nombre()} no tiene prestado el libro con ISBN {isbn}.")
            return False

    # --- Búsquedas ---

    #  Funcionalidad: Buscar libros por: Título, Autor, Categoría.
    def buscar_libros(self, criterio: str, valor_busqueda: str):
        """
        Busca libros en el catálogo disponible según el criterio especificado.
        """
        resultados = []
        valor_busqueda = valor_busqueda.lower() # Búsqueda no sensible a mayúsculas
        
        # Iterar sobre los valores del diccionario de disponibles.
        for libro in self.__libros_disponibles.values():
            criterio_evaluar = ""
            
            if criterio == "titulo":
                criterio_evaluar = libro.get_titulo().lower()
            elif criterio == "autor":
                criterio_evaluar = libro.get_autor().lower()
            elif criterio == "categoria":
                criterio_evaluar = libro.get_categoria().lower()
            else:
                print("Criterio de búsqueda inválido.")
                return

            if valor_busqueda in criterio_evaluar:
                resultados.append(libro)
        
        if resultados:
            print(f"\n--- Resultados de búsqueda ({criterio}: '{valor_busqueda}') ---")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros disponibles para el criterio {criterio} '{valor_busqueda}'.")

    #  Funcionalidad: Listar libros prestados a un usuario.
    def listar_libros_prestados_usuario(self, user_id: int):
        """Muestra la lista de libros actualmente prestados a un usuario específico."""
        if user_id not in self.__usuarios_registrados:
            print(f"Error: El usuario con ID {user_id} no está registrado.")
            return
        
        usuario = self.__usuarios_registrados[user_id]
        # Acceso a la lista encapsulada en el modelo.
        libros = usuario.get_libros_prestados()
        
        print(f"\n--- Libros prestados a {usuario.get_nombre()} (ID: {user_id}) ---")
        if libros:
            for libro in libros:
                print(libro)
        else:
            print("El usuario no tiene libros prestados actualmente.")

    def listar_todos_libros_disponibles(self):
        """Muestra todos los libros que están actualmente en el catálogo disponible."""
        print("\n--- Catálogo de Libros Disponibles ---")
        if not self.__libros_disponibles:
            print("No hay libros disponibles en este momento.")
        else:
            for libro in self.__libros_disponibles.values():
                print(libro)

    def listar_todos_usuarios(self):
        """Muestra todos los usuarios registrados en el sistema."""
        print("\n--- Usuarios Registrados ---")
        if not self.__usuarios_registrados:
            print("No hay usuarios registrados en este momento.")
        else:
            for usuario in self.__usuarios_registrados.values():
                print(usuario)