#Un conjunto es una colección desordenada de elementos únicos.
# Definiendo un conjunto
numeros = {1, 2, 3, 4, 5}

# Agregar un elemento
numeros.add(6)

# Intentar agregar un duplicado (no tendrá efecto)
numeros.add(3)

# Eliminar un elemento
numeros.remove(2)

print(numeros)  # Output: {1, 3, 4, 5, 6} (el orden puede variar)
