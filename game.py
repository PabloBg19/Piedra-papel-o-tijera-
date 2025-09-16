import tkinter as tk
from PIL import Image, ImageTk
import random

play = False
puntosIA=0
puntosJugador=0
ronda=0

ventana = tk.Tk()       #crea la ventana
ventana.title("Piedra papel o tijera")
ventana.geometry("390x844")

textoTitulo = tk.Label(ventana, text="Piedra, Papel o Tijera")
textoTitulo.pack() #coloca el texto en la ventana

def juego():
    ventana.destroy()
    ventanaJuego = tk.Tk()
    ventanaJuego.title("JUGAR")
    ventanaJuego.geometry("390x844")

    #creacion de la imagen
    imgRoca = Image.open("image/Roca.png")
    imgRoca = imgRoca.resize((90,90))
    imgRoca = ImageTk.PhotoImage(imgRoca)

    imgPapel = Image.open("image/Papel.png")
    imgPapel = imgPapel.resize((90,90))
    imgPapel = ImageTk.PhotoImage(imgPapel)

    imgTijera = Image.open("image/Tijera.png")
    imgTijera = imgTijera.resize((90,90))
    imgTijera = ImageTk.PhotoImage(imgTijera)

    def cambiar_estado(eleccion_jugador):
        
        global play
        global puntosIA
        global puntosJugador
        global ronda
        play = True
        #funcion de la IA
        if play == True:
            eleccion = ["Tijera", "Papel", "Roca"]
            eleccionIA = random.choice(eleccion)
            print(eleccionIA)
            print(eleccion_jugador)

            #Mostrar Imagen
            if eleccionIA == "Papel":
                labelPapel = tk.Label(ventanaJuego, image=imgPapel)
                labelPapel.place(x= 200, y=300, anchor="center")
            elif eleccionIA == "Tijera":
                labelTijera = tk.Label(ventanaJuego, image=imgTijera)
                labelTijera.place(x= 200, y= 300, anchor="center")
            elif eleccionIA == "Roca":
                labelRoca = tk.Label(ventanaJuego, image=imgRoca)
                labelRoca.place(x= 200, y= 300, anchor="center")

            #Funcion de puntuaje            
            if eleccionIA == eleccion_jugador:
                puntosIA+=0
                puntosJugador+=0
                ronda+=1
                print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)
            elif (eleccion_jugador=="Roca" and eleccionIA=="Tijera") or (eleccion_jugador=="Tijera" and eleccionIA=="Papel") or (eleccion_jugador=="Papel" and eleccionIA=="Roca"):
                puntosJugador+=1
                ronda+=1
                print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)
            else:
                puntosIA+=1
                ronda+=1
                print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)

            if puntosJugador >=3:
                labelTexto2 = tk.Label(ventanaJuego, text="GANASTE")
                labelTexto2.place(x=200, y=600, anchor="center")
            elif puntosIA >=3:
                labelTexto3 = tk.Label(ventanaJuego, text="PERDISTE")
                labelTexto3.place(x=200, y=600, anchor="center")

        labelEleccionJugador = tk.Label(ventanaJuego, text=("TU: ", eleccion_jugador))
        labelEleccionJugador.place(x=150, y=400, anchor="center")

        labelVS = tk.Label(ventanaJuego , text="VS")
        labelVS.place(x=200, y=400, anchor="center")

        labelEleccionIA = tk.Label(ventanaJuego, text=("IA: ", eleccionIA))
        labelEleccionIA.place(x=250, y=400, anchor="center")

        if eleccionIA == eleccion_jugador:
            labelEmpate= tk.Label(ventanaJuego, text="  EMPATE NADIE SUMA PUNTO  ")
            labelEmpate.place(x=200, y=500, anchor="center" )
        elif (eleccion_jugador=="Roca" and eleccionIA=="Tijera") or (eleccion_jugador=="Tijera" and eleccionIA=="Papel") or (eleccion_jugador=="Papel" and eleccionIA=="Roca"):
            labelGanar= tk.Label(ventanaJuego, text="   GANASTE SUMAS UN PUNTO   ")
            labelGanar.place(x=200, y=500, anchor="center" )
        else:
            labelPerder= tk.Label(ventanaJuego, text="PERDISTE LA IA SUMA UN PUNTO")
            labelPerder.place(x=200, y=500, anchor="center" )


        label_PuntosJugador= tk.Label(ventanaJuego, text=puntosJugador)
        label_PuntosJugador.place(x=40, y=220, anchor="sw")

        label_PuntosIA= tk.Label(ventanaJuego, text=puntosIA)
        label_PuntosIA.place(x=360, y=220, anchor="sw")
            
    label_TextJugador= tk.Label(ventanaJuego, text="JUGADOR: ") 
    label_TextJugador.place(x=40, y=200, anchor="sw")  

    label_TextIA= tk.Label(ventanaJuego, text="IA: ") 
    label_TextIA.place(x=360, y=200, anchor="se") 

         
    #hacer boton la imagen
    buttonRoca = tk.Button(ventanaJuego, image=imgRoca, command=lambda: cambiar_estado("Roca"))
    ventanaJuego.update()
    buttonRoca.place(x=40, y=ventanaJuego.winfo_height() - 100, anchor="sw")
    
    buttonPapel = tk.Button(ventanaJuego, image=imgPapel, command=lambda: cambiar_estado("Papel"))
    ventanaJuego.update()
    buttonPapel.place(x= 200, y=ventanaJuego.winfo_height() - 100, anchor="s")

    buttonTijera = tk.Button(ventanaJuego, image=imgTijera, command=lambda: cambiar_estado("Tijera"))
    ventanaJuego.update()
    buttonTijera.place(x= 360, y=ventanaJuego.winfo_height() - 100, anchor="se")

    ventanaJuego.mainloop()

botonPlay = tk.Button(ventana, text="JUGAR", command=juego)
botonPlay.pack()


ventana.mainloop()