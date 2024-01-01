from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import datetime
import calendar,datetime
import os
import sys
#aqui declaro funciones de uso general 

class generic:
    dato = 0 
    def __init__(self,controlador):
        self.controlador = controlador
        

    def leer_imagen(path,size):
            return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

    def centrar_ventana(self,ventana,aplicacion_ancho,aplicacion_largo):
            pantalla_ancho = ventana.winfo_screenwidth()
            pantalla_largo = ventana.winfo_screenheight()
            x = int((pantalla_ancho/2) - (aplicacion_ancho/2))
            y = int((pantalla_largo/2) - (aplicacion_largo/2))
            return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")




         



    def mes(self,n):
            if n == 1:
                return "enero"
            if n == 2:
                return "febrero"
            if n == 3: 
                return "marzo"
            if n == 4:
                return "abril"
            if n == 5:
                return "mayo"
            if n == 6:
                return "junio"
            if n == 7:
                return "julio"
            if n == 8:
                return "agosto"
            if n == 9:
                return "septiembre"
            if n == 10:
                return "octubre"
            if n == 11:
                return "noviembre"
            if n == 12:
                return "diciembre"
            

    def mensualidad(self,id_aparta,meses,fecha):
                
                m = meses.split("-")
                d = "X"
                for ct in m:
                    
                    if len(ct) >0:
                        e = self.controlador.consulta_morosos(int(id_aparta),ct) 
                                                
                        if len(e) == 0 or e == "O":
                             self.controlador.update_moroso(ct,id_aparta,d)
                             


                

    def morosos(self):
            now = datetime.datetime.now()
            
            year = now.year
                
            month = now.month

            day = now.day
        
            m = self.mes(month)                        
            a = self.controlador.consulta_nro_apartamento()
            d = "O"
            for ct in a:                                
                
                e = self.controlador.consulta_morosos(m,ct[0])            
                i = e[0]  
                           
                for dt in ct:                             
                     if day > 15  and i[0] != "X" :                                           
                        self.controlador.update_moroso(m,dt,d)
                        
                     
                
                     
    
                    

                            
            


            
                
                        






            



