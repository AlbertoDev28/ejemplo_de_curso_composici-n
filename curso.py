class Curso:

    def __init__(self, nombre_curso):
        self.__nombre_curso = nombre_curso
        self.__listas_cursos = []


    def leccion_curso(self, nvo_curso):
        self.__listas_cursos.append(nvo_curso)


    def lecciones_mostrar(self):
        print(f"Nombre Leccion: {self.__nombre_curso}")
        for curso in self.__listas_cursos:
            print(curso.curso_info())
            curso.calcular_curso()
