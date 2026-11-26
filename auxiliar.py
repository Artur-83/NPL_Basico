import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo(
        titulo:str = "Selecciona un archivo",
        tipos_archivo: list[tuple[str, str]] | None = None,
) -> str | None:
    """Abre el explorador de archivos para seleccionar un archivo (no una carpeta) y devuelve su ruta como cadena de texto.Si se cancela devuelve None."""

    root = tk.Tk()
    root.withdraw() #Oculta la ventana principal vacía de tkinter
    root.attributes("-topmost", True) #Trae el diálogo al frente

    if tipos_archivo is None:
        tipos_archivo = [("Todos los archivos","*.*")]

    ruta = filedialog.askopenfilename(
        title=titulo,
        filetypes = tipos_archivo,
    )
    root.destroy() #Libera los recursos de la ventana oculta

    return ruta if ruta else None

if __name__ == "__main__":
    # Ejemplo de uso de filtraciones por extensiones
    archivo = seleccionar_archivo(
        titulo="Elige un documento o tabla",
        tipos_archivo = [
            ("Archivos CSV y Exel", "*.csv;*.xlsx"),
            ("Imágenes", "*png*.jpg*.jpeg"),
            ("Todos los archivos", "*.*")
        ]
    )

    if archivo:
        print(f"Archivo seleccionado: {archivo}")
    else:
        print("No se seleccionó ningún archivo.")


def cargar_texto(ruta: str) -> str:
    """Carga el contenido de la ruta del archivo que seleccionaste"""
    with open(ruta, "r") as file:
        texto = file.read()
    return texto