from tkinter import *
from tkinter import messagebox
#Desarrollado por Jairo Elicer Rojas Herrera
####################################################################################

def IniciarArchivo():
    archivo = open("agenda.txt", "a")
    archivo.close()

####################################################################################
def CargarArchivo():
    archivo = open("agenda.txt", "r")
    linea = archivo.readline()
    if(linea):
        while(linea):
            if(linea):
                if(linea[-1] == '\n'):
                    linea = linea[:-1]
                lista.append(linea)
                linea = archivo.readline()
    archivo.close()

####################################################################################
def GuardarContacto():
    nom = nombre.get()
    ap = app.get()
    am = apm.get()
    co = correo.get()
    tel = telefono.get()
    lista.append(nom+"$"+ap+"$"+am+"$"+tel+"$"+co)
    EscribirContacto()
    nombre.set("")
    app.set("")
    apm.set("")
    correo.set("")
    telefono.set("")
    Consultar()

####################################################################################
def EscribirContacto():
    archivo = open("agenda.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()

####################################################################################
def Consultar():
    textArea = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    textArea.insert(INSERT, "Nombre\tApellido P\t\tApellido M\t\tTeléfono\t\tCorreo\n")

    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        textArea.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    textArea.place(x=20,y=230)
    spinTelefono = Spinbox(ventana, value=(valores),textvariable=contEliminar).place(x=450, y=50)
    if (lista ==[]):
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)
    textArea.config(state=DISABLED)

####################################################################################
def Eliminar():
    eliminado = contEliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if contEliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    EscribirContacto()
    Consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)
        
####################################################################################
def Validar():
    
    if(nombre.get() == "" or app.get() == "" or apm.get()=="" or telefono.get()=="" or correo.get() ==""):
        messagebox.showwarning("Dato vacio","Por favor no deje campos vacios");
    else:
        if(telefono.get().isdigit()):
            GuardarContacto()
            return True
        else:
            messagebox.showwarning("Dato no valido","Ingrese un numero de telefono valido");
            return True
        

ventana = Tk()
lista = []
nombre = StringVar()
app = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
contEliminar = StringVar()
bg = "SeaGreen1"
letraColor = "#FFF"
IniciarArchivo()
CargarArchivo()
Consultar()

# Contruyendo los widgets del frame

ventana.title("Agenda de contactos")
ventana.geometry("700x500")
ventana.configure(bg=bg)

labelTitulo = Label(ventana, text="Agenda", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=270, y=10)

labelNombre = Label(ventana, text="Nombre", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=50, y=50)
inputNombre = Entry(ventana, textvariable=nombre).place(x=200, y=50)

labelApp = Label(ventana, text="Apellido paterno", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=50, y=80)
inputApp = Entry(ventana, textvariable=app).place(x=200, y=80)

labelApm = Label(ventana, text="Apellido materno", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=50, y=110)
inputApm = Entry(ventana, textvariable=apm).place(x=200, y=110)

labelTelefono = Label(ventana, text="Telefono", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=50, y=140)
inputTelefono = Entry(ventana, textvariable=telefono).place(x=200, y=140)

labelCorreo = Label(ventana, text="Correo:", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=50, y=170)
inputCorreo = Entry(ventana, textvariable=correo).place(x=200, y=170)

labelEliminar = Label(ventana, text="Teléfono", bg=bg,fg=letraColor, font=("Verdana", 12)).place(x=370, y=50)
spinTelefono = Spinbox(ventana, textvariable=contEliminar).place(x=450, y=50)

btnGuardar = Button(ventana, text="Guardar",command=Validar, bg="lime green",fg="black").place(x=230, y=200)
btnEliminar = Button(ventana, text="Eliminar",command=Eliminar,bg="firebrick1", fg="black").place(x=490, y=80)

mainloop()

