import pytubefix
from pytubefix import YouTube
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import font
import re

url_guardada = None
yt = None


def guardar_url():
    global url_guardada, yt
    url_guardada = entrada.get()

    patron_youtube = re.compile(r'(https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+|https?://youtu\.be/[\w-]+)')
    
    if url_guardada: 
        if patron_youtube.match(url_guardada):  
            try:
                yt = YouTube(url_guardada)
                print("URL guardada:", url_guardada)
                label_resultado.config(text=f"Tu video es: {yt.title}", fg="black")
                label_tiempo.config(text=f"Duración: {yt.length} segundos", fg="black")
            except Exception as e:
                label_resultado.config(text="Error al obtener el video.", fg="red")
                label_tiempo.config(text="")
        else:
            label_resultado.config(text="Por favor, introduce una URL válida de YouTube.", fg="red")
            label_tiempo.config(text="")
    else:
        label_resultado.config(text="Por favor, introduce una URL.", fg="black")
        label_tiempo.config(text="")

def descargaVid():
    if yt:
        
        carpeta_videos = "Videos"
        if not os.path.exists(carpeta_videos):
            os.makedirs(carpeta_videos)

        videoStream = yt.streams.get_highest_resolution()
        messagebox.showinfo("Descargar Video", "¡Descargando video!")
        videoStream.download(output_path=carpeta_videos)
        messagebox.showinfo("Descargar Video", f"¡Video descargado en la carpeta '{carpeta_videos}'!")
    else: messagebox.showerror("error","introduce una url y precione 'Obtener video' antes")

def descargarAud():
    if yt:
        carpeta_audios = "Audios"
        if not os.path.exists(carpeta_audios):
            os.makedirs(carpeta_audios)
        audioStream = yt.streams.filter(only_audio=True).first()
        messagebox.showinfo("Descargar Audio", "¡Descargando audio!")
        audioStream.download(output_path=carpeta_audios)
        messagebox.showinfo("Descargar Audio", f"¡Audio descargado en la carpeta '{carpeta_audios}'!")
    
ventana = tk.Tk()

ventana.title("YT DOWNLOADER")
ventana.geometry("500x500")
ventana.configure(bg="#f4f4f4") 

fuente_titulo = font.Font(family="Arial", size=16, weight="bold")
fuente_botones = font.Font(family="Arial", size=12, weight="bold")
titulo = tk.Label(ventana, text="YT Downloader", font=fuente_titulo, bg="#f4f4f4", fg="#ff0068")
titulo.pack(pady=20)
entrada = tk.Entry(ventana, width=50, font=("Arial", 14), bd=2, relief="sunken", justify="center", fg="#333333")
entrada.pack(pady=20)
botonGuardar = tk.Button(ventana, text="Obtener Video", width=20, height=2, font=fuente_botones, command=guardar_url, bg="#ff0068", fg="white", bd=1, relief="raised", activebackground="#ff4c85")
botonGuardar.pack(pady=20)
label_resultado = tk.Label(ventana, text="", bg="#f4f4f4", fg="#333333", font=("Arial", 12))
label_resultado.pack(pady=10)


label_tiempo = tk.Label(ventana, text="", bg="#f4f4f4", fg="#333333", font=("Arial", 12))
label_tiempo.pack(pady=10)
frame_botones = tk.Frame(ventana, bg="#f4f4f4")
frame_botones.pack(pady=30)
botonVid = tk.Button(frame_botones, text="Video", width=20, height=2, font=fuente_botones, command=descargaVid, bg="#ff0068", fg="white", bd=1, relief="raised", activebackground="#ff4c85")
botonVid.pack(side="left", padx=15)
botonAud = tk.Button(frame_botones, text="Audio", width=20, height=2, font=fuente_botones, command=descargarAud, bg="#ff0068", fg="white", bd=1, relief="raised", activebackground="#ff4c85")
botonAud.pack(side="left", padx=15)


ventana.mainloop()

