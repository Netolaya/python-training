cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

data = cadena.split('\n')
cabecera = data[0]
_, nombre_key, email_key, telefono_key, descuento_key = cabecera.split(";")
valores = data[1:]
clientes = {}
for valor in valores:
    campos = valor.split(";")
    nif, nombre, email, telefono, descuento = campos
    clientes[nif] = {
        nombre_key: nombre,
        email_key: email,
        telefono_key: telefono,
        descuento_key: descuento
    }

print(clientes)