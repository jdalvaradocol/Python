import tkinter as tk

class interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Interfaz Interactiva")
        self.ventana.geometry("700x150")
        self.ventana.configure(bg="#f0f0f0")
        
        # 1. Crear el cuadro de texto (Entry)
        self.contenedor = tk.Frame(self.ventana, bg="#f0f0f0", pady=15)
        self.contenedor.pack()
        
        tk.Label(self.contenedor, text="Estado:", font=("Arial", 24, "bold"), bg="#f0f0f0").grid(row=0, column=0, padx=5)
        
        self.cuadro_texto = tk.Entry(self.contenedor, font=("Arial", 24), width=30)
        self.cuadro_texto.insert(0, "Ningún botón presionado") # Texto inicial
        self.cuadro_texto.grid(row=0, column=1, padx=5)
        
        # 2. Crear el contenedor para los botones
        self.panel_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        self.panel_botones.pack(pady=5)
        
        # Botón 1
        self.btn_uno = tk.Button(
            self.panel_botones, 
            text="Botón 1", 
            font=("Arial", 24, "bold"),
            bg="#F38021", 
            fg="white", 
            command=self.accion_boton_1
        )
        self.btn_uno.grid(row=0, column=0, padx=10)
        
        # Botón 2
        self.btn_dos = tk.Button(
            self.panel_botones, 
            text="Botón 2", 
            font=("Arial", 24, "bold"),
            bg="#4CAF50", 
            fg="white", 
            command=self.accion_boton_2
        )
        self.btn_dos.grid(row=0, column=1, padx=10)
        
    def accion_boton_1(self):
        """Borra el cuadro de texto y escribe que se presionó el Botón 1."""
        self.cuadro_texto.delete(0, tk.END)  # Limpia el texto anterior
        self.cuadro_texto.insert(0, "¡Presionaste el Botón 1!") # Inserta el nuevo texto  
        
    def accion_boton_2(self):
        """Borra el cuadro de texto y escribe que se presionó el Botón 2."""
        self.cuadro_texto.delete(0, tk.END)  # Limpia el texto anterior
        self.cuadro_texto.insert(0, "¡Presionaste el Botón 2!") # Inserta el nuevo texto          
        
# Ejecución de la aplicación

root = tk.Tk()
app = interfaz(root)
root.mainloop()