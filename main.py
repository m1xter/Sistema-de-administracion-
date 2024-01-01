# el programa se corre desde aqui 
from Principal.Window import Ventana
from sesion.login import loginventana
from subprocess import call

#para mira que usuarios hay creados solo ve a la tabla usuario  mira el tipo de permiso que tiene y inicia sesion con ese 
#usuario y ya 
call('/xampp/xampp_start.exe')
loginventana()  