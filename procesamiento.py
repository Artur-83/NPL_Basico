stop_word = {"el","la","los","las","un","una","unos","unas",
    "de","del","que","y","o","es","en","a","por","para","con",
    "su","sus","al"}

def limpiar(texto: str) -> str:
    """Elimina los signos de puntuación del texto:"""
    texto = texto.lower()
    signos = ",.;:!¡¿?()[]{\}"
    for signo in signos:
        texto = texto.replace(signo, "")
    return texto

def token(texto: str) -> list:
    """ Convierte el texto de una cadena a una lista"""
    return texto.split()

def stopWords (token: list) -> list:
    """Elimina las stop words del texto"""
    texto_limpio = []
    for palabra in token:
        if palabra not in stop_word:
            texto_limpio.append(palabra)
    return texto_limpio

print("Procesamiento cargado correctamente")