def suma(a,b,c):
    return a+b+c
'''
print(suma(3,5))
print(suma(4,6))
print(suma(1,2)+3)
print(suma(suma(1,2),3))
'''
#print(suma(1,2,3))
def saludo(a):
    msg = "hola " + a
    return msg
nombre=input("escribe tu nombre:")
print(saludo(nombre))
