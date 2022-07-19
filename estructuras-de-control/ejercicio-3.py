

numero=int(input("ingrese un numero entero: "))
impar=1
lista_impares = ["1"]
while impar<numero:
    #print(impar)
    impar=impar+2 #5
    if impar<=numero:
        lista_impares.append(str(impar))

#for i in range(numero+1):
#    if i % 2 != 0:
#        lista_impares.append(str(i))


print(" , ".join(lista_impares))