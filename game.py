import tkinter as tk
from PIL import Image, ImageTk

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
    imgRoca = imgRoca.resize((60,60))
    imgRoca = ImageTk.PhotoImage(imgRoca)

    
    #hacer boton la imagen
    buttonRoca = tk.Button(ventanaJuego, image=imgRoca, command="Roca")
    ventanaJuego.update()
    buttonRoca.place(x=40, y=ventanaJuego.winfo_height() - 100, anchor="sw")
    
    ventanaJuego.mainloop()

botonPlay = tk.Button(ventana, text="JUGAR", command=juego)
botonPlay.pack()

ventana.mainloop()