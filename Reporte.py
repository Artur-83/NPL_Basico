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

    print("REPORTE DE ANÁLISIS DE TEXTO")

    print("ESTADÍSTICAS BÁSICAS")

    print(f"Total de palabras: {contar(texto)}")

    print(f"Total de caracteres (con espacios): {char_con(texto)}")

    print(f"Total de caracteres (sin espacios): {char_sin(texto)}")

    print(f"Total de oraciones: {contar_oraciones(texto)}")

    print(
        f"Promedio de longitud de palabras: "
        f"{promedio_longitud_palabra(texto)}"
    )

    print(
        f"Promedio de longitud de oraciones: "
        f"{promedio_longitud_oracion(texto)}"
    )

    print("\nPROCESAMIENTO NLP")

    print(f"Tokens generados: {len(tokens)}")

    print(
        f"Tokens después de eliminar stopwords: "
        f"{len(tokens_filtrados)}"
    )

    print(
        f"Diversidad Léxica (TTR): "
        f"{diversidad_lexica(tokens_filtrados)}"
    )

    print("\nTOP 5 PALABRAS MÁS FRECUENTES")

    palabras_top = top5(tokens_filtrados)

    for palabra, frecuencia in palabras_top:

        print(f"{palabra} -> {frecuencia}")

    print("\nANÁLISIS DE SENTIMIENTO")

    print(f"Clasificación: {clasificacion}")

    print(f"Puntuación: {puntuacion}")

    print("\n" + "=" * 50)


print("reporte cargado correctamente")