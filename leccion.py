class Leccion:

    def __init__(self, curso_titulo, duracion, completado):
        self.__curso_titulo = curso_titulo
        self.__duracion = duracion
        self.__completado = completado



    def curso_info(self):
        return (f"Nombre del Curso: {self.__curso_titulo} | Tiempo Cursado: {self.__duracion}Min | "
                f"Tiempo del Curso: {self.__completado}Min")


    def calcular_curso(self):
        print(f"porcentaje cursado: {round((self.__duracion / self.__completado) * 100, 2)} %")
