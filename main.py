import auxiliar
import procesamiento

ruta = auxiliar.seleccionar_archivo()
print(ruta)

texto = auxiliar.cargar_texto(ruta)

texto_limpio = procesamiento.limpiar(texto)

# 2. Convertir la cadena en lista de tokens
tokens = procesamiento.token(texto_limpio)

# 3. Filtrar stop words
palabras_filtradas = procesamiento.stopWords(tokens)
print("3. Sin stop words:", palabras_filtradas)