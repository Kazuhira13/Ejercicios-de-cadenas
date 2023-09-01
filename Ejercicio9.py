print("Coloque su mes de nacimiento dd/mm/aaa:")
dia = input("dia:")
mes = input("mes:")
año = input("año:")
print(dia +"/"+ mes+"/"+ año)
#Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = input("Coloque su mes de nacimiento dd/mm/aaa:")
dd = fecha[:fecha.find("/")]
espacio = fecha[fecha.find("/")+1:]
mm = espacio[:espacio.find("/")]
aaa = espacio[espacio.find("/")+1:]
print("dia:",dd)
print("mes:",mm)
print("año:",aaa)