#Una lista es una colección ordenada y mutable que permite elementos duplicados.
# Definiendo una lista
frutas = ["manzana", "banana", "cereza"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Agregar un elemento
frutas.append("naranja")
frutas.append("pera")

# Acceder a un elemento
print(frutas[1])  # Output: banana

# Modificar un elemento
frutas[0] = "kiwi"

# Eliminar un elemento
frutas.remove("cereza")

print(frutas)  # Output: ['kiwi', 'banana', 'naranja']
resultado = frutas + numeros
print(resultado)


