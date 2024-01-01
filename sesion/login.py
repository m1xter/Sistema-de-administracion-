from tkinter import *
from tkinter import messagebox
from util.generic import *
from .registro_usuario import registro_usuario
from sql.motor_inicio import *
from sql.controlador import Controlador
from sql.motor_sql import motorsql
from Principal.Window import Ventana
from subprocess import call
import os
import sys

class loginventana():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("800x500")
        self.ventana.config(bg='#DADCE7')
        self.ventana.resizable(0,0)
        self.ventana.protocol("WM_DELETE_WINDOW",self.cierre)

        ruta = self.rutas('Imgs\condominio_logo.ico')        
        self.ventana.iconbitmap(ruta)
        self.imgframe(self.ventana)
        self.form_frame(self.ventana)
        self.ventana.mainloop()

    def cierre(self):
        call('/xampp/xampp_stop.exe')
        self.ventana.destroy()

    def imgframe(self,master):
        ruta = self.rutas("Imgs/condominio_logo.png")
        self.logo = generic.leer_imagen(ruta,(250,200))

        self.frame_logo = Frame(master, bd=0, width=300, relief=SOLID, padx=5, pady=5, bg='#00081d')
        self.frame_logo.pack(side='left', expand='no',fill='both')

        self.label = Label(self.frame_logo, image=self.logo, bg='#00081d')
        self.label.place(x=0, y=0, relwidth=1,relheight=1)
    
    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)

    

    def form_frame(self,master):
        self.frame_form = Frame(master, bd=0, relief=SOLID, bg='#DADCE7')
        self.frame_form.pack(side='right', expand=YES,fill=BOTH)

        self.frame_form_top = Frame(self.frame_form, height = 50, bd=0, relief=SOLID, bg='black')
        self.frame_form_top.pack(side="top",fill='x')
        
        self.title_lbl = Label(self.frame_form_top, text='Inicio de Sesión', font=('Arial Black Bold', 20), fg="#00081d", bg="#DADCE7", pady=25)
        self.title_lbl.pack(expand='yes',fill='both')



        self.frame_form_fill = Frame(self.frame_form, height = 50, bd=0, relief=SOLID, bg='#DADCE7')
        self.frame_form_fill.pack(side="bottom",expand="yes",fill="both")
                
        etiqueta_usuario = Label(self.frame_form_fill, text="Usuario:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="w")
        etiqueta_usuario.pack(fill='x', padx=20,pady=5)
        self.usuario =Entry(self.frame_form_fill, font=('Arial', 15))
        
        self.usuario.pack(fill='x',padx=20, pady=10)
        
        etiqueta_contraseña = Label(self.frame_form_fill, text="Contraseña:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="w")
        etiqueta_contraseña.pack(fill='x', padx=20,pady=5)
        self.contraseña = Entry(self.frame_form_fill, font=('Arial', 15))
        
        self.contraseña.pack(fill='x',padx=20, pady=10)
        self.contraseña.config(show="*")
        
        inicio = Button(self.frame_form_fill, text="Iniciar Sesion", font=('Arial', 12), bg= '#0040FF', bd=0, fg="#fff",activebackground='#00081d',activeforeground='white',command= lambda : self.inicio(self.usuario.get(),self.contraseña.get()))
        inicio.pack(fill='x', padx=20,pady=20)

        self.espacio = Label(self.frame_form_fill,bg="#DADCE7")
        self.espacio.pack(padx=20,pady=30)
        
        self.etiqueta_registro = Label(self.frame_form_fill,text="necesitas la clave maestra o ingresar con un usuario ya creado",bg="#DADCE7",font=('Arial',12))
        self.etiqueta_registro.pack(padx=10,pady=10)
        
        
        
    def inicio(self,usu,contra):

        if busqueda_usu(usu,contra) == True:
            self.ventana.destroy()
            

            v = validacion_datos(usu,contra)
            r = mostrar_usuario(usu,contra)
            

            bd = motorsql(v)
            

            controlador = Controlador(bd)

            
            Ventana(controlador,r)
            





