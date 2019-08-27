import csv

def cargadatos():
	results = []
	with open("TablaCapitales.csv", encoding='utf-8') as csvfile:
	    reader = csv.reader(csvfile) 
	    for row in reader: 
	        results.append(row)
	return results

#array =cargadatos()
#print(array)