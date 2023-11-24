class Alumno:
    def __init__(self, nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad
              
    def leerNota(self):
        return self.nota

    def registrarNota(self):
        while True:
            try:
                nota = int(input(f"Ingrese nota del siguiente alumno - {self.nombre} {self.apellido}: "))
                if nota < 0 or nota > 20:
                    print("La nota debe estar en un rango de 0 a 20. Intente nuevamente.")
                    continue
                self.nota = nota
                break
            except ValueError as ve:
                print(f"Ingrese solo números para la nota. {ve}")