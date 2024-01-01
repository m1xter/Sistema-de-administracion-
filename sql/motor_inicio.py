from tkinter import messagebox
import pymysql



def validacion_datos(usu,contra):
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="condominio_bd"
    )

    fcursor = bd.cursor()

    fcursor.execute("SELECT permisos FROM usuarios WHERE nombre_usuario= '"+usu+"' and contrasena='"+contra+"' ")
    f = fcursor.fetchall()
    if f:        
        for vl in f:
            for ve in vl:
                return ve

        
    else:
        messagebox.showinfo(title="inicio incorrecto",message="Usuario y contrasena no registrados por favor registrese")
        
    
    bd.close()




def mostrar_usuario(usu,contra):
     bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="condominio_bd"
    )
     
     fcursor = bd.cursor()

     fcursor.execute("SELECT nombre_usuario,permisos FROM usuarios WHERE nombre_usuario= '"+usu+"' and contrasena='"+contra+"' ")
     
     return fcursor.fetchall()
     




def busqueda_usu(usu,contra):
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="condominio_bd"
    )

    fcursor = bd.cursor()

    fcursor.execute("SELECT contrasena FROM usuarios WHERE nombre_usuario= '"+usu+"' and contrasena='"+contra+"' ")

    if fcursor.fetchall():
        messagebox.showinfo(title="inicio correcto",message="Usuario y contrasena correcta")
        return True
    else:
        messagebox.showinfo(title="inicio incorrecto",message="Usuario y contrasena no registrados por favor registrese")
        
    
    bd.close()






def definir_permisos(tipo_permiso):

    if tipo_permiso == "admin":
        bd = pymysql.connect( host="localhost", user="root", passwd="", db="condominio_bd")
        print("admin")
        return bd 
    if tipo_permiso == "presidente":
        bd = pymysql.connect( host="localhost", user="admin_a3", passwd="condominioa3", db="condominio_bd")
        return bd
    if tipo_permiso == "tesorero":
        bd = pymysql.connect( host="localhost", user="user_a3", passwd="condominioa3", db="condominio_bd")
        return bd


def Registrar_usuario(usu,contra,admin):
        
        bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="condominio_bd"
        )
    
        fcursor = bd.cursor()
        
        try:
            sql = "INSERT INTO usuarios(nombre_usuario,contrasena,permisos) values('{0}','{1}','{2}')".format(usu,contra,admin)
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso",title="Aviso")    
        except:
            bd.rollback()
            messagebox.showinfo(message="Registro fallido",title="Aviso")
        
            
        bd.close()




        