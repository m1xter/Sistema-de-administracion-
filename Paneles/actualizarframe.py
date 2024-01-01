from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox
from util.generic import *
import os
import sys


class Actualizarframe:
    
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
        
        self.etiqueta  = Label(master,text="ACTUALIZAR",bg='#0040FF', font=('Arial',15),fg='white')
        self.etiqueta.place(x=2,y=0)
        
        
        self.boton_rpersona = Button(master,image=self.img1,compound='left',bd=0,bg='#7b7b7c',activebackground='#515151',command= lambda : self.indi_frame(self.frame_de_Ap),width=148,height=50)
        self.boton_rpersona.place(x=25,y=80)
        
        lbl_rpersona = Label(master, text="PERSONA", font=('arial bold','10'), bg='#515151',fg='white',anchor='s',width=18, height=1)
        lbl_rpersona.place(x=25,y=130)
        #------------------------------
        self.boton_rapto = Button(master,image=self.img2,bd=0,bg='#0195ff',activebackground='#025895',command= lambda : self.indi_frame(self.frame_de_Aa),width=148,height=50)
        self.boton_rapto.place(x=25,y=165)
        
        lbl_rapto = Label(master, text="APARTAMENTO", font=('arial bold','10'), bg='#025895',fg='white',anchor='s',width=18, height=1)
        lbl_rapto.place(x=25,y=215)
        #------------------------------
        self.boton_ringreso = Button(master,image=self.img3,bd=0,bg='#feba01',activebackground='#bd8902',command= lambda : self.indi_frame(self.frame_de_Ai),width=148,height=50)
        self.boton_ringreso.place(x=25,y=250)
        
        lbl_ringreso = Label(master, text="INGRESO", font=('arial bold','10'), bg='#bd8902',fg='white',anchor='s',width=18, height=1)
        lbl_ringreso.place(x=25,y=300)
       #------------------------------
        self.boton_rretiro = Button(master,image=self.img4,bd=0,bg='#c63522',activebackground='#982719',command= lambda : self.indi_frame(self.frame_de_Ae),width=148,height=50)
        self.boton_rretiro.place(x=25,y=335)
        
        lbl_rretiro = Label(master, text="RETIRO", font=('arial bold','10'), bg='#982719',fg='white',anchor='s',width=18, height=1)
        lbl_rretiro.place(x=25,y=385)


    def inicio(self,master):
        self.inicio_frame = Frame(master,bg="#e5e4e4",height=500,width=700)
        self.inicio_frame.place(x=200)

        self.Apframe = Frame(master)
        self.Aaframe = Frame(master)
        self.Aiframe = Frame(master)
        self.Aeframe = Frame(master)

    def validate_entry(self,text):
        return text.isalpha()
    
    def validate_entry2(self,text):
        return text.isdigit()
    
    def frame_de_Ap(self,master):
        self.Apframe = Frame(master,bg="#e5e4e4")
        self.Apframe.place(x=200)
        self.Apframe.config(height=500,width=700)
        

        self.texto1 = Label(self.Apframe,text="Actualizar Personas",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.texto1.place(x=40,y=5)

        self.cuadro = Frame(self.Apframe,bg="#515151",height=5,width=500)
        self.cuadro.place(x=40,y=45)

        self.texto2 = Label(self.Apframe,text="Filtra los Datos de la Persona por la Cédula",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=60)

        self.texto2 = Label(self.Apframe,text="Cédula:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=100)

        self.cedula= ttk.Entry(self.Apframe,textvariable=self.id_persona,font=('Arial','12'),width=15)        
        self.cedula.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S"))
        self.cedula.place(x=120,y=100)

        self.texto2 = Label(self.Apframe,text="Primer Nombre:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=40,y=160)

        self.pnombre= ttk.Entry(self.Apframe,textvariable=self.nom_persona,font=('Arial','12'),width=15)
        self.pnombre.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry),"%S"))        
        self.pnombre.place(x=40,y=190)

        self.texto2 = Label(self.Apframe,text="Segundo Nombre:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=190,y=160)

        self.snombre= ttk.Entry(self.Apframe,textvariable=self.nom_persona2,font=('Arial','12'),width=15)  
        self.snombre.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry),"%S"))      
        self.snombre.place(x=190,y=190)

        self.texto2 = Label(self.Apframe,text="Primer Apellido:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=340,y=160)

        self.papellido= ttk.Entry(self.Apframe,textvariable=self.ape_persona,font=('Arial','12'),width=15)      
        self.papellido.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry),"%S"))  
        self.papellido.place(x=340,y=190)

        self.texto2 = Label(self.Apframe,text="Segundo Apellido:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=490,y=160)

        self.spellido= ttk.Entry(self.Apframe,textvariable=self.ape_persona2,font=('Arial','12'),width=15)        
        self.spellido.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry),"%S"))
        self.spellido.place(x=490,y=190)

        
        self.texto2 = Label(self.Apframe,text="Nro de Telefono:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=40,y=240)

        self.ntelefono= ttk.Entry(self.Apframe,textvariable=self.nro_telefono,font=('Arial','12'),width=15) 
        self.ntelefono.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S"))       
        self.ntelefono.place(x=40,y=270)

        self.texto2 = Label(self.Apframe,text="Tipo:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=190,y=240)
        
        self.propiedad = ttk.Combobox(self.Apframe,values=("propietario","inquilino"),textvariable=self.tipo,font=('Arial','12'),width=15)
        self.propiedad.place(x=190,y=270)

        self.texto2 = Label(self.Apframe,text="Edad:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=360,y=240)

        self.edad= ttk.Entry(self.Apframe,textvariable=self.edadp,font=('Arial','12'),width=15)       
        self.edad.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S")) 
        self.edad.place(x=360,y=270)


        self.boton1 = Button(self.Apframe,font=('Arial','12'),bg='#0040FF',fg='white',width=8,height=1,text="Buscar",bd=0,command= lambda : self.click_buscar_persona(self.cedula.get()))
        self.boton1.place(x=270,y=95)

        self.actualizar_btn = Button(self.Apframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Actualizar",bd=0,command= lambda : self.actualizar_persona())
        self.actualizar_btn.place(x=400,y=350)



    def frame_de_Aa(self,master):
        self.Aaframe = Frame(master,bg="#e5e4e4")
        self.Aaframe.place(x=200)
        self.Aaframe.config(height=500,width=700)

        self.etiqueta1  = Label(self.Aaframe,text="Actualizar Apartamentos",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.etiqueta1.place(x=40,y=5)

        self.cuadro = Frame(self.Aaframe,bg="#025895",height=5,width=500)
        self.cuadro.place(x=40,y=45)
        
    
        self.texto2 = Label(self.Aaframe,text="Filtra los Datos del Apartamento por el Nro",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=60)


        self.texto2 = Label(self.Aaframe,text="Nro de Apartamento:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=100)

        self.apartamento= ttk.Entry(self.Aaframe,textvariable=self.id_aparta,font=('Arial','12'),width=10) 
        self.apartamento.config(validate='key',validatecommand=(self.Aaframe.register(self.validate_entry2),"%S"))       
        self.apartamento.place(x=220,y=100)

        self.texto2 = Label(self.Aaframe,text="Propietario:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=200)

        r2 = self.controlador.consulta_propietario("propietario")
        self.propietario = ttk.Combobox(self.Aaframe,font=('Arial','12'),width=15,values=(r2))
        self.propietario.config(validate='key',validatecommand=(self.Aaframe.register(self.validate_entry2),"%S"))
        self.propietario.place(x=50,y=230)

        
        self.texto2 = Label(self.Aaframe,text="Inquilino:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=250,y=200)

        r = self.controlador.consulta_propietario("inquilino")
        self.inquilino = ttk.Combobox(self.Aaframe,font=('Arial','12'),width=15,values=(r))    
        self.inquilino.config(validate='key',validatecommand=(self.Aaframe.register(self.validate_entry2),"%S"))    
        self.inquilino.place(x=250,y=230)

        self.aparta_btn = Button(self.Aaframe,font=('Arial','12'),bg='#0040FF',fg='white',width=8,height=1,text="Buscar",bd=0,command= lambda : self.click_buscar_apartamento(self.apartamento.get()) )
        self.aparta_btn.place(x=350,y=95)

        self.actualizar_btn = Button(self.Aaframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Actualizar",bd=0,command= lambda : self.actualizar_apartamento())
        self.actualizar_btn.place(x=400,y=350)



    def frame_de_Ai(self,master):
        self.Aiframe = Frame(master,bg="#e5e4e4")
        self.Aiframe.place(x=200)
        self.Aiframe.config(height=500,width=700)

        
        self.texto1 = Label(self.Aiframe,text="Actualizar Ingresos",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.texto1.place(x=40,y=5)

        self.cuadro = Frame(self.Aiframe,bg="#bd8902",height=5,width=500)
        self.cuadro.place(x=40,y=45)

        self.texto2 = Label(self.Aiframe,text="Filtra los Datos del Ingreso por la Fecha",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=60)

        self.texto2 = Label(self.Aiframe,text="Fecha:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=100)

        self.calendario1 = DateEntry(self.Aiframe,font=('Arial',12),width=15,selectmode = 'day')
        self.calendario1.config(state="readonly")
        self.calendario1.place(x=120,y=100)

        self.texto2 = Label(self.Aiframe,text="Nro de Apartamento:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=140)

        self.nro_apartamento= ttk.Entry(self.Aiframe,font=('Arial',12),width=15)
        self.nro_apartamento.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S"))        
        self.nro_apartamento.place(x=50,y=170)

        self.texto2 = Label(self.Aiframe,text="Tipo de Pago:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=220,y=140)

        self.pago= ttk.Entry(self.Aiframe,font=('Arial',12),width=15)        
        self.pago.place(x=220,y=170)
        

        self.texto2 = Label(self.Aiframe,text="Cantidad Depositada:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=390,y=140)

        self.cant_dinero= ttk.Entry(self.Aiframe,font=('Arial',12),width=15)  
        self.cant_dinero.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S"))      
        self.cant_dinero.place(x=390,y=170)

        self.texto2 = Label(self.Aiframe,text="Meses:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=210)

        self.meses= ttk.Entry(self.Aiframe,font=('Arial',12),width=50)        
        self.meses.place(x=120,y=210)
        
        

        self.aparta_btn = Button(self.Aiframe,font=('Arial','12'),bg='#0040FF',fg='white',width=10,height=1,text="Buscar",bd=0,command= lambda : self.click_buscar_ingreso(self.calendario1.get_date()))
        self.aparta_btn.place(x=310,y=100)

        self.actualizar_btn = Button(self.Aiframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Actualizar",bd=0,command= lambda : self.actualizar_ingreso())
        self.actualizar_btn.place(x=400,y=400)


    def tabla_ingresos(self,master,info):
        #el titulo de la tabla
        self.texto2 = Label(master,text="Seleccione la fila del Ingreso a Actualizar",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=250)
        #tabla
        self.tree2 = ttk.Treeview(master,height=10,columns=('id',"apto","fecha","tipo de pago","meses pagos","cantidad depositada"))
        
        self.tree2.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree2.grid(row=0, column=0, sticky=NSEW)

        self.tree2.column('#0', stretch=NO, minwidth=0, width=0)        
        self.tree2.column('id',stretch=NO, minwidth=0, width=0)
        self.tree2.heading("apto",text="Apto")
        self.tree2.column("apto",width=70)
        self.tree2.heading("fecha",text="fecha")
        self.tree2.column("fecha",width=100)
        self.tree2.heading("tipo de pago",text="tipo de pago")
        self.tree2.column("tipo de pago",width=100)
        self.tree2.heading("meses pagos",text="meses pagos")
        self.tree2.column("meses pagos",width=100)
        self.tree2.heading("cantidad depositada",text="cantidad depositada")
        self.tree2.column("cantidad depositada",width=150)        
        self.tree2.place(x=50,y=280,width=524,height=110)

        for dt in info:
            
            self.tree2.insert("",'end',values=(dt[0],dt[1],dt[5],dt[2],dt[3],dt[4]))


        
        

    def frame_de_Ae(self,master):
        self.Aeframe = Frame(master,bg="#e5e4e4")
        self.Aeframe.place(x=200)
        self.Aeframe.config(height=500,width=700)

        self.texto1 = Label(self.Aeframe,text="Actualizar Retiros",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.texto1.place(x=40,y=5)

        self.cuadro = Frame(self.Aeframe,bg="#982719",height=5,width=500)
        self.cuadro.place(x=40,y=45)

        self.texto2 = Label(self.Aeframe,text="Filtra los Datos de Retiros por la Fecha",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=60)

        self.texto2 = Label(self.Aeframe,text="Fecha:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=100)

        self.calendario2 = DateEntry(self.Aeframe,font=('Arial',12),width=15,selectmode = 'day')
        self.calendario2.config(state="readonly")
        self.calendario2.place(x=120,y=100)


        self.texto2 = Label(self.Aeframe,text="Cantidad Retirada:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=140)

        self.cant_retirada= ttk.Entry(self.Aeframe,font=('Arial',12),width=15)        
        self.cant_retirada.config(validate='key',validatecommand=(self.Apframe.register(self.validate_entry2),"%S"))
        self.cant_retirada.place(x=220,y=140)


        self.texto2 = Label(self.Aeframe,text="Causa:",font='Arial,12',bg='#e5e4e4')
        self.texto2.place(x=50,y=170)

        self.texto  = Text(self.Aeframe,font=('Arial',12),width=50,height=2)
        self.texto.place(x=50,y=200)

        self.aparta_btn = Button(self.Aeframe,font=('Arial','12'),bg='#0040FF',fg='white',width=10,height=1,text="Buscar",bd=0,command= lambda : self.click_buscar_egresos(self.calendario2.get_date())) 
        self.aparta_btn.place(x=310,y=100)

        self.actualizar_btn = Button(self.Aeframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Actualizar",bd=0,command= lambda : self.actualizar_egresos())
        self.actualizar_btn.place(x=400,y=400)


    

    def tabla_retiros(self,master,info):
        
        self.texto2 = Label(master,text="Seleccione la fila del Retiro a Actualizar",font='Arial,12',fg='#0040FF',bg='#e5e4e4')
        self.texto2.place(x=50,y=250)
        
        self.tree3 = ttk.Treeview(master,height=10,columns=("id","fecha","causa","cantidad retirada"))

        self.tree3.bind('<<TreeviewSelect>>', self.item_selected2)
        self.tree3.grid(row=0, column=0, sticky=NSEW)

        self.tree3.column('#0', stretch=NO, minwidth=0, width=0)        
        self.tree3.column('id',stretch=NO, minwidth=0, width=0)
        self.tree3.heading("fecha",text="fecha")
        self.tree3.column("fecha",width=100)
        self.tree3.heading("causa",text="causa")
        self.tree3.column("causa",width=100)
        self.tree3.heading("cantidad retirada",text="cantidad retirada")
        self.tree3.column("cantidad retirada",width=100)
        
        self.tree3.place(x=50,y=280,width=600,height=110)

        
        for dt in info:
            self.tree3.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3]))







    def indi_frame(self,fr):
        self.Apframe.destroy()
        self.Aaframe.destroy()
        self.Aiframe.destroy()
        self.Aeframe.destroy() 
        fr(self.factualizar)


    def limpiar_variable(self):
        self.id_persona.set('')
        self.nom_persona.set('')

    def limpiar_caja(self):
        self.pnombre.config(text = "")
        self.nom_persona.update()
        self.limpiar_variable()
    

    
    def limpiar3(self):
        self.nro_apartamento.delete("0","end")
        self.pago.delete("0","end")
        self.meses.delete("0","end")
        self.cant_dinero.delete("0","end")

    def limpiar4(self):
        self.texto.delete("1.0","end")
        self.cant_retirada.delete("0","end")
        

    def click_buscar_persona(self,cedula):
        self.cedula.config(text = "")
        self.cedula.update()
        id_persona = self.id_persona.get()
        if id_persona == '':
            messagebox.showerror("ERROR", "SE REQUIERE LA CEDULA PARA UBICAR A LA PERSONA")
        else:
            info = self.controlador.consulta_datos_personas(id_persona)
            if info:                
                for ct in info:
                    self.nom_persona.set('')
                    self.pnombre.insert(0,ct[0])                
                    self.nom_persona2.set('')
                    self.snombre.insert(0,ct[1])
                    self.ape_persona.set('')
                    self.papellido.insert(0,ct[2])
                    self.ape_persona2.set('')
                    self.spellido.insert(0,ct[3])
                    self.nro_telefono.set('')
                    self.ntelefono.insert(0,ct[4])
                    self.edadp.set('')
                    self.edad.insert(0,ct[6])
                    self.tipo.set('')
                    self.propiedad.insert(0,ct[5])
                
            else:
                self.lbl2_id_mat.config(text = "NO ENCONTRADO")
                self.lbl2_id_mat.update()
                self.actualizar_btn.config(state='disable')
                self.nom_actualizar.set('')
                self.entry_id.config(state='normal')


    
    def actualizar_persona(self):
            a = self.cedula.get()
            b = self.pnombre.get()
            c = self.snombre.get()
            d = self.papellido.get()
            e = self.spellido.get()
            f = self.ntelefono.get()
            g = self.edad.get()
            h = self.propiedad.get()

            if a == "" or b == "" or c== "" or d =="" or e =="" or f == "" or g =="":
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
                return
            if "-" in g  or '-' in f:
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
                return
            if not b.isalpha() or not c.isalpha() or not d.isalpha() or not e.isalpha() or not h.isalpha():
                messagebox.showerror("ERROR", "no se admiten numeros en casillas alphabeticas")
                
            else:        
                if self.controlador.update_persona(b,c,d,e,a,f,h,g):                    
                    self.limpiar_caja()
                
    
    
    
    def click_buscar_apartamento(self,nro):
        self.apartamento.config(text = "")
        self.apartamento.update()
        id_aparta = self.id_aparta.get()
        if id_aparta == '':
            messagebox.showerror("ERROR", "SE REQUIERE EL NUMERO DE APARTAMENTO PARA UBICAR EL APARTAMENTO")
        else:
            info = self.controlador.consulta_datos_apartamentos(nro)
            if info:                
                for ct in info:
                    self.propietario.insert(0,ct[0])
                    self.inquilino.insert(0,ct[1])
    
            
    def actualizar_apartamento(self):
            a = self.apartamento.get()
            b = self.propietario.get()
            c = self.inquilino.get()

            if a == "" or b == "" :
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
                return
            if "-" in b  or '-' in a:
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
                return
            if  not b.isdecimal() or not c.isdecimal() :
                messagebox.showerror("ERROR", "no se admiten letras en casillas numericas")
                return
            else:        
                if self.controlador.update_aparta(a,b,c):
                    self.limpiar_caja()
                
            
    
    def click_buscar_ingreso(self,fecha):        
        id_fecha = self.calendario1.get()
        if id_fecha == '':
            messagebox.showerror("ERROR", "SE REQUIERE LA FECHA DEL INGRESO PARA BUSCAR EL INGRESO")
        else:
            info = self.controlador.consulta_datos_ingreso(fecha)
            if info:                
                self.tabla_ingresos(self.Aiframe,info)
    

    def item_selected(self,event):
        for selected_item in self.tree2.selection():
            item = self.tree2.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            self.limpiar3()
            self.nro_apartamento.insert(0,record[1])
            self.pago.insert(0,record[3])
            self.meses.insert(0,record[4])
            self.cant_dinero.insert(0,record[5])
            self.id_ingreso = record[0]
            
    
    def item_selected2(self,event):
        for selected_item in self.tree3.selection():
            item = self.tree3.item(selected_item)
            record = item['values']
            # show a message
            print(record)            
            self.limpiar4()
            self.texto.insert('1.0',record[2])
            self.cant_retirada.insert(0,record[3])            
            self.id_egreso = record[0]

    def actualizar_ingreso(self):
            a = self.nro_apartamento.get()
            b = self.pago.get()
            c = self.meses.get()
            d = self.cant_dinero.get()
            e = self.calendario1.get_date()
            f = self.id_ingreso

            if a == "" or b == "" or c =="" or d =="" :
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
                return
            if "-" in d:
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
                return
            if  not d.isdecimal():
                messagebox.showerror("ERROR", "no se admiten letras en casillas numericas")
                return
            else:        
                if self.controlador.update_ingresos(f,e,a,c,b,d):
                    self.limpiar_caja()

    
    def click_buscar_egresos(self,fecha):        
        id_fecha = self.calendario2.get()
        if id_fecha == '':
            messagebox.showerror("ERROR", "SE REQUIERE LA FECHA DEL INGRESO PARA BUSCAR EL EGRESO")
        else:
            info = self.controlador.consulta_datos_egreso(fecha)
            if info:               
                print(info)
                self.tabla_retiros(self.Aeframe,info)
                    
    
    def actualizar_egresos(self):
            a = self.calendario2.get_date()
            b = self.texto.get('1.0','end')
            c = self.cant_retirada.get()
            d  = self.id_egreso
            if a == "" or b == "" or c ==""  :
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
                return
            if "-" in c:
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
                return            
            else:        
                if self.controlador.update_egresos(d,a,b,c):
                    self.limpiar_caja()