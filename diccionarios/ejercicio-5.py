cursos={"matematica":6,
        "fisica":4,
        "quimica":5}
suma=0
for curso in list(cursos.keys()):
    credito=cursos[curso]
    mensaje=f"{curso} tiene {credito} creditos."
    print(mensaje)
    suma=suma+credito
print(suma)
