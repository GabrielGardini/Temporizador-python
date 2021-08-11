from tkinter import *
from tkinter import ttk
import pygame
from datetime import *


timer= Tk()
timer.title("Temporizador")
timer.geometry("300x300")
timer.maxsize(300,300)
pygame.mixer.init()

class Timer:
    def __init__(self,main):
        self.timer = ['00:00:00']
        self.nb=ttk.Notebook(main)
        self.nb.place(x=0,y=0,width=300,height=300)

        self.tela1=Frame(self.nb)
        self.nb.add(self.tela1,text="Temporizador")
        self.tela1.configure(background="#F1FEC6")

        self.tela2=Frame(self.nb)
        self.nb.add(self.tela2,text="Créditos")
        self.tela2.configure(background="#F1FEC6")

#######################################################################################################################################
#############################################       CONFIGURAÇÃO DA TELA1        #####################################################
#######################################################################################################################################       
        self.tempo=Label(self.tela1,text=self.timer[0],font=("Sylfaen",18),bg="#F1FEC6",fg="black")
        self.tempo.place(x=75,y=20,width=150,height=50)

        self.recebe_horas=Entry(self.tela1,text="",font=("Sylfaen", 15),justify=RIGHT) # horas
        self.recebe_horas.place(x=105,y=90,width=40,height=30)

        self.dois_pontos=Label(self.tela1,text=":",font=("Sylfaen", 15),bg="#F1FEC6")
        self.dois_pontos.place(x=145,y=90,width=10,height=30)

        self.recebe_minutos2=Entry(self.tela1,font=("Sylfaen", 15)) # minutos
        self.recebe_minutos2.place(x=155,y=90,width=40,height=30)


        self.start_btn=Button(self.tela1,text="Iniciar",bg="yellow",font=("Sylfaen", 13))
        self.start_btn.place(x=90,y=150,width=120,height=30)
        self.start_btn.bind('<Button-1>', self.salvar_tempo)

        self.stop_btn=Button(self.tela1, text="Parar",font=("Sylfaen",13 ,"bold"),bg="red",command=self.parar)
        self.stop_btn.place(x=125,y=230,width=50,height=30)

        self.stop= False

#######################################################################################################################################
#############################################       CONFIGURAÇÃO DA TELA2         #####################################################
#######################################################################################################################################
        self.info=Label(self.tela2,text="Obrigado por utilizar! \n \n Criado por Gabriel Gardini \n \n @ggardini1",font=("Sylfaen", 13),bg="#F1FEC6")
        self.info.place(x=50,y=50,width=200,height=150)

        
    def salvar_tempo(self, event):
        hora = self.recebe_horas.get()
        minuto = self.recebe_minutos2.get()

        if hora == '':
            hora = 0
        else:
            hora = int(hora)
            
        if minuto == '':
            minuto = 0
        else:
            minuto = int(minuto)

        time_string = f'{hora:02d}:{minuto:02d}:00'

        self.rodar_tempo(time_string)

    def rodar_tempo(self, time_string):
        self.tempo.config(text=time_string)
        my_time = datetime.strptime(time_string, '%H:%M:%S')
        total_time = my_time.hour*3600 + my_time.minute*60 + my_time.second - 1
        if total_time >= 0 and self.stop==False:
            hour, minute = divmod(total_time, 3600)
            minute2, second = divmod(minute, 60)
            new_time_string = f'{hour:02d}:{minute2:02d}:{second:02d}'
            self.tempo.after(1000, lambda t = new_time_string : self.rodar_tempo(t))
        elif total_time>0 and self.stop==True:
                self.stop=False
                self.tempo["text"]="00:00:00"
        elif self.tempo["text"]=="00:00:00":
                pygame.mixer.music.load("sons\House.mp3")
                pygame.mixer.music.play()
            
    def parar(self):
        self.stop=True
        pygame.mixer.music.stop()
        


temporizador = Timer(timer)
timer.mainloop()




