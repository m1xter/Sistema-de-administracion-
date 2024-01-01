import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
#operaciones
class sistema_de_monedas():
    #procura tener el constructor siempre de primero es menos confuso asi
    def __init__(self):  
        self.resultado = 0
        self.ventana = tk.Tk()
        self.ventana.title('Conversor de Moneda')
        self.ventana.geometry("")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.config(relief="groove")
        self.ventana.resizable(width=0, height=0)

        
        
        #FRAME CUADRO LATERAL DE COLOR
        frame_izq = tk.Frame(self.ventana, bd=0, width=10, relief=tk.SOLID, bg='#0040FF')
        frame_izq.pack(side='left', expand=tk.NO,fill=tk.BOTH)
        
        #FRAME FORMULARIO TOTAL
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side='right', expand=tk.YES,fill=tk.BOTH)
        
        #FRAME DE FORMULARIO TOTAL PARA TITULO
        frame_form_top = tk.Frame(frame_form, height = 40, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top",fill=tk.X)

        #titulo
        title = tk.Label(frame_form_top, text='Conversor de Moneda', font=('Arial', 24), fg="white", bg="#0040FF", pady=5)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        
        #FRAME DE FORMULARIO TOTAL PARA RELLENADO DE DATOS

        frame_form_fill = tk.Frame(frame_form, width=390, height = 360, bd=0, relief=tk.SOLID, bg='white')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        
        #-----------------------------------------------------------------------
        
        #FUNCIONES A MOSTRAR EN PANTALLA
        self.ingreso_cantidad(frame_form_fill)
        self.on_select(frame_form_fill)
        self.combo2(frame_form_fill)
        self.etiqueta_tasa(frame_form_fill)
        self.etiqueta_resultado(frame_form_fill)
        self.boton_resultado(frame_form_fill)
        
        self.ventana.mainloop()


     
    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)
    

    #AQUI EMPEZAMOS A CREAR DICHAS FUNCIONES
        
    def ingreso_cantidad(self, frame_form_fill):
        #TEXTO: INGRESE CANTIDAD
        self.etiqueta_divisa1 = tk.Label(frame_form_fill,text='Ingrese la Cantidad de Dinero a Convertir ', font=('Arial, 12'), bg="#fff", fg="black", anchor="w")
        self.etiqueta_divisa1.pack()
        self.etiqueta_divisa1.place(x=20,y=10)
        
        #CASILLA PARA INGRESAR CANTIDAD
        self.cant = ttk.Entry(frame_form_fill, font=('Arial', 10))
        self.cant.pack()
        self.cant.place(x=20,y=40)
                   
        #COMBOBOX DE DIVISA INICIAL
    def on_select(self, frame_form_fill):            
        def selected(event):
            self.combobox2.set("")
            self.combobox2.config(values=self.opciones[self.combobox1.get()])
        self.opciones = {"BS": ("COP", "USD"),"COP": ("BS", "USD"),"USD": ("BS", "COP")}  
        self.combobox1 = ttk.Combobox(frame_form_fill,width="10", state="readonly", values=tuple(self.opciones.keys()))
        self.combobox1.bind("<<ComboboxSelected>>",selected)
        self.combobox1.pack()
        self.combobox1.place(x=200,y=40)
            
    
        
    def combo2(self,frame_form_fill):
        #TEXTO: A QUE DIVISA CONVERTIR?
        self.etiqueta_divisa2 = tk.Label(frame_form_fill,text='¿A que moneda lo quieres convertir?: ', font=('Arial, 12'), bg="#fff", fg="black", anchor="w")
        self.etiqueta_divisa2.pack()
        self.etiqueta_divisa2.place(x=20,y=80)
        
        #COMBOBOX PARA LA DIVISA A CONVERTIR
        self.combobox2 = ttk.Combobox(frame_form_fill,width="10", state="readonly")
        self.combobox2.pack(side="top",fill=tk.X)
        self.combobox2.place(x=20,y=110)
            
            
    
    def etiqueta_tasa(self,frame_form_fill):
        #TEXTO: INGRESE LA TASA DE CAMBIO
        self.etiqueta_tasa = tk.Label(frame_form_fill,text="Ingrese la tasa de cambio de hoy: ", font=('Arial, 12'), bg="#fff", fg="black", anchor="w")
        self.etiqueta_tasa.pack()
        self.etiqueta_tasa.place(x=20,y=160)
        
        #CASILLA PARA INGRESAR LA TASA DE CAMBIO
        self.tasa = ttk.Entry(frame_form_fill,font=('Times', 10))
        self.tasa.pack()
        self.tasa.place(x=20,y=190)
    
    #FUNCION PARA MOSTRAR LOS RESULTADOS
    def etiqueta_resultado(self,frame_form_fill):   
        self.etiqueta_resultado = tk.Label(frame_form_fill, font=('Arial, 12'), bg="#fff", fg="black", anchor="w")
        self.etiqueta_resultado.pack()
        self.etiqueta_resultado.place(x=120,y=250)


    #FUNCION DE LAS OPERACIONES MATEMATICAS
    def cambio_valores(self,frame_form_fill):
        self.cantidad  = float(self.cant.get())
        self.tasa_cambio  = float(self.tasa.get())
        self.divisa1 = self.combobox1.get()
        self.divisa2 = self.combobox2.get()
        
        
        #CONDICIONES
        if self.divisa1 == "BS" and self.divisa2 == "COP":
            self.resultado = self.cantidad * self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"
            
        if self.divisa1 == "BS" and self.divisa2 == "USD":
            self.resultado = self.cantidad / self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"
            
        if self.divisa1 == "COP" and self.divisa2 == "BS":
            self.resultado = self.cantidad / self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"
            
        if self.divisa1 == "COP" and self.divisa2 == "USD":
            self.resultado = self.cantidad / self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"

        if self.divisa1 == "USD" and self.divisa2 == "BS":
            self.resultado = self.cantidad * self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"

        if self.divisa1 == "USD" and self.divisa2 == "COP":
            self.resultado = self.cantidad * self.tasa_cambio
            self.etiqueta_resultado["text"] = f"{round(self.resultado, 2)}  {str(self.divisa2)}"


    #aqui llamamos a la funcion que hace la operacion
    def boton_resultado(self,frame_form_fill):
        #boton:
        self.Boton = tk.Button(frame_form_fill,text="Procesar Datos", font=('Arial', 15), bg= '#0040FF', bd=0, fg="#fff", command= lambda  : self.cambio_valores(frame_form_fill) )
        self.Boton.pack(side="top",fill=tk.X)
        self.Boton.place(x=120,y=290)


     
