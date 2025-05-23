
# 📚 Book Management System with Excel

This Python project allows you to manage a small book database stored in an Excel file (`libros.xlsx`). It's designed as a simple tool to register, view, and maintain a collection of books.

## 🔧 Current Features

- **Load books from Excel**: Reads the `libros.xlsx` file if it exists, or creates a new empty DataFrame if not found.
- **Save books to Excel**: Saves the DataFrame with book information into an Excel file.
- **Add a new book**: Lets you register a new book, as long as the title does not already exist.

## 📁 Excel File Structure

The Excel file contains the following columns:

- `título`: Book title (in uppercase).
- `autor`: Author name (in uppercase).
- `género`: Genre (in uppercase).
- `año`: Year of publication (integer).
- `disponible`: Number of copies available (integer).
- `reposicion`: Replacement cost per copy (float).

## 🚀 How to Use

1. Make sure you have Python 3.x installed.
2. Install the required libraries if you haven't already:
   ```bash
   pip install pandas openpyxl
   ```
3. Save the script to a file, for example, `book_manager.py`.
4. Run the script:
   ```bash
   python book_manager.py
   ```
5. Use the `agregar_libro(df)` function to add books. Make sure to first load the DataFrame using `cargar_desde_excel()`.

## 📝 Usage Example

```python
df_books = cargar_desde_excel()
df_books = agregar_libro(df_books)
guardar_en_excel(df_books)
```

## ⚠️ Notes

- The system prevents duplicate books by checking if the title already exists.
- All text entries are stored in uppercase for consistency.
- The Excel file is updated every time the DataFrame is saved.

## 📌 Requirements

- Python 3.6 or higher
- pandas
- openpyxl (for handling `.xlsx` files)
