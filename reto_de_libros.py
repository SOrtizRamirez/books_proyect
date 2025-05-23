import pandas as pd

# Función para cargar libros desde el archivo Excel
def cargar_desde_excel(archivo="libros.xlsx"):
    try:
        df = pd.read_excel(archivo)
        return df
    except FileNotFoundError:
        print("No se encontró el archivo. Se creará uno nuevo al guardar.")
        return pd.DataFrame(columns=["título", "autor", "género", "año", "disponible", "reposicion"])

# Función para guardar libros en el archivo Excel
def guardar_en_excel(df, archivo="libros.xlsx"):
    df.to_excel(archivo, index=False)
    print(f"\nDatos guardados correctamente en '{archivo}'.")

# --- Función para agregar un nuevo libro ---
def agregar_libro(df):
    titulo = input("Digite el título del libro: ").upper()
    if titulo in df["título"].values:
        print("¡Error! El título ya existe.")
    else:
        autor = input("Digite el nombre del autor: ").upper()
        año = int(input("Digite el año de publicación del libro: "))
        disponible = int(input("¿Cuántos libros hay disponibles? "))
        reposicion = float(input("¿Cuánto es la reposición? "))

        nuevo_libro = {
            "título": titulo,
            "autor": autor,
            "género": input("Digite el género del libro: ").upper(),
            "año": año,
            "disponible": disponible,
            "reposicion": reposicion
        }
        df = df.append(nuevo_libro, ignore_index=True)
        print(f"Libro '{titulo}' agregado correctamente.")
    
    return df