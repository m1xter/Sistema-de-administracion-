from tkinter import *
import sys
from .Mainframe import mainframe
from Paneles.homeframe import homeframe
from  Paneles.actualizarframe import Actualizarframe as Actualizar
from Paneles.eliminarframe import Eliminarframe as eliminar
from Paneles.registroframe import registro
from sql.motor_inicio import *
from util.generic import *
from subprocess import call
from tkinter.messagebox import askyesno, askquestion
from Paneles.Generargframe import MenuOpciones
class Ventana:

    def __init__(self,controlador,r):        
        self.root = Tk()
        self.root.title("sistema de condominio")
        self.root.geometry("1000x500")
        self.root.resizable(0,0)

        self.root.protocol("WM_DELETE_WINDOW",self.cierre)


        ruta = self.rutas('Imgs\condominio_logo.ico')
        
        self.root.iconbitmap(ruta)
        
        self.r = r
        self.controlador = controlador

        
        self.menu(self.root)
        self.bienvenido(self.root)
        self.mframe = mainframe(self.root)
        self.mframe.indicador(homeframe,self.controlador)
        self.mostrar_usuario(self.root)
        self.saldo_total(self.root)
        self.root.mainloop()

    def rutas(self,ruta):
         try:
            rutabase = sys.__MEIPASS
         except Exception:
              rutabase = os.path.abspath(".")
         return os.path.join(rutabase,ruta)
    

    def cierre(self):
        answer = askyesno(title="confimacion",message="seguro que quieres cerrar el programa ? ")

        if answer:
            call('/xampp/xampp_stop.exe')
            self.root.destroy()
        
    

    #Acá definí el frame para mostrar el bienvenido para x usuario
    def bienvenido(self,master):
        options_frame = Frame(master,bg="#001345")
        options_frame.pack(side=TOP)
        options_frame.pack_propagate(False)
        options_frame.config(width=1000,height=40)
        #self.info(options_frame)

        #self.etiqueta  = Label(options_frame,text="saldo total ", font=('bold',10), bg='#e5e4e4')
        #self.etiqueta.place(x=650,y=10)


    def saldo_total(self,master):
        

        self.ingresos = 0
        r = self.controlador.consulta_ingresos()
        for cr  in r:
            self.ingresos = self.ingresos + sum(cr)


        self.egresos = 0
        e = self.controlador.consulta_egresos()
        for ce  in e:
            self.egresos = self.egresos + sum(ce)

        self.saldo_mes = self.ingresos - self.egresos

        if self.saldo_mes < 0:
            messagebox.showwarning(title="AVISO",message=("saldo insuficiente"))
            
            
        if self.saldo_mes > 0:
            self.controlador.update_saldo_condo(self.saldo_mes)

        self.lb_saldo = Label(master,text="Saldo Total:  "+" "+f"{self.saldo_mes}"+"  COP")
        self.lb_saldo.config(font=("Arial",13),bg='#001345',fg='white')
        self.lb_saldo.place(x=700,y=10)


    def mostrar_usuario(self,master):

        
        re = self.r
        for ct in re:
            self.lb_usu = Label(master,text="usuario:  "+ct[0]+"   "+"permisos:  "+ct[1])
            self.lb_usu.config(font=("Arial",13),bg='#001345',fg='white')
            self.lb_usu.place(x=150,y=10)
            

        






    def menu(self,master):
        options_frame = Frame(master,bg="#00081d")
        options_frame.pack(side=LEFT)
        options_frame.pack_propagate(False)
        options_frame.config(width=110,height=500)
        self.botones(options_frame)
        
    def hide_indicator(self):
        self.home_indicator.config(bg="#777EA6")
        self.registrar_indicator.config(bg="#777EA6")
        self.mensualidad_indicator.config(bg="#777EA6")
        self.generar_indicator.config(bg="#777EA6")
        
        self.opciones_indicator.config(bg="#777EA6")
    
    def indi(self,lb):
        self.hide_indicator()
        lb.config(bg="#FB9062")

    #BOTONES DEL MENU
    def botones(self,master):
        
        #LABEL QUE MUESTRA EL LOGO
        ruta = self.rutas(".\Imgs\condominio_logo.png")
        self.logom = generic.leer_imagen(ruta,(100,80))
        
        self.logo_menu = Label(master,image=self.logom, bg='#00081d')
        self.logo_menu.place(x=2,y=15)
        
        
        #BOTON DE HOME
        self.home_btn = Button(master,text="Home",font=('bold',12),fg='#ffffff',bd=0,bg="#001345",anchor='w', activebackground='#00081d',activeforeground='#FB9062',command= lambda : [self.mframe.indicador(homeframe,self.controlador),self.indi(self.home_indicator,),self.saldo_total(self.root)] )
        self.home_btn.config(width=11, height=1)
        self.home_btn.place(x=8,y=120)
        #SELECCIÓN DE BOTON DE HOME
        self.home_indicator = Label(master,text=' ',bg="#777EA6")
        self.home_indicator.place(x= 3,y=120,width=5,height=30)

        #BOTON DE REGISTRO
        self.registrar_btn = Button(master,text="Registrar",font=('bold',12),fg='#ffffff',bd=0,bg="#001345", anchor='w',activebackground='#00081d',activeforeground='#FB9062',command= lambda :[ self.mframe.indicador(registro,self.controlador),self.indi(self.registrar_indicator),self.saldo_total(self.root)])
        self.registrar_btn.config(width=11, height=1)
        self.registrar_btn.place(x=8,y=160)
        #SELECCIÓN DE BOTON DE REGISTRO
        self.registrar_indicator = Label(master,text=' ',bg="#777EA6")
        self.registrar_indicator.place(x= 3,y=160,width=5,height=30)
        
        #BOTON DE MENSUALIDAD
        self.mensualidad_btn = Button(master,text="Actualizar",font=('bold',12),fg='#ffffff',bd=0,bg="#001345",anchor='w',activebackground='#00081d',activeforeground='#FB9062',
        command= lambda : [self.mframe.indicador(Actualizar,self.controlador),self.indi(self.mensualidad_indicator)] )
        self.mensualidad_btn.config(width=11, height=1)
        self.mensualidad_btn.place(x=8,y=200)
        #SELECCIÓN DE BOTON DE MENSUALIDAD
        self.mensualidad_indicator = Label(master,text=' ',bg="#777EA6")
        self.mensualidad_indicator.place(x= 3,y=200,width=5,height=30)
        
        #BOTON DE GENERAR
        self.generar_btn = Button(master,text="Eliminar",font=('bold',12),fg='#ffffff',bd=0,bg="#001345", anchor='w', activebackground='#00081d',activeforeground='#FB9062',command= lambda :[ self.mframe.indicador(eliminar,self.controlador),self.indi(self.generar_indicator)])
        self.generar_btn.config(width=11, height=1)
        self.generar_btn.place(x=8,y=240)
        #SELECCIÓN DE BOTON DE GENERAR
        self.generar_indicator = Label(master,text=' ',bg="#777EA6")
        self.generar_indicator.place(x= 3,y=240,width=5,height=30)      


        #BOTON DE GENERAR
        self.opciones_btn = Button(master,text="Opciones",font=('bold',12),fg='#ffffff',bd=0,bg="#001345", anchor='w', activebackground='#00081d',activeforeground='#FB9062',command= lambda :[ self.mframe.indicador(MenuOpciones,self.controlador),self.indi(self.opciones_indicator)])
        self.opciones_btn.config(width=11, height=1)
        self.opciones_btn.place(x=8,y=280)
        #SELECCIÓN DE BOTON DE GENERAR
        self.opciones_indicator = Label(master,text=' ',bg="#777EA6")
        self.opciones_indicator.place(x= 3,y=280,width=5,height=30)      
        
        
        


        #BOTON DE SALIR        
        self.salir_btn = Button(master,text="Salir",font=('bold',12),fg='#ffffff',bd=0,bg="#001345",anchor='w',activebackground='#00081d',activeforeground='#FB9062',
        command= lambda : [self.indi(self.opciones_indicator),call('/xampp/xampp_stop.exe'),sys.exit()] )
        self.salir_btn.config(width=11, height=1)
        self.salir_btn.place(x=7,y=430)
        #SELECCIÓN DE BOTON DE OPCIONES
        self.salir_indicator = Label(master,text=' ',bg="#777EA6")
        self.salir_indicator.place(x= 3,y=430,width=5,height=30)
    
    def set_controlador(self,controlador):
        self.controlador = controlador