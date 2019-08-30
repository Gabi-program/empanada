from tkinter import *
from busAG import *
import bestHeu
import busHeu
import carga
import Output

CapitalesArg = carga.cargadatos()

provOptions = ("Cdad. de Bs. As.", "Córdoba","Corrientes","Formosa","La Plata","La Rioja","Mendoza","Neuquén","Paraná","Posadas","Rawson","Resistencia","Río Gallegos","S.F.d.V.d. Catamarca","S.M. de Tucumán,","S.S. de Jujuy","Salta","San Juan","San Luis","Santa Fe","Santa Rosa","Sgo. Del Estero","Ushuaia","Viedma")

def MainWindow ():
	mainOptionWindow = Tk()
	mainOptionWindow.title("Viajante")

	
	#------------------------- positioning
	frame1 = Frame(width=150, height=100,bd=2)
	frame1.grid(row=0)
	frame2 = Frame(width=150, height=100,bd=2)
	frame2.grid(row=1)
	frame3 = Frame(width=150, height=100,bd=2)
	frame3.grid(row=2)

	frame4 = Frame(width=250, height=100,bd=2)
	frame4.grid(row=0, column = 1, sticky = W)
	frame5 = Frame(width=250, height=100,bd=2)
	frame5.grid(row=2, column=1)

	#---------------------------
	
	#--------------------------- create buttons
	button1 = Button(frame1, text = "Busqueda Heuristica", command = lambda:BusquedaHeu(provincia.get()))
	button1.place(relx=0.5, rely=0.5, anchor=CENTER)
	button2 = Button(frame2, text = " Mejor Busqueda", command= lambda:BestBusquedaHeu())
	button2.place(relx=0.5, rely=0.5, anchor=CENTER)
	button3 = Button(frame3, text = "Busqueda AG", command = lambda:BusquedaAG(provCross.get(), provMut.get(), elitVar.get()))
	button3.place(relx=0.5, rely=0.5, anchor=CENTER)
	#--------------------------- 
	
	#--------------------------- Provincia list
	provincia = StringVar(frame4)
	provincia.set(provOptions[0]) # default value

	provMenu = OptionMenu(frame4, provincia, *provOptions)
	provMenu.place(relx=0.5, rely=0.5, anchor=CENTER)
	#---------------------------

	#--------------------------- GA variables
	frameAG = Frame(frame5, width=125, height=100,bd=2)
	frameAG.place(relx = 0.25, rely = 0.5, anchor= CENTER)

	provCross = StringVar()
	provCross.set("0.8")
	

	provMut = StringVar()
	provMut.set("0.1")

	if ((float(provMut.get()) < 0) or (float(provMut.get()) > 1)):
		provCross.set("0.8")

	val = (frame5.register(validateCross), "%P")
	labelCross = Label(frameAG, text = "Crossover:" )
	labelCross.grid(row= 0, column = 0)
	entryCross = Entry(frameAG, textvariable = provCross, validate = "key", validatecommand = val, width = 10)
	entryCross.grid(row = 0, column=1)

	spaceing = Frame(frameAG, width = 125, height = 10)
	spaceing.grid(row=1, columnspan = 2)

	labelMut = Label(frameAG, text = "Mutation:" )
	labelMut.grid(row=2)
	entryMut = Entry(frameAG, textvariable = provMut, validate = "key", validatecommand = val, width = 10)
	entryMut.grid(row = 2, column=1)

	elitVar = BooleanVar()
	elitVar.set(True)
	elitCheck = Checkbutton(frame5, text= "Elitism", variable=elitVar)
	elitCheck.place(relx = 0.75, rely = 0.5, anchor= CENTER)

	#--------------------------- 


	#--------------------------- Activate
	mainOptionWindow.mainloop()

def validateCross(prov):
	if prov == "":
		return True

	try:
		if ((float(prov) < 0) or (float(prov) > 1)):
			return False
		return True
	except ValueError:
		return False

def BusquedaHeu (cap):
	origen=busHeu.BuscarIndice(cap,CapitalesArg)
	Resultados = busHeu.BusquedaHeuristicaDeUnOrigen(origen,CapitalesArg)
	#print(Resultados)
	Output.resultScreen(Resultados)

def BestBusquedaHeu ():

	Resultados=bestHeu.busquedaHeuTotal(CapitalesArg)
	#print(Resultados)
	Output.resultScreen(Resultados)

def BusquedaAG (provC, provM, Elit):
	print("Crossover: {0} // Mutacion: {1} // Elitismo: {2}".format(float(provC), float(provM), Elit))
	pob = Population(float(provC), float(provM), Elit)
	#Output.resultScreen(pob.output())
	print(pob.output())
	while pob.Gen < 500:
		#print(pob.output().get("total"))
		pob.nextGen()
	print(pob.output())
	Output.resultScreen(pob.output())

if __name__ == "__main__":
	MainWindow()