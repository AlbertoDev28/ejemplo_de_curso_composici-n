from curso import Curso
from leccion import Leccion

def main():

    curso1 = Curso("Curso de progamacion")
    lecciones = Leccion("base datos",80,300)
    lecciones1 = Leccion("Variable",90,200)


    curso1.leccion_curso(lecciones)
    curso1.leccion_curso(lecciones1)
    curso1.lecciones_mostrar()

if __name__ == "__main__":
    main()