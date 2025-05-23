import pandas as pd

# Function to upload books from excel
def cargar_desde_excel(archivo="libros.xlsx"): #Here we named the function and called from excel
    try: #Here we said try the next block
        df = pd.read_excel(archivo) #If we found the excel's book then
        return df #We return the data frame
    except FileNotFoundError: #else
        print("No se encontró el archivo. Se creará uno nuevo al guardar.") #Print an error and say we're going to created a new excel book
        return pd.DataFrame(columns=["título", "autor", "género", "año", "disponible", "reposicion"]) #With these columns

# Function to save books on excel
def guardar_en_excel(df, archivo="libros.xlsx"): #Here we are going to define a function for saving new data on the excel book
    df.to_excel(archivo, index=False) #we save the dataframe in a excel book in the way "archivo", and we said we don't need a extra default column
    print(f"\nDatos guardados correctamente en '{archivo}'.") #We print a message about a data successfully save on the excel book

# --- Function to saving a book on excel ---
def agregar_libro(df): #We define a new function for saving a book on the dataframe
    titulo = input("Digite el título del libro: ").upper() #We asked for a new book title
    if titulo in df["título"].values: #We search if the book is already existing on excel
        print("¡Error! El título ya existe.") #If it existed we send a error
    else: #else the book doesn't exist
        autor = input("Digite el nombre del autor: ").upper() #we ask for the autor
        año = int(input("Digite el año de publicación del libro: ")) #the year of publication
        if año >= 1800 and año <= 2024: #And we validate the year before asking for another thing
            disponible = int(input("¿Cuántos libros hay disponibles? ")) #if the year is correct we ask for the other parameter (availability)
            if disponible >= 0: #We validate if availability is correct, then
                reposicion = float(input("¿Cuánto es la reposición? ")) # we ask for the amount of reposition
                if reposicion > 50: # If reposition is bigger than 50 pesos, then
                    nuevo_libro = { #We saved on the excel book
                        "título": titulo,
                        "autor": autor,
                        "género": input("Digite el género del libro: ").upper(),
                        "año": año,
                        "disponible": disponible,
                        "reposicion": reposicion
                    }
                    df = df._append(nuevo_libro, ignore_index=True) #Then we added the new libro to the data frame
                    guardar_en_excel(df) #We upload on excel
                    print(f"Libro '{titulo}' agregado correctamente.") #And we send a successfull message 
                else:
                    print("La reposición debe tener un valor mayor a 50 pesos") #if is not bigger than 50 pesos, we send an error 
            else:
                print("¡Error! La disponibilidad del libro debe ser mayor a 0.") #If availability is not correct, we send an error
        else:
            print("¡Error! El año de publicación debe estar entre 1800 y 2024.") #If the validation of year is not successful we send an error
    
    return df #We return the dataframe for uploading

# --- Function for removing a book ---
def eliminar_libro(df): #We define the name of the function and the parameter that is on the dataframe
    titulo = input("¿Qué libro desea eliminar? (Título del libro): ").upper() #We ask for the book's name 
    if titulo in df["título"].values: #If it does exist we first have to know if the user is sure about the desicion
        seguro: str = str(input("¿Está seguro que desea eliminar el libro? ")).upper() #We ask for it
        if seguro in ["SÍ", "SI"]: #If the user is sure
            df = df[df["título"] != titulo] #We remove the book from the excel's book
            guardar_en_excel(df) #We upload on excel
            print(f"Libro '{titulo}' eliminado correctamente.") #And we print a message of successful
        else:
            print(f"Libro '{titulo}' no ha sido eliminado.") #If the user is not sure about it, we don't remove the book and we send a message
    else:
        print("¡Error! Libro no encontrado.") #But if the book doesn't exist, we send a error message
    return df #And we return the dataframe for uploading it

# --- Function for searching a book ---
def buscar_libro(df): #We defined the name of the function and it will be works on the dataframe
    opcion: str  = str(input("¿Desea buscar por nombre (TÍTULO) o por autor (AUTOR)? ")).upper() #We ask if the user wish to search with title or author
    if opcion in ["TÍTULO", "TITULO"]: #If is by title
        titulo = input("Digite el título del libro: ").upper() #We ask for the title
        libro = df[df["título"] == titulo] #And we search with it
    elif opcion in ["AUTOR"]: #If is by author
        autor = input("Digite el nombre del autor: ").upper() #We ask for the author
        libro = df[df["autor"] == autor] #And we search with it
    else:
        print("Opción no válida.") #If user doesn't write well, we send an error
        return #And we return to the menu
    
    if libro.empty: #If the book doesn't exist
        registro:str = str(input("Libro no encontrado. ¿Desea registrarlo? ")).upper() #We return the message and we ask if the user want to record the book
        if registro in ["SÍ", "SI"]: #If user said yes
            agregar_libro(df) #We go to function that add the new book
        else:
            return #Else, we go to menu
    else:
        print(libro) #if it does exist we print the information
    
# --- Function to see the total cost ---
def ver_costos(df): #We defined the name and say where we are going to work
    total:float = 0 #We start with the total cost in zero
    for _, libro in df.iterrows(): #We roam on the excel's book in each row
        subtotal:float = float(libro["disponible"] * libro["reposicion"]) #subtotal is the var that is going to multiply the available count and the count of replacement
        print(f"{libro['título']}: {subtotal} pesos") #we are going to print every book's  subtotal
        total += subtotal #And we add up to total
    print(f"\nCosto total de reposición de todos los libros: {total} pesos") #And we print the total

# we upload the books from the excel's book
df_libros = cargar_desde_excel()

# Menu
while True: #We are going to execute the menu 
    print("¡Bienvenido de nuevo!")
    menu = input("¿Qué deseas hacer hoy? \nPara buscar un libro: B \nPara eliminar un libro: E\nPara registrar un nuevo libro: R \nPara ver costos totales: C\nPara salir: S\n")
    
    if menu.upper() == "B": #Is user want to search
        buscar_libro(df_libros) #We call the function for searching
    elif menu.upper() == "E": #If user want to errase a book
        df_libros = eliminar_libro(df_libros) #We call the function for errasing
    elif menu.upper() == "R": #if user want to add new books
        df_libros = agregar_libro(df_libros) #We call the function for registering
    elif menu.upper() == "C": #If user said that want to see the costs
        ver_costos(df_libros) #We call the function for costs
    elif menu.upper() == "S": #If the user want to scape 
        guardar_en_excel(df_libros) #We save all we did
        break #And close the program
    else:
        print("Opción no válida.") #Error message if user doesn't write a correct answer


