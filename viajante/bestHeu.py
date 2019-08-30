import busHeu

def busquedaHeuTotal(Capitales):
	#esta funcion utilizara la busqueda heuristica por origen y las comparara
	# devolviendo la mejor de ellas
	mintot=1000000
	for i in range(len((Capitales))-1):
		resultado=busHeu.BusquedaHeuristicaDeUnOrigen(i+1,Capitales)
		if resultado.get("total")<mintot:
			mintot=resultado.get("total")
			#print(Capitales[i+1][0])
			#print(mintot)
			#print("entro")
			mejorHeu=i+1
			output=resultado
	#print("el mejor camino para recorrer todas las capitales es partiendo de ",Capitales[mejorHeu][0]," y recorre ",mintot,"km")
	return output