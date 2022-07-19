from pickle import TRUE


facturas={}
continuar = True 
cant_pendiente=0
cant_pagada=0
while continuar:
    motivo=input("Que desea realizar? (ingresar/pagar/terminar): ")

    if motivo=="ingresar":
        factura=input("Ingrese en numero de factura: ")
        valor=int(input("ingrese el valor de la factura: "))
        facturas[factura]=valor
        cant_pendiente=cant_pendiente+valor
        print(facturas)
        print(f"cantidad pagada: {cant_pagada}")
        print(f"Cantidad pendiente de pago: {cant_pendiente}")

    elif motivo=="pagar":
        factura=input("Que numero de factura desea pagar: ")
        if factura not in facturas:
            print(f"No exista la factura {factura}")
            continue
        cant_pagada=cant_pagada+facturas[factura]
        cant_pendiente=cant_pendiente-facturas[factura]
        del facturas[factura]
        print(facturas)
        print(f"cantidad pagada: {cant_pagada}")
        print(f"Cantidad pendiente de pago: {cant_pendiente}")
    elif motivo=="terminar":
        continuar=False
        print(f"cantidad pagada: {cant_pagada}")
        print(f"Cantidad pendiente de pago: {cant_pendiente}")
        print("gracias, adios")
    
