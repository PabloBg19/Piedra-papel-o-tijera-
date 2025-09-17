import pygame
import tkinter as tk
from PIL import Image, ImageTk

class CambiarSonido:
    def __init__(self, sonidos, parent, volumen_inicial=0.5):
        # Inicializar Pygame para audio (si no está inicializado)
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        # Guardar sonidos (ya son objetos pygame.mixer.Sound)
        self.sonidos = sonidos
        self.volumen = volumen_inicial
        self.canal = pygame.mixer.Channel(0)  # Usar canal 0 para controlar reproducción
        
        # Establecer volumen inicial para todos los sonidos
        for sonido in self.sonidos:
            sonido.set_volume(self.volumen)
        
        # Crear ventana Toplevel en lugar de Tk
        self.root = tk.Toplevel(parent)
        self.root.title("Ajustes de Sonido")
        self.root.geometry("390x844")
        
        # Cargar imagen de fondo con Pillow
        try:
            imagen = Image.open("image/fondoSound.jpg")
            imagen = imagen.resize((390, 844), Image.Resampling.LANCZOS)
            self.fondo = ImageTk.PhotoImage(imagen)
            fondo_label = tk.Label(self.root, image=self.fondo)
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Mantener referencia explícita
            fondo_label.image = self.fondo
        except Exception as e:
            print(f"Error al cargar imagen: {e}")
        
        # Etiqueta para mostrar el volumen actual
        self.label_volumen = tk.Label(self.root, text=f"Volumen: {int(self.volumen * 100)}%", 
                                     font=("Arial", 12), bg="white")
        self.label_volumen.pack(pady=10)
        
        # Slider para ajustar el volumen
        self.slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, 
                              label="Ajustar Volumen", command=self.cambiar_volumen)
        self.slider.set(self.volumen * 100)  # Valor inicial en porcentaje
        self.slider.pack(pady=10)
        
        # Botones para reproducir cada sonido
        self.boton_sonido1 = tk.Button(self.root, text="Reproducir Across the Stars", 
                                      command=lambda: self.reproducir_sonido(0),
                                      font=("Press Start 2P", 10), fg="black", bg="white")
        self.boton_sonido1.pack(pady=10)
        
        self.boton_sonido2 = tk.Button(self.root, text="Reproducir Life is a Highway", 
                                      command=lambda: self.reproducir_sonido(1),
                                      font=("Press Start 2P", 10), fg="black", bg="white")
        self.boton_sonido2.pack(pady=10)
        
    def cambiar_volumen(self, valor):
        # Actualizar volumen (valor del slider está en 0-100, lo convertimos a 0-1)
        self.volumen = float(valor) / 100
        for sonido in self.sonidos:
            sonido.set_volume(self.volumen)
        self.label_volumen.config(text=f"Volumen: {int(self.volumen * 100)}%")
        # Actualizar volumen del canal si está reproduciendo
        if self.canal.get_busy():
            self.canal.set_volume(self.volumen)
    
    def reproducir_sonido(self, indice):
        # Detener cualquier sonido que esté sonando en el canal
        self.canal.stop()
        # Reproducir el sonido seleccionado en el canal
        self.canal.play(self.sonidos[indice])
    
    def run(self):
        # Iniciar el bucle principal de la ventana
        self.root.transient(self.root.master)  # Hacer la ventana secundaria
        self.root.grab_set()  # Capturar eventos hasta que se cierre
        self.root.wait_window()  # Esperar hasta que se cierre la ventana