from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from util.generic import *
from sql.motor_inicio import Registrar_usuario


class registro_usuario:
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.title("Registro de Usuario")
        self.ventana.geometry("500x500")
        self.ventana.config(bg='#DADCE7')
        self.ventana.resizable(0,0)
        
        self.form_frame(self.ventana)
        self.ventana.mainloop()

    def form_frame(self,master):

        self.lb1 = Label(master,text="Registro de Usuario",font=('Arial Black Bold', 20), fg="#00081d", bg="#DADCE7", pady=25)
        self.lb1.pack(fill='y')

        self.lb2 = Label(master,text="Usuario:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="center")
        self.lb2.pack(fill='x',padx=20,pady=5)

        self.usuario =Entry(master, font=('Arial', 15))
        self.usuario.pack(fill='x',padx=20, pady=10)


        self.lb2 = Label(master,text="Contraseña:", font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="center")
        self.lb2.pack(fill='x',padx=20,pady=5)
        
        self.contra =Entry(master, font=('Arial', 15))
        self.contra.pack(fill='x',padx=20, pady=10)
        self.contra.config(show="*")
        
        self.lb2 = Label(master,text='Seleccione el "Tipo de Permiso Para Usuario"', font=('Arial, 12'), fg="#00081d",bg='#DADCE7', anchor="w")
        self.lb2.pack(padx=20,pady=5)

        self.combo = ttk.Combobox(master,width=10,font=('Arial', 15))
        self.combo['values'] = ('admin','presidente','tesorero')
        self.combo.config(state="readonly")
        self.combo.pack(fill='x',padx=20,pady=8)
        
        
        self.boton2 = Button(master,text="Confirmar",font=('bold',15),fg='white',bd=0,bg="#0040FF",activebackground='#00081d',activeforeground='white',command= lambda : Registrar_usuario(self.usuario.get(),self.contra.get(),self.combo.get()))
        self.boton2.config(width=10)
        self.boton2.pack(side=RIGHT,padx=70,pady=60)
