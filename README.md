#Sistema de Gestión de Libros con Excel
Este proyecto en Python permite gestionar una pequeña base de datos de libros almacenada en un archivo Excel (libros.xlsx). Está pensado como una herramienta sencilla para registrar, consultar y mantener actualizada una colección de libros.

🔧 Funcionalidades actuales
Cargar libros desde Excel: Lee el archivo libros.xlsx si existe, o crea un nuevo DataFrame vacío si no se encuentra.

Guardar libros en Excel: Guarda el DataFrame con la información de libros en un archivo Excel.

Agregar un nuevo libro: Permite registrar un nuevo libro si su título no está repetido.

📁 Estructura del archivo libros.xlsx
El archivo contiene las siguientes columnas:

título: Título del libro (en mayúsculas).

autor: Nombre del autor (en mayúsculas).

género: Género del libro (en mayúsculas).

año: Año de publicación (entero).

disponible: Cantidad de libros disponibles (entero).

reposicion: Costo de reposición por unidad (decimal).

🚀 Cómo usar
Asegúrate de tener instalado Python 3.x.

Instala la biblioteca pandas y openpyxl si no la tienes:

bash
Copiar
Editar
pip install pandas openpyxl
Guarda el script en un archivo, por ejemplo, gestor_libros.py.

Ejecuta el script:

bash
Copiar
Editar
python gestor_libros.py
Usa la función agregar_libro(df) para añadir libros. Asegúrate de tener cargado previamente el DataFrame con cargar_desde_excel().

📝 Ejemplo de uso
python
Copiar
Editar
df_libros = cargar_desde_excel()
df_libros = agregar_libro(df_libros)
guardar_en_excel(df_libros)
⚠️ Notas
El sistema evita agregar libros duplicados comparando títulos.

Todos los textos se almacenan en mayúsculas para mantener uniformidad.

El archivo Excel se actualiza cada vez que se guarda el DataFrame.

📌 Requisitos
Python 3.6 o superior

pandas

openpyxl (para manejar archivos .xlsx)
