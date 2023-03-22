
print("\n\nCuestion 4:")
alumnos = {}

for i in range(3):
    nombre = input("Introduzca el nombre : ")
    nota = float(input("Introduzca la nota: "))
    while(nota < 0 or nota > 10):
        nota = float(input("Introduzca una nota entre 0 y 10: "))

    alumnos[nombre] = nota


#print(notas)
maxima = 0
contador = 0
nombre=list(alumnos.keys())
notas=list(alumnos.values())


for nota in notas:
    contador = contador + 1
    if maxima < nota:
        maxima = nota
        mejorAlumno = nombre[contador - 1]
        print(mejorAlumno)






print("La nota máxima es del alumno:", mejorAlumno)
print("La nota máxima es:", maxima)


print("\n\nCuestion 6:")


def calculo(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    distancia = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
    return distancia


coordenadasTupla = ()
for i in range(3):
    if i == 0:
        x = int(input("Introduzca la corrdenada (X): "))

    if i == 1:
        y = int(input("Introduzca la corrdenada (y): "))

    if i == 2:
        z = int(input("Introduzca la corrdenada (z): "))
        coordenadasTupla = (x, y, z)

coordenadasLista = []
for i in range(3):
    if i == 0:
        x = int(input("Introduzca la corrdenada (X): "))
        coordenadasLista.append(x)
    if i == 1:
        y = int(input("Introduzca la corrdenada (y): "))
        coordenadasLista.append(y)
    if i == 2:
        z = int(input("Introduzca la corrdenada (z): "))
        coordenadasLista.append(z)

distancia = calculo(coordenadasTupla, coordenadasLista)

print("La distancia es: ", distancia)

