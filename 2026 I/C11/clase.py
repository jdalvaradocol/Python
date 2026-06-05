import tkinter as tk
import math

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x300")
        
        # 1. Variables para manejar el estado de la calculadora
        self.valor_entero    = 0   # Acumula la parte entera del número que se está ingresando
        self.valor_decimal   = 0   # Acumula la parte decimal del número que se está ingresando
        self.index_decimal   = 10  # Para calcular la posición decimal (10, 100, 1000, etc.)
        self.caso            = 0   # 0: ingresando primer número, 1: operador seleccionado, esperando segundo número
        self.valor_operador  = ""  # Almacena el operador seleccionado (+, -, x, /)
        self.decimal         = 0   # Indica si se ha presionado el punto decimal (0: no, 1: sí)    
        self.valor_operadorA = 0   # Almacena el primer número ingresado antes de seleccionar un operador
        self.valor_operadorB = 0   # Almacena el segundo número ingresado después de seleccionar un operador   
        
        self.texto_pantalla = tk.StringVar()    # Variable de control para el texto que se muestra en la pantalla de la calculadora
        self.texto_pantalla.set("")            # Inicializa la pantalla con ""
        
        # 2. Crear la pantalla de salida de la calculadora
        self.pantalla = tk.Label(
            self.ventana, 
            textvariable=self.texto_pantalla, 
            font=("Arial", 14, "bold"), 
            bg="#ffffff", 
            relief="sunken", 
            bd=2,
            height=2
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
        
    # 3. Función: Crea los botones de la calculadora y los coloca en la ventana. 
        self.crear_botones()

    def crear_botones(self):
        salida = ['7', '8', '9', '/', '4', '5', '6', 'x', '3', '2', '1', '+', '0', '.', '=', '-']
        contador = 0
        
        for fila in range(1, 5):         
            for columna in range(4):     
                numero = salida[contador]  
                
                # Al estar dentro de una clase, llamamos al método con self.boton_presionado
                btn = tk.Button(
                    self.ventana, 
                    text=f"{numero}", 
                    command=lambda n=numero: self.boton_presionado(n),
                    width=10,
                    height=2
                )
                btn.grid(row=fila, column=columna, padx=5, pady=5)
                contador += 1 

        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)

    # 4. MÉTODO: Procesa el botón. 
    def boton_presionado(self, valor):
        
        valor_total = self.valor_entero + self.valor_decimal
        print(f"Valor numérico actual en total: {valor_total}")

        if valor == "=":
            
            valor_operadorB = valor_total
            
            if self.valor_operador == '+':
                resultado = self.valor_operadorA + valor_operadorB      
            elif self.valor_operador == '-':
                resultado = self.valor_operadorA - valor_operadorB  
            elif self.valor_operador == 'x':
                resultado = self.valor_operadorA * valor_operadorB  
            elif self.valor_operador == '/':
                if valor_operadorB != 0:
                    resultado = self.valor_operadorA / valor_operadorB  
                else:
                    self.texto_pantalla.set("Error: División por cero")
                    return
            
            self.texto_pantalla.set(f"{self.valor_operadorA} {self.valor_operador} {valor_operadorB} = {resultado}")
            
            self.valor_entero = 0
            self.valor_decimal = 0  
            self.caso = 0
            self.valor_operador = ""
            self.valor_operadorA = 0
            self.valor_operadorB = 0
            self.index_decimal = 10
    
            return 
            
        elif valor in ['+', '-', 'x', '/']:
            
            self.valor_operador = valor
            self.caso = 1
            self.valor_entero = 0
            self.valor_decimal = 0
            self.decimal = 0
            self.index_decimal = 10
            self.valor_operadorA = valor_total

            self.texto_pantalla.set(f"{self.valor_operadorA} {self.valor_operador}")
            return
            
        elif valor == '.':
            self.decimal = 1
            
            if self.caso == 0:        
                self.texto_pantalla.set(f"{int(valor_total)}.")
            elif self.caso == 1:        
                self.texto_pantalla.set(f"{self.valor_operadorA} {self.valor_operador} {int(valor_total)}.")

            return

        numero = int(valor)

        if self.decimal == 1:
            self.valor_decimal += (numero / self.index_decimal) 
            valor_total = self.valor_entero + self.valor_decimal
            self.index_decimal *= 10
        else:
            self.valor_entero = (self.valor_entero * 10) + numero
            valor_total = self.valor_entero
        
        print(f"Valor entero: {self.valor_entero}, Valor decimal: {self.valor_decimal}")

        if self.decimal == 1:
            digitos_decimales = int(math.log10(self.index_decimal)) - 1
            texto_num = f"{valor_total:.{digitos_decimales}f}"
        else:
            texto_num = f"{int(valor_total)}"

        if self.caso == 0:        
            self.texto_pantalla.set(texto_num)
        elif self.caso == 1:        
            self.texto_pantalla.set(f"{self.valor_operadorA} {self.valor_operador} {texto_num}")

# main loop
# estructura principal del programa, se ejecuta al iniciar el programa
root = tk.Tk()
mi_app = Calculadora(root) 
root.mainloop()
