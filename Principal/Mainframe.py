from tkinter import*
from tkinter import ttk



class mainframe:

    def __init__(self,master):

        self.frame = Frame(master,bg="deep sky blue")              
        self.frame.pack(side=LEFT)
        self.frame.pack_propagate(False)
        self.frame.config(height=500,width=900)

    def clean(self):
        for frame in self.frame.winfo_children():
            frame.destroy()

    def indicador(self,page,controlador):
        self.clean()
        page(self.frame,controlador)