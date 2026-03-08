# [referencia source 49-56] Tarea: Clase Usuario (modelo)
class Usuario:
    """
    Representa a un usuario registrado en la biblioteca.
    Aplica encapsulamiento para proteger los atributos.
    """

    def __init__(self, user_id: int, nombre: str):
        self.__user_id = user_id  # ID de usuario único (público para identificación)
        self.__nombre = nombre
        
        # [referencia source 54, 56] Requisito técnico:
        # Utilizar lista para almacenar los libros actualmente prestados.
        # Las listas permiten añadir/quitar elementos fácilmente manteniendo orden de solicitud.
        self.__libros_prestados = [] 

    # Getters para acceder a la información encapsulada
    def get_user_id(self) -> int:
        return self.__user_id

    def get_nombre(self) -> str:
        return self.__nombre

    # [referencia source 80] Funcionalidad: Listar libros prestados a un usuario.
    def get_libros_prestados(self) -> list:
        # Retorna una copia de la lista para evitar manipulación externa directa
        return list(self.__libros_prestados)

    def añadir_libro_prestado(self, libro_objeto):
        """Añade un objeto Libro a la lista de préstamos del usuario."""
        self.__libros_prestados.append(libro_objeto)

    def devolver_libro_prestado(self, isbn: str) -> object:
        """
        Intenta devolver un libro. Busca por ISBN en la lista, lo elimina y lo devuelve.
        Retorna None si el usuario no tiene ese libro.
        """
        libro_encontrado = None
        for i, libro in enumerate(self.__libros_prestados):
            if libro.get_isbn() == isbn:
                libro_encontrado = self.__libros_prestados.pop(i)
                break
        return libro_encontrado

    def __str__(self):
        num_libros = len(self.__libros_prestados)
        return f"ID Usuario: {self.__user_id} | Nombre: {self.__nombre} | Libros en préstamo: {num_libros}"