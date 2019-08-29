import carga
import random


	#esta funcion se encargara de buscar la ruta mas corta utilizando algoritmos geneticos
	#es posible que se necesite hacermas archivos que se encargen de la poblacion y genes


distancias = carga.cargadatos()

class Cromosoma:
	#inicializa el cromosoma
	def __init__(self, newData = None):
		self.data = []
		if newData == None:
			base = list(range(1, 25))
			#print(base)
			for i in range(len(base)):
				selection = random.randint(0, 23 -i)
				self.data.append(base[selection])
				base[selection] = base[23-i]
		else:
			self.data = newData
		self.kmRecorridos = self.distance(distancias) 

	#le calcula la distancia
	def distance(self, distan):
		sum = 0
		for i in range(23):
			#print(i)
			#print(self.data[i], self.data[i+1],  sep=" /---/ ")
			sum += int(distan[self.data[i]][self.data[i+1]])
		sum += int(distan[self.data[23]][self.data[0]])
		return sum



class Population:
	#crea la poblacion
	def __init__(self, crosProv, mutProv):
		self.popu = []
		self.crosProv = crosProv
		self.mutProv = mutProv
		for i in range(50):
			self.popu.append(Cromosoma())
		self.Gen = 0

	#metodo de crosover
	def Crossover(padre1, padre2):
		primerElem = padre1.data[0]
		elemABuscar = padre2.data[0]
		listaCros = [0]
		while True:
			index = padre1.data.index(elemABuscar)
			listaCros.append(index)
			if primerElem == padre2.data[index]:
				break
			elemABuscar = padre2.data[index]
		hijo1=[]
		hijo2=[]
		for i in range(len(padre1.data)):
			if i in listaCros:
				hijo1.append(padre2.data[i])
				hijo2.append(padre1.data[i])
			else:
				hijo1.append(padre1.data[i])
				hijo2.append(padre2.data[i])

		hijo1 = Cromosoma(hijo1)
		hijo2 = Cromosoma(hijo2)

		return [hijo1, hijo2]

	#metodo de mutaion
	def Mutation(mutar):
		numACambiar1 = random.randint(0,23)
		numACambiar2 = random.randint(0,23)
		while numACambiar1 == numACambiar2:
			numACambiar2 = random.randint(0,23)
		temp = mutar.data[numACambiar1]
		mutar.data[numACambiar1] = mutar.data[numACambiar2]
		mutar.data[numACambiar2] = temp

	#calcula el total de km tecorridos por toda la popu
	def KmTotal (self):
	  sum = 0
	  for elem in self.popu:
	    sum += elem.kmRecorridos
	  return sum
	 
	# esto se utiliza para buscar los mejores padres y guardarlos (Elitismo)
	def serchbest(self):
	  padres =[]
	  if(self.popu[0].kmRecorridos <= self.popu[1].kmRecorridos):
	    padres += [self.popu[0], self.popu[1]]
	  else:
	    padres += [self.popu[1], self.popu[0]]
	    
	    
	  for i in range(2, len(self.popu)):
	    mover = self.popu[i]
	    if(padres[0].kmRecorridos > mover.kmRecorridos):
	      padres[1] = padres[0]
	      padres[0] = mover
	    elif(padres[1].kmRecorridos > mover.kmRecorridos):
	      padres[1] = mover
	      
	  return padres


	#crea a la siguiente generacion
	def nextGen(self):
		#inicializa lo necesario
		ruleta = []
		newList = []
		kmTotal =  self.KmTotal()
		#crea la ruleta
		for i in range(len(self.popu)):
		  ruleta += [i] * int((1 - float(self.popu[i].kmRecorridos / kmTotal))*100)
		
		#agrega a los mejores padres a la lista
		newList += self.serchbest()
		
		#crea a los hijos con cros over y mutacion
		while len(newList) < 50:
		  crom1 = self.popu[ruleta[random.randint(0, len(ruleta)-1)]]
		  crom2 = self.popu[ruleta[random.randint(0, len(ruleta)-1)]]
		
		  if(random.random() < self.crosProv):
		    temp = Population.Crossover(crom1, crom2)
		    crom1 = temp[0]
		    crom2 = temp[1]
		    
		  if(random.random() < self.mutProv):
		    Population.Mutation(crom1)
		    
		  if(random.random() < self.mutProv):
		    Population.Mutation(crom2)
		    
		  newList += [crom1, crom2]
		
		#los guarda como la nueva poblacion y aumenta el contador de generacion
		self.popu = newList
		self.Gen += 1

	#devuelve una libreria para ser inpimida en un mapa
	def output(self):
		bestCrom = self.popu[0]
		for i in range(1, len(self.popu)):
			if bestCrom.kmRecorridos > self.popu[i].kmRecorridos:
				bestCrom = self.popu[i]

		output = {"orden": bestCrom.data, "total": bestCrom.kmRecorridos}
		return output
		    
		    
if __name__ == "__main__":
  pob = Population(.8,.1)
  print(pob.output())
  while pob.Gen < 500:
  	print(pob.Gen)
  	pob.nextGen()
  print(pob.output())