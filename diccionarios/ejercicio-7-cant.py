cesta={}
continuar = True
while continuar:
    #cesta[producto]=precio
    producto=input("igrese el producto: ")
    precio=float(input("Ingrese el precio del producto: "))
    cantidad=float(input("Ingrese la cantidad de kilos: "))
    continuar =input("Desea agregar mas productos (SI/NO)").upper() == "SI"
    cesta[producto]= {
        "precio": precio,
        "cantidad": cantidad
    }
print(cesta)
total = 0
for product in cesta.keys():
    sub_precio = cesta[product]["precio"] * cesta[product]["cantidad"]
    print(product, '\t', sub_precio)
    total = total + sub_precio

print(total)

