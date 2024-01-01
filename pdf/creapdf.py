import jinja2
import pdfkit
import os
from tkinter import filedialog
from tkinter import messagebox


    

def crea_pdf(fecha,ruta_template,info,rutacc=""):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {'page-size': 'Letter','margin-top':'0.05in','margin-right':'0.05in','margin-left':'0.05in','margin-bottom':'0.05in','encoding':'UTF-8'}
    
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') 
    
    
    my_dir = filedialog.askdirectory()
    ruta_salida= my_dir+f"/ingreso_factura{fecha}.pdf"    
    pdfkit.from_string(html,ruta_salida,css=rutacc,options=options,configuration=config)
    messagebox.showinfo(title="PDF",message="el PDF se ha creado correctamente")
    


def crea_pdf2(fecha,ruta_template,info,rutacc=""):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {'page-size': 'Letter','margin-top':'0.05in','margin-right':'0.05in','margin-left':'0.05in','margin-bottom':'0.05in','encoding':'UTF-8'}
    
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') 
    
    
    my_dir = filedialog.askdirectory()
    ruta_salida= my_dir+f"/comprobante_retido{fecha}.pdf"    
    pdfkit.from_string(html,ruta_salida,css=rutacc,options=options,configuration=config)
    messagebox.showinfo(title="PDF",message="el PDF se ha creado correctamente")
    


   