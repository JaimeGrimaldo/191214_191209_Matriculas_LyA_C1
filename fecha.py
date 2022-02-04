fecha = "201224"
aniosValidos = ["20","21","22"]

extraerAnio1 = fecha[0]
extraerAnio2 = fecha[1]

anio = extraerAnio1 + extraerAnio2
print("Año extraido:",anio)

for i in range(len(aniosValidos)):
    if anio == aniosValidos[i]:
        print("Año valido")
        break
    else:
        print("Año invalido")


