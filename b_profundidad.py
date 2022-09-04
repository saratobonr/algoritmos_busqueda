values = {
    "Pereira": "Medellin",
    "Manizales": "Medellin",
    "Puerto Berrio": "Medellin",
    "Ibague": "Pereira",
    "Honda": "Manizales",
    "Tunja": "Puerto Berrio",
    "Melgar": "Ibague",
    "Facatativa": "Honda",
    "Bogota": "Tunja",
    "Bogota": "Melgar",
    "Bogota": "Facatativa"
}

path = []


def search(start, valueToFind):
    path.append(start)
    # si encontramos el valor, lo devolvemos
    if start == valueToFind:
        return valueToFind
    # recorremos todos los elementos en busca del valor de start
    for k, v in values.items():
        result = 0
        # si el valor del elemento tiene como padre al valor de start
        if v == start:
            # llamamos a la función recursivamente enviando el nuevo padre
            result = search(k, valueToFind)

        # si hemos recibido algun resultado es que hemos encontrado el elemento
        if result:
            return result

    path.pop()
    # si llegamos aqui, es que hemos llegado al final de una profundidad
    return 0


result = search("Medellin", "Bogota")
if result:
    print('Resultado búsqueda por profundida: ', path)
else:
    print("No existe")
