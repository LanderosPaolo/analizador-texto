# Se le pide al usuario que ingrese el texto a analizar
texto = input("Ingresa el texto que quieres analizar: ").lower()

# Se crea una lista vacía
letras = []

# Se le pide al usuario que ingrese letras a su elección
letra1 = input("Ingresa la primera letra (puede ser cualquiera y solo debe ser 1): ").lower()
letra2 = input("Ingresa la segunda letra (puede ser cualquiera y solo debe ser 1): ").lower()
letra3 = input("Ingresa la tercera letra (puede ser cualquiera y solo debe ser 1): ").lower()

# Se agregan las letras al arreglo vacío
letras.append(letra1)
letras.append(letra2)
letras.append(letra3)

# Se crea un contador para cada letra
contador1 = texto.count(letras[0])
contador2 = texto.count(letras[1])
contador3 = texto.count(letras[2])

# Se crea el método para contar cuantas palabras y caracteres especiales hay en todo el texto
palabras = texto.split()

# Primera y última letra del texto
primer_caracter = texto[0]
ultimo_caracter = texto[-1]

# Texto invertido
palabras.reverse()
texto_invertido = ' '.join(palabras)

# Está Python en el texto?
incognita = "python" in texto
if (incognita == True):
    incognita = "Si"
else:
    incognita = "No"

# Se imprime el analisis
print(f"""
- La letra "{letras[0]}" aparece "{contador1}" veces en el texto ingresado
- La letra "{letras[1]}" aparece "{contador2}" veces en el texto ingresado
- La letra "{letras[2]}" aparece "{contador3}" veces en el texto
- El texto tiene una cantidad de "{len(palabras)}" palabras
- El primer y último caracter son "{primer_caracter}" y "{ultimo_caracter}" respectivamente
- El texto invertido sería: {texto_invertido}
- ¿Aparece Python en el texto?: {incognita}
""")