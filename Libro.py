class Libro:
    def __init__(self,nombreLibro,autorLibro,numPaginas,paginasLeidas = None):
        self.nombreLibro = nombreLibro
        self.autorLibro = autorLibro
        self.numPaginas = numPaginas
        self.paginasLeidas = paginasLeidas


    def mostrarDatosLibro(self):
        print("Los datos del libro son:")
        print(f"Nombre del libro: {self.nombreLibro}")
        print(f"Autor/a del libro: {self.autorLibro}")
        print(f"Paginas totales del libro: {self.numPaginas}")
        
        