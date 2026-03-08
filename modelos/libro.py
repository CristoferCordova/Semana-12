# Tarea: Clase Libro (modelo)
class Libro:
    """
    Representa un libro dentro del sistema de la biblioteca.
    Aplica encapsulamiento para proteger los atributos.
    """

    def __init__(self, isbn: str, titulo: str, autor: str, categoria: str):
        self.__isbn = isbn  # Identificador único (público para la búsqueda, protegido por encapsulamiento)
        
        # Utilizar tupla para almacenar título y autor (inmutables).
        self.__datos_principales = (titulo, autor)
        
        self.__categoria = categoria

    # Getters para acceder a la información encapsulada
    def get_isbn(self) -> str:
        return self.__isbn

    def get_titulo(self) -> str:
        # Retorna el primer elemento de la tupla
        return self.__datos_principales[0]

    def get_autor(self) -> str:
        # Retorna el segundo elemento de la tupla
        return self.__datos_principales[1]

    def get_categoria(self) -> str:
        return self.__categoria

    def __str__(self):
        # Método para representar el objeto como cadena de texto
        return f"ISBN: {self.__isbn} | Título: {self.get_titulo()} | Autor: {self.get_autor()} | Categoría: {self.__categoria}"