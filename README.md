# Proyecto de Análisis de Texto en Python

Este proyecto es una aplicación simple escrita en Python que permite a los usuarios ingresar un texto y realizar diversas operaciones de análisis sobre él. Está diseñado como una herramienta interactiva que recopila información sobre el texto ingresado, como la frecuencia de letras específicas, el número de palabras y caracteres especiales, y si la palabra "Python" está presente en el texto. A continuación, se proporciona una descripción detallada de las características y el funcionamiento del proyecto.

## Características del Proyecto

- **Ingreso de Texto:** Al iniciar el programa, se le pide al usuario que ingrese el texto que desea analizar. El texto se convierte a minúsculas para garantizar la consistencia en los análisis.

- **Selección de Letras:** Luego, se le solicita al usuario que ingrese tres letras de su elección, una por una. Cada letra debe ser un único carácter y es tratada en minúsculas.

- **Conteo de Letras:** El proyecto cuenta cuántas veces aparece cada una de las tres letras ingresadas en el texto proporcionado. Los resultados se almacenan en tres variables diferentes: `contador1`, `contador2`, y `contador3`.

- **Conteo de Palabras:** Se divide el texto en palabras utilizando un espacio en blanco como separador. El proyecto cuenta cuántas palabras hay en el texto y almacena el resultado en la variable `palabras`.

- **Análisis de Caracteres Especiales:** El proyecto también identifica el primer y último carácter del texto ingresado y los almacena en las variables `primer_caracter` y `ultimo_caracter`, respectivamente.

- **Texto Invertido:** El texto ingresado se invierte, es decir, se invierten el orden de las palabras, y se almacena en la variable `texto_invertido`. Esto permite al usuario ver el texto de manera inversa.

- **Verificación de la Presencia de "Python":** El proyecto verifica si la palabra "Python" está presente en el texto. Si es así, se establece la variable `incognita` en "Si"; de lo contrario, se establece en "No".

- **Visualización de Resultados:** Finalmente, el proyecto muestra un resumen de los resultados, que incluye la frecuencia de las letras ingresadas, el número de palabras, el primer y último carácter, el texto invertido y la presencia de "Python" en el texto.

## Cómo Ejecutar el Proyecto

1. Asegúrate de tener Python instalado en tu sistema.

2. Copia y pega el código proporcionado en un archivo de Python (por ejemplo, `analisis_de_texto.py`).

3. Ejecuta el programa en tu entorno de desarrollo o en la línea de comandos.

4. Sigue las instrucciones para ingresar el texto y las letras.

5. Observa los resultados en la salida de la consola.

Este proyecto es una excelente manera de practicar y aprender Python mientras realizas análisis simples de texto. Puedes personalizarlo y ampliar sus características según tus necesidades y habilidades en programación. ¡Diviértete explorando y analizando tus textos con este proyecto!
