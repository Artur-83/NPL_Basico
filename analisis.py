positivas ={
    "excelente","bueno","feliz","fantastico","genial",
    "increible","maravilloso", "positivo"
}

negativas ={ "malo",
    "terrible", "triste", "horrible", "pesimo", "problema", "odio", "negativo"
}
def contar(texto: str) -> int:
    """Cuenta el número de palabras en el texto"""
    return len(texto.split())

def char_sin(texto: str) -> int:
    """Cuenta el número de caracteres que hay en el texto"""
    contados = 0
    for caracter in texto:
        if caracter != " ":
            contados +=1
    return contados

def char_con(texto: str) -> int:
    """Cuenta el número de caracteres que hay en el texto sin contar los espacios"""
    return len(texto) 

def contar_oraciones(texto: str) -> int:
    """Cuenta el número de oraciones que hay en el texto"""
    contador = 0
    for caracter in texto:
        if caracter in ".!?":
            contador += 1
    return contador

def promedio_longitud_palabra(texto: str) -> float:
    """Calcula el promedio de longitud de las palabras que h ay en el texto"""
    palabras = texto.split()
    if len(palabras)== 0:
        return 0
    suma = 0
    for palabra in palabras:
        suma += len (palabra)
    return round(suma / len(palabras), 2)

def promedio_longitud_oracion(texto: str) -> float:
    """Calcula el promedio de la longitud que tienes las oraciones dentro del texto"""
    total_oraciones = contar_oraciones(texto)
    if total_oraciones == 0:
        return 0
    total_palabras = len(texto.split())
    return round(total_palabras / total_oraciones, 2)

def diversidad_lexica(token: list) ->float:
    """Calcula la diversidad lexica que tiene el texto"""
    if len(token) == 0:
        return 0
    palabras_unicas = set(token)
    return round(len(palabras_unicas) / len(token), 3)

def frecuencia(token: list) -> dict:
    """Calcula la frecuencia con la que aparecen palabras"""
    frecuencias ={}
    for palabra in token:
        if palabra in frecuencias:
            frecuencia[palabra] +=1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def top5(token: list) ->list:
    """Calcula las 5 palabras que más aparecen en el texto"""
    frecuencia = frecuencia(token)
    lista = []
    for palabra in frecuencias:
        lista.append((palabra, frecuencias[palabra]))
    n = len(lista)
    for i in range(n):
        for j in range (n-i-1):
            if lista[j][1] < lista[j+1][1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal
    return lista[:5]

def sentimiento(token: list) -> tuple:
    """Determina el sentimiento que tenga el texto"""
    puntuacion = 0
    for palabra in token:
        if palabra in positivas:
            puntuacion +=1
        elif palabra in negativas:
            puntuacion -=1
    if puntuacion > 0:
        sentimiento = "Positivo"
    elif puntuacion <0:
        sentimiento = "Negativo"
    else:
        sentimiento = "Neutral"
    return sentimiento, puntuacion

print("analisis cargado correctamente")

