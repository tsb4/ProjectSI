
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
        self.robot_x, self.robot_y, self.robot_dir = 0, 0, 0
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

    #def move_left(self):
    #    x_anterior, y_anterior = self.robot_x, self.robot_y
    #    x_atual, y_atual = x_anterior, y_anterior-1
    #    self.robot_x, self.robot_y = x_atual, y_atual
    #    self.create_matriz_image(x_atual,y_atual,"left")
    #    self.display_image(x_atual,y_atual,270)
    #    for i in range(3):
    #        x_reset = x_anterior+i
    #        cor = self.matrizBase[x_reset][y_atual+3]
    #        #self.Matrix[x_reset][y+3] = self.matrizBase[x_reset][y+3] VERIFICAR ESSE TRECHO DE CODIGO PARA QUE A MATRIX SENDO UTILIZADA FIQUE COM ZERO APOS O ROBO ANDAR
    #        print("Valor da cor ",cor) 
    #        if(cor in (0,2,3,4,5)):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_reset,y_atual+3
    #            button.grid(row=x_reset, column=y_atual+3)
    #        elif(cor == 7):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_reset,y_atual+3
    #            button.grid(row=x_reset, column=y_atual+3)
    #
    #def move_right(self):
    #    x_anterior, y_anterior = self.robot_x, self.robot_y
    #    x_atual, y_atual = x_anterior, y_anterior+1
    #    self.robot_x, self.robot_y = x_atual, y_atual
    #    self.create_matriz_image(x_atual,y_atual,"right")
    #    self.display_image(x_atual,y_atual,90)
    #    for i in range(3):
    #        x_reset = x_anterior+i
    #        cor = self.matrizBase[x_reset][y_anterior]
    #        #self.Matrix[x_reset][y_anterior] = self.matrizBase[x_reset][y_anterior]
    #        print("Valor da cor ",cor) 
    #        if(cor in (0,2,3,4,5)):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_reset,y_anterior
    #            button.grid(row=x_reset, column=y_anterior)
    #        elif(cor == 7):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_reset,y_anterior
    #            button.grid(row=x_reset, column=y_anterior)
    #
    #def move_up(self):
    #    x_anterior, y_anterior = self.robot_x, self.robot_y
    #    x_atual, y_atual = x_anterior-1, y_anterior
    #    self.robot_x, self.robot_y = x_atual, y_atual
    #    self.create_matriz_image(x_atual,y_atual,"up")
    #    self.display_image(x_atual,y_atual,180)
    #    for i in range(3):
    #        y_reset = y_anterior+i
    #        cor = self.matrizBase[x_atual+3][y_reset]
    #        #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
    #        print("Valor da cor ",cor) 
    #        if(cor in (0,2,3,4,5)):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_atual+3,y_reset
    #            button.grid(row=x_atual+3, column=y_reset)
    #        elif(cor == 7):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_atual+3,y_reset
    #            button.grid(row=x_atual+3, column=y_reset)
    #
    #def move_down(self):
    #    x_anterior, y_anterior = self.robot_x, self.robot_y
    #    x_atual, y_atual = x_anterior+1, y_anterior
    #    self.robot_x, self.robot_y = x_atual, y_atual
    #    self.create_matriz_image(x_atual,y_atual,"down")
    #    self.display_image(x_atual,y_atual,0)
    #    for i in range(3):
    #        y_reset = y_anterior+i
    #        cor = self.matrizBase[x_anterior][y_reset]
    #        #self.Matrix[x_anterior][y_reset] = self.matrizBase[x_reset][y+3]
    #        print("Valor da cor ",cor) 
    #        if(cor in (0,2,3,4,5)):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_anterior,y_reset
    #            button.grid(row=x_anterior, column=y_reset)
    #        elif(cor == 7):
    #            button = tk.Button(self, text="", width=1, height=1)
    #            button._coords = x_anterior,y_reset
    #            button.grid(row=x_anterior, column=y_reset)
    #
    def move_forward(self):
        if(self.robot_dir==0): #UP
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior-1, y_anterior
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"up")
            self.display_image(x_atual,y_atual,180)
            for i in range(3):
                #y_reset = y_anterior+i
                #cor = self.matrizBase[x_atual+3][y_reset]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                button = tk.Button(self, text="", width=1, height=1)
                button._coords = x_atual+3,y_atual+i
                button.grid(row=x_atual+3, column=y_atual+i)
        elif(self.robot_dir==1): #RIGHT
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior, y_anterior+1
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"right")
            self.display_image(x_atual,y_atual,90)
            for i in range(3):
                #y_reset = y_anterior+i
                #cor = self.matrizBase[x_atual+3][y_reset]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                button = tk.Button(self, text="", width=1, height=1)
                button._coords = x_atual+i,y_atual-1
                button.grid(row=x_atual+i, column=y_atual-1)
        elif(self.robot_dir==2): #DOWN
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior+1, y_anterior
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"down")
            self.display_image(x_atual,y_atual,0)
            for i in range(3):
                #y_reset = y_anterior+i
                #cor = self.matrizBase[x_atual+3][y_reset]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                button = tk.Button(self, text="", width=1, height=1)
                button._coords = x_atual-1,y_atual+i
                button.grid(row=x_atual-1, column=y_atual+i)
        elif(self.robot_dir==3): #LEFT
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior, y_anterior-1
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"left")
            self.display_image(x_atual,y_atual,270)
            for i in range(3):
                #y_reset = y_anterior+i
                #cor = self.matrizBase[x_atual+3][y_reset]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                button = tk.Button(self, text="", width=1, height=1)
                button._coords = x_atual+i,y_atual+3
                button.grid(row=x_atual+i, column=y_atual+3)
    
    def turn_right(self):
        x_atual, y_atual = self.robot_x, self.robot_y
        if(self.robot_dir==0):
            self.create_matriz_image(x_atual,y_atual,"right")
            self.display_image(x_atual,y_atual,90)
            self.robot_dir = 1
        elif(self.robot_dir==1):
            self.create_matriz_image(x_atual,y_atual,"down")
            self.display_image(x_atual,y_atual,0)
            self.robot_dir = 2
        elif(self.robot_dir==2):
            self.create_matriz_image(x_atual,y_atual,"left")
            self.display_image(x_atual,y_atual,270)
            self.robot_dir = 3
        elif(self.robot_dir==3):
            self.create_matriz_image(x_atual,y_atual,"up")
            self.display_image(x_atual,y_atual,1800)
            self.robot_dir = 0
    
    def turn_left(self):
        x_atual, y_atual = self.robot_x, self.robot_y
        if(self.robot_dir==2):
            self.create_matriz_image(x_atual,y_atual,"right")
            self.display_image(x_atual,y_atual,90)
            self.robot_dir = 1
        elif(self.robot_dir==3):
            self.create_matriz_image(x_atual,y_atual,"down")
            self.display_image(x_atual,y_atual,0)
            self.robot_dir = 2
        elif(self.robot_dir==0):
            self.create_matriz_image(x_atual,y_atual,"left")
            self.display_image(x_atual,y_atual,270)
            self.robot_dir = 3
        elif(self.robot_dir==1):
            self.create_matriz_image(x_atual,y_atual,"up")
            self.display_image(x_atual,y_atual,1800)
            self.robot_dir = 0



                
                   





    #Função que inicializa o fluxo de do robo na segunda etapa
    #Por enquanto não foram criadas as regras de produção, apenas um fluxo de entendimento
    #Para movimrntar, aperte a letra+ enter
    #CIMA - w
    #Direira - d
    #Edsquerda - a
    #Baixo - s


    def start_first_part(self):
        if(True):
            self.after(1000, self.start_first_part)
          
            com ='f'

            if(com=='f'):
                self.move_forward()
            elif(com=='x'):
                self.turn_right()
            elif(com=='z'):
                self.turn_left()
                
            else:
               pass

    def looking_forward(self):
        if(self.robot_dir == 0): #UP
            return self.Matrix[self.robot_x-3][self.robot_y+1]
        
        if(self.robot_dir == 1): #RIGHT
            print(self.Matrix[self.robot_x+3][self.robot_y+1])
            return self.Matrix[self.robot_x+3][self.robot_y+1]
    
        if(self.robot_dir == 2): #DOWN
            return self.Matrix[self.robot_x+1][self.robot_y+3]
        
        if(self.robot_dir == 3): #LEFT
            return self.Matrix[self.robot_x+3][self.robot_y+1]
    
    def looking_right(self):
        pass

    def looking_left(self):
        pass

    def on_start_button_first_part(self, event):
        self.start_first_part()

    def start_second_part(self):
        while(True):
            #self.after(1000, self.start_second_part)
            
            if(self.looking_forward() == 7):
                print("OBJETO")
            if(self.looking_forward() == 6):
                print("PAREDE")


            com = input("ENTRADA") 
            if(com=='f'):
                self.move_forward()
            elif(com=='x'):
                self.turn_right()
            elif(com=='z'):
                self.turn_left()
                
            else:
               pass

    def on_start_button_second_part(self, event):
        self.start_second_part()

        
                

    #Função que coloca a cor desejada no indice da matriz (x,y) escolhidos
    def create_color_matriz(self, x, y, color):        
        button = tk.Button(self, text="", width=1, height=1,bg=color)
        button._coords = x,y
        button.grid(row=x, column=y)

    #Esta função funciona para a criação da matriz do robo das diferentes direções que ele irá operar
    #Dentro desta função, ela já chama a função de criar as cores em vermelho do robo
    def create_matriz_image(self, x, y, dir):

        if(dir == "up"):
            print("UP\n")
            self.Matrix[x][y] = 2
            self.create_color_matriz(x,y,"red") 
            self.Matrix[x][y+1] = 3
            self.create_color_matriz(x,y+1,"red") 
            self.Matrix[x][y+2] = 4
            self.create_color_matriz(x,y+2,"red") 
            
            for j in range(3):
                for i in range(1,3):
                    self.Matrix[x+i][y+j] = 5
                    self.create_color_matriz(x+i,y+j,"red") 
        
        elif(dir == "down"):
            print("DOWN\n")
            self.Matrix[x+2][y] = 4
            self.create_color_matriz(x+2,y,"red") 
            self.Matrix[x+2][y+1] = 3
            self.create_color_matriz(x+2,y+1,"red") 
            self.Matrix[x+2][y+2] = 2
            self.create_color_matriz(x+2,y+2,"red") 
            
            for j in range(3):
                for i in range(0,2):
                    self.Matrix[x+i][y+j] = 5
                    self.create_color_matriz(x+i,y+j,"red") 
        
        elif(dir == "right"):
            print("RIGHT\n")
            self.Matrix[x][y+2] = 2
            self.create_color_matriz(x,y+2,"red") 
            self.Matrix[x+1][y+2] = 3
            self.create_color_matriz(x+1,y+2,"red") 
            self.Matrix[x+2][y+2] = 4
            self.create_color_matriz(x+2,y+2,"red") 

            for j in range(0,2):
                for i in range(3):
                    self.Matrix[x+i][y+j] = 5
                    self.create_color_matriz(x+i,y+j,"red")             
        
        elif(dir == "left"):
            print("LEFT\n")
            self.Matrix[x][y] = 4
            self.create_color_matriz(x,y,"red") 
            self.Matrix[x+1][y] = 3
            self.create_color_matriz(x+1,y,"red") 
            self.Matrix[x+2][y] = 2
            self.create_color_matriz(x+2,y,"red") 
            
            for j in range(1,3):
                for i in range(3):
                    self.Matrix[x+i][y+j] = 5
                    self.create_color_matriz(x+i,y+j,"red")
    

    #O parametro GRAU define como a imagem vai aparecer na matriz (pra baixo, pra cima, pra direita ou esquerda)
    def display_image(self, x, y, grau):
        load = Image.open("robot.jpg")
        load = load.rotate(grau)
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
        buttonStart.bind("<Button-1>", self.on_start_button_first_part)
        #buttonStart.grid(row=int(self.h/2), column=int(self.w)+1, columnspan=10)
        buttonStart.place(x=1200, y=520)
        self.display_image(0, 0,90)
      

    #Esta função inicia a segunda parte de identificações que o robo irá fazer
    #Nesta parte não tem linhas, apenas as paredes (em azul com valor de 6), e os objetos a serem coletados (em bege no valor de 7)
    #O robo começa na posição 1,1 na matriz geral, e sua matriz interna possui os valores de 2,3,4 para os sensores (esta parte esta em analise, já que na segunda etapa
    #   talvez nao precisemos desses valores e sim falar que existem apenas dois sensores, um ultrassonico e outro de cor para identificar os objetos), e o restante do corpo
    #   do robo possui 5 como valor, e todos em vermelho
    def display_grid_second_part(self):
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        x_ini ,y_ini = 1,1
        self.robot_x, self.robot_y, self.robot_dir = x_ini, y_ini, 1

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
                #elif(self.Matrix[x][y]==4 or self.Matrix[x][y]==3 or self.Matrix[x][y]==2 or self.Matrix[x][y]==5):
                #    button = tk.Button(self, text="", width=1, height=1, bg="red")
                elif(self.Matrix[x][y]==7):
                    button = tk.Button(self, text="", width=1, height=1, bg="peru")   
                button._coords = x, y
                button.grid(row=x, column=y)
        
        self.create_matriz_image(x_ini,y_ini,"right")
        self.display_image(x_ini,y_ini,90)
        self.matrizBase = self.Matrix
        
        #self.on_start_button_second_part(x_ini,y_ini)
        buttonStart = tk.Button(self, text="START", width=10, height=1)
        buttonStart.bind("<Button-1>", self.on_start_button_second_part)
        buttonStart.grid(row=int(self.h)+1, column=int(self.w/2)-5, columnspan=10)
        #buttonStart.place(x=1200, y=520)

if __name__ == '__main__':
    App().mainloop()
