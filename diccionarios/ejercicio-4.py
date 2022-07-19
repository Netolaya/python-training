## 02/05/2022
## 02 de mayo del 2022

fecha = input("Escribir fecha en el formato dd/mm/aaaa: ")

meses = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "setiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

dia, mes, anio = fecha.split("/")

if mes not in meses:
    print("Mes invalido")
else:
    mes = meses[mes]
    mensaje = f"{dia} de {mes} del {anio}"
    print(mensaje)
