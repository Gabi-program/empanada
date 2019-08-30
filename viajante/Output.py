from tkinter import *
from PIL import Image, ImageTk

class resultScreen:
  
  #es la lista de puntos en el mapa
  listOfPoints = [{"provincia":"Cdad. de Bs. As.", "posX":205, "posY":185, "puntoRef":1},
  {"provincia":"Córdoba", "posX":146, "posY":143, "puntoRef":1},
  {"provincia":"Corrientes", "posX":212, "posY":92, "puntoRef":1},
  {"provincia":"Formosa", "posX":215, "posY":75, "puntoRef":1},
  {"provincia":"La Plata", "posX":213, "posY":195, "puntoRef":1},
  {"provincia":"La Rioja", "posX":114, "posY":121, "puntoRef":1},
  {"provincia":"Mendoza", "posX":94, "posY":166, "puntoRef":1},
  {"provincia":"Neuquén", "posX":104, "posY":245, "puntoRef":1},
  {"provincia":"Paraná", "posX":188, "posY":150, "puntoRef":1},
  {"provincia":"Posadas", "posX":244, "posY":93, "puntoRef":1},
  {"provincia":"Rawson", "posX":136, "posY":303, "puntoRef":1},
  {"provincia":"Resistencia", "posX":205, "posY":91, "puntoRef":1},
  {"provincia":"Río Gallegos", "posX":107, "posY":415, "puntoRef":1},
  {"provincia":"S.F.d.V.d. Catamarca", "posX":125, "posY":104, "puntoRef":1},
  {"provincia":"S.M. de Tucumán,", "posX":131, "posY":82, "puntoRef":1},
  {"provincia":"S.S. de Jujuy", "posX":130, "posY":48, "puntoRef":1},
  {"provincia":"Salta", "posX":130, "posY":58, "puntoRef":1},
  {"provincia":"San Juan", "posX":93, "posY":145, "puntoRef":1},
  {"provincia":"San Luis", "posX":121, "posY":172, "puntoRef":1},
  {"provincia":"Santa Fe", "posX":182, "posY":145, "puntoRef":1},
  {"provincia":"Santa Rosa", "posX":144, "posY":215, "puntoRef":1},
  {"provincia":"Sgo. Del Estero", "posX":144, "posY":97, "puntoRef":1},
  {"provincia":"Ushuaia", "posX":117, "posY":455, "puntoRef":1},
  {"provincia":"Viedma", "posX":157, "posY":270, "puntoRef":1}]
  
  def __init__(self, result):
    #crea ventana
    mainWindow = Toplevel()
    #print(len(self.listOfPoints))
    mainWindow.title("Mapa")


    #imagen del mapa
    img = self.cargaImagen()
    imageHeight = img.height()
    imageWidth = img.width()

    #carga los puntos de listOfPoints
    #self.cargaPuntos()
    
    
    #frame del mapa
    self.mapaFrame = Frame(mainWindow, height = imageHeight, width = imageWidth, bd = 1)
    self.mapaFrame.grid(row=0, column = 0)
    
    #imagen del mapa
    self.mapa = Canvas(self.mapaFrame, height = imageHeight, width = imageWidth, bg= "black")
    self.mapa.pack()
   
    """
    #capa de lineas a dibujar
    self.capaLineas = Canvas(self.mapa, height = imageHeight, width = imageWidth)
    self.capaLineas.pack()
    
    #capa de puntos a dibujar
    self.capaPuntos = Canvas(self.capaLineas, height = imageHeight, width = imageWidth)
    self.capaLineas.pack()
    """

    #frame donde se mostraran los datos textuales
    self.datos = Frame(mainWindow, height = imageHeight, width = 40, bd = 1, padx= 5)
    self.datos.grid(row=0, column=1)
    
    #se dibuja en el mapa
    self.mapa.create_image(1,1, image= img, anchor = NW)
    self.creaPuntos(self.mapa)
    self.creaLineas(self.mapa, result)
    self.mapa.tag_raise("capital")
    
    
    
    #cargar los otros datos del result en self.datos
    #spacing 1
    Label(self.datos, height = 1).grid(row=0,column=0)
    
    #lista del recorrido
    #titulo
    Label(self.datos, text="lista de recorrido:").grid(row=1, column=0)
    #lista
    listbox = Listbox(self.datos, height = 25)
    listbox.grid(row=3, column=0, columnspan = 2)
    self.cargaListBox(listbox, result)
    
    #spacing 2
    Label(self.datos, height= 1).grid(row=5,column=0,columnspan=2)
    
    #total recorrido
    #titulo
    Label(self.datos, text="total recorrido:").grid(row=6, column=0)
    #valor result.total
    Label(self.datos, text=str(result["total"])).grid(row=7, column=0)
    
    
    
    mainWindow.mainloop()
    return
    

  def cargaImagen(self):
    img = Image.open("mapa.png")
    heightImg = img.height
    widthImg = img.width
    resizeImg = img.resize((int(widthImg/2), int(heightImg/2)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image= resizeImg)
    return img
    
  def cargaPuntos(self):
    #carga los puntos de las provincias en el mapa y las agrega en la lista
    return
     
  def creaPuntos(self, canvas):
    radio = 3
    for elem in self.listOfPoints:
      elem["puntoRef"] = canvas.create_oval(elem["posX"]-radio,elem["posY"]-radio,elem["posX"]+radio,elem["posY"]+radio, fill = "red", tag= "capital")
    return
       
  def creaLineas(self, canvas, resultado):
    linePos = (0,0,0,0)
    orden = resultado["orden"]
    #print(orden)
    for i in range(len(orden)-1):
      #print(i+1, ornden[i+1])
      #print(self.listOfPoints[orden[i+1]])
      iniPos = self.listOfPoints[orden[i]-1]
      endPos = self.listOfPoints[orden[i+1]-1]
      linePos = (iniPos["posX"], iniPos["posY"], endPos["posX"], endPos["posY"])
      """
      linePos[0] = iniPos["posX"]
      linePos[1] = iniPos["posY"]
      linePos[2] = endPos["posX"]
      linePos[3] = endPos["posY"]
      """
      canvas.create_line(linePos,fill="red", tag="recorrido", width= 2)
    return
   
  def cargaListBox(self, listbox, res):
    orden = res["orden"]
    for i in range(len(orden)):
      listbox.insert(END, str(self.listOfPoints[orden[i]-1]["provincia"]))
   
   
   
if __name__=="__main__":
  #crear un resultdo falso
  resultado = {"orden":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], "total": 100}
  test = resultScreen(resultado)