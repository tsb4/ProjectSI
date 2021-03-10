
from PIL import Image, ImageTk
import tkinter as tk
import random
import time
import numpy

##Convencoes Importantes
##Matriz
#1 - Linha
#2 - Sensor Esquerdo
#3 - Sensor Central
#4 - Sensor Direito
#5 - Corpo do robot
#6 - Muro
#7 - Objetos coletados/Objetivo
#
##Instruções para fazer caminho
#1 click Botão Esquerdo - Linha
#1 Click Botao Direito - Muro
#2 clicks botao esquerdo - Objetivo
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.w, self.h = 30, 30
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        self.matrizBase = self.Matrix
        for j in range(3):
            if(j==2):
                self.Matrix[0][2] = 2
                self.Matrix[1][2] = 3
                self.Matrix[2][2] = 4
            else:
                for i in range(3):
                    self.Matrix[i][j]=5
        #self.display_grid()
        self.display_grid_second_part()

    def on_button_1_click(self, event):
        print('on_button_1_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 1
        button = tk.Button(self, text="", width=1, height=1, bg="black")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-1>", self.on_button_3_click)
        print(self.Matrix)

    
    def on_button_2_click(self, event):
        print('on_button_2_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 6
        button = tk.Button(self, text="", width=1, height=1, bg="blue")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-3>", self.on_button_2_click)
        print(self.Matrix)
    
    def on_button_3_click(self, event):
        print('on_button_3_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]=7
        button = tk.Button(self, text="", width=1, height=1, bg="peru")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-1>", self.on_button_3_click)
        print(self.Matrix)

    def on_start_button(self):
        narra = numpy.array(self.Matrix)
        print(narra)
        x,y = 1,20
        print("STARTING")
        button = tk.Button(self, text="G", width=1, height=1, bg="green")
        button._coords = x,y
        button.grid(row=x, column=y)
        print(self.Matrix)
        
        while(input("Entrada") != 0):
            xm1, ym1 = x, y
            x,y = x, y-1
            self.display_image(x,y)
            
            if(xm1 == x and ym1 > y):
                for i in range(3):
                    x_reset = xm1+i
                    cor = self.matrizBase[x_reset][ym1+3]
                    print("Valor da cor ",cor) 
                    if(cor == 0):
                        button = tk.Button(self, text="", width=1, height=1)
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
                    elif(cor in (2,3,4,5)):
                        button = tk.Button(self, text="", width=1, height=1)
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
                    elif(cor == 6):
                        button = tk.Button(self, text="", width=1, height=1,bg="blue")
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
            elif(xm1 == x and ym1 < y):
                for i in range(3):
                    x_reset = xm1+i
                    cor = self.matrizBase[x_reset][ym1]
                    print("Valor da cor ",cor) 
                    if(cor == 0):
                        button = tk.Button(self, text="", width=1, height=1)
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
                    elif(cor in (2,3,4,5)):
                        button = tk.Button(self, text="", width=1, height=1)
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
                    elif(cor == 6):
                        button = tk.Button(self, text="", width=1, height=1,bg="blue")
                        button._coords = x_reset,ym1
                        button.grid(row=x_reset, column=ym1)
        

    def display_image(self, x, y):
        load = Image.open("robot.jpg")
        load = load.rotate(90)
        load = load.resize((100,70))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=x, column=y, rowspan=3, columnspan=3)
    


    
    def display_grid(self):
        for x in range(self.h):
            for y in range(self.w):
                if(self.Matrix[x][y]==2 or self.Matrix[x][y]==3 or self.Matrix[x][y]==4 or self.Matrix[x][y]==5):
                    button = tk.Button(self, text="", width=1, height=1, bg="red")
                else:
                    button = tk.Button(self, text="", width=1, height=1)

                button._coords = x, y
                button.grid(row=x, column=y)
                button.bind("<Button-1>", self.on_button_1_click)
                button.bind("<Button-3>", self.on_button_2_click)
        buttonStart = tk.Button(self, text="START", width=10, height=1)
        buttonStart.bind("<Button-1>", self.on_start_button)
        #buttonStart.grid(row=int(self.h/2), column=int(self.w)+1, columnspan=10)
        buttonStart.place(x=1200, y=520)
        self.display_image(0, 0)
      

    
    def display_grid_second_part(self):
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]

        x ,y = 1,20
        
        for j in range(y,y+3):
            if(j==y+2):
                self.Matrix[x][y+2] = 2
                self.Matrix[x+1][y+2] = 3
                self.Matrix[x+2][y+2] = 4
            else:
                for i in range(x,x+3):
                    self.Matrix[x+i][y+j]=5
        self.display_image(x,y)

        objects = []
        for i in range(3):
            x=random.randint(5, self.h-3)
            y=random.randint(5, self.w-3)
            objects.append((x,y)) 
            self.Matrix[x][y] = 7
        

        for x in range(self.h):
            for y in range(self.w):
                button = tk.Button(self, text="", width=1, height=1)
                if(x==0 or y==0 or x==self.h-1 or y ==self.w-1):
                    self.Matrix[x][y] = 6
                    button = tk.Button(self, text="", width=1, height=1, bg="blue")
                elif(self.Matrix[x][y]==4 or self.Matrix[x][y]==3 or self.Matrix[x][y]==2 or self.Matrix[x][y]==5):
                    button = tk.Button(self, text="", width=1, height=1, bg="red")
                elif(self.Matrix[x][y]==7):
                    button = tk.Button(self, text="", width=1, height=1, bg="peru")   
                button._coords = x, y
                button.grid(row=x, column=y)
                
        self.matrizBase = self.Matrix
        self.on_start_button()

if __name__ == '__main__':
    App().mainloop()
