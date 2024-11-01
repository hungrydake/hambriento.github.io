import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mensaje para Mi Novia")
root.geometry("400x200")
root.configure(bg='lightpink')

# Mensaje especial
mensaje = "¡Eres la luz de mi vida! 🌟\nSiempre estoy pensando en ti.\nTe amo mucho tigrsitop ❤️"

# Función para mostrar el mensaje
def mostrar_mensaje():
    etiqueta_mensaje.config(text=mensaje)

# Crear una etiqueta para el mensaje
etiqueta_mensaje = tk.Label(root, text="", bg='lightpink', font=("Helvetica", 14))
etiqueta_mensaje.pack(pady=20)

# Botón para mostrar el mensaje
boton_mostrar = tk.Button(root, text="holap", command=mostrar_mensaje, bg='white', font=("Helvetica", 12))
boton_mostrar.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()