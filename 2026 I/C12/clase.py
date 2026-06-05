from ast import If
import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CalculadoraSeñales:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Señales (NumPy)")
        self.ventana.geometry("800x500")
        self.ventana.configure(bg="#f5f5f5")
        
        # Estado de la calculadora
        self.parametro_activo = "Amplitud" # Controla dónde escriben los botones
        
        # --- 1. PANEL IZQUIERDO: Interfaz Estilo Calculadora ---
        panel_izquierdo = tk.Frame(self.ventana, bg="#f5f5f5", padx=10, pady=10)
        panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)
        
        # Pantallas de lectura para los parámetros
        tk.Label(panel_izquierdo, text="Configurar Señal", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=5)
        
        # Variables de control de Tkinter
        self.txt_amplitud = tk.StringVar(value="1")
        self.txt_frecuencia = tk.StringVar(value="2")
        
        # Botones selectores que actúan como "pantalla" interactiva
        self.btn_sel_amp = tk.Button(
                                        panel_izquierdo, 
                                        textvariable=self.txt_amplitud,
                                        font=("Arial", 14, "bold"), 
                                        bg="#e0e0e0", 
                                        bd=2, 
                                        relief="groove", 
                                        command=lambda: self.cambiar_foco("Amplitud")
                                    )
        self.btn_sel_amp.pack(fill=tk.X, pady=2)
        tk.Label(panel_izquierdo, text="↑ Amplitud (A) ↑", font=("Arial", 9, "italic"), bg="#f5f5f5", fg="#666").pack()
        
        self.btn_sel_frec = tk.Button(
                        panel_izquierdo, 
                        textvariable=self.txt_frecuencia, 
                        font=("Arial", 14, "bold"), 
                        bg="#ffffff", bd=2, 
                        relief="groove", 
                        command=lambda: self.cambiar_foco("Frecuencia")
            )
        self.btn_sel_frec.pack(fill=tk.X, pady=2)
        tk.Label(panel_izquierdo, text="↑ Frecuencia (Hz) ↑", font=("Arial", 9, "italic"), bg="#f5f5f5", fg="#666").pack(pady=(0, 10))
        
        # Teclado de la Calculadora
        panel_botones = tk.Frame(panel_izquierdo, bg="#f5f5f5")
        panel_botones.pack()
        
        botones = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', 'C',
            '='
        ]
        
        fila = 0
        columna = 0
        for boton in botones:
            # Estilos dinámicos para los botones especiales
            if boton == '=':
                btn = tk.Button(
                    panel_botones, 
                    text=boton, 
                    font=("Arial", 12, "bold"), 
                    bg="#191CE6", fg="white", 
                    width=18, 
                    height=2, 
                    command=self.graficar_senal
                    )
                btn.grid(row=fila, column=columna, columnspan=3, padx=3, pady=3)
                break
            elif boton == 'C':
                btn = tk.Button(
                    panel_botones, 
                    text=boton, 
                    font=("Arial", 12, "bold"), 
                    bg="#94e925", 
                    fg="white", 
                    width=5, 
                    height=2, 
                    command=self.limpiar_parametro)
            else:
                btn = tk.Button(
                    panel_botones, 
                    text=boton, 
                    font=("Arial", 12), 
                    width=5, 
                    height=2, 
                    command=lambda b=boton: self.digito_presionado(b)
                    )
                
            btn.grid(row=fila, column=columna, padx=3, pady=3)
            columna += 1
            if columna > 2:
                columna = 0
                fila += 1
                
        # Resaltar visualmente el parámetro activo al iniciar
        self.cambiar_foco("Amplitud")

        # --- 2. PANEL DERECHO: Gráfica de Matplotlib ---
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.ejes = self.figura.add_subplot(111)
        self.configurar_ejes()
        
        self.canvas_matplotlib = FigureCanvasTkAgg(self.figura, master=self.ventana)
        self.canvas_matplotlib.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Graficar señal inicial
        self.graficar_senal()

    def configurar_ejes(self):
        self.ejes.grid(True, linestyle='--', alpha=0.6)
        self.ejes.set_xlabel("Tiempo (segundos)", fontsize=10)
        self.ejes.set_ylabel("Voltaje / Amplitud", fontsize=10)
        self.ejes.axhline(0, color='black', linewidth=1)

    def cambiar_foco(self, destino):
        """Cambia el parámetro que recibirá los números del teclado."""
        self.parametro_activo = destino
        if destino == "Amplitud":
            self.btn_sel_amp.configure(bg="#b3d4fc") # Azul claro indicador
            self.btn_sel_frec.configure(bg="#ffffff")
        else:
            self.btn_sel_frec.configure(bg="#b3d4fc")
            self.btn_sel_amp.configure(bg="#ffffff")

    def digito_presionado(self, digito):
        """Suma caracteres al parámetro activo, emulando la calculadora original."""
        if self.parametro_activo == "Amplitud":
            variable_actual = self.txt_amplitud 
        else:
            variable_actual = self.txt_frecuencia
        valor_viejo = variable_actual.get()
        
        # Evitar ceros a la izquierda innecesarios o múltiples puntos
        if valor_viejo == "0" and digito != ".":
            variable_actual.set(digito)
        elif digito == "." and "." in valor_viejo:
            return
        else:
            variable_actual.set(valor_viejo + digito)

    def limpiar_parametro(self):
        if self.parametro_activo == "Amplitud":
            self.txt_amplitud.set("0")
        else:
            self.txt_frecuencia.set("0")

    def graficar_senal(self):
        """Toma los datos numéricos acumulados y ejecuta la matemática vectorial de NumPy."""
        try:
            A = float(self.txt_amplitud.get())
            f = float(self.txt_frecuencia.get())
        except ValueError:
            return # Previene errores si los campos quedan vacíos o mal escritos

        # Vectores con numpy:
        # Generamos un vector de tiempo continuo 't' que va de 0 a 1 segundo con 1000 muestras
        if f > 5:
            t = np.linspace(0, 1, 1000*int(f))  # Aumentamos la resolución proporcional a la frecuencia para curvas suaves
        else:
            t = np.linspace(0, 5/f, 1000)       # Resolución estándar para frecuencias bajas
            
        # Calculamos toda la onda senoidal simultáneamente en un solo paso matemático
        y = A * np.sin(2 * np.pi * f * t)
        
        # Renderizado en Matplotlib
        self.ejes.clear()
        self.configurar_ejes()
        self.ejes.set_title(f"Señal: {A} · sin(2π · {f}Hz · t)", fontsize=11, fontweight='bold', color='#1a1a1a')
        
        # Dibujamos la señal procesada por NumPy
        self.ejes.plot(t, y, color="#2196F3", linewidth=2.5)
        
        # Ajustamos los límites automáticos para que la gráfica siempre se encuadre de forma estética
        self.ejes.set_xlim([0, (1/f) * 5]) # Mostrar al menos 5 ciclos de la señal
        if A != 0:
            self.ejes.set_ylim([-A * 1.2, A * 1.2])
            
        self.canvas_matplotlib.draw()

root = tk.Tk()
app = CalculadoraSeñales(root)
root.mainloop()