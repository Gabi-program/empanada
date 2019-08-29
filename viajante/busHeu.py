import carga
import Output

def BuscarIndice(ori,Capitales):
	inx="nada"
	for i in range(len(Capitales)):
		if Capitales[i][0]==ori:
			inx=i 
			break
	return inx

def BusquedaHeuristicaDeUnOrigen(origen,Capitales):
	#esta funcion buscara la distancia mas chica desde un origen dado
	#para buscarlo vera cual es la capital mas cercana de la posicion en la que se encuentra
	Resultados=[origen]
	total=0
	CapActual=origen
	minimo=999999
	while (len(Resultados))!=len(Capitales)-1:
		for i in range(len(Capitales[CapActual])-1):
			if (i+1)!=CapActual:
				if (int(Capitales[CapActual][i+1])<minimo) and ((i+1) not in Resultados):
					minimo=int(Capitales[CapActual][i+1])
					indice=i+1
		CapActual=indice
		total=total+minimo
		minimo=999999
		Resultados.append(indice)
	#Resultados.append(origen)
	total=total+int(Capitales[indice][origen])
	output={"orden":Resultados,"total":total}
	return output


'''def outputBusqueda(origen, array):
	sol = BusquedaHeuristicaDeUnOrigen(origen, array)
	#despues de guardar la solucion en sol esta funcion pasara el resultado a unas funciones de output.py
	#para mostrarlo en pantalla,supongo que sera el mapa
	pass'''

