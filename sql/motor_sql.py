from tkinter import messagebox
import pymysql 
from pymysql.err import *
from pymysql import Error
from util.generic import *
from datetime import date
from datetime import datetime
import calendar,datetime


class motorsql():


    #constructor de la clase motor_sql
    def __init__(self,tipo_permiso):
         self.tipo_permiso = tipo_permiso

    def definir_permisos(self,tipo_permiso):

        if tipo_permiso == "admin":
            conexion = pymysql.connect( host="localhost", user="root", passwd="", db="condominio_bd")            
            return conexion
        if tipo_permiso == "presidente":
            conexion = pymysql.connect( host="localhost", user="admin_a3", passwd="condominioa3", db="condominio_bd")
            return conexion
        if tipo_permiso == "tesorero":
            conexion = pymysql.connect( host="localhost", user="user_a3", passwd="condominioa3", db="condominio_bd")
            return conexion


    
    #REGISTROS//////////////////////////////////////////////////////////////////////////////////////////////////
    def Registrar_usuario(self,usu,contra,admin):
        

        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        
        try:
            sql = "INSERT INTO usuarios(nombre_usuario,contrasena,permisos) values('{0}','{1}','{2}')".format(usu,contra,admin)
            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Registro exitoso",title="Aviso")    
        except Error as e:
            return e
            
        


    def Registrar_persona(self,p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()

        
        try:
            sql = "INSERT INTO personas(primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,cedula,nro_telefono,tipo,edad) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad)
            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Registro exitoso",title="Aviso")    
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.self.manejo_errores(code,mesage)



    def Registro_propietario(self,nroapa,propi,inqui):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
                sql = "INSERT INTO apartamentos (nro_aparta,Propietario,Inquilino) VALUES ('{0}','{1}','{2}')".format(nroapa,propi,inqui)
                fcursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo(message="Registro exitoso",title="Aviso")    
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)
    


    def Registrar_pagos(self,nroapa,fecha,tipo,mes,cant):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
                sql="INSERT INTO ingresos (nro_apartamento,fecha,tipo_pago,meses,cant_dinero) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(nroapa,fecha,tipo,mes,cant)
                fcursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo(message="Registro exitoso",title="Aviso")
                
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage)
    


    def Registrar_pagos(self,nroapa,fecha,tipo,mes,cant):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
                sql="INSERT INTO ingresos (nro_apartamento,fecha,tipo_pago,meses,cant_dinero) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(nroapa,fecha,tipo,mes,cant)
                fcursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo(message="Registro exitoso",title="Aviso")    
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage)


    
    def registrar_egreso(self,fecha,texto,cantidad):
         
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()

        try:
                sql  = "INSERT INTO egresos (fecha,causa,cant_retirada) VALUES ('{0}','{1}','{2}')".format(fecha,texto,cantidad)
                fcursor.execute(sql)
                con.commit()
                con.close() 
                messagebox.showinfo(message="Registro exitoso",title="Aviso")        
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage) 
            
        
    
    

    def Registro_tabla_mensualidad(self,nroapa):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        enero = ''
        febrero = ''
        marzo = ''
        abril = ''
        mayo = ''
        junio = ''
        julio = ''
        agosto = ''
        septiembre = ''
        octubre = ''
        noviembre = ''
        diciembre = ''

        try:
                sql = f"INSERT INTO mensualidad  (apartamento,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre) VALUES ('{nroapa}','{enero}','{febrero}','{marzo}','{abril}','{mayo}','{junio}','{julio}','{agosto}','{septiembre}','{octubre}','{noviembre}','{diciembre}')"

                fcursor.execute(sql)
                con.commit()
                con.close()                
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)


    
    #CONSULTAS//////////////////////////////////////////////////////////////////
    def consulta_propietario(self,inquilino):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()

        fcursor.execute("SELECT cedula FROM personas WHERE tipo= '"+inquilino+"' ")
        con.close()

        return fcursor.fetchall() 
    
    def Consulta_datos_inquilinos(self):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT * FROM `personas`")
        con.close()
        return fcursor.fetchall()

    def Consulta_apartamento(self):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT nro_aparta FROM apartamentos;")
        con.close()

        return fcursor.fetchall() 

    


    def Consulta_datos_apartamento(self):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT * FROM `apartamentos`")
        con.close()

        return fcursor.fetchall()
    
        
    def Consulta_nro_apartamento(self):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT nro_aparta FROM `apartamentos`")
        con.close()

        return fcursor.fetchall()

    def consulta_pagos(self):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT nro_apartamento,fecha,tipo_pago,meses,cant_dinero FROM ingresos")
        con.close()

        return fcursor.fetchall()

    def consulta_ingresos(self):
        
        now = datetime.datetime.now()
        
        year = now.year
        
        month = now.month
        
        calendar.monthrange(year,month)
        last_day = calendar.monthrange (year, month) [1] ## último día
        
        start = datetime.date(year,month,1)
        
        end = datetime.date(year,month,last_day)        
        



        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT cant_dinero FROM ingresos  Where fecha  BETWEEN '{start}'  AND  '{end}' ")
        con.close()

        return fcursor.fetchall()
    
        
    def consulta_egresos(self):
        
        now = datetime.datetime.now()
        
        year = now.year
        
        month = now.month
        
        
        calendar.monthrange(year,month)
        last_day = calendar.monthrange (year, month) [1] ## último día
        
        start = datetime.date(year,month,1)
        
        end = datetime.date(year,month,last_day)        
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT cant_retirada FROM egresos  Where fecha  BETWEEN '{start}'  AND  '{end}' ")
        con.close()

        return fcursor.fetchall()
    
    
    def consulta_datos_egresos(self):
         
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT * FROM egresos")
        con.close()

        return fcursor.fetchall()
    
    def consulta_datos_personas(self,cedula):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,nro_telefono,tipo,edad FROM personas WHERE cedula = '{cedula}';")
        con.close()

        return fcursor.fetchall()
    
    def consulta_datos_apartamentos(self,nro):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT  Propietario,Inquilino FROM apartamentos WHERE nro_aparta = '{nro}'")
        con.close()

        return fcursor.fetchall()
    
    def consulta_datos_ingreso(self,fecha):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT  id_ingreso,nro_apartamento,tipo_pago,meses,cant_dinero,fecha FROM ingresos WHERE fecha = '{fecha}'")
        con.close()

        return fcursor.fetchall()
    
    def consulta_datos_egreso(self,fecha):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute(f"SELECT  id_egresos,fecha,causa,cant_retirada FROM egresos WHERE fecha = '{fecha}'")
        con.close()

        return fcursor.fetchall()

    def consulta_morosos(self,mes,aparta):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT  julio FROM mensualidad WHERE apartamento = '{1}' ".format(mes,aparta))
        con.close()

        return fcursor.fetchall()

    def consulta_mensualidad(self):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        fcursor.execute("SELECT * FROM mensualidad ")
        con.close()

        return fcursor.fetchall()


    #ACTUALIZACIONES///////////////////////////////////////////
    def update_saldo_condo(self,saldo):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
                sql = "UPDATE saldo_condo SET Saldo_condominio = '{0}' WHERE id_saldo = 1;".format(saldo)
                fcursor.execute(sql)
                con.commit()
                con.close()        
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage)

    def update_moroso(self,mes,aparta,d):
        
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        
        try:
                sql = f"UPDATE   mensualidad SET  {mes} = '{d}' WHERE apartamento = '{aparta}' "
                fcursor.execute(sql)
                con.commit()
                con.close()        
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage)
    

    def update_persona(self,p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad):
         
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()

        
        try:
            sql = f"UPDATE personas SET primer_nombre = '{p_nombre}' , segundo_nombre = '{s_nombre}' , primer_apellido = '{p_apellido}',segundo_apellido = '{s_apellido}',nro_telefono = {nro_telefono} , tipo = '{tipo}',edad = '{edad}' WHERE cedula = '{cedula}' "
            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Actualizacion exitosa",title="Aviso")    
        except Error as e:     
            con.rollback()       
            code, mesage = e.args            
            self.manejo_errores(code,mesage)
    
    def update_apartamento(self,nroapa,propi,inqui):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
                sql = f"UPDATE apartamentos SET Propietario = '{propi}', Inquilino = '{inqui}' where nro_aparta = '{nroapa}'"
                fcursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo(message="Acutualizacion exitosa",title="Aviso")    
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)
    
    
    def update_ingresos(self,id,fecha,apa,meses,pago,dinero):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
            sql=f"UPDATE ingresos SET fecha = '{fecha}',nro_apartamento = '{apa}', meses = '{meses}' ,tipo_pago = '{pago}', cant_dinero = '{dinero}' WHERE id_ingreso='{id}'"
            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Acutualizacion exitosa",title="Aviso")    
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)
    


    def update_mensualidad(self,id,enero,febrero,marzo):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
            sql=f"UPDATE mensualidad  SET  enero = '{enero}'"

            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Acutualizacion exitosa",title="Aviso")    
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)


    
    def update_egresos(self,id,fecha,causa,dinero):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
            
        try:
            sql=f"UPDATE egresos SET causa = '{causa}', cant_retirada = '{dinero}',fecha = '{fecha}'  WHERE id_egresos ='{id}'"
            fcursor.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo(message="Acutualizacion exitosa",title="Aviso")    
        except Error as e:
                con.rollback()       
                code, mesage = e.args            
                self.manejo_errores(code,mesage)
    #ELIMINAR/////////////////////////////////////////////////////////////////////////////////////////
    def eliminar_Persona(self,id_persona):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        try:
            sql = f"DELETE FROM `personas` WHERE `cedula`= '{id_persona}'"
            fcursor.execute(sql)
            result = fcursor.rowcount
            fcursor.execute("commit")
            con.close()
            return result
        except Error as e:
            con.rollback()
            code,message = e.args
            self.manejo_errores(code,message)

    def eliminar_aparta(self,id_aparta):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        try:
            sql = f"DELETE FROM `apartamentos` WHERE `nro_aparta`= '{id_aparta}'"
            fcursor.execute(sql)
            result = fcursor.rowcount
            fcursor.execute("commit")
            con.close()
            return result
        except Error as e:
            con.rollback()
            code,message = e.args
            self.manejo_errores(code,message)

    def eliminar_ingreso(self,id):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        try:
            sql = f"DELETE FROM `ingresos` WHERE `id_ingreso`= '{id}' "
            fcursor.execute(sql)
            result = fcursor.rowcount
            fcursor.execute("commit")
            con.close()
            return result
        except Error as e:
            con.rollback()
            code,message = e.args
            self.manejo_errores(code,message)
    
    def eliminar_egreso(self,id):
        con = self.definir_permisos(self.tipo_permiso)
        fcursor = con.cursor()
        try:
            sql = f"DELETE FROM `egresos` WHERE `id_egresos`= '{id}'"
            fcursor.execute(sql)
            result = fcursor.rowcount
            fcursor.execute("commit")
            con.close()
            return result
        except Error as e:
            con.rollback()
            code,message = e.args
            self.manejo_errores(code,message)




    
    def manejo_errores(self,code,mesage):            
            if code == 1142:
                messagebox.showinfo(message="No tienes los permisos suficientes para realizar esta operacion",title="Aviso")
            if code == 2003:
                messagebox.showinfo(message="Por favor active Xampp para poder usar el programa",title="Aviso")
            if code == 10061:
                messagebox.showinfo(message="Por favor active Xampp para poder usar el programa",title="Aviso")
            
            else:
                messagebox.showinfo(code,mesage)