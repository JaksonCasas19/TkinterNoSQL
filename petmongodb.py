from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image,ImageTk


def conectarDB():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['TestStore'] #Nombrar a la base de datos
	collection = db['products'] #Crear collecciones, conjunto de datos

def salirAplicacion():
	valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
	if(valor == "yes"):
		root.destroy()

def limpiarCampos():
	nombre.set("")
	Precio.set("")


def crear():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['TestStore']
	collection = db['products'] 
	print(nombre.get())
	collection.insert_one({"nombre":nombre.get(),"Precio":Precio.get()})

def info():
	messagebox.showinfo("Información","Desarrollado por\nJakson Casas 2021")

root = Tk()
root.title("No-SQL")
root.config(bg="white")

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300)
root.geometry('310x290')
root.resizable(False,False) 

#Empezar barra
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

CrudMenu = Menu(barraMenu, tearoff=0)
CrudMenu.add_command(label="Crear")
CrudMenu.add_command(label="Leer")
CrudMenu.add_command(label="Editar")
CrudMenu.add_command(label="Eliminar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de",command=info)

barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CrudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)




#----- Empezar campos -----


miHead=Frame(root)
miHead.config(bg="#03B898")
miHead.pack()


labelTitulo=Label(miHead,text="Tkinter No-SQL",bg="#03B898",fg="white")
labelTitulo.grid(row=0,column=0,pady=9,padx=110,columnspan=2, sticky="w"+"e")

miFrame=Frame(root)
miFrame.config(bg="white")
miFrame.pack()

nombre = StringVar()
Precio = StringVar()



nombreLabel = Label(miFrame, text="Nombre:",bg="white")
nombreLabel.grid(row=1,column=0,sticky="e",pady=10,padx=10)
precioLabel = Label(miFrame, text="Precio:",bg="white")
precioLabel.grid(row=2,column=0,sticky="e",pady=10,padx=10)


cuadroNombre = Entry(miFrame,textvariable=nombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroPrecio = Entry(miFrame,textvariable=Precio)
cuadroPrecio.grid(row=2,column=1,padx=10,pady=10)

#Botones CRUD

secBoton =Frame(root)
secBoton.config(bg="white",pady=25)
secBoton.pack()

botonCrear=Button(secBoton, text="Crear",bd=0,bg="#3DCC8E",fg="white",command=crear)
botonCrear.grid(row=1,column=1,sticky="e",padx=5,pady=5)

botonLeer=Button(secBoton, text="Leer",bd=0,bg="SeaGreen3",fg="white")
botonLeer.grid(row=1,column=2,sticky="e",padx=5,pady=5)

botonActualizar=Button(secBoton, text="Actualizar",bd=0,bg="goldenrod1",fg="white")
botonActualizar.grid(row=1,column=3,sticky="e",padx=5,pady=5)

botonEliminar=Button(secBoton, text="Eliminar",bd=0,bg="firebrick1",fg="white")
botonEliminar.grid(row=1,column=4,sticky="e",padx=5,pady=5)


miFrame2=Frame(root)
miFrame2.config(bg="#4A4A4A")
miFrame2.pack()

imagen=ImageTk.PhotoImage(Image.open(r'D:\Curso HTML5 and CSS 3\Python\MongoDBandPython\PetMongoDB\whiteMongo.png').resize((110,33)))
label1=Label(miFrame2, image=imagen,borderwidth=0)
label1.grid(row=4,column=1,sticky="s",columnspan=2,padx=100,pady=15)
#label1.pack()

root.mainloop()