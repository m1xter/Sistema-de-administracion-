from tkinter import*
from tkinter import ttk
from datetime import date
from datetime import datetime
import calendar,datetime
from sql.motor_sql import motorsql
from util.generic import *
import os
import sys

class homeframe:

    
    def __init__(self,master,controlador):
        self.fhome = Frame(master,bg="#e5e4e4")
        self.fhome.pack()
        self.fhome.config(height=500,width=900)

        ruta1 = self.rutas(".\Imgs\icon_1.png")
        ruta2 = self.rutas(".\Imgs\icon_2.png")
        ruta3 = self.rutas(".\Imgs\icon_3.png")
        ruta4 = self.rutas(".\Imgs\icon_4.png")
        ruta5 = self.rutas(".\Imgs\icon_5.png")

        self.logo_btn1 = generic.leer_imagen(ruta1,(100,90))
        self.logo_btn2 = generic.leer_imagen(ruta2,(100,90))
        self.logo_btn3 = generic.leer_imagen(ruta3,(100,90))
        self.logo_btn4 = generic.leer_imagen(ruta4,(100,90))
        self.logo_btn5 = generic.leer_imagen(ruta5,(100,90))
        
        
        self.controlador = controlador
        g = generic(controlador)
        g.morosos()
        self.inicio()
        #self.combo_mensualidad(self.fhome)
        #self.combo_pagos(self.fhome)
        #self.combo_retiros(self.fhome)

    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)
    
    
    def inicio(self):
        self.tabla_mensualidad(self.fhome)
        self.botones(self.fhome)
        #self.saldo_total(self.fhome)
        #self.tabla_pagos(self.fhome)
        #self.tabla_retiros(self.fhome)
        self.lb1 = Label()
        self.lb2 = Label()
        self.lb3 = Label()
        self.lb4 = Label()
        self.lb5 = Label()
        self.tree1 = ttk.Treeview()
        self.tree2 = ttk.Treeview()
        self.tree3 = ttk.Treeview()
        self.tree4 = ttk.Treeview()
        self.tree5 = ttk.Treeview()
        self.combo2 = ttk.Combobox()
        self.combo3 = ttk.Combobox()
        self.combo4 = ttk.Combobox()


    def tabla_personas(self,master):
        #el titulo de la tabla
        
        a = self.controlador.consulta_datos_inquilinos()


        self.lb5  = Label(master,text="PERSONAS",font='Arial,15',bg='#515151', fg='#ffffff')
        self.lb5.config(width=88)
        self.lb5.place(x=50,y=180)
        #tabla
        self.tree5 = ttk.Treeview(master,height=10,columns=("nom1","nom2","ape1","ape2","tlf","tipo","edad"))
        
        self.tree5.heading("#0",text="Cedula")
        self.tree5.column("#0",width=80)
        self.tree5.heading("nom1",text="Primer Nombre")
        self.tree5.column("nom1",width=130)
        self.tree5.heading("nom2",text="Segundo Nombre")
        self.tree5.column("nom2",width=130)
        self.tree5.heading("ape1",text="Primer Apellido")
        self.tree5.column("ape1",width=130)
        self.tree5.heading("ape2",text="Segundo Apellido")
        self.tree5.column("ape2",width=130)
        self.tree5.heading("tlf",text="Telefono")
        self.tree5.column("tlf",width=80)
        self.tree5.heading("tipo",text="Tipo")
        self.tree5.column("tipo",width=70)
        self.tree5.heading("edad",text="Edad")
        self.tree5.column("edad",width=45)
        
        self.tree5.place(x=50,y=200,width=800)

        for  dt in a:
            self.tree5.insert("",'end',text=dt[0],values=(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))

    #Acá clone tablas para verificar la acción de los botones cuadrados  
    def tabla_apto(self,master):
        #el titulo de la tabla
        
        fecha = datetime.datetime.now()
        a = self.controlador.Consulta_datos_apartamento()


        self.lb4  = Label(master,text="APARTAMENTOS"+ "  " + f"{fecha.year}",font='Arial,12',bg='#025894', fg='#ffffff')
        self.lb4.config(width=88)
        self.lb4.place(x=50,y=180)
        #tabla
        self.tree4 = ttk.Treeview(master,height=10,columns=("propietario","inquilino"))
        
        self.tree4.heading("#0",text="nro apto")
        self.tree4.column("#0",width=200)
        self.tree4.heading("propietario",text="propietario")
        self.tree4.column("propietario",width=300)
        self.tree4.heading("inquilino",text="inquilino")
        self.tree4.column("inquilino",width=295)
        
        self.tree4.place(x=50,y=200,width=800)

        for  dt in a:
            self.tree4.insert("",'end',text=dt[0],values=(dt[1],dt[2]))


    def tabla_mensualidad(self,master):
        #el titulo de la tabla
        
            fecha = now = datetime.datetime.now()

            
            self.lb1  = Label(master,text="MENSUALIDAD" + "    " + f"{fecha.year}",font='Arial,12',bg='#017229', fg='#ffffff')
            self.lb1.config(width=88)
            self.lb1.place(x=50,y=180)
            #tabla
            self.tree1 = ttk.Treeview(master,height=10,columns=("1","2","3","4","5","6","7","8","9","10","11","12"))
            self.tree1.heading("#0",text="Apto")
            self.tree1.column("#0",width=45)
            self.tree1.heading("1",text="Enero")
            self.tree1.column("1",width=62)
            self.tree1.heading("2",text="Febrero")
            self.tree1.column("2",width=62)
            self.tree1.heading("3",text="Marzo")
            self.tree1.column("3",width=62)
            self.tree1.heading("4",text="Abril")
            self.tree1.column("4",width=62)
            self.tree1.heading("5",text="Mayo")
            self.tree1.column("5",width=62)
            self.tree1.heading("6",text="Junio")
            self.tree1.column("6",width=62)        
            self.tree1.heading("7",text="Julio")
            self.tree1.column("7",width=63)        
            self.tree1.heading("8",text="Agosto")
            self.tree1.column("8",width=63)        
            self.tree1.heading("9",text="Septiembre")
            self.tree1.column("9",width=63)        
            self.tree1.heading("10",text="Octubre")
            self.tree1.column("10",width=63)        
            self.tree1.heading("11",text="Noviembre")
            self.tree1.column("11",width=63)        
            self.tree1.heading("12",text="Diciembre")
            self.tree1.column("12",width=63)        
            self.tree1.place(x=50,y=200,width=800)

            a = self.controlador.consulta_mensualidad()
            for ct in a:
                self.tree1.insert("","end",text=ct[0],values=(ct[1],ct[2],ct[3],ct[4],ct[5],ct[6],ct[7],ct[8],ct[9],ct[10],ct[11],ct[12]))

            


    def tabla_ingresos(self,master):
        #el titulo de la tabla
        
        fecha = datetime.datetime.now()
        c =self.controlador.consulta_pagos()
        
        self.lb2  = Label(master,text="PAGOS" + "    " + f"{fecha.year}",font='Arial,12',bg='#bc8902', fg='#ffffff')
        self.lb2.config(width=88)
        self.lb2.place(x=50,y=180)
        #tabla
        self.tree2 = ttk.Treeview(master,height=10,columns=("fecha","tipo de pago","meses pagos","cantidad depositada"))
        
        self.tree2.heading("#0",text="Apto")
        self.tree2.column("#0",width=60)
        self.tree2.heading("fecha",text="Fecha")
        self.tree2.column("fecha",width=100)
        self.tree2.heading("tipo de pago",text="Tipo de Pago")
        self.tree2.column("tipo de pago",width=150)
        self.tree2.heading("meses pagos",text="Meses Pagos")
        self.tree2.column("meses pagos",width=350)
        self.tree2.heading("cantidad depositada",text="Cantidad Depositada")
        self.tree2.column("cantidad depositada",width=135)        
        self.tree2.place(x=50,y=200,width=800)

        

        for  dt in c:
            self.tree2.insert("",'end',text=dt[0],values=(dt[1],dt[2],dt[3],dt[4]))
      

    def tabla_retiros(self,master):
        #el titulo de la tabla
        
        fecha = datetime.datetime.now()

        e = self.controlador.consulta_datos_egresos()

        self.lb3  = Label(master,text="RETIROS" + "    " + f"{fecha.year}",font='Arial,12',bg='#982618', fg='#ffffff')
        self.lb3.config(width=88)
        self.lb3.place(x=50,y=180)
        #tabla
        self.tree3 = ttk.Treeview(master,height=10,columns=("causa","cantidad retirada"))
        
        self.tree3.heading("#0",text="Fecha")
        self.tree3.column("#0",width=200)
        self.tree3.heading("causa",text="Causa")
        self.tree3.column("causa",width=400)
        self.tree3.heading("cantidad retirada",text="Cantidad retirada")
        self.tree3.column("cantidad retirada",width=195)
        
        self.tree3.place(x=50,y=200,width=800)

        
        
    

        for dt in e:
            self.tree3.insert("",'end',text=dt[1],values=(dt[2],dt[3]))
    

    #Acá agregué los botones cuadrados del Home
    def botones(self,master):
        
        self.frame_home = Frame(master,bg='#0040FF',height=30,width=900)
        self.frame_home.place(x=0,y=0)
        
        self.etiqueta  = Label(master,text="HOME",bg='#0040FF', font=('Arial',15),fg='white')
        self.etiqueta.place(x=2,y=0)
        
        
        #BOTON DE PERSONAS
        personas_btn = Button(master,image=self.logo_btn5, compound=CENTER, bd=0, bg='#7b7b7c',activebackground='#515151', command= lambda : self.indicador_tabla(self.tabla_personas),width=155,height=100)
        personas_btn.place(x=30,y=40)
        #LABEL DE BOTON DE PERSONAS
        personas_lbl = Label(master, text="PERSONAS", font=('arial bold','10'), bg='#515151',fg='white',anchor='s')
        personas_lbl.config(width=19, height=1)
        personas_lbl.place(x=30,y=140)
        
        #BOTON DE APARTAMENTOS
        apartamentos_btn = Button(master,image=self.logo_btn1, compound=CENTER, bd=0, bg='#0195ff',activebackground='#025895', command= lambda : self.indicador_tabla(self.tabla_apto),width=155,height=100)
        apartamentos_btn.place(x=200,y=40)
        #LABEL DE BOTON DE APARTAMENTOS
        apartamentos_lbl = Label(master, text="APARTAMENTOS", font=('arial bold','10'), bg='#025895',fg='white',anchor='s')
        apartamentos_lbl.config(width=19, height=1)
        apartamentos_lbl.place(x=200,y=140)

        #BOTON DE MENSUALIDAD
        mensualidad_btn = Button(master, image=self.logo_btn2, compound=CENTER, bd=0, bg='#00a63a',activebackground='#00722a', command= lambda : self.indicador_tabla(self.tabla_mensualidad),width=155,height=100)
        mensualidad_btn.place(x=370,y=40)
        #LABEL DE BOTON DE MENSUALIDAD
        mensualidad_lbl = Label(master, text="MENSUALIDAD", font=('arial bold','10'), bg='#00722a',fg='white',anchor='s')
        mensualidad_lbl.config(width=19, height=1)
        mensualidad_lbl.place(x=370,y=140)
        
        #BOTON DE INGRESOS       
        ingresos_btn = Button(master,image=self.logo_btn3, compound=CENTER, bd=0, bg='#feba01',activebackground='#bd8902', command= lambda : self.indicador_tabla(self.tabla_ingresos),width=155,height=100)
        ingresos_btn.place(x=540,y=40)
        #LABEL DE BOTON DE INGRESOS
        ingresos_lbl = Label(master, text="INGRESOS", font=('arial bold','10'), bg='#bd8902',fg='white',anchor='s')
        ingresos_lbl.config(width=19, height=1)
        ingresos_lbl.place(x=540,y=140)

        #BOTON DE RETIROS
        retiros_btn = Button(master,image=self.logo_btn4,compound=CENTER, bd=0,bg='#c63522',activebackground='#982719', command= lambda : self.indicador_tabla(self.tabla_retiros),width=155,height=100)
        retiros_btn.place(x=710,y=40)
        #LABEL DE BOTON DE RETIROS
        retiros_lbl = Label(master, text="RETIROS", font=('arial bold','10'), bg='#982719',fg='white',anchor='s')
        retiros_lbl.config(width=19, height=1)
        retiros_lbl.place(x=710,y=140)
        
        
    
    #def combo_mensualidad(self,master):
    #    self.combo = ttk.Combobox(master,width=10)
    #    self.combo['values'] = ('enero','febrero','marzo','abril')
    #    self.combo.place(x=20,y=250)
#
    #
    #def combo_pagos(self,master):
    #    self.combo = ttk.Combobox(master,width=10)
    #    self.combo['values'] = ('2023','2024','2025','2026')
    #    self.combo.place(x=20,y=250)
#
    #
    #def combo_retiros(self,master):
    #    self.combo = ttk.Combobox(master,width=10)
    #    self.combo['values'] = ('2023','2024','2025','2026')
    #    self.combo.place(x=20,y=250)

    
    

    def clean(self):
        pass


    def indicador_tabla(self,tabla):        
        self.tree1.destroy()
        self.tree2.destroy()
        self.tree3.destroy()
        self.tree4.destroy()
        self.tree5.destroy()
        self.lb1.destroy()
        self.lb2.destroy()
        self.lb3.destroy()
        self.lb4.destroy()
        self.lb5.destroy()

        tabla(self.fhome)
        
        
        

            


        





