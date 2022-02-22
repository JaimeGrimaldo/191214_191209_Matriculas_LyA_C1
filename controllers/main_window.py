from importlib.resources import path
from tkinter import messagebox
from PySide2.QtWidgets import QWidget
from views.main_window import VentanaPrincipal
import string
import webbrowser

#Diccionarios para la filtracion y analisis
cadena = ""
baneados = ["I","O","Q","Ñ"]
abcCompleto = string.ascii_uppercase #Esto sirve para saber todo el abecedario para hacer futuras comparaciones.
correr = True
cocheOax = False
cochePuebla = False
camionOax = False
camionPuebla = False
placaEncontrada = False

diccAutosOax = ["H","J","K","L","M"]
diccAutosPuebla1 = ["N","P","R","S","T","U","V","W","X","Y","Z"]
diccAutosPuebla2 = ["A","B","C","D","E","F","G","H","J"]
diccCamionOaxaca = ["R","S","T","U","V","X","Y"]
diccCamionPuebla = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R"]
#PLACA: THA-001-A

class Ventana(QWidget, VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Evaluar.clicked.connect(self.start)
        self.Limpiar.clicked.connect(self.limpiarCampo)
        self.Diagrama.clicked.connect(self.abrirPDF)

    
    def comprobarNumerosCoches(self,segundaSeccion):
        global correr
        for i in range(999):
            if int(segundaSeccion) == i:
                #print("Numero de placa identificado:",i)
                correr = True
                break
    
    def comprobarNumeroCamion(self,segundaSeccion):
        global correr
        for i in range(9999):
            if int(segundaSeccion) == i:
                #print("Numero correcto:",i)
                correr = True
                break
    
    def comprobardigito3(self,primeraSeccion):
        global correr
        for i in range(len(abcCompleto)):
                    if primeraSeccion[2] == abcCompleto[i]:
                        #print("3er digito correcto")
                        correr = True
                        break
                    else:
                        print("Hay un problema con el 3er digito de la matricula")
                        break
    
    def comprobardigitoFinal(self,terceraSeccion):
        global correr
        for i in range(len(abcCompleto)):
            if terceraSeccion == abcCompleto[i]:
                #print("Ultimo digito valido")
                correr = True
                break
            else:
                #print("Error en el ultimo digito de la matricula")
                break
    
    def evaluarCadena(self):
        global cocheOax, correr, cochePuebla, camionPuebla, camionOax, placaEncontrada
        cadena = self.CampoCadena.text()
        if (len(cadena)) < 9:
            print("Error, faltan datos en la cadena")
        else:
            separarCadena = cadena.split("-")
            primeraSeccion = separarCadena[0]
            segundaSeccion = separarCadena[1]
            terceraSeccion = separarCadena[2]

            print("\nEsto contienen las secciones:",primeraSeccion,segundaSeccion,terceraSeccion)
            for i in range(len(primeraSeccion)):
                for j in range(len(baneados)):
                    if primeraSeccion[i] == baneados[j]:
                        print("-- Error hay un caracter no permitido -- ")
                        quit()
            
        # -- VEHICULOS
        if primeraSeccion[0] == "T" or primeraSeccion[0] == "U":
            # OAXACA
            for i in range(len(diccAutosOax)):
                if primeraSeccion[0] == "T" and primeraSeccion[1] == diccAutosOax[i]:
                    print("Vehiculo oaxaca valido -->", primeraSeccion[0], diccAutosOax[i])
                    cocheOax = True
                    placaEncontrada = True
                    break
            # PUEBLA
            for i in range(len(diccAutosPuebla1)):
                if primeraSeccion[0] == "T" and primeraSeccion[1] == diccAutosPuebla1[i]:
                    print("Vehiculo puebla valido -->",primeraSeccion[0], diccAutosPuebla1[i])
                    cochePuebla = True
                    placaEncontrada = True
                    break
            for i in range(len(diccAutosPuebla2)):
                if primeraSeccion[0] == "U" and primeraSeccion[1] == diccAutosPuebla2[i]:
                    print("Vehiculo puebla valido -->",primeraSeccion[0], diccAutosPuebla2[i])
                    cochePuebla = True
                    placaEncontrada = True
                    break
            self.comprobardigito3(primeraSeccion)
            self.comprobarNumerosCoches(segundaSeccion)
            self.comprobardigitoFinal(terceraSeccion)

        # -- CAMIONES
            # OAXACA
        else: 
            if primeraSeccion[0] == "R" or primeraSeccion[0] == "S":
                for i in range(len(diccCamionOaxaca)):
                    if primeraSeccion[0] == "R" and primeraSeccion[1] == diccCamionOaxaca[i]:
                        print("Camion oaxaca valido -->",primeraSeccion[0], diccCamionOaxaca[i])
                        camionOax = True
                        placaEncontrada = True
                        break
                # PUEBLA
                for i in range(len(diccCamionPuebla)):
                    if primeraSeccion[0] == "R" and primeraSeccion[1] == "Z":
                        print("Camion de puebla -->")
                        camionPuebla = True
                        placaEncontrada = True
                        break
                    if primeraSeccion[0] == "S" and primeraSeccion[1] == diccCamionPuebla[i]:
                        print("Camion de puebla -->")
                        camionPuebla = True
                        placaEncontrada = True
                        break
                self.comprobarNumeroCamion(segundaSeccion)
                self.comprobardigitoFinal(terceraSeccion)

        if placaEncontrada == True:
            if correr == True:
                if cocheOax == True:
                    messagebox.showinfo(message="PLACAS DE OAXACA", title="VEHICULO IDENTIFICADO")
                if cochePuebla == True:
                    messagebox.showinfo(message="PLACAS DE PUEBLA", title="VEHICULO IDENTIFICADO")
                if camionPuebla == True:
                    messagebox.showinfo(message="PLACAS DE PUEBLA", title="CAMION IDENTIFICADO")
                if camionOax == True:
                    messagebox.showinfo(message="PLACAS DE OAXACA", title="CAMION IDENTIFICADO")
                correr = False
                cocheOax = False
                cochePuebla = False
                camionPuebla = False
                camionOax = False
                placaEncontrada = False
        else:
            messagebox.showinfo(message="PLACAS NO RECONOCIDAS", title="ERROR")

    def limpiarCampo(self):
        self.CampoCadena.clear()

    def start(self):
        self.evaluarCadena()

    def abrirPDF(self):
        path = 'https://docs.google.com/document/d/1IeLEIMhq4hMdjPWsxpPlqWticIFwFW61oGMYxg2Xdfw/edit?usp=sharing'
        webbrowser.open_new(path)
        


        

