## calcular la suma de los 2 primeros numeros pares
## 2, 4, 6, 8, 10, 12, 14

## calcula la suma de 1
## 2 

## primeros : 2
## 1+3

## primeros: 3
## 1+3+5

## 4
## 1+3+5+7

## 5
## 1+3+5+7+9

numero=int(input("ingrese un numero: "))
def suma(n):
    if n==1:
        return 2
    else:
        return suma(n-1)+(n*2)
print(suma(numero))

def suma_impares(n):
    if n==1:
        return 1
    else:
        return suma_impares(n-1)+((n*2)-1)
print(suma_impares(numero))