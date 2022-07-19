cesta={
}
producto=input("igrese el producto: ")
precio=int(input("Ingrese el precio del producto: "))
while producto!="ninguno":
    cesta[producto]=precio
    producto=input("igrese el producto: ")
    if producto=="ninguno":
        break 
    precio=int(input("Ingrese el precio del producto: "))   
print(cesta)
print(sum(cesta.values()))