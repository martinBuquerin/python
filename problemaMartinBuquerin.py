import random

archivo = open("./PERSONAL.txt", "w", encoding="utf-8")
archivo.close()
empleados = []

for i in range(10):
    codigo = "Cod-" + str(i+1)
    nombre = "Empleado-" + str(i+1)
    sexo = random.randint(1, 2)
    fecha_ant = random.randint(2000, 2018)
    categoria = random.randint(1, 6)
    if categoria == 1:
        sueldo = 3500
    if categoria == 2:
        sueldo = 2800
    if categoria == 3:
        sueldo = 2200
    if categoria == 4:
        sueldo = 1900
    if categoria == 5:
        sueldo = 1500
    if categoria == 6:
        sueldo = 1200
    empleado = [codigo, nombre, sexo, fecha_ant, categoria, sueldo]
    empleados.append(empleado)

archivo = open("./PERSONAL.txt", "a", encoding="utf-8")
print("Apartado A:\n", file=archivo)
print("Apartado A:")
for empleado in empleados:
    print(empleado)
    print(empleado, file=archivo)


print("\nApartado C:", file=archivo)
print("Apartado C:")
cate = int(input("Elija una categoria: "))
sexo = int(input("Elija una sexo: "))
print("Categoria elegida: ", cate , file=archivo)
print("Sexo elegido: ", sexo , file=archivo)
for empleado in empleados:
    if empleado[4] == cate and empleado[2] == sexo:
        print(empleado)
        print(empleado, file=archivo)
total = 0
media = 0
for empleado in empleados:
    antiguedad = 2023 - empleado[3]
    total = total + antiguedad
    media = total/10
    #print(antiguedad)

print("\n\nApartado E:")
print("\nApartado E:", file=archivo)
print("la media de antiguedad es: %.2f" % media +" años" )
print("la media de antiguedad es: %.2f" % media +" años", file=archivo )
