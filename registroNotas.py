import pickle
from alumnos import Alumno

def guardar_alumnos(lista_alumnos):
    with open('alumnos.pkl', 'wb') as archivo:
        pickle.dump(lista_alumnos, archivo)

def cargar_alumnos():
    try:
        with open('alumnos.pkl', 'rb') as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return []

def obtener_promedio(lista_alumnos):
    if lista_alumnos:
        notas = [alumno.nota for alumno in lista_alumnos]
        return sum(notas) / len(notas)
    return 0

def obtener_suma_notas(lista_alumnos):
    if lista_alumnos:
        return sum(alumno.nota for alumno in lista_alumnos)
    return 0

def main():
    lista_alumnos = cargar_alumnos()

    print("Bienvenidos al registro de notas")

    while True:
        print("R: Registrar Alumnos")
        print("C: Calificar a los alumnos")
        print("P: Promedio de notas de los alumnos")
        print("S: Suma de notas de los alumnos")
        print("X: Salir")
        comando = input("Ingrese comando: ")

        if comando.upper() == 'R':
            nombre = input("Ingrese nombre del alumno: ")
            apellido = input("Ingrese apellido del alumno: ")
            while True:
                try:
                    edad = int(input("Ingrese edad del alumno: "))   
                    if edad < 1 or edad > 100: 
                        print("La edad debe estar en un rango de 1 a 100. Intente nuevamente.")
                        continue
                    edad = edad
                    break
                except ValueError as e:
                    print(e)
            nacionalidad = input("Ingrese nacionalidad del alumno: ")

            
            alumno = Alumno(nombre, apellido, edad, 0, nacionalidad)
            lista_alumnos.append(alumno)
            guardar_alumnos(lista_alumnos)

        elif comando.upper() == 'C':
            for alumno in lista_alumnos:                
                print(f"La nota del alumno {alumno.nombre} es : {alumno.leerNota()}")
                alumno.registrarNota()
            guardar_alumnos(lista_alumnos)

        elif comando.upper() == 'P':
            promedio = obtener_promedio(lista_alumnos)
            print(f"El promedio de notas para {len(lista_alumnos)} alumnos es: {promedio:.2f}")

        elif comando.upper() == 'S':
            suma_notas = obtener_suma_notas(lista_alumnos)
            print(f"La suma de notas de {len(lista_alumnos)} alumnos es: {suma_notas}")

        elif comando.upper() == 'X':
            guardar_alumnos(lista_alumnos)
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()