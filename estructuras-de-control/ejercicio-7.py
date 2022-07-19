from unittest import result


numero=int(input("ingrese un numero: "))
for num in range(1,11):
    resultado=num*numero
    #mensaje=str(num)+ "x" +str(numero)+"="+str(resultado)
    mensaje=f"{num} x {numero} = {resultado}"
    print(mensaje)