from sql.motor_sql import *


class Controlador():
    def __init__(self, modelo):
        self.modelo = modelo
    #REGISTROS///////////////////////////////////////
    def Registrar_usuario(self,usu,contra,admin):
        info = self.modelo.Registrar_usuario(usu,contra,admin)
        return info
    
    def Registrar_persona(self,p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad):
        info = self.modelo.Registrar_persona(p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad)
        return info
    
    
    def Registro_propietario(self,nroapa,propi,inqui):
        info = self.modelo.Registro_propietario(nroapa,propi,inqui)
        return info
    
    def registrar_egreso(self,fecha,texto,cantidad):
        info = self.modelo.registrar_egreso(fecha,texto,cantidad)
        return info

    
    def Registrar_pagos(self,nroapa,fecha,tipo,mes,cant):
        info = self.modelo.Registrar_pagos(nroapa,fecha,tipo,mes,cant)
        return info
    
    def Registro_tabla_mensualidad(self,nroapa):
        info = self.modelo.Registro_tabla_mensualidad(nroapa)
        return info

    #CONSULTAS////////////////////////////////////////////////
    def Consulta_apartamento(self):
        info = self.modelo.Consulta_apartamento()
        return info
    
    def consulta_datos_inquilinos(self):
        info = self.modelo.Consulta_datos_inquilinos()
        return info
    
    def consulta_pagos(self):
        info = self.modelo.consulta_pagos()
        return info
    
    def consulta_saldo_condo(self):
        info = self.modelo.consulta_saldo_condo()
        return info
    
    def consulta_propietario(self,inquilino):
        info =  self.modelo.consulta_propietario(inquilino)
        return info
    
    def Consulta_datos_apartamento(self):
        info = self.modelo.Consulta_datos_apartamento()
        return info
    
    def consulta_ingresos(self):
        info = self.modelo.consulta_ingresos()
        return info
    
    def consulta_egresos(self):
        info = self.modelo.consulta_egresos()
        return info
    
    def consulta_datos_egresos(self):
        info = self.modelo.consulta_datos_egresos()
        return info
    
    def consulta_datos_personas(self,cedula):
        info = self.modelo.consulta_datos_personas(cedula)
        return info
    
    def consulta_datos_apartamentos(self,nro):
        info = self.modelo.consulta_datos_apartamentos(nro)
        return info

    def consulta_datos_ingreso(self,fecha):
        info  = self.modelo.consulta_datos_ingreso(fecha)
        return info
    
    def consulta_datos_egreso(self,fecha):
        info  = self.modelo.consulta_datos_egreso(fecha)
        return info

    def consulta_nro_apartamento(self):
        info = self.modelo.Consulta_nro_apartamento()
        return info
    
    def consulta_morosos(self,mes,id_aparta):
        info = self.modelo.consulta_morosos(mes,id_aparta)
        return info
    def consulta_mensualidad(self):
        info = self.modelo.consulta_mensualidad()
        return info

    #ACTUALIZACIONES//////////////////////////////////  
    def update_saldo_condo(self,saldo):
        info = self.modelo.update_saldo_condo(saldo)
        return info
    def update_moroso(self,mes,aparta,d):
        info = self.modelo.update_moroso(mes,aparta,d)
        return info
    
    def update_persona(self,p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad):
        info = self.modelo.update_persona(p_nombre,s_nombre,p_apellido,s_apellido,cedula,nro_telefono,tipo,edad)
        return info

    def update_aparta(self,nroapa,propi,inqui):
        info = self.modelo.update_apartamento(nroapa,propi,inqui)
        return info
    
    def update_ingresos(self,id,fecha,apa,meses,pago,dinero):
        info = self.modelo.update_ingresos(id,fecha,apa,meses,pago,dinero)
        return info
    
    def update_egresos(self,id,fecha,causa,dinero):
        info = self.modelo.update_egresos(id,fecha,causa,dinero)
        return info
    #ELIMINAR//////////////////////////////////////////////////////////
    def eliminar_persona(self,id_persona):
        info = self.modelo.eliminar_Persona(id_persona)
        return info
    
    def eliminar_apartamento(self,id_aparta):
        info = self.modelo.eliminar_aparta(id_aparta)
        return info

    def eliminar_egreso(self,id):
        info = self.modelo.eliminar_egreso(id)
        return info
    
    def eliminar_ingreso(self,id):
        info = self.modelo.eliminar_ingreso(id)
        return info