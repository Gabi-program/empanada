import carga
import Output
import busHeu
import bestHeu
from busAG import *

def BusHeuPorCiudad():
	origen="nada"
	while origen=="nada":
		capital=input("ingrese capital de origen: ")
		origen=busHeu.BuscarIndice(capital,CapitalesArg)
	Resultados=busHeu.BusquedaHeuristicaDeUnOrigen(origen,CapitalesArg)
	#print(Resultados)
	Output.resultScreen(Resultados)

def BusMejorHeu():
	Resultados=bestHeu.busquedaHeuTotal(CapitalesArg)
	#print(Resultados)
	Output.resultScreen(Resultados)


def BusGenetic():
  pob = Population(.8,.4)
  Output.resultScreen(pob.output())
  print(pob.output())
  while pob.Gen < 500:
  	print(pob.output().get("total"))
  	pob.nextGen()
  print(pob.output())
  Output.resultScreen(pob.output())

CapitalesArg = carga.cargadatos()

#Despliega el menu de opciones
'''
while True:
	print("Como quiere resolver el problema del viajante?")
	print("1-Buscando la mejor ruta desde una ciudad ingresada")
	print("2-Buscando la mejor ruta posible")
	print("3-Buscar una buena ruta mediante un algoritmo genetico")
	print("4-Salir del programa")
	op=(input())
	if op=="1":	
		BusHeuPorCiudad()
	elif op=="2":
		BusMejorHeu()
	elif op=="3":
		BusGenetic()

	elif op=="4":
		break'''