#Una tupla es una colección ordenada pero inmutable, lo que significa que no se puede modificar después de su creación
# Definiendo una tupla
colores = ("rojo", "verde", "azul")

# Acceder a un elemento
print(colores[0])  # Output: rojo
print(colores[1]) # Output: verde

# No se pueden modificar elementos, pero sí reasignar la variable
colores = ("amarillo", "negro", "blanco")
print(colores)  # Output: ('amarillo', 'negro', 'blanco')
