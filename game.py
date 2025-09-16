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

wallpaper= Image.open("image/fondo.jpg")
wallpaper= wallpaper.resize((390, 844))
fondo = ImageTk.PhotoImage(wallpaper)

labelWallpaper = tk.Label(ventana, image=fondo)
labelWallpaper.place(x=0, y=0, relwidth=1, relheight=1)

textoTitulo = tk.Label(
    ventana, 
    text="PIEDRA, PAPEL\nO\nTIJERA",
    font=("Press Start 2P", 20),
    bg="#05051d",  # Color azul oscuro similar al de tu imagen
    fg='white',    # Texto blanco
    relief='flat', # Sin relieve
    borderwidth=0  # Sin borde
)
textoTitulo.place(x=200, y=80, anchor="center")



def juego():
    ventana.destroy()
    ventanaJuego = tk.Tk()
    ventanaJuego.title("JUGAR")
    ventanaJuego.geometry("390x844")

    wallpaper= Image.open("image/wallpaper.jpg")
    wallpaper= wallpaper.resize((390, 844))
    fondo = ImageTk.PhotoImage(wallpaper)

    labelWallpaper = tk.Label(ventanaJuego, image=fondo)
    labelWallpaper.place(x=0, y=0, relwidth=1, relheight=1)

    # Color de fondo para que coincida con la imagen
    COLOR_FONDO = '#4a90e2'  # Azul similar al de tu imagen

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

    textoJuego = tk.Label(ventanaJuego, text="PULSA UN OBJETO PARA JUGAR", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
    textoJuego.place(x=200, y=70, anchor="center")

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
                labelPapel = tk.Label(ventanaJuego, image=imgPapel, bg=COLOR_FONDO)
                labelPapel.place(x= 200, y=300, anchor="center")
            elif eleccionIA == "Tijera":
                labelTijera = tk.Label(ventanaJuego, image=imgTijera, bg=COLOR_FONDO)
                labelTijera.place(x= 200, y= 300, anchor="center")
            elif eleccionIA == "Roca":
                labelRoca = tk.Label(ventanaJuego, image=imgRoca, bg=COLOR_FONDO)
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
                labelTexto2 = tk.Label(ventanaJuego, text="GANASTE", font=("Press Start 2P", 12), bg=COLOR_FONDO, fg='white')
                labelTexto2.place(x=200, y=600, anchor="center")
            elif puntosIA >=3:
                labelTexto3 = tk.Label(ventanaJuego, text="PERDISTE", font=("Press Start 2P", 12), bg=COLOR_FONDO, fg='white')
                labelTexto3.place(x=200, y=600, anchor="center")

        labelEleccion = tk.Label(ventanaJuego, text=f"TU: {eleccion_jugador} VS IA: {eleccionIA}", font=("Press Start 2P", 7), bg=COLOR_FONDO, fg='white')
        labelEleccion.place(x=200, y=400, anchor="center")

        if eleccionIA == eleccion_jugador:
            labelEmpate = tk.Label(ventanaJuego, text="EMPATE, NADIE SUMA PUNTO", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
            labelEmpate.place(x=200, y=500, anchor="center")
        elif (eleccion_jugador == "Roca" and eleccionIA == "Tijera") or (eleccion_jugador == "Tijera" and eleccionIA == "Papel") or (eleccion_jugador == "Papel" and eleccionIA == "Roca"):
            labelGanar = tk.Label(ventanaJuego, text="GANASTE, SUMAS UN PUNTO", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
            labelGanar.place(x=200, y=500, anchor="center")
        else:
            labelPerder = tk.Label(ventanaJuego, text="PERDISTE, LA IA SUMA UN PUNTO", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
            labelPerder.place(x=200, y=500, anchor="center")

        label_PuntosJugador= tk.Label(ventanaJuego, text=puntosJugador, font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
        label_PuntosJugador.place(x=40, y=220, anchor="sw")

        label_PuntosIA= tk.Label(ventanaJuego, text=puntosIA, font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white')
        label_PuntosIA.place(x=340, y=220, anchor="sw")
            
    label_TextJugador= tk.Label(ventanaJuego, text="JUGADOR: ", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white') 
    label_TextJugador.place(x=40, y=200, anchor="sw")  

    label_TextIA= tk.Label(ventanaJuego, text="IA: ", font=("Press Start 2P", 10), bg=COLOR_FONDO, fg='white') 
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

botonPlay = tk.Button(ventana, text="JUGAR", command=juego, font=("Press Start 2P", 20), fg="black", bg="white")
botonPlay.place(x=200, y=250, anchor="center" )

botonPlay = tk.Button(ventana, text="AJUSTES", command=juego, font=("Press Start 2P", 20), fg="black", bg="white")
botonPlay.place(x=200, y=400, anchor="center" )

botonPlay = tk.Button(ventana, text="HISTORIAL", command=juego, font=("Press Start 2P", 20), fg="black", bg="white")
botonPlay.place(x=200, y=550, anchor="center" )

botonPlay = tk.Button(ventana, text="SALIR", command=juego, font=("Press Start 2P", 20), fg="black", bg="white")
botonPlay.place(x=200, y=700, anchor="center" )

ventana.mainloop()