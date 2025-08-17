# Developers: UNIVERSIDAD
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
import subprocess
import time
from tkinter import scrolledtext

#Crear ventana
v0=Tk()
v0.title("Toolkits for Linux")
v0.geometry("800x500+100+100")

def clean():
            destino.set('')
            cuerpo.set('')
            asunto.set('')


#Zonas de funciones
def SendMail():
              ck2=str(check2.get())
              if (ck2=="" or ck2=="0"):
                                        print("Sending Email Now...")
                                        d=str(destino.get())
                                        a=str(asunto.get())
                                        c=str(cuerpo.get())
                                        enc="#!/bin/bash"
                                        e="echo"
                                        tab=" "
                                        cd='"'
                                        b="|"
                                        comando="mail -s"

                                        cadena1=(str(e)+''+str(tab)+''+str(cd)+''+str(c)+''+str(cd)+''+str(tab)+''+str(b)+''+str(tab)+''+str(comando)+''+str(tab)+''+str(cd)+''+str(a)+''+str(cd)+''+str(tab)+''+str(d))
                                        os.system("sudo chmod -R 777 /home/franklin/send.sh")
                                        pf=open("/home/franklin/send.sh","w")
                                        pf.write(enc)
                                        pf.write("\n")
                                        pf.write(cadena1)
                                        pf.write("\n")
                                        pf.close()

                                        time.sleep(0.1)

                                        #ejecutar el script
                                        os.system("sudo /./home/franklin/send.sh")
                                        clean()
                                        messagebox.showinfo("INFO",message="CORREO ENVIADO CON EXITO")

              if (ck2=="1"):
                            print("Sending Email Now...")
                            d=str(destino.get())
                            a=str(asunto.get())
                            c=str(cuerpo.get())
                            enc="#!/bin/bash"
                            e=" echo "
                            tab=" "
                            cd='"'
                            b="|"
                            comando=" | mail -s"
                            #--------------------- Variables provisional ------------------
                            ruta="cd /home/franklin/Backups"
                            v='file=$(ls -l | tail -n1 | cut -d " " -f9)'
                            ad="uuencode $file $file > /tmp/out.mail"
                            #ap=" < /tmp/out.mail"
                            llavei="{"
                            llavef="}"
                            apc=" cat /tmp/out.mail"
                            cadena0=(str(e)+''+str(cd)+''+str(c)+''+str(cd))
                            cadena1=(str(comando)+''+str(tab)+''+str(cd)+''+str(a)+''+str(cd)+''+str(tab)+''+str(d))
                            os.system("sudo chmod -R 777 /home/franklin/send2.sh")
                            pf=open("/home/franklin/send2.sh","w")
                            pf.write(enc)
                            pf.write("\n")
                            pf.write(ruta)
                            pf.write("\n")
                            pf.write(v)
                            pf.write("\n")
                            pf.write(ad)
                            pf.write("\n")
                            pf.write(llavei)
                            pf.write("\n")
                            pf.write(cadena0)
                            pf.write("\n")
                            pf.write(apc)
                            pf.write("\n")
                            pf.write(llavef)
                            pf.write(cadena1)
                            pf.write("\n")
                            pf.close()

                            time.sleep(0.1)

                            #ejecutar el script
                            os.system("sudo /./home/franklin/send2.sh")
                            clean()
                            messagebox.showinfo("INFO",message="CORREO ENVIADO CON EXITO")
                            
def EvaluarCheck1():
                    print("Listar Respaldo...")
                    ck1=str(check1.get())
                    if (ck1=="1"):
                                  os.system("sudo ls -l /home/franklin/Backups > infobak.txt")
                                  valor1=subprocess.check_output("cat /home/franklin/infobak.txt",shell=True)
                                  area1=scrolledtext.ScrolledText(v0,width=80,height=15,background="#00ccff")
                                  area1.place(x=10,y=200)
                                  area1.insert(END,valor1)
                                  
                    if (ck1=="0"):
                                  messagebox.showinfo("INFO",message="Casilla vasilla")
                                  
                    
def EvaluarCheck2():
                    print("Adjuntar Respaldo...")
                    
def CrearBK():
              os.system("sudo /./home/franklin/backupsunah.sh")
              messagebox.showinfo("INFO",message="Respaldo Creado con Exito")
              
    
# variables fonts
txt1=font.Font(family="Arial",size=18)
txt2=font.Font(family="Arial",size=12)

def EvaluarComboMenu():
                        print("Menu de opciones...")
                        cb=str(combomenu.get())
                        if (cb=="firewall"):#condicion y opcion de menu
                                            v2=Toplevel(bg="#00ccff")#crear una pantalla
                                            v2.title("Configuracion Firewall")#titulo de la pantalla
                                            v2.geometry("700x400+150+250")#tamaño de la pantalla
                                            def EvaluarRadio2():#funcion de seleccion de radiobutton
                                                                vinet2=inet2.get()#almacena el valor del radiobutton en una variable
                                                                global puerto,proto,agt#nombrar variables
                                                                agt=StringVar()#tipo de dato de la variales
                                                                puerto=StringVar()
                                                                proto=StringVar()
                                                      
                                                                if (vinet2==1):#primera condicion

                                                                    def agregar_puerto():#funcion para agregar puertos
                                                                        puerto_p=puerto.get()#variable que almacena el valor del puerto
                                                                        subprocess.run(["sudo","ufw","allow",puerto_p])#comando para agregar puerto
                                                                        messagebox.showinfo("INFO",message="Puerto agregado con exito")#mensaje de que se realizo con exito
                                                                        

                                                                    label_p=Label(v2,text="Ingrese el Puerto:",font=text_p,background="#99ffff",foreground="#0000cc").place(x=250,y=80)#objeto visual con color la caja y color la letra
                                                                    txt_puerto=Entry(v2,textvariable=puerto,width=25).place(x=420,y=80)#textbox para escritura
                                                                    label_p=Label(v2,text="Ingrese el Protocolo:",font=text_p,background="#99ffff",foreground="#0000cc").place(x=250,y=150)#objeto visual con color la caja y color la letra
                                                                    txt_proto=Entry(v2,textvariable=proto,width=25).place(x=420,y=150)#textbox para escritura
                                                                    bnt_agregar=Button(v2,text="Agregar Puerto",font=text_b,background="#3366ff",foreground="#00ffff",command=agregar_puerto).place(x=420,y=260)#button que completa la tarea
                                                                    
                                                                if (vinet2==2):#segunda condicion
                                                                    def eliminar_puerto():#funcion para eliminar puertos
                                                                        puerto_p=puerto.get()#variable que almacena el valor del puerto
                                                                        subprocess.run(["sudo","ufw","delete","allow",puerto_p])#comando para agregar puerto
                                                                        messagebox.showinfo("INFO",message="Puerto eliminado con exito")#mensaje de que se realizo con exito
                                                                        
                                                                    label_p=Label(v2,text="Ingrese el Puerto:",font=text_p,background="#99ffff",foreground="#0000cc").place(x=250,y=80)#objeto visual con color la caja y color la letra
                                                                    txt_puerto=Entry(v2,textvariable=puerto,width=25).place(x=420,y=80)#textbox para escritura
                                                                    label_p=Label(v2,text="Ingrese el Protocolo:",font=text_p,background="#99ffff",foreground="#0000cc").place(x=250,y=150)#objeto visual con color la caja y color la letra
                                                                    txt_proto=Entry(v2,textvariable=proto,width=25).place(x=420,y=150)#textbox para escritura
                                                                    btn_eliminar=Button(v2,text="Eliminar Puerto",background="#3366ff",foreground="#00ffff",command=eliminar_puerto,font=text_b).place(x=420,y=260)#button que completa la tarea
                                                                    
                                                                if (vinet2==3):#tercera condicion
                                                                    os.system("sudo ufw status > infopuert.txt")#transcribe lo de ufw a un archivo .txt
                                                                    valor2=subprocess.check_output("cat /home/franklin/infopuert.txt",shell=True)#proceso para mostrar lo que contiene el archivo.txt
                                                                    area1=scrolledtext.ScrolledText(v2,width=55,height=15,background="#ccffff")#caja donde se enlista los puertos
                                                                    area1.place(x=210,y=90)#posicion de la caja 
                                                                    area1.insert(END,valor2)
                                         
                                            text_t=font.Font(family="Areal",size=18)#formato del tipo de texto
                                            text_p=font.Font(family="Areal",size=12)
                                            text_b=font.Font(family="Areal",size=14)
                                        

                                            label_t=Label(v2,text="Configuraciones de Firewall",font=text_t,background="#00ccff",foreground="#000066").place(x=200,y=1)#titulo de la pantalla
                                            global inet2,style#nombrar variables
                                            style=ttk.Style()#variable que tipo estilo
                                            style.configure("Custom.TRadiobutton",background="#ccffff",foreground="#000066")#diseño de los radiobutton
                                            inet2=IntVar()#variable tipo entero
                                            r1=ttk.Radiobutton(v2,text="Agregar Puerto",variable=inet2,value=1,style="Custom.TRadiobutton",command=EvaluarRadio2)#objeto de radiobutton
                                            r1.place(x=50,y=70)#posicion del radiobutton
                                            r2=ttk.Radiobutton(v2,text="Eliminar Puerto",variable=inet2,value=2,style="Custom.TRadiobutton",command=EvaluarRadio2)
                                            r2.place(x=50,y=150)
                                            r3=ttk.Radiobutton(v2,text="Enlistar Puertos",variable=inet2,value=3,style="Custom.TRadiobutton",command=EvaluarRadio2)
                                            r3.place(x=50,y=250)
                                            
                        if (cb=="Configurar_IP"):#condicion del combomenu
                                                 v1=Toplevel(background="#006600")#pantalla con color
                                                 v1.title("Configuracion Protocolo TCP /IPV4")#titulo de la pantalla
                                                 v1.geometry("700x300+150+250")#tamaño de la pantalla

                                                 def EvaluarRadio():#funcion de los radiobuttons
                                                                    vinet=inet.get()#variable que almacena el numero de radiobutton que se selecciona
                                                                    
                                                                    if (vinet==1):#condicion si el primer radiobutton es seleccionado
                                                                                 #Variables
                                                                                 global ether,ipaddress,netmask,gateway,dns
                                                                                 ether=StringVar()
                                                                                 ipaddress=StringVar()
                                                                                 netmask=StringVar()
                                                                                 gateway=StringVar()
                                                                                 dns=StringVar()
                                                                                 
                                                                                 def updateEther():#funcion para simplificar la infomacion que se desea
                                                                                    os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')#comando para obtener la palabra deseada (enp0s3) y la almacena en un .txt
                                                                                    valor=subprocess.check_output("cat inter.txt",shell=True,text=True)#comando para mostrar lo que hay en inter.txt
                                                                                    valorf=valor.strip()#variable que almacena el strip obtenido
                                                                                    ether.set(valorf)# almacena lo de la variable en tipo string
                                                                                    
                                                                                 updateEther()#llamado de la funcion
                                                                                 
                                                                                 def inet_static_interface():
                                                                                     #Variables que almacenan los que se escribe en los textbox 
                                                                                     e=str(ether.get())
                                                                                     ip=str(ipaddress.get())
                                                                                     n=str(netmask.get())
                                                                                     gw=str(gateway.get())
                                                                                     ds=str(dns.get())
                                                                                     tipo="static"
                                                                                     #metodo static sin netplan
                                                                                     if (inett==0):#condicion cuando el radiobutton del netplan no esta seleccionado 
                                                                                         #Constantes
                                                                                         linea1="auto lo" # choose
                                                                                         linea2="iface lo inet loopback" # choose
                                                                                         linea3="auto "
                                                                                         linea3_A=(str(linea3)+''+str(e)) #choose
                                                                                         linea4a="iface "
                                                                                         linea4b=" inet "
                                                                                         linea4_A=(str(linea4a)+''+str(e)+''+str(linea4b)+''+str(tipo)) #choose
                                                                                         linea5="address "
                                                                                         linea5_A=(str(linea5)+''+str(ip)) #choose
                                                                                         linea6="netmask "
                                                                                         linea6_A=(str(linea6)+''+str(n)) #choose
                                                                                         linea7="gateway "
                                                                                         linea7_A=(str(linea7)+''+str(gw)) #choose
                                                                                         linea8="dns-nameservers "
                                                                                         linea8_A=(str(linea8)+''+str(ds)) #choose
                                                                                     
                                                                                         os.system("sudo chmod -R 777 /etc/network/interfaces")#da permisos al archivo
                                                                                         os.system("sudo echo 1 > /etc/network/interfaces")
                                                                                         pf=open("/etc/network/interfaces","w")#abre el archivo para la modificacion
                                                                                         pf.write(linea1)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea2)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea3_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea4_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea5_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea6_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea7_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea8_A)
                                                                                         pf.write("\n")
                                                                                         pf.close()
                                                                                         time.sleep(0.1)#tiempo para realizar los cambios
                                                                                         os.system("sudo chmod -R 644 /etc/network/interfaces")#quitar los permisos
                                                                                         os.system("sudo ifdown enp0s3 && ifup enp0s3")#activa la ip por que la interfaz esta apagada
                                                                                         messagebox.showinfo("INFO",message="Cambios Aplicados en RED")#mensaje cuando termina el proceso y fue exitoso
                                                                                     else:#condicion con static y el radiobutton del netplan esta seleccionado
                                                                                         #Constantes
                                                                                            net="network:"
                                                                                            tapp="        "
                                                                                            pp=":"
                                                                                            ver="    version: 2"
                                                                                            ett="    ethernets:"
                                                                                            pp=":"
                                                                                            dhh="            dhcp4: no"
                                                                                            ad="            addresses:"
                                                                                            yi=" ["
                                                                                            yf="]"
                                                                                            gi="                - "
                                                                                            ga="            gateway4: "
                                                                                            na="            nameservers:"
                                                                                            lineaa="        {e}:"
                                                                                            ad1="                addresses:"

                                                                                            os.system("sudo chmod -R 777 /etc/netplan/50-cloud-init.yaml")#da los permisos
                                                                                            os.system("sudo echo 1 > /etc/netplan/50-cloud-init.yaml")
                                                                                            pf=open("/etc/netplan/50-cloud-init.yaml","w")#apertura del archivo para la modificacion
                                                                                            pf.write(net)
                                                                                            pf.write("\n")
                                                                                            pf.write(ver)
                                                                                            pf.write("\n")
                                                                                            pf.write(ett)
                                                                                            pf.write("\n")
                                                                                            pf.write(tapp)
                                                                                            pf.write(e)
                                                                                            pf.write(pp)
                                                                                            pf.write("\n")
                                                                                            pf.write(dhh)
                                                                                            pf.write("\n")
                                                                                            pf.write(ad)
                                                                                            pf.write("\n")
                                                                                            pf.write(gi)
                                                                                            pf.write(ip)
                                                                                            pf.write("\n")
                                                                                            pf.write(ga)
                                                                                            pf.write(gw)
                                                                                            pf.write("\n")
                                                                                            pf.write(na)
                                                                                            pf.write("\n")
                                                                                            pf.write(ad1)
                                                                                            pf.write(yi)
                                                                                            pf.write(ds)
                                                                                            pf.write(yf)
                                                                                            pf.write("\n")
                                                                                            pf.close()
                                                                                            time.sleep(0.1)#tiempo de espera
                                                                                            os.system("sudo chmod -R 644 /etc/netplan/50-cloud-init.yaml")#revertir los permisos 
                                                                                            os.system("sudo netplan apply")
                                                                                            messagebox.showinfo("INFO",message="Cambios Aplicados en RED") #mensaje cuando se termina la modificacion y es exitoso

                                                                                     
                                                                                 #objetos visuales con su 
                                                                                 label_ether=Label(v1,text="Interface Static:",font=text_p,background="#ccffcc",foreground="#003300").place(x=20,y=80)
                                                                                 label_ip=Label(v1,text="Ip address :", font=text_p,background="#ccffcc",foreground="#003300").place(x=20,y=110)
                                                                                 label_mask=Label(v1,text="Netmask:",font=text_p,background="#ccffcc",foreground="#003300").place(x=20,y=140)
                                                                                 label_gw=Label(v1,text="Gateway:", font=text_p,background="#ccffcc",foreground="#003300",).place(x=20,y=170)
                                                                                 label_dns=Label(v1,text="DNS:",font=text_p,background="#ccffcc",foreground="#003300").place(x=20,y=200)
                                                                                 #textbox que permiten el ingreso de valores
                                                                                 txt_ether=Entry(v1,textvariable=ether,width=15).place(x=150,y=80)
                                                                                 txt_ip=Entry(v1,textvariable=ipaddress,width=20).place(x=120,y=110)
                                                                                 txt_mask=Entry(v1,textvariable=netmask,width=20).place(x=120,y=140)
                                                                                 txt_gw=Entry(v1,textvariable=gateway,width=20).place(x=120,y=170)
                                                                                 txt_dns=Entry(v1,textvariable=dns,width=30).place(x=120,y=200)
                                                                                 #boton que realiza la aplicacion de la funcion para que se guarden los cambios realizados
                                                                                 btn_save=Button(v1,text="Save",background="#66ff66",foreground="#003300",command=inet_static_interface).place(x=120,y=260)
                                                                                 

                                                                    if (vinet==2):#condicion que el segundo radiobutton este seleccionado
                                                                                 global ether2#nombrar variable
                                                                                 ether2=StringVar()#tipo de la variable
                                                                                 def updateEther2():#funcion para simplificar la informacion
                                                                                    os.system('lshw -C network | grep "enp0s3" | cut -d " " -f10 > inter.txt')#comando para cortar y obtener la palabra que se desea (enp0s3)
                                                                                    valor=subprocess.check_output("cat inter.txt",shell=True,text=True)#mostra informacion del documento inter.txt
                                                                                    valorf=valor.strip()#variable que almacena el strip obtenido
                                                                                    ether2.set(valorf)# almacena lo de la variable en tipo string
                                                                                 updateEther2()#llamado de la funcion
                                                                                 def inet_dhcp_interface():
                                                                                     e=str(ether2.get())#asignar variable
                                                                                     tipo="dhcp"
                                                                                     if (inett==0):#metodo dhcp sin netplan
                                                                                         #Constantes
                                                                                         linea1="auto lo" # choose
                                                                                         linea2="iface lo inet loopback" # choose
                                                                                         linea3="auto "
                                                                                         linea3_A=(str(linea3)+''+str(e)) #choose
                                                                                         linea4a="iface "
                                                                                         linea4b=" inet "
                                                                                         linea4_A=(str(linea4a)+''+str(e)+''+str(linea4b)+''+str(tipo)) #choose
                                                                                         os.system("sudo chmod -R 777 /etc/network/interfaces")#dar permisos
                                                                                         os.system("sudo echo 1 > /etc/network/interfaces")
                                                                                         pf=open("/etc/network/interfaces","w")#apertura del documento para ser modificado
                                                                                         pf.write(linea1)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea2)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea3_A)
                                                                                         pf.write("\n")
                                                                                         pf.write(linea4_A)
                                                                                         pf.write("\n")
                                                                                         pf.close()
                                                                                         time.sleep(0.1)#tiempo de espera
                                                                                         os.system("sudo chmod -R 644 /etc/network/interfaces")#asignar los permisos nuevamente
                                                                                         os.system("sudo ifdown enp0s3 && ifup enp0s3")#activa la ip por que la interfaz esta apagada
                                                                                         messagebox.showinfo("INFO",message="Cambios Aplicados en RED")#mensaje de proceso realizado exitosamente
                                                                                     else:#condicion de metodo dhcp con el radiobutton del netplan esta seleccionado
                                                                                         #Constantes
                                                                                            net="network:"
                                                                                            tapp="    "
                                                                                            ett="    ethernets:"
                                                                                            dhh="            dhcp4: true"
                                                                                            ver="    version: 2"
                                                                                            pp=":"
                                                                                            lineaa=f"        {e}:"

                                                                                            os.system("sudo chmod -R 777 /etc/netplan/50-cloud-init.yaml")#dar permiso
                                                                                            os.system("sudo echo 1 > /etc/netplan/50-cloud-init.yaml")
                                                                                            pf=open("/etc/netplan/50-cloud-init.yaml","w")#apertura del documento para poder ser modificado
                                                                                            pf.write(net)
                                                                                            pf.write("\n")
                                                                                            pf.write(ett)
                                                                                            pf.write("\n")
                                                                                            pf.write(lineaa)
                                                                                            pf.write("\n")
                                                                                            pf.write(dhh)
                                                                                            pf.write("\n")
                                                                                            pf.write(ver)
                                                                                            pf.write("\n")
                                                                                            pf.close()
                                                                                            time.sleep(0.1)
                                                                                            os.system("sudo chmod -R 644 /etc/netplan/50-cloud-init.yaml")#quitar permisos
                                                                                            os.system("sudo netplan apply")
                                                                                            messagebox.showinfo("INFO",message="Cambios Aplicados en RED")#mensaje de que se realizo con exito el proceso

                                                                                 #objeto visual    
                                                                                 label_ether=Label(v1,text="Interface Dhcp:",font=text_p,background="#ccffcc",foreground="#003300").place(x=20,y=100)
                                                                                 txt_ether=Entry(v1,textvariable=ether2,width=15).place(x=150,y=100)#textbox que permite el ingreso de valores
                                                                                 btn_dhcp=Button(v1,text="Activar DHCP",background="#66ff66",foreground="#003300",command=inet_dhcp_interface).place(x=120,y=150)#boton que guarda los cambios

                                                                    if (vinet==3):#condicion de enlistar o consultar ip
                                                                                  os.system("cat /etc/network/interfaces > infored.txt")#comando que transmite la informacion a un txt
                                                                                  valor1=subprocess.check_output("cat /home/franklin/infored.txt",shell=True)#comando que muestra el documento txt
                                                                                  area1=scrolledtext.ScrolledText(v1,width=80,height=10,background="#ccffcc",foreground="#003300")#donde se muestra la informacion
                                                                                  area1.place(x=10,y=100)#ubicacion
                                                                                  area1.insert(END,valor1)                                
                                                                        

                                                 text_t=font.Font(family="Areal",size=18)#diseño del texto
                                                 text_p=font.Font(family="Areal",size=12)

                                                 label_t=Label(v1,text="Configuracion IPv4",font=text_t,background="#99ff99",foreground="#003333").place(x=200,y=1)#objetos visuales con su personalizacion
                                                 label_inet=Label(v1,text="Metodo Red -->",font=text_p,background="#99ff99",foreground="#003333").place(x=50,y=50)
                                                 global inet,inett,style1#nombrar variables
                                                 style1=ttk.Style()#tipo de la variable
                                                 style1.configure("Custom.TRadiobutton",background="#99ff99",foreground="#003333")#diseño del radiobutton
                                                 inett=IntVar()#tipo de dato
                                                 inet=IntVar()#tipo de dato
                                                 r1=ttk.Radiobutton(v1,text="Static",variable=inet,value=1,style="Custom.TRadiobutton",command=EvaluarRadio)#radiouttons
                                                 r1.place(x=190,y=50)#ubicacion
                                                 r2=ttk.Radiobutton(v1,text="DHCP",variable=inet,value=2,style="Custom.TRadiobutton",command=EvaluarRadio)
                                                 r2.place(x=260,y=50)
                                                 r3=ttk.Radiobutton(v1,text="Consultar IP",variable=inet,value=3,style="Custom.TRadiobutton",command=EvaluarRadio)
                                                 r3.place(x=340,y=50)
                                                 r4=ttk.Radiobutton(v1,text="Netplan",variable=inett,value=4,style="Custom.TRadiobutton",command=EvaluarRadio)
                                                 r4.place(x=460,y=50)
                                                 

                                                 
                                                 v1.mainloop()

label_t=Label(v0,text="Toolkits for Linux",font=txt1).place(x=100, y=5)
label_destino=Label(v0,text="Destinatario :",font=txt2).place(x=10,y=50)
label_asunto=Label(v0,text="Asunto:",font=txt2).place(x=10,y=80)
label_cuerpo=Label(v0,text="Cuerpo Correo:",font=txt2).place(x=10,y=110)

#variables
global destino,asunto,cuerpo
destino=StringVar()
asunto=StringVar()
cuerpo=StringVar()
txt_destino=Entry(v0,textvariable=destino,width=30).place(x=135,y=50)
txt_asunto=Entry(v0,textvariable=asunto,width=40).place(x=135,y=80)
txt_cuerpo=Entry(v0,textvariable=cuerpo,width=50).place(x=135,y=110)
global check1
check1=StringVar()
c1=ttk.Checkbutton(v0,text="Lista Respaldo",variable=check1,command=EvaluarCheck1)
c1.place(x=465,y=40)
global check2
check2=StringVar()
c2=ttk.Checkbutton(v0,text="Adjuntar Respaldo",variable=check2)
c2.place(x=465,y=60)
#Combobox
global combomenu
combomenu=StringVar()
cmb1=ttk.Combobox(v0,textvariable=combomenu,values=["Configurar_IP","Listar_Usuarios","Matar_Usuarios","firewall"])
cmb1.place(x=600,y=5)
btn_combo=Button(v0,text="Ejecutar",command=EvaluarComboMenu).place(x=500,y=5)

#botones
btn_enviar=Button(v0,text="Enviar",command=SendMail).place(x=10,y=150)
btn_crearbk=Button(v0,text="CrearRespaldo",command=CrearBK).place(x=100,y=150)

v0.mainloop()
