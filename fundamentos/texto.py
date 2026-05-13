print("Hola 'Mundo'")
print('Hola "Mundo 2"')

ingles = "I'm Luis"

multiples = """Hola
Mundo
desde
comillas
triples"""

print(ingles)
print(multiples)

palabra = "Murciélago"
print(len(palabra))

texto = "Este curso es de fundamentos de Python"
estaIncluida = "Python" in texto
noEstaIncluida = "Javascript" not in texto

print(estaIncluida)
print(noEstaIncluida)

mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)
print(minuscula)

espacios = "    Este es el texto    "
print(espacios)

sinEspacios = espacios.strip()
print(sinEspacios)