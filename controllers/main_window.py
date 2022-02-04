from cgitb import text
from importlib.resources import path
from tkinter import messagebox
from PySide2.QtWidgets import QWidget
from views.main_window import VentanaPrincipal
import string
import webbrowser

#Diccionarios para la filtracion y analisis
cadena = ""
abcOax2 = ["H","J","K","L","M"]
baneados = ["I","O","Q","Ñ"]
diccionarioCaracterPuebla = ["N","P","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","J"]
camionOax = ["R","S","T","U","V","W","X","Y"]
camionPuebla = ["Z","A","B","C","D","E","F","G","H","J","K","L","M","N","P","R"]
abcCompleto = string.ascii_uppercase #Esto sirve para saber todo el abecedario para hacer futuras comparaciones.
correr = True
cocheOax = False
cochePuebla = False
BanderacamionOax = False
BanderacamionPuebla = False



class Ventana(QWidget, VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Evaluar.clicked.connect(self.start)
        self.Limpiar.clicked.connect(self.limpiarCampo)
        self.Diagrama.clicked.connect(self.abrirPDF)

    def evaluarCadena(self):
        global cocheOax, correr, cochePuebla, camionPuebla, camionOax, BanderacamionOax, BanderacamionPuebla
        correr = True
        cocheOax = False
        cadena = self.CampoCadena.text()
        if (len(cadena)) < 9:
            print("Error, faltan datos en la cadena")
        else:
            #print("Esto contiene la cadena ingresada:",cadena)
            separarCadena = cadena.split("-")
            #print("Ahora esto contiene la cadena:",separarCadena)

            primeraSeccion = separarCadena[0]
            segundaSeccion = separarCadena[1]
            terceraSeccion = separarCadena[2]

            print("\nEsto contienen las secciones:",primeraSeccion,segundaSeccion,terceraSeccion)
            for i in range(len(baneados)):
                if primeraSeccion[1] != baneados[i]:
            ###! VEHICULOS
                    if primeraSeccion[0] == "T" or primeraSeccion[0] == "U":
                        print("- Primer caracter",primeraSeccion[0])
                        # Oaxaca
                        for i in range(len(abcOax2)):
                            if primeraSeccion[1] == abcOax2[i] and primeraSeccion[0] != "U":
                                print("- Segundo caracter:",abcOax2[i])
                                cocheOax = True
                                break
                        # Puebla
                        for i in range(len(diccionarioCaracterPuebla)):
                            if primeraSeccion[1] == diccionarioCaracterPuebla[i]:
                                print("- Segundo caracter:",diccionarioCaracterPuebla[i])
                                cochePuebla = True
                                break
                        for i in range(len(abcCompleto)):
                            if primeraSeccion[2] == abcCompleto[i]:
                                print("- Tercer caracter",abcCompleto[i])
                                break
                    else:
                        ###! CAMIONES
                        if primeraSeccion[0] == "R" or primeraSeccion[0] == "S":
                            print("- Primer caracter",primeraSeccion[0])
                            for i in range(len(camionOax)):
                                if primeraSeccion[1] == camionOax[i] and primeraSeccion[0] != "S":
                                    print("- Segundo caracter:",camionOax[i])
                                    BanderacamionOax = True
                                    break
                            for i in range(len(camionPuebla)):
                                if primeraSeccion[1] == camionPuebla[i]:
                                    print("- Segundo caracter:",camionPuebla[i])
                                    BanderacamionPuebla = True
                                    break
                        else:
                            print("No se identifica")
                            correr = False
                            break
                    if correr == True:
                        if cadena[3] == "-" or cadena[2] == "-":
                            if cadena[7] == "-":
                                print("Guiones correctos")
                            for i in range(9):
                                if int(segundaSeccion[0]) == i:
                                    print("- Numero:",i)
                            for i in range(9):
                                if int(segundaSeccion[1]) == i:
                                    print("- Numero:",i)
                            for i in range(9):
                                if int(segundaSeccion[2]) == i:
                                    print("- Numero:",i)
                            if BanderacamionOax or BanderacamionPuebla:
                                if int(segundaSeccion[3]) == i:
                                    print("- Numero:",i)
                            for i in range(len(abcCompleto)):
                                if terceraSeccion == abcCompleto[i]:
                                    print("- Ultimo caracter:", abcCompleto[i])
                            print("--- CADENA COMPLETADA ---")
                            if cocheOax:
                                print("--- AUTOMOVIL - OAXACA ---")
                                messagebox.showinfo(message="PLACAS DE OAXACA", title="VEHICULO IDENTIFICADO")
                                cocheOax = False
                                break
                            if cochePuebla:
                                print("--- AUTOMOVIL - PUEBLA ---")
                                messagebox.showinfo(message="PLACAS DE PUEBLA", title="VEHICULO IDENTIFICADO")
                                cochePuebla = False
                                break
                            if BanderacamionOax:
                                print("--- CAMION - OAXACA ---")
                                messagebox.showinfo(message="PLACAS DE OAXACA", title="CAMION IDENTIFICADO")
                                BanderacamionOax = False
                                break
                            if BanderacamionPuebla:
                                print("--- CAMION - PUEBLA ---")
                                messagebox.showinfo(message="PLACAS DE PUEBLA", title="CAMION IDENTIFICADO")
                                BanderacamionPuebla = False
                                break
                        else:
                            print("--- ERROR EN GUIONES ---")
                else:
                    print("- Caracter no permitido:",baneados[i])
                    break
            # Evaluar numeros

    def limpiarCampo(self):
        self.CampoCadena.clear()

    def start(self):
        self.evaluarCadena()

    def abrirPDF(self):
        path = 'https://docs.google.com/document/d/1IeLEIMhq4hMdjPWsxpPlqWticIFwFW61oGMYxg2Xdfw/edit?usp=sharing'
        webbrowser.open_new(path)
        


        

