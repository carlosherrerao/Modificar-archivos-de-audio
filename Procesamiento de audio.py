# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:29:46 2020

@author: parka
"""
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pydub import AudioSegment
import librosa
import shutil
import soundfile
import audio_metadata

# Start coding here
class Application:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        
        self.archivos = None
        self.archivo = None
        self.folder_selected = None
        self.bit_depth = tk.IntVar()
        self.downsample = tk.IntVar()
        self.informacion =  ""
        
        root.title('Herramientas')
        #color de fondo de la ventana
        root.configure(bg='#000000')
        # Establecemos el tamaño de la raíz
        root.geometry("680x460+0+0")
        
        #image_button1=photo = tk.PhotoImage(file = r"imagenes\mp3_to_wav.jpg")
        image_button1 = ImageTk.PhotoImage(Image.open(r'imagenes\\mp3_to_wav.png'))
        image_button2 = ImageTk.PhotoImage(Image.open(r'imagenes\\boton_editaraudios.png'))
        image_button3 = ImageTk.PhotoImage(Image.open(r'imagenes\\ver info.png'))
        image_button4 = ImageTk.PhotoImage(Image.open(r'imagenes\\audacity.png'))
        #Button 1
        button1 = tk.Button(root,image =image_button1,bg='#000000',relief="solid",command = lambda: self.CambiarFormato(root))
        button1.image =image_button1
        button1.place(x=20,y=20) 
        #Button 2
        button2 = tk.Button(root,image =image_button2,bg='#000000',relief="solid",command = lambda: self.Editar_parametros_audio(root))
        button2.image =image_button2
        button2.place(x=240,y=20) 
        #Button 3
        button3 = tk.Button(root,image =image_button3,bg='#000000',relief="solid",command = lambda: self.ver_info(root))
        button3.image =image_button3
        button3.place(x=460,y=20)
        #Button 4
        button4 = tk.Button(root,image =image_button4,bg='#000000',relief="solid",command = self.abrir_audacity)
        button4.image =image_button4
        button4.place(x=20,y=240) 
    def CambiarFormato(self,root):
        
        newWindow = tk.Toplevel(root) 
        
        newWindow.title("Cambiar formato de audio") 
          
        newWindow.configure(bg='#000000')
        # Establecemos el tamaño de la raíz
        newWindow.geometry("500x226+680+0")
        #columnas y filas para un pack grid
        newWindow.columnconfigure(0, weight=1)
        newWindow.rowconfigure(0, weight=1)
        
        #Label que corresponde al texto
        titulo = tk.Label(newWindow,text="Cambiar formato Mp3 a WAV:",
                          font=("Segou UI",16),
                          bg='#000000',
                          fg="white")
        
        titulo.place(x=108,y=20)
        
        #Texto 
        texto1 = tk.Label(newWindow,text="Selecciona los archivos de audio:",
                          font=("Segou UI",14),
                          bg='#000000', 
                          fg="white")
        
        texto1.place(x=50,y=80)
        
        #Boton de selecciona un archivo
        button = tk.Button(newWindow, text='Open', 
                           font=("Segou UI",14),
                           bg='#3f3f3f',  
                           fg="white",
                           relief="solid",
                           command=self.seleccionar_archivos)
        
        button.place(x=382,y=77)

        #Texto 
        texto2 = tk.Label(newWindow,text="Guardar en:",
                          font=("Segou UI",14),
                          bg='#000000', 
                          fg="white")
        
        texto2.place(x=50,y=128)        
        
        #Boton de selecciona una ruta
        button2 = tk.Button(newWindow, text='Open', 
                           font=("Segou UI",14),
                           bg='#3f3f3f',  
                           fg="white",
                           relief="solid",
                           command=self.seleccionar_folder)
        
        button2.place(x=382,y=125)        
        
        #Button
        button3 = tk.Button(newWindow,text='Cambiar',
                            font=("Segou UI",14),
                            bg='#3f3f3f', 
                            fg="white", 
                            relief="solid",
                            command = self.Cambiar)
        button3.place(x=208,y=176)
    def ver_info(self, root):
        newWindow = tk.Toplevel(root) 
        
        newWindow.title("Ver propiedades del audio") 
          
        newWindow.configure(bg='#000000')
        # Establecemos el tamaño de la raíz
        newWindow.geometry("500x327+680+0")
        #columnas y filas para un pack grid
        newWindow.columnconfigure(0, weight=1)
        newWindow.rowconfigure(0, weight=1) 
        
        #Label que corresponde al texto
        titulo = tk.Label(newWindow,text="Ver propiedades del audio:",
                          font=("Segou UI",16),
                          bg='#000000',
                          fg="white")
        
        titulo.place(x=108,y=20)        
        #Texto 
        texto1 = tk.Label(newWindow,text="Selecciona el archivo de audio:",
                          font=("Segou UI",14),
                          bg='#000000', 
                          fg="white")
        
        texto1.place(x=50,y=80)
        #Texto 
        info = tk.Label(newWindow, text ="",
                          font=("Segou UI",14),
                          bg='#000000', 
                           width= 40,
                          fg="white")

        info.place(x=50,y=128)        
        #Boton de selecciona un archivo
        button = tk.Button(newWindow, text='Open', 
                           font=("Segou UI",14),
                           bg='#3f3f3f',  
                           fg="white",
                           relief="solid",
                           command = lambda : self.Mostrar_info(info))
        
        button.place(x=382,y=77)

    def abrir_audacity(self):
        os.startfile(r'C:\Program Files (x86)\Audacity\audacity.exe')

        
    def Mostrar_info(self,info):
        filename = filedialog.askopenfilename(filetypes =[('WAV Files', '*.wav')])
        self.archivo = list(filename)
        wav = ''.join(self.archivo)
        propiedades = audio_metadata.load(wav)
        
        
        Ruta1 = "Ruta: " + str(propiedades["filepath"])
        Ruta = self.formato(Ruta1)
        AudioFormat =  "AudioFormat: " + str(propiedades["streaminfo"]['audio_format'])
        Bit_depth = "Bit_depth: " + str(propiedades["streaminfo"]['bit_depth'])
        Sample_rate = "Sample_rate: " + str(propiedades["streaminfo"]['sample_rate'])
        
        self.informacion = Ruta+'\n'+AudioFormat+'\n'+Bit_depth+'\n'+Sample_rate
        info.config(text = self.informacion)
    def formato(self,texto):
        n = 0
        cadena = ""
        for i in range(len(texto)):
            if n == 30:
                cadena = cadena + '\n'+ texto[i]
                n = 0
            else:
                cadena = cadena + texto[i]
                n = n+1
        return cadena
    def Editar_parametros_audio(self,root):
        
        newWindow = tk.Toplevel(root) 
        
        newWindow.title("Editar propiedades del audio") 
          
        newWindow.configure(bg='#000000')
        # Establecemos el tamaño de la raíz
        newWindow.geometry("500x327+680+0")
        #columnas y filas para un pack grid
        newWindow.columnconfigure(0, weight=1)
        newWindow.rowconfigure(0, weight=1)
        
        #Label que corresponde al texto
        titulo = tk.Label(newWindow,text="Editar propiedades del audio:",
                          font=("Segou UI",16),
                          bg='#000000',
                          fg="white")
        
        titulo.place(x=108,y=20)
        
        #Texto 
        texto1 = tk.Label(newWindow,text="Selecciona el archivo de audio:",
                          font=("Segou UI",14),
                          bg='#000000', 
                          fg="white")
        
        texto1.place(x=50,y=80)
        
        #Boton de selecciona un archivo
        button = tk.Button(newWindow, text='Open', 
                           font=("Segou UI",14),
                           bg='#3f3f3f',  
                           fg="white",
                           relief="solid",
                           command=self.seleccionar_archivo)
        
        button.place(x=382,y=77)

        #Texto 
        texto2 = tk.Label(newWindow,text="Guardar en:",
                          font=("Segou UI",14),
                          bg='#000000', 
                          fg="white")
        
        texto2.place(x=50,y=128)        
        
        #Boton de selecciona una ruta
        button2 = tk.Button(newWindow, text='Open', 
                           font=("Segou UI",14),
                           bg='#3f3f3f',  
                           fg="white",
                           relief="solid",
                           command=self.seleccionar_folder)
        
        button2.place(x=382,y=125)        
                                                 
        checkbutton1 = tk.Checkbutton(newWindow, text="Cambiar bit depth:",
                                     font=("Segou UI",14),
                                     bg="#000000",
                                     fg="white",
                                     selectcolor="#000000",
                                     variable=self.bit_depth, 
                                     onvalue=1, offvalue=0)
        checkbutton1.place(x=50,y=176)
        
        checkbutton2 = tk.Checkbutton(newWindow, text="Cambiar Frec. muestreo:",
                                     font=("Segou UI",14),
                                     bg="#000000",
                                     fg="white",
                                     selectcolor="#000000",
                                     variable=self.downsample, 
                                     onvalue=1, offvalue=0)
        
        checkbutton2.place(x=50,y=224)        
        #Button
        button3 = tk.Button(newWindow,text='Cambiar',
                            font=("Segou UI",14),
                            bg='#3f3f3f', 
                            fg="white", 
                            relief="solid",
                            command = self.Editar)
        button3.place(x=208,y=272)
        
        
    def seleccionar_folder(self, event=None):
        self.folder_selected = filedialog.askdirectory()
        
    def seleccionar_archivos(self,event=None):
        filename = filedialog.askopenfilenames(filetypes =[('Mp3 Files', '*.mp3')])
        self.archivos = list(filename)
        
    def seleccionar_archivo(self,event=None):
        filename = filedialog.askopenfilename(filetypes =[('WAV Files', '*.wav')])
        self.archivo = list(filename)        
        
    def obtener_nombre(self, ruta):
        nombre = ''
        i = len(ruta)-1
        while ruta[i]!= '/':
            nombre = ruta[i] + nombre
            i = i-1
        nombre = nombre[0:len(nombre)-3] + 'wav'    
        return nombre     
    
    def obtener_nombre2(self, ruta):
        nombre = ''
        i = len(ruta)-1
        while ruta[i]!= '/':
            nombre = ruta[i] +""+nombre
            i = i-1
        return nombre      
    
    def Editar(self):
        
        wav = ''.join(self.archivo)
        print(str(wav))
        
        wav_temp = 'temp/' + self.obtener_nombre2(wav)
        print(str(wav_temp))
        wav_save= self.folder_selected + '/' + self.obtener_nombre2(wav)
        print(str(wav_save))
        
        #copiar
        shutil.copy(wav, wav_temp)
        #wav = mp3[0:len(mp3)-3] + 'wav'
        
        if (self.bit_depth.get()): 
            #checkbutton seleccionado
            print('seleccionado')
            y, s = librosa.load(wav_temp, sr=16000)
            #librosa.output.write_wav(, y, s)
            soundfile.write(wav_temp, y, s) 
        if (self.downsample.get()): 
            #checkbutton seleccionado
            print('seleccionado')
            data, samplerate = soundfile.read(wav_temp)
            soundfile.write(wav_temp, data, samplerate, subtype='PCM_16') 

        shutil.copy(wav_temp, wav_save)
        
                           
    def Cambiar(self):
        print(self.archivos)
        for i in range(len(self.archivos)):
            mp3 = self.archivos[i]
            wav = self.folder_selected + '/' + self.obtener_nombre(mp3)
            #wav = mp3[0:len(mp3)-3] + 'wav'
            sound = AudioSegment.from_mp3(mp3)
            sound.export(wav, format="wav")
        
if __name__ == "__main__":
    app = tk.Tk()
    window = Application(app)
    app.mainloop()