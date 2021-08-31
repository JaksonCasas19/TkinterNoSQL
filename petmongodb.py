from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image,ImageTk


def conectarDB():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['MusicStore'] #Nombrar a la base de datos
	collection = db['playList'] #Crear collecciones, conjunto de datos

def salirAplicacion():
	valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
	if(valor == "yes"):
		root.destroy()

def limpiarCampos():
	idValue.set("")
	artista.set("")
	song.set("")
	comboCategoria.set("")

def crear():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['MusicStore']
	collection = db['playList'] 
	collection.insert_one({"_id":idValue.get(),"artista":artista.get(),"song":song.get(),"genero":comboCategoria.get()})
	limpiarCampos()
	messagebox.showinfo("BBDD","¡Registro insertado con éxito!")

def info():
	messagebox.showinfo("Información","Desarrollado por\nJakson Casas 2021")

def leer():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['MusicStore'] 
	collection = db['playList']
	BuscarId = idValue.get()
	results = collection.find({"_id":BuscarId})#{"Precio":90}

	for r in results:
		artista.set(r['artista'])
		song.set(r['song'])
		comboCategoria.set(r['genero'])
def actualizar():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['MusicStore'] 
	collection = db['playList'] 
	BuscarId = idValue.get()
	ObtenerNombre = str(artista.get())
	ObtenerSong = str(song.get())
	ObtenerCat = str(comboCategoria.get())
	collection.update_one({"_id":BuscarId},{"$set":{"artista":ObtenerNombre,"song":ObtenerSong,"genero":ObtenerCat}})
	messagebox.showinfo("BBDD","¡Se actualizo con éxito!")

def eliminar():
	MONGO_URI = 'mongodb://localhost'
	client = MongoClient(MONGO_URI)
	db = client['MusicStore'] 
	collection = db['playList'] 
	BuscarId = idValue.get()
	collection.delete_one({"_id":BuscarId})
	limpiarCampos()
	messagebox.showinfo("BBDD","¡Se elimino con éxito!")


root = Tk()
root.title("No-SQL")
root.config(bg="white")

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300)
root.geometry('310x380')
root.resizable(False,False) 

#Empezar barra
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

CrudMenu = Menu(barraMenu, tearoff=0)
CrudMenu.add_command(label="Crear",command=crear)
CrudMenu.add_command(label="Leer",command=leer)
CrudMenu.add_command(label="Editar",command=actualizar)
CrudMenu.add_command(label="Eliminar",command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
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

idValue = StringVar()
artista = StringVar()
song = StringVar()


idLabel = Label(miFrame, text="Id:",bg="white")
idLabel.grid(row=1,column=0,sticky="e",pady=10,padx=10)
artistaLabel = Label(miFrame, text="Artista:",bg="white")
artistaLabel.grid(row=2,column=0,sticky="e",pady=10,padx=10)
songLabel = Label(miFrame, text="Song:",bg="white")
songLabel.grid(row=3,column=0,sticky="e",pady=10,padx=10)
categoriaLabel = Label(miFrame, text="Género:",bg="white")
categoriaLabel.grid(row=4,column=0,sticky="e",pady=10,padx=10)

cuadroId = Entry(miFrame,textvariable=idValue)
cuadroId.grid(row=1,column=1,padx=10,pady=10)
cuadroArtista = Entry(miFrame,textvariable=artista)
cuadroArtista.grid(row=2,column=1,padx=10,pady=10)
cuadroSong = Entry(miFrame,textvariable=song)
cuadroSong.grid(row=3,column=1,padx=10,pady=10)
comboCategoria=ttk.Combobox(miFrame,values=["Rock","Pop","Regueton","Electro","Salsa","Latino"])
comboCategoria.grid(row=4,column=1,padx=10,pady=10)
comboCategoria.current(0)

#Botones CRUD
secBoton =Frame(root)
secBoton.config(bg="white",pady=25)
secBoton.pack()

botonEliminar=Button(secBoton, text="Eliminar",bd=0,bg="firebrick1",fg="white",command=eliminar)
botonEliminar.grid(row=1,column=1,sticky="e",padx=5,pady=5)

botonLeer=Button(secBoton, text="Leer",bd=0,bg="SeaGreen3",fg="white",command=leer)
botonLeer.grid(row=1,column=2,sticky="e",padx=5,pady=5)

botonActualizar=Button(secBoton, text="Actualizar",bd=0,bg="goldenrod1",fg="white",command=actualizar)
botonActualizar.grid(row=1,column=3,sticky="e",padx=5,pady=5)

botonCrear=Button(secBoton, text="Crear",bd=0,bg="#3DCC8E",fg="white",command=crear)
botonCrear.grid(row=1,column=4,sticky="e",padx=5,pady=5)


miFrame2=Frame(root)
miFrame2.config(bg="#4A4A4A")
miFrame2.pack()

imagen=ImageTk.PhotoImage(Image.open(r'D:\Curso HTML5 and CSS 3\Python\MongoDBandPython\PetMongoDB\whiteMongo.png').resize((110,33)))
label1=Label(miFrame2, image=imagen,borderwidth=0)
label1.grid(row=4,column=1,sticky="s",columnspan=2,padx=100,pady=15)
#label1.pack()

root.mainloop()