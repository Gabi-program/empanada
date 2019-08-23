import csv

def cargadatos():
	results = []
	with open("TablaCapitales.csv", encoding='utf-8') as csvfile:
	    reader = csv.reader(csvfile) 
	    for row in reader: 
	        results.append(row)
	return results

def BusquedaHeuristicaDeUnOrigen(origen,array):
	pass

array =cargadatos()
print(array)