## hacer un programa que pida el inicio, final, y el salto y lo muestre en pantalla

num_inicio = int(input("Ingrese el numero inicial: "))
num_final = int(input("Ingrese el numero final: "))
multi = int(input("Ingrese el multiplo: "))
for num in range(num_inicio,num_final+1):
    if num%multi==0:
        print(num)