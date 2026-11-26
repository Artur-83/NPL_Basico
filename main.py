from auxiliar import seleccionar_archivo
from auxiliar import cargar_texto

from Reporte import generar_reporte


def main():

    ruta = seleccionar_archivo(
        titulo="Seleccione el archivo de texto",
        tipos_archivo=[
            ("Archivos de texto", "*.txt")
        ]
    )

    if ruta:

        texto = cargar_texto(ruta)

        generar_reporte(texto)

    else:

        print("No se seleccionó ningún archivo.")


if __name__ == "__main__":
    main()