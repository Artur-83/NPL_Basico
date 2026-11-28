from procesamiento import limpiar
from procesamiento import token
from procesamiento import stopWords

from analisis import contar
from analisis import char_con
from analisis import char_sin
from analisis import contar_oraciones
from analisis import promedio_longitud_palabra
from analisis import promedio_longitud_oracion
from analisis import diversidad_lexica
from analisis import top5
from analisis import sentimiento


def generar_reporte(texto):

    texto_limpio = limpiar(texto)

    tokens = token(texto_limpio)

    tokens_filtrados = stopWords(tokens)

    clasificacion, puntuacion = sentimiento(tokens_filtrados)

    print("****REPORTE DE ANÁLISIS DE TEXTO****")

    print("**ESTADÍSTICAS BÁSICAS**")

    print("Total de palabras: ", contar(texto))

    print("Total de caracteres (con espacios): ",char_con(texto))

    print("Total de caracteres (sin espacios): ",char_sin(texto))

    print("Total de oraciones: ",contar_oraciones(texto))

    print("Promedio de longitud de palabras: ",promedio_longitud_palabra(texto))
    

    print("Promedio de longitud de oraciones: ",promedio_longitud_oracion(texto))

    print("\nPRrocesamiento NLP")

    print("Tokens generados: ",len(tokens))

    print("Tokens después de eliminar stopwords: ",len(tokens_filtrados))

    print("Diversidad Léxica (TTR): ",diversidad_lexica(tokens_filtrados))

    print("\nTOP 5 palabras más frecuentes")

    palabras_top = top5(tokens_filtrados)

    for palabra, frecuencia in palabras_top:

        print(palabra," -> ",frecuencia)

    print("\nAnálisis de sentimiento")

    print("Clasificación:",clasificacion)

    print("Puntuación:", puntuacion)

    print("\n" + "=" * 50)


print("reporte cargado correctamente")