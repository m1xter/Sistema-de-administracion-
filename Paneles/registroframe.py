from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from sql.motor_sql import *
from util import calculos
from util.generic import *
from pdf.creapdf import *
from sql.controlador import Controlador
from tkinter import messagebox
from tkinter.messagebox import askyesno
import os
import sys



class registro:
    
    
    # esta es la clase del frame de registros aqui van todos los formularios para realizar algun tipo  de registro a la base de datos

    def __init__(self,master,controlador) :
        self.fregistro = Frame(master,bg="#b9bccc")
        self.fregistro.pack()
        self.fregistro.config(height=500,width=900)

        self.controlador = controlador

        ruta1 = self.rutas("Imgs/btn1.png")
        ruta2 = self.rutas("Imgs/btn2.png")
        ruta3 = self.rutas("Imgs/btn3.png")
        ruta4 = self.rutas("Imgs/btn4.png")

        self.img1 = generic.leer_imagen(ruta1,(50,50))
        self.img2 = generic.leer_imagen(ruta2,(40,40))
        self.img3 = generic.leer_imagen(ruta3,(40,45))
        self.img4 = generic.leer_imagen(ruta4,(40,40))
        self.menu_botones(self.fregistro)

        self.inicio(self.fregistro)
        
        
    
    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)
    

    def menu_botones(self,master):
        
        self.frame_title = Frame(master,bg='#0040FF',height=30,width=900)
        self.frame_title.place(x=0,y=0)
        
        self.etiqueta  = Label(master,text="REGISTRO",bg='#0040FF', font=('Arial',15),fg='white')
        self.etiqueta.place(x=2,y=0)
      

        self.boton_rpersona = Button(master,image=self.img1,compound='left',bd=0,bg='#7b7b7c',activebackground='#515151',command= lambda : self.indi_frame(self.frame_de_rp),width=148,height=50)
        self.boton_rpersona.place(x=25,y=80)
        
        lbl_rpersona = Label(master, text="PERSONA", font=('arial bold','10'), bg='#515151',fg='white',anchor='s',width=18, height=1)
        lbl_rpersona.place(x=25,y=130)
        #------------------------------
        self.boton_rapto = Button(master,image=self.img2,bd=0,bg='#0195ff',activebackground='#025895',command= lambda : self.indi_frame(self.frame_de_ra),width=148,height=50)
        self.boton_rapto.place(x=25,y=165)
        
        lbl_rapto = Label(master, text="APARTAMENTO", font=('arial bold','10'), bg='#025895',fg='white',anchor='s',width=18, height=1)
        lbl_rapto.place(x=25,y=215)
        #------------------------------
        self.boton_ringreso = Button(master,image=self.img3,bd=0,bg='#feba01',activebackground='#bd8902',command= lambda : self.indi_frame(self.frame_de_ri),width=148,height=50)
        self.boton_ringreso.place(x=25,y=250)
        
        lbl_ringreso = Label(master, text="INGRESO", font=('arial bold','10'), bg='#bd8902',fg='white',anchor='s',width=18, height=1)
        lbl_ringreso.place(x=25,y=300)
       #------------------------------
        self.boton_rretiro = Button(master,image=self.img4,bd=0,bg='#c63522',activebackground='#982719',command= lambda : self.indi_frame(self.frame_de_re),width=148,height=50)
        self.boton_rretiro.place(x=25,y=335)
        
        lbl_rretiro = Label(master, text="RETIRO", font=('arial bold','10'), bg='#982719',fg='white',anchor='s',width=18, height=1)
        lbl_rretiro.place(x=25,y=385)

    


    def inicio(self,master):
        self.inicio_frame = Frame(master,bg="#e5e4e4",height=500,width=700)
        self.inicio_frame.place(x=200)
        
        self.rpframe = Frame(master)
        self.raframe = Frame(master)
        self.riframe = Frame(master)
        self.reframe = Frame(master)


    #rp = registro persona
    def frame_de_rp(self,master):
        self.rpframe = Frame(master,bg="#e5e4e4")
        self.rpframe.place(x=200)
        self.rpframe.config(height=500,width=700)

        self.etiqueta1  = Label(self.rpframe,text="Registro de Personas",font=('Arial',20),bg='#e5e4e4',fg='black').place(x=40,y=5)

        self.cuadro = Frame(self.rpframe,bg="#515151",height=5,width=500)
        self.cuadro.place(x=40,y=45)
        
        self.etiqueta2 = Label(self.rpframe,text="Primer Nombre:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=40,y=90)

        self.pnombre = ttk.Entry(self.rpframe,font=('Arial',12),width=15)
        self.pnombre.config(validate='key',validatecommand=(self.rpframe.register(self.validate_entry),"%S"))
        self.pnombre.place(x=40,y=130)

        self.etiqueta3 = Label(self.rpframe,text="Segundo Nombre:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta3.place(x=200,y=90)

        self.snombre = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)
        self.snombre.config(validate='key',validatecommand=(self.rpframe.register(self.validate_entry),"%S"))
        self.snombre.place(x=200,y=130)

        self.etiqueta2 = Label(self.rpframe,text="Primer Apellido:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=360,y=90)

        self.papellido = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)
        self.papellido.config(validate='key',validatecommand=(self.rpframe.register(self.validate_entry),"%S"))
        self.papellido.place(x=360,y=130)

        self.etiqueta2 = Label(self.rpframe,text="Segundo Apellido:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=520,y=90)

        self.sapellido = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)
        self.sapellido.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry),"%S"))
        self.sapellido.place(x=520,y=130)

        self.etiqueta2 = Label(self.rpframe,text="Edad:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=40,y=200)

        self.edad = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)        
        self.edad.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry2),"%S"))
        self.edad.place(x=40,y=240)

        self.etiqueta2 = Label(self.rpframe,text="Cedula:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=200,y=200)

        self.cedula = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)
        self.cedula.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry2),"%S"))
        self.cedula.place(x=200,y=240)

        self.etiqueta2 = Label(self.rpframe,text="Nro de Telefono:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=360,y=200)

        self.ntelefono = ttk.Entry(self.rpframe,font=('Arial','12'),width=15)
        self.ntelefono.config(validate='key',validatecommand=(self.rpframe.register(self.validate_entry2 ),"%S"))
        self.ntelefono.place(x=360,y=240)
        
        self.etiqueta2 = Label(self.rpframe,text="Tipo:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=520,y=200)
        
        self.propiedad = ttk.Combobox(self.rpframe,font=('Arial','12'),width=15,values=("propietario","inquilino"))
        self.propiedad.config(state="readonly")
        self.propiedad.place(x=520,y=240)

        self.boton1 = Button(self.rpframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Registrar",bd=0,command= lambda : self.validar_persona())
        self.boton1.place(x=400,y=350)

        self.boton2 = Button(self.rpframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="limpiar",bd=0,command= lambda : self.limpiar(self.cedula,self.pnombre,self.snombre,self.papellido,self.sapellido,self.ntelefono,self.edad))
        self.boton2.place(x=100,y=350)
    

    def limpiar(self,entry,entry2,entry3,entry4,entry5,entry6,entry7):
            entry.delete("0","end")
            entry2.delete("0","end")
            entry3.delete("0","end")
            entry4.delete("0","end")
            entry5.delete("0","end")
            entry6.delete("0","end")
            entry7.delete("0","end")

    def limpiar2(self,entry,entry2,entry3):
            entry.delete("0","end")
            entry2.delete("0","end")
            entry3.delete("0","end")

    def limpiar3(self,entry,entry2,entry3):
         entry.delete("0","end")
         entry2.delete("1.0","end")
         entry3.delete("0","end")

    #ra = registro apartamento
    def frame_de_ra(self,master):
        

        self.raframe = Frame(master,bg="#e5e4e4")
        self.raframe.place(x=200)
        self.raframe.config(height=500,width=700)

        self.etiqueta1  = Label(self.raframe,text="Registro de Apartamentos",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.etiqueta1.place(x=40,y=5)

        self.cuadro = Frame(self.raframe,bg="#025895",height=5,width=500)
        self.cuadro.place(x=40,y=45)
        
        self.etiqueta2 = Label(self.raframe,text="Nro de apartamento:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=40,y=90)

        self.nroaparta = ttk.Entry(self.raframe,font=('Arial',12),width=15)
        self.nroaparta.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry2),"%S"))
        self.nroaparta.place(x=40,y=120)

        self.etiqueta3 = Label(self.raframe,text="Propietario del Apto:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta3.place(x=250,y=90)

        r = self.controlador.consulta_propietario("propietario")
        self.entrada1 = ttk.Combobox(self.raframe,font=('Arial',12),width=15,values=(r))
        self.entrada1.config(state="readonly")
        self.entrada1.place(x=250,y=120)

        self.etiqueta2 = Label(self.raframe,text="Inquilino del Apto:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=450,y=90)

        r2 = self.controlador.consulta_propietario("inquilino")
        self.entrada2 = ttk.Combobox(self.raframe,font=('Arial',12),width=15,values=(r2))
        self.entrada2.config(state="readonly")
        self.entrada2.place(x=450,y=120)
        
        


        self.boton1 = Button(self.raframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Registrar",bd=0,command= lambda : self.validar_apartamento() )
        self.boton1.place(x=400,y=350)

        self.boton2 = Button(self.raframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="limpiar",bd=0,command= lambda : self.limpiar2(self.nroaparta,self.entrada1,self.entrada2))
        self.boton2.config(width=20)
        self.boton2.place(x=100,y=350)

        
    #ri  = registro ingreso
    def frame_de_ri(self,master):

                        
        self.riframe = Frame(master,bg="#e5e4e4")
        self.riframe.place(x=200)
        self.riframe.config(height=500,width=700)

        self.etiqueta1  = Label(self.riframe,text="Registro de Ingresos",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.etiqueta1.place(x=40,y=5)

        self.cuadro = Frame(self.riframe,bg="#bd8902",height=5,width=500)
        self.cuadro.place(x=40,y=45)
        
        self.etiqueta2 = Label(self.riframe,text="Apartamento:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=50,y=90)

        r = self.controlador.Consulta_apartamento()
        self.aparta = ttk.Combobox(self.riframe,font=('Arial',12),width=15,values=(r))
        self.aparta.config(state="readonly")
        self.aparta.place(x=50,y=120)

        self.etiqueta3 = Label(self.riframe,text="Fecha:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta3.place(x=250,y=90)

        self.calendario = DateEntry(self.riframe,font=('Arial',12),width=15,selectmode = 'day')
        self.calendario.config(state="readonly")
        self.calendario.place(x=250,y=120)
    
        self.etiqueta2 = Label(self.riframe,text="Tipo de Pago:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=450,y=90)

        self.tipo = ttk.Combobox(self.riframe,font=('Arial',12),width=15,values=("pago-condominio"))
        self.tipo.config(state="readonly")
        self.tipo.place(x=450,y=120)

        self.etiqueta2 = Label(self.riframe,text="seleccione los meses a pagar",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=50,y=170)

        self.entrada1 = Button(self.riframe,font=('Arial',12),fg='white',bg='#0040FF',width=8,height=1,text="Meses",bd=0,command= lambda : self.seleccion_mesees())
        self.entrada1.place(x=50,y=200)

        self.pantallames = ttk.Entry(self.riframe,font=('Arial',12),width=50)
        self.pantallames.config(takefocus=False)
        self.pantallames.place(x=150,y=200)

        self.divisa = Label(self.riframe,text="Conversor de Moneda:",font='Arial,12',bg='#e5e4e4')
        self.divisa.place(x=50,y=260)

        self.cambio = Button(self.riframe,font=('Arial',12),fg='white',bg='#0040FF',width=8,height=1,text="Conversor",bd=0,command= lambda : [calculos.sistema_de_monedas(),self.insertar()])
        self.cambio.place(x=50,y=290)
        
        self.etiqueta2 = Label(self.riframe,text="Cantidad de dinero:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=250,y=260)
        
        self.dinero= ttk.Entry(self.riframe,font=('Arial',12),width=15)
        self.dinero.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry2),"%S"))
        self.dinero.place(x=250,y=290)        

        self.boton1 = Button(self.riframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Registrar",bd=0,command= lambda : self.validar_pagos())
        self.boton1.config(width=20)
        self.boton1.place(x=400,y=350)
        
        
        
        


    def generar_pdf(self):
        a = self.aparta.get()
        b = self.calendario.get_date()         
        c = self.tipo.get()
        d = self.pantallames.get()
        e = self.dinero.get()
        info = {"dinero":f"{e}","concepto":f"{c}","apto":f"{a}","meses":f"{d}"}
        ruta_template = "./pdf/1template.html"

        crea_pdf(f"{b}",ruta_template,info)

    def generar_pdf2(self):
        a = self.calendario2.get_date()
        b = self.texto.get("1.0","end")
        c = self.dinero2.get()
        info = {"fecha":f"{a}","dinero":f"{c}","concepto":f"{b}"}
        ruta_template = "./pdf/2template.html"
        crea_pdf2(f"{a}",ruta_template,info)

    def validate_entry(self,text):
        return text.isalpha()
    
    def validate_entry2(self,text):
        return text.isdigit()
    
    def seleccion_mesees(self):
        self.root = Toplevel()
        self.root.title("seleccion de meses")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.config(bg="#e5e4e4")
        
        self.texto = Label(self.root,text="Selecciona los meses que desees registrar",font='Arial,12',bg='#e5e4e4',fg="black")
        self.texto.place(x=114,y=30)


        self.ene = Button(self.root,text="enero",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("enero"))
        self.ene.config(width=10)
        self.ene.place(x=50,y=80)

        self.fe = Button(self.root,text="febrero",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("febrero"))
        self.fe.config(width=10)
        self.fe.place(x=150,y=80)

        self.mar = Button(self.root,text="marzo",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("marzo"))
        self.mar.config(width=10)
        self.mar.place(x=250,y=80)

        self.ab = Button(self.root,text="abril",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("abril"))
        self.ab.config(width=10)
        self.ab.place(x=350,y=80)

        self.may = Button(self.root,text="mayo",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("mayo"))
        self.may.config(width=10)
        self.may.place(x=50,y=130)

        self.jun = Button(self.root,text="junio",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("junio"))
        self.jun.config(width=10)
        self.jun.place(x=150,y=130)

        self.jul = Button(self.root,text="julio",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("julio"))
        self.jul.config(width=10)
        self.jul.place(x=250,y=130)

        self.agos = Button(self.root,text="agosto",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("agosto"))
        self.agos.config(width=10)
        self.agos.place(x=350,y=130)

        self.sep = Button(self.root,text="septiembre",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("septiembre"))
        self.sep.config(width=10)
        self.sep.place(x=50,y=180)
                
        self.oc = Button(self.root,text="octubre",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("octubre"))
        self.oc.config(width=10)
        self.oc.place(x=150,y=180)
        
        self.oc = Button(self.root,text="noviembre",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("noviembre"))
        self.oc.config(width=10)
        self.oc.place(x=250,y=180)
        
        self.oc = Button(self.root,text="diciembre",bg='#0040FF',fg='white',command= lambda : self.insetar_mes("diciembre"))
        self.oc.config(width=10)
        self.oc.place(x=350,y=180)
        


    #re = registro egreso
    def frame_de_re(self,master):
        self.reframe = Frame(master,bg="#e5e4e4")
        self.reframe.place(x=200)
        self.reframe.config(height=500,width=700)


        self.etiqueta1  = Label(self.reframe,text="Registro de Retiros",font=('Arial',20),bg='#e5e4e4',fg='black')
        self.etiqueta1.place(x=40,y=5)

        self.cuadro = Frame(self.reframe,bg="#982719",height=5,width=500)
        self.cuadro.place(x=40,y=45)
        
        self.etiqueta2 = Label(self.reframe,text="Fecha del Retiro:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta2.place(x=50,y=90)

        self.calendario2 = DateEntry(self.reframe,font=('Arial','12'),width=15,selectmode = 'day')
        self.calendario2.config(state="readonly")
        self.calendario2.place(x=50,y=130)

        self.etiqueta1  = Label(self.reframe,text="Concepto de Retiro:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta1.place(x=50,y=180)

        self.texto  = Text(self.reframe,font=('Arial','12'))
        self.texto.config(width=50,height=6)
        self.texto.place(x=50,y=220)
        
        self.etiqueta1  = Label(self.reframe,text="Cantidad del Retiro:",font='Arial,12',bg='#e5e4e4')
        self.etiqueta1.place(x=260,y=90)
        
        self.dinero2= ttk.Entry(self.reframe,font=('Arial',12),width=15)        
        self.dinero2.config(validate='key',validatecommand=(self.riframe.register(self.validate_entry2),"%S"))
        self.dinero2.place(x=260,y=130)    

        self.rbton = Button(self.reframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Registrar",bd=0,command= lambda : self.Validar_egresos())
        self.rbton.place(x=400,y=350)

        self.boton2 = Button(self.reframe,font=('Arial','12'),bg='#0040FF',fg='white',width=20,height=1,text="Limpiar",bd=0,command= lambda : self.limpiar3(self.calendario2,self.texto,self.dinero2))
        self.boton2.place(x=100,y=350)

    

    def indi_frame(self,fr):
        self.rpframe.destroy()
        self.raframe.destroy()
        self.riframe.destroy()
        self.reframe.destroy()
        fr(self.fregistro)

    


    #metodos con funcionalidad

    def validar_persona(self):
         a = self.cedula.get()
         b = self.pnombre.get()
         c = self.snombre.get()
         d = self.papellido.get()
         e = self.sapellido.get()
         f = self.ntelefono.get()
         g = self.edad.get()
         h = self.propiedad.get()

         if a == "" or b == "" or c== "" or d =="" or e =="" or f == "" or g =="":
              messagebox.showerror("ERROR", "Debe ingresar todos los campos")
         if "-" in g  or '-' in f:
              messagebox.showerror("ERROR", "no se admiten numeros negativos")
         if not b.isalpha() or not c.isalpha() :
            messagebox.showerror("ERROR", "no se admiten numeros en casillas alphabeticas")
            
         else:        
             self.controlador.Registrar_persona(b,c,d,e,a,f,h,g)

    
    def validar_pagos(self):
         a = self.aparta.get()
         b = self.calendario.get_date()
         
         c = self.tipo.get()
         d = self.pantallames.get()
         e = self.dinero.get().replace(".",",")

         if a == "" or b == "" or c== "" or d =="" or e =="":
              messagebox.showerror("ERROR", "Debe ingresar todos los campos")
         if "-" in e :
              messagebox.showerror("ERROR", "no se admiten numeros negativos")
         else:
             
             self.controlador.Registrar_pagos(int(a),b,c,d,float(e))
             answer = askyesno(title='PDF',message="quieres generar un pdf de esta pago?")
             if answer:
                  self.generar_pdf()
             g = generic(self.controlador)
             g.mensualidad(a,d,b)

    
    def validar_apartamento(self):
         a = self.nroaparta.get()
         b = self.entrada1.get()
         c = self.entrada2.get()
            
         if a == "" or b == "" or c== "" :
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
         if "-" in a :
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
         else:        
               
               self.controlador.Registro_propietario(int(a),b,c) 
               self.controlador.Registro_tabla_mensualidad(int(a))
    

    def Validar_egresos(self):
         a = self.calendario2.get_date()
         b = self.texto.get("1.0","end")
         c = self.dinero2.get()
         self.ingresos = 0;
        
         if a == "" or b == "" or c== "" :
                messagebox.showerror("ERROR", "Debe ingresar todos los campos")
         if "-" in c :
                messagebox.showerror("ERROR", "no se admiten numeros negativos")
         else:        
            r = self.controlador.consulta_ingresos()
            for cr  in r:
                self.ingresos = self.ingresos + sum(cr)

            if int(c) > self.ingresos:
                messagebox.showwarning(title="AVISO",message="SALDO INSUFICIENTE")

            if int(c) < self.ingresos:
                self.controlador.registrar_egreso(a,b,float(c))

                answer = askyesno(title='PDF',message="quieres generar un pdf del egreso ?")
                if answer:
                    self.generar_pdf2()

    




    def insertar(self):
         self.dinero.insert(0,calculos.resultado)


    def insetar_mes(self,mes):
         self.pantallames.insert(0,"-"+mes)
         
