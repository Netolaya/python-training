x = 10 #alcance global

def modificar():
    x = 2 #alcance local

modificar()

# python hace distincion entre mayusculas y minusculas
aB = 2
Ab = 4
print(aB)
print(Ab)

# no esta permitido estos nombres de variable
# 2num
# var-iable
# var able

def deF():
    return 2

a = None
if a is None:
    print("a es nullo")



a = list("letras")
print(a)