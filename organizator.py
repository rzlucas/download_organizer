import os
import shutil

def organizar_descargas():
    # Lista de carpetas a organizar
    carpetas_descargas = [os.path.join(os.path.expanduser("~"), "Downloads")]
    # Agrega otras rutas si es necesario
    carpetas_descargas.append("D:\\Descargas")  

    subcarpetas = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Vídeos": [".mp4", ".mov", ".avi"],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z"],
        "Otros": []
    }

    for carpeta_descargas in carpetas_descargas:
        if not os.path.exists(carpeta_descargas):
            print(f"La carpeta de Descargas no existe: {carpeta_descargas}")
            continue

        for archivo in os.listdir(carpeta_descargas):
            ruta_archivo = os.path.join(carpeta_descargas, archivo)

            # Verifica si es un archivo
            if os.path.isfile(ruta_archivo):
                extension = os.path.splitext(archivo)[1].lower()
                movido = False

                # Intenta mover el archivo a la subcarpeta correspondiente
                for subcarpeta, extensiones in subcarpetas.items():
                    if extension in extensiones:
                        carpeta_destino = os.path.join(carpeta_descargas, subcarpeta)
                        os.makedirs(carpeta_destino, exist_ok=True)
                        try:
                            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                            print(f"Movido: {archivo} -> {carpeta_destino}")
                            movido = True
                            break
                        except Exception as e:
                            print(f"Error al mover {archivo}: {e}")

                # Si no coincide con ninguna extensión, va a la carpeta "Otros"
                if not movido:
                    carpeta_destino = os.path.join(carpeta_descargas, "Otros")
                    os.makedirs(carpeta_destino, exist_ok=True)
                    try:
                        shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                        print(f"Movido a 'Otros': {archivo}")
                    except Exception as e:
                        print(f"Error al mover {archivo} a 'Otros': {e}")

if __name__ == "__main__":
    organizar_descargas()
