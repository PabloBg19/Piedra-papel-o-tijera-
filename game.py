import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
from settingsSounds import CambiarSonido

play = False
puntosIA = 0
puntosJugador = 0
ronda = 0
partidaGanadaUsuario = 0
partidaGanadaIA = 0
# Variables globales del juego
def main(): 
    

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Piedra papel o tijera")
    ventana.geometry("390x844")

    # Configurar el fondo de la ventana principal
    wallpaper = Image.open("image/fondo.jpg")
    wallpaper = wallpaper.resize((390, 844))
    fondo = ImageTk.PhotoImage(wallpaper)

    labelWallpaper = tk.Label(ventana, image=fondo)
    labelWallpaper.place(x=0, y=0, relwidth=1, relheight=1)
    labelWallpaper.image = fondo  # Mantener referencia

    # Crear el título del juego
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

    # Inicializar pygame y reproducir sonido de fondo
    pygame.mixer.init()
    sonidos = [
        pygame.mixer.Sound("sounds/Across the Stars- Love Theme.mp3"),
        pygame.mixer.Sound("sounds/Life is a Highway.mp3")
    ]

    sonido_aleatorio = random.choice(sonidos)
    sonido_aleatorio.play()

    def ajustes():
        """Función para abrir la ventana de ajustes"""
        # Crear instancia de CambiarSonido con la lista de sonidos y la ventana principal como parent
        app = CambiarSonido(sonidos=sonidos, parent=ventana, volumen_inicial=0.5)
        app.run()

    def juego():
        """Función principal del juego"""
        ventana.withdraw()  # Ocultar la ventana principal
        
        # Crear ventana secundaria para el juego
        ventanaJuego = tk.Toplevel(ventana)  # Usar Toplevel en lugar de Tk
        ventanaJuego.title("JUGAR")
        ventanaJuego.geometry("390x844")

        # Configurar fondo de la ventana de juego
        wallpaper = Image.open("image/wallpaper.jpg")
        wallpaper = wallpaper.resize((390, 844))
        fondo = ImageTk.PhotoImage(wallpaper)

        labelWallpaper = tk.Label(ventanaJuego, image=fondo)
        labelWallpaper.place(x=0, y=0, relwidth=1, relheight=1)
        labelWallpaper.image = fondo  # Mantener referencia

        # Color de fondo para que coincida con la imagen
        COLOR_FONDO = '#4a90e2'  # Azul similar al de tu imagen

        # Cargar y redimensionar las imágenes del juego
        imgRoca = Image.open("image/Roca.png")
        imgRoca = imgRoca.resize((90, 90))
        imgRoca = ImageTk.PhotoImage(imgRoca)

        imgPapel = Image.open("image/Papel.png")
        imgPapel = imgPapel.resize((90, 90))
        imgPapel = ImageTk.PhotoImage(imgPapel)

        imgTijera = Image.open("image/Tijera.png")
        imgTijera = imgTijera.resize((90, 90))
        imgTijera = ImageTk.PhotoImage(imgTijera)

        imgReturn = Image.open("Image/return.png")
        imgReturn = imgReturn.resize((50, 50))  # Tamaño del botón de retorno
        imgReturn = ImageTk.PhotoImage(imgReturn)

        # Texto de instrucciones
        textoJuego = tk.Label(
            ventanaJuego, 
            text="PULSA UN OBJETO PARA JUGAR", 
            font=("Press Start 2P", 10), 
            bg=COLOR_FONDO, 
            fg='white'
        )
        textoJuego.place(x=200, y=70, anchor="center")

        def cambiar_estado(eleccion_jugador):
            """Función que maneja la lógica del juego cuando el jugador hace una elección"""
            global play, puntosIA, puntosJugador, ronda, partidaGanadaUsuario, partidaGanadaIA
            
            play = True
            
            # Lógica de la IA
            if play == True:
                eleccion = ["Tijera", "Papel", "Roca"]
                eleccionIA = random.choice(eleccion)
                print(eleccionIA)
                print(eleccion_jugador)

                # Mostrar la imagen de la elección de la IA
                if eleccionIA == "Papel":
                    labelPapel = tk.Label(ventanaJuego, image=imgPapel, bg=COLOR_FONDO)
                    labelPapel.place(x=200, y=300, anchor="center")
                    labelPapel.image = imgPapel
                elif eleccionIA == "Tijera":
                    labelTijera = tk.Label(ventanaJuego, image=imgTijera, bg=COLOR_FONDO)
                    labelTijera.place(x=200, y=300, anchor="center")
                    labelTijera.image = imgTijera
                elif eleccionIA == "Roca":
                    labelRoca = tk.Label(ventanaJuego, image=imgRoca, bg=COLOR_FONDO)
                    labelRoca.place(x=200, y=300, anchor="center")
                    labelRoca.image = imgRoca

                # Función de puntuaje - determinar ganador de la ronda
                if eleccionIA == eleccion_jugador:
                    # Empate
                    puntosIA += 0
                    puntosJugador += 0
                    ronda += 1
                    print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)
                elif (eleccion_jugador == "Roca" and eleccionIA == "Tijera") or \
                    (eleccion_jugador == "Tijera" and eleccionIA == "Papel") or \
                    (eleccion_jugador == "Papel" and eleccionIA == "Roca"):
                    # Jugador gana
                    puntosJugador += 1
                    ronda += 1
                    print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)
                else:
                    # IA gana
                    puntosIA += 1
                    ronda += 1
                    print(ronda, " puntosIA: ", puntosIA, " puntos Jugador", puntosJugador)

                # Verificar si alguien ganó el juego (primero en llegar a 3 puntos)
                if puntosJugador >= 3:
                    labelTexto2 = tk.Label(
                        ventanaJuego, 
                        text="GANASTE", 
                        font=("Press Start 2P", 12), 
                        bg=COLOR_FONDO, 
                        fg='white'
                    )
                    puntosIA = 0
                    puntosJugador = 0
                    partidaGanadaUsuario += 1
                    labelTexto2.place(x=200, y=600, anchor="center")
                elif puntosIA >= 3:
                    labelTexto3 = tk.Label(
                        ventanaJuego, 
                        text="PERDISTE", 
                        font=("Press Start 2P", 12), 
                        bg=COLOR_FONDO, 
                        fg='white'
                    )
                    puntosIA = 0
                    puntosJugador = 0
                    partidaGanadaIA += 1
                    labelTexto3.place(x=200, y=600, anchor="center")

                textoRonda = tk.Label(
                    ventanaJuego, 
                    text=f"RONDAS GANADAS \n TU: {partidaGanadaUsuario} IA: {partidaGanadaIA}",
                    font=("Press Start 2P", 12),
                    bg=COLOR_FONDO,
                    fg='white'
                )
                textoRonda.place(x=200, y=ventanaJuego.winfo_height() - 50, anchor="s")

            # Mostrar las elecciones de ambos jugadores
            labelEleccion = tk.Label(
                ventanaJuego, 
                text=f"TU: {eleccion_jugador} VS IA: {eleccionIA}", 
                font=("Press Start 2P", 7), 
                bg=COLOR_FONDO, 
                fg='white'
            )
            labelEleccion.place(x=200, y=400, anchor="center")

            # Mostrar el resultado de la ronda
            if eleccionIA == eleccion_jugador:
                labelEmpate = tk.Label(
                    ventanaJuego, 
                    text="      EMPATE, NADIE SUMA PUNTO     ", 
                    font=("Press Start 2P", 10), 
                    bg=COLOR_FONDO, 
                    fg='white'
                )
                labelEmpate.place(x=200, y=500, anchor="center")
            elif (eleccion_jugador == "Roca" and eleccionIA == "Tijera") or \
                (eleccion_jugador == "Tijera" and eleccionIA == "Papel") or \
                (eleccion_jugador == "Papel" and eleccionIA == "Roca"):
                labelGanar = tk.Label(
                    ventanaJuego, 
                    text="       GANASTE, SUMAS UN PUNTO         ", 
                    font=("Press Start 2P", 10), 
                    bg=COLOR_FONDO, 
                    fg='white'
                )
                labelGanar.place(x=200, y=500, anchor="center")
            else:
                labelPerder = tk.Label(
                    ventanaJuego, 
                    text=" PERDISTE, LA IA SUMA UN PUNTO", 
                    font=("Press Start 2P", 10), 
                    bg=COLOR_FONDO, 
                    fg='white'
                )
                labelPerder.place(x=200, y=500, anchor="center")

            # Mostrar puntuación actual del jugador
            label_PuntosJugador = tk.Label(
                ventanaJuego, 
                text=puntosJugador, 
                font=("Press Start 2P", 10), 
                bg=COLOR_FONDO, 
                fg='white'
            )
            label_PuntosJugador.place(x=40, y=220, anchor="sw")

            # Mostrar puntuación actual de la IA
            label_PuntosIA = tk.Label(
                ventanaJuego, 
                text=puntosIA, 
                font=("Press Start 2P", 10), 
                bg=COLOR_FONDO, 
                fg='white'
            )
            label_PuntosIA.place(x=340, y=220, anchor="sw")

        # Etiquetas para mostrar quién es cada jugador
        label_TextJugador = tk.Label(
            ventanaJuego, 
            text="JUGADOR: ", 
            font=("Press Start 2P", 10), 
            bg=COLOR_FONDO, 
            fg='white'
        ) 
        label_TextJugador.place(x=40, y=200, anchor="sw")  

        label_TextIA = tk.Label(
            ventanaJuego, 
            text="IA: ", 
            font=("Press Start 2P", 10), 
            bg=COLOR_FONDO, 
            fg='white'
        ) 
        label_TextIA.place(x=360, y=200, anchor="se") 

        # Crear botones con las imágenes - Botón Roca
        buttonRoca = tk.Button(
            ventanaJuego, 
            image=imgRoca, 
            command=lambda: cambiar_estado("Roca")
        )
        ventanaJuego.update()
        buttonRoca.place(x=40, y=ventanaJuego.winfo_height() - 100, anchor="sw")
        
        # Botón Papel
        buttonPapel = tk.Button(
            ventanaJuego, 
            image=imgPapel, 
            command=lambda: cambiar_estado("Papel")
        )
        ventanaJuego.update()
        buttonPapel.place(x=200, y=ventanaJuego.winfo_height() - 100, anchor="s")

        # Botón Tijera
        buttonTijera = tk.Button(
            ventanaJuego, 
            image=imgTijera, 
            command=lambda: cambiar_estado("Tijera")
        )
        ventanaJuego.update()
        buttonTijera.place(x=360, y=ventanaJuego.winfo_height() - 100, anchor="se")

        def salir_juego():
            """Función para cerrar la ventana de juego y volver al menú principal"""
            ventanaJuego.destroy()
            ventana.deiconify()  # Mostrar la ventana principal nuevamente

        buttonreturn = tk.Button(
            ventanaJuego,
            image=imgReturn,
            command=salir_juego
        )

        buttonreturn.place(x=0, y=ventanaJuego.winfo_height(), anchor="sw")

        # Iniciar el bucle principal de la ventana de juego
        ventanaJuego.mainloop()

    # Botones del menú principal
    botonPlay = tk.Button(
        ventana, 
        text="JUGAR", 
        command=juego, 
        font=("Press Start 2P", 20), 
        fg="black", 
        bg="white"
    )
    botonPlay.place(x=200, y=250, anchor="center")

    botonAjustes = tk.Button(
        ventana, 
        text="AJUSTES", 
        command=ajustes, 
        font=("Press Start 2P", 20), 
        fg="black", 
        bg="white"
    )
    botonAjustes.place(x=200, y=400, anchor="center")

    botonHistorial = tk.Button(
        ventana, 
        text="HISTORIAL", 
        command=juego, 
        font=("Press Start 2P", 20), 
        fg="black", 
        bg="white"
    )
    botonHistorial.place(x=200, y=550, anchor="center")

    botonSalir = tk.Button(
        ventana, 
        text="SALIR", 
        command=ventana.quit, 
        font=("Press Start 2P", 20), 
        fg="black", 
        bg="white"
    )
    botonSalir.place(x=200, y=700, anchor="center")

    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()

if __name__ == "__main__":
    main()