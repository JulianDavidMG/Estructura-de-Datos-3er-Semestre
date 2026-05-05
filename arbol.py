class Nodo:
    def __init__(self, valor, es_carpeta=True):
        self.valor = valor  # El nombre del archivo o carpeta
        self.es_carpeta = es_carpeta  # Si es una carpeta (True) o archivo (False)
        self.hijos = []  # Los archivos o carpetas dentro de esta carpeta

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def mostrar_contenido(self, nivel=0):
        indentacion = " " * (nivel * 2)
        if self.es_carpeta:
            print(f"{indentacion}Carpeta: {self.valor}")
            for hijo in self.hijos:
                hijo.mostrar_contenido(nivel + 1)  # Recursión para mostrar el contenido
        else:
            print(f"{indentacion}Archivo: {self.valor}")


# Crear las carpetas y archivos
raiz = Nodo("root", es_carpeta=True)  # Carpeta raíz

carpeta_a = Nodo("carpeta_a", es_carpeta=True)
carpeta_b = Nodo("carpeta_b", es_carpeta=True)

archivo_a1 = Nodo("archivo_a1.txt", es_carpeta=False)
archivo_a2 = Nodo("archivo_a2.txt", es_carpeta=False)
archivo_b1 = Nodo("archivo_b1.txt", es_carpeta=False)

# Agregar archivos a las carpetas
carpeta_a.agregar_hijo(archivo_a1)
carpeta_a.agregar_hijo(archivo_a2)
carpeta_b.agregar_hijo(archivo_b1)

# Agregar carpetas a la raíz
raiz.agregar_hijo(carpeta_a)
raiz.agregar_hijo(carpeta_b)

# Mostrar el contenido del sistema de archivos
raiz.mostrar_contenido()