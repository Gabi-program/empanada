import carga
import random

distancias = carga.cargadatos()

class Cromosoma:
	def __init__():
		self.data = []
		base = range(24)
		for i in base:
			selection = random.randint(0, 23 -i)
			self.data.append(base[selection])
			base[selection] = base[23-i]
		self.kmRecorridos = self.distance(distancias) 

	def distance(distan):
		sum = 0
		for i in range(23):
			sum += distan[self.data[i]][self.data[i+1]]
		sum += distan[self.data[23]][self.data[0]]
		return sum



class Population:
	def __init__(crosProv, mutProv):
		self.popu = []
		self.crosProv = crosProv
		self.mutProv = mutProv
		for i in range(50):
			self.popu.append(Cromosoma)
		self.Gen = 0

	def Crosover(padre1, padre2):
		primerElem = padre1[0]
		elemABuscar = padre2[0]
		listaCros = [0]
		while True:
			index =´padre1.index(elemABuscar)
			listaCros.append(index)
			if primerElem == padre2[index]:
				break
			elemABuscar = padre2[index]
		hijo1=[]
		hijo2=[]
		for i in range(23):
			if i in listaCros:
				hijo1.append(padre2[i])
				hijo2.append(padre1[i])
			else:
				hijo1.append(padre1[i])
				hijo2.append(padre2[i])

		return [hijo1, hijo2]


	def Mutation(mutar):
		numACambiar1 = random.randint(0,23)
		numACambiar2 = random.randint(0,23)
		while numACambiar1 == numACambiar2:
			numACambiar2 = random.randint(0,23)
		temp = mutar[numACambiar1]
		mutar[numACambiar1] = mutar[numACambiar2]
		mutar[numACambiar2] = temp


	def nextGen():
		orderedList = [-1]*8
		newList = []
		for elem in self.popu:
			temp = elem
			for i in len(orderedList):
				if(orderedList[i]== -1):
					orderedList[i] = elem
					break
				if(orderedList[i].kmRecorridos < temp.kmRecorridos):
					temp = orderedList[i]
					orderedList[i] = elem

			for i in len(orderedList):
				for j in range(i+1, len(orderedList)):
					





def busquedaAG():
	#esta funcion se encargara de buscar la ruta mas corta utilizando algoritmos geneticos
	#es posible que se necesite hacermas archivos que se encargen de la poblacion y genes
	pass