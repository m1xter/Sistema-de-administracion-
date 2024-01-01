from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox
from util.generic import *
from sql.motor_inicio import Registrar_usuario
import os
import sys


class MenuOpciones:
    
    def __init__(self,master,controlador) :
        
        self.factualizar = Frame(master,bg="#b9bccc")
        self.factualizar.pack()
        self.factualizar.config(height=500,width=900)

        self.controlador = controlador

        ruta1 = self.rutas("Imgs/btn1.png")
        ruta2 = self.rutas("Imgs/btn2.png")
        ruta3 = self.rutas("Imgs/btn3.png")
        ruta4 = self.rutas("Imgs/btn4.png")
        

        self.img1 = generic.leer_imagen(ruta1,(50,50))
        self.img2 = generic.leer_imagen(ruta2,(40,40))
        self.img3 = generic.leer_imagen(ruta3,(40,45))
        self.img4 = generic.leer_imagen(ruta4,(40,40))

        self.id_persona = StringVar()
        self.nom_persona = StringVar()
        self.nom_persona2 = StringVar()
        self.ape_persona = StringVar()
        self.ape_persona2 = StringVar()
        self.nro_telefono = StringVar()
        self.tipo = StringVar()
        self.edadp = StringVar()


        self.id_aparta = StringVar()
        self.id_ingreso = StringVar()
        self.id_egreso = StringVar()


        self.menu_botones(self.factualizar)
        self.inicio(self.factualizar)
        
        

    
    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)
    

    def menu_botones(self,master):
        
        self.frame_title = Frame(master,bg='#0040FF',height=30,width=900)
        self.frame_title.place(x=0,y=0)
        
        self.etiqueta  = Label(master,text="OPCIONES",bg='#0040FF', font=('Arial',15),fg='white')
        self.etiqueta.place(x=2,y=0)
        
        
        self.boton_rpersona = Button(master,image=self.img1,compound='left',bd=0,bg='#7b7b7c',activebackground='#515151',command= lambda : self.indi_frame(self.frame_de_Ap),width=148,height=50)
        self.boton_rpersona.place(x=25,y=80)
        
        lbl_rpersona = Label(master, text="USUARIOS", font=('arial bold','10'), bg='#515151',fg='white',anchor='s',width=18, height=1)
        lbl_rpersona.place(x=25,y=130)
        """#------------------------------
        self.boton_rapto = Button(master,image=self.img2,bd=0,bg='#0195ff',activebackground='#025895',command= lambda : self.indi_frame(self.frame_de_Aa),width=148,height=50)
        self.boton_rapto.place(x=25,y=165)
        
        lbl_rapto = Label(master, text="", font=('arial bold','10'), bg='#025895',fg='white',anchor='s',width=18, height=1)
        lbl_rapto.place(x=25,y=215)
        #------------------------------
        self.boton_ringreso = Button(master,image=self.img3,bd=0,bg='#feba01',activebackground='#bd8902',command= lambda : self.indi_frame(self.frame_de_Ai),width=148,height=50)
        self.boton_ringreso.place(x=25,y=250)
        
        lbl_ringreso = Label(master, text="", font=('arial bold','10'), bg='#bd8902',fg='white',anchor='s',width=18, height=1)
        lbl_ringreso.place(x=25,y=300)
       #------------------------------
        self.boton_rretiro = Button(master,image=self.img4,bd=0,bg='#c63522',activebackground='#982719',command= lambda : self.indi_frame(self.frame_de_Ae),width=148,height=50)
        self.boton_rretiro.place(x=25,y=335)
        
        lbl_rretiro = Label(master, text="", font=('arial bold','10'), bg='#982719',fg='white',anchor='s',width=18, height=1)
        lbl_rretiro.place(x=25,y=385)
       """

    def inicio(self,master):
        self.inicio_frame = Frame(master,bg="#e5e4e4",height=500,width=700)
        self.inicio_frame.place(x=200)

        self.Apframe = Frame(master)
        self.Aaframe = Frame(master)
        self.Aiframe = Frame(master)
        self.Aeframe = Frame(master)

    def frame_de_Ap(self,master):
        self.Apframe = Frame(master,bg="#e5e4e4")
        self.Apframe.place(x=200)
        self.Apframe.config(height=500,width=700)
        
        self.lb1 = Label(self.Apframe,text="Registro de Usuario ",font=('Arial Black Bold', 15), fg="#00081d", bg="#DADCE7", pady=25)
        self.lb1.pack(fill='y')

        self.lb2 = Label(self.Apframe,text="Usuario:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="center")
        self.lb2.pack(fill='x',padx=70,pady=5)

        self.usuario =Entry(self.Apframe, font=('Arial', 15))
        self.usuario.pack(fill='x',padx=70, pady=10)


        self.lb2 = Label(self.Apframe,text="Contraseña:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="center")
        self.lb2.pack(fill='x',padx=70,pady=5)
        
        self.contra =Entry(self.Apframe, font=('Arial', 15))
        self.contra.pack(fill='x',padx=70, pady=10)
        self.contra.config(show="*")
        
        self.lb2 = Label(self.Apframe,text='Seleccione el "Tipo de Permiso Para Usuario"', font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="w")
        self.lb2.pack(padx=70,pady=5)

        self.combo = ttk.Combobox(self.Apframe,width=10,font=('Arial', 15))
        self.combo['values'] = ('admin','presidente','tesorero')
        self.combo.config(state="readonly")
        self.combo.pack(fill='x',padx=70,pady=8)
        

        self.boton2 = Button(self.Apframe,text="Confirmar",font=('bold',15),fg='white',bd=0,bg="#0040FF",activebackground='#00081d',activeforeground='white',command= lambda : Registrar_usuario(self.usuario.get(),self.contra.get(),self.combo.get()))
        self.boton2.config(width=10)
        self.boton2.pack(padx=40,pady=40)

    def frame_de_Aa(self,master):
        pass
    def frame_de_Ai(self,master):
        pass

    
        
        

    def frame_de_Ae(self,master):
        pass

    


    def indi_frame(self,fr):
        self.Apframe.destroy()
        self.Aaframe.destroy()
        self.Aiframe.destroy()
        self.Aeframe.destroy() 
        fr(self.factualizar)


    