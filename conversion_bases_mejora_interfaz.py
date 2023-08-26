# Importamos la biblioteca tkinter para la interfaz gráfica
import tkinter as tk

# Definimos la función que se encargará de la conversión de bases
def convert_base():
    # Obtenemos los valores ingresados por el usuario
    num = num_entry.get()
    from_base = int(from_base_entry.get())
    to_base = int(to_base_entry.get())

    # Separamos la parte entera y decimal del número
    integer_part, _, decimal_part = num.partition('.')

    # Inicializamos la variable que almacenará el resultado de la parte entera
    integer_result = ''
    integer_part = int(integer_part, from_base)
    while integer_part > 0:
        remainder = integer_part % to_base
        if 0 <= remainder <= 9:
            integer_result = str(remainder) + integer_result
        else:
            integer_result = chr(ord('A') + remainder - 10) + integer_result
        integer_part //= to_base

    # Inicializamos la variable que almacenará el resultado de la parte decimal
    decimal_result = ''
    decimal_value = 0
    for i, digit in enumerate(decimal_part):
        if '0' <= digit <= '9':
            val = int(digit)
        else:
            val = ord(digit.upper()) - ord('A') + 10
        decimal_value += val * (from_base ** -(i + 1))

    # Limitamos a 5 decimales
    for _ in range(5):
        decimal_value *= to_base
        digit = int(decimal_value)
        if 0 <= digit <= 9:
            decimal_result += str(digit)
        else:
            decimal_result += chr(ord('A') + digit - 10)
        decimal_value -= digit

    # Mostramos el resultado en la etiqueta correspondiente
    result = integer_result + '.' + decimal_result
    result_label.config(text=f"Resultado: {result}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Conversor de Bases")
root.geometry("500x400")
root.configure(bg='#FFFFFF')

# Etiquetas y campos de texto
num_label = tk.Label(root, text="Número:", font=('Poppins', 14), bg='#FFFFFF')
num_label.place(x=100, y=50)
num_entry = tk.Entry(root, font=('Poppins', 14), width=20)
num_entry.place(x=220, y=50)

from_base_label = tk.Label(root, text="Base original:", font=('Poppins', 14), bg='#FFFFFF')
from_base_label.place(x=100, y=100)
from_base_entry = tk.Entry(root, font=('Poppins', 14), width=20)
from_base_entry.place(x=220, y=100)

to_base_label = tk.Label(root, text="Base a convertir:", font=('Poppins', 14), bg='#FFFFFF')
to_base_label.place(x=100, y=150)
to_base_entry = tk.Entry(root, font=('Poppins', 14), width=20)
to_base_entry.place(x=250, y=150)

# Botón para realizar la conversión
convert_button = tk.Button(root, text="Convertir", command=convert_base, font=('Poppins', 14), bg='#007BFF', fg='#FFFFFF', relief='solid', borderwidth=1, highlightthickness=0, bd=0, padx=20, pady=10, border=0)
convert_button.place(x=220, y=200)
convert_button.config(highlightbackground='#007BFF', highlightcolor= "#007BFF")

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Resultado:", font=('Poppins', 14), bg='#FFFFFF')
result_label.place(x=220, y=250)

# Iniciamos el bucle principal de la aplicación
root.mainloop()
