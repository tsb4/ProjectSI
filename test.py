from PIL import Image, ImageTk
import tkinter as tk
import random
import time
import numpy as np
from copy import copy, deepcopy

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
        self.w, self.h = 20, 20
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        self.Objects = []
        self.ObjectsNum = 0
        self.SmallWall = False
        self.matrizBase = self.Matrix
        self.robot_x, self.robot_y, self.robot_dir = 0, 0, 0
        self.wall_x,self.wall_y = 0,0
        for j in range(3):
            if(j==2):
                self.Matrix[0][2] = 2
                self.Matrix[1][2] = 3
                self.Matrix[2][2] = 4
            else:
                for i in range(3):
                    self.Matrix[i][j]=5
        self.desviando = 0
        self.firstPart = True
        self.display_grid()
        #self.display_grid_second_part()
        #self.display_grid()
        #self.display_grid_second_part()
        self.numberOfOjects = 0

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

    def move_back_color(self,x,y,color):
        if(color != 1 and color != 6):
            button = tk.Button(self, text="", width=1, height=1)
            button._coords = x,y
            button.grid(row=x, column=y)
        elif(color == 1):
            button = tk.Button(self, text="", width=1, height=1,bg="black")
            button._coords = x,y
            button.grid(row=x, column=y)
        elif(color == 6):
            button = tk.Button(self, text="", width=1, height=1,bg="blue")
            button._coords = x,y
            button.grid(row=x, column=y)

    def move_forward(self):
        if(self.robot_dir==0): #UP
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior-1, y_anterior
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"up")
            self.display_image(x_atual,y_atual,180)
            for i in range(3):
                #y_reset = y_anterior+i
                cor = self.matrizBase[x_atual+3][y_atual+i]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                self.move_back_color(x_atual+3,y_atual+i,cor)

        elif(self.robot_dir==1): #RIGHT
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior, y_anterior+1
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"right")
            self.display_image(x_atual,y_atual,90)
            for i in range(3):
                y_reset = y_anterior+i
                cor = self.matrizBase[x_atual+i][y_atual-1]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                self.move_back_color(x_atual+i,y_atual-1,cor)
                #button = tk.Button(self, text="", width=1, height=1)
                #button._coords = 
                #button.grid(row=x_atual+i, column=y_atual-1)
        elif(self.robot_dir==2): #DOWN
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior+1, y_anterior
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"down")
            self.display_image(x_atual,y_atual,0)
            for i in range(3):
                y_reset = y_anterior+i
                cor = self.matrizBase[x_atual-1][y_atual+i]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor) 
                self.move_back_color(x_atual-1,y_atual+i,cor)
                #button = tk.Button(self, text="", width=1, height=1)
                #button._coords = x_atual-1,y_atual+i
                #button.grid(row=x_atual-1, column=y_atual+i)
        elif(self.robot_dir==3): #LEFT
            x_anterior, y_anterior = self.robot_x, self.robot_y
            x_atual, y_atual = x_anterior, y_anterior-1
            self.robot_x, self.robot_y = x_atual, y_atual
            self.create_matriz_image(x_atual,y_atual,"left")
            self.display_image(x_atual,y_atual,270)
            for i in range(3):
                y_reset = y_anterior+i
                cor = self.matrizBase[x_atual+i][y_atual+3]
                #self.Matrix[x+3][y_reset] = self.matrizBase[x_reset][y+3]
                #print("Valor da cor ",cor)
                self.move_back_color(x_atual+i,y_atual+3,cor)
                #button = tk.Button(self, text="", width=1, height=1)
                #button._coords = x_atual+i,y_atual+3
                #button.grid(row=x_atual+i, column=y_atual+3)
    
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
            self.display_image(x_atual,y_atual,180)
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
            self.display_image(x_atual,y_atual,180)
            self.robot_dir = 0
    
    def sensor_left(self):
        sensor_x, sensor_y = 0, 0
        if(self.robot_dir==0): #UP
            sensor_x=self.robot_x
            sensor_y = self.robot_y
        if(self.robot_dir==1): #RIGHT
            sensor_x = self.robot_x
            sensor_y = self.robot_y+2
        if(self.robot_dir==2): #DOWN
            sensor_x=self.robot_x+2
            sensor_y = self.robot_y+2
        if(self.robot_dir==3): #LEFT
            sensor_x=self.robot_x+2
            sensor_y = self.robot_y
        return self.matrizBase[sensor_x][sensor_y]
    
    def sensor_central(self):
        sensor_x, sensor_y = 0, 0
        if(self.robot_dir==0): #UP
            sensor_x=self.robot_x
            sensor_y = self.robot_y+1
        if(self.robot_dir==1): #RIGHT
            sensor_x = self.robot_x+1
            sensor_y = self.robot_y+2
        if(self.robot_dir==2): #DOWN
            sensor_x=self.robot_x+2
            sensor_y = self.robot_y+1
        if(self.robot_dir==3): #LEFT
            sensor_x=self.robot_x+1
            sensor_y = self.robot_y
        return self.matrizBase[sensor_x][sensor_y]

    def sensor_right(self):
        sensor_x, sensor_y = 0, 0
        if(self.robot_dir==0): #UP
            sensor_x=self.robot_x
            sensor_y = self.robot_y+2
        if(self.robot_dir==1): #RIGHT
            sensor_x = self.robot_x+2
            sensor_y = self.robot_y+2
        if(self.robot_dir==2): #DOWN
            sensor_x=self.robot_x+2
            sensor_y = self.robot_y
        if(self.robot_dir==3): #LEFT
            sensor_x=self.robot_x
            sensor_y = self.robot_y
        return self.matrizBase[sensor_x][sensor_y]
    
    def looking_forward_obs(self):
        self.wall_x, self.wall_y = 0, 0
        if(self.robot_dir==0): #UP
            self.wall_x=self.robot_x-1
            self.wall_y = self.robot_y+1
        if(self.robot_dir==1): #RIGHT
            self.wall_x = self.robot_x+1
            self.wall_y = self.robot_y+3
        if(self.robot_dir==2): #DOWN
            self.wall_x=self.robot_x+3
            self.wall_y = self.robot_y+1
        if(self.robot_dir==3): #LEFT
            self.wall_x=self.robot_x+1
            self.wall_y = self.robot_y-1
        return self.matrizBase[self.wall_x][self.wall_y]

    def looking_left_obs(self):
        self.wall_x, self.wall_y = 0, 0
        if(self.robot_dir==0): #UP
            self.wall_x=self.robot_x-1
            self.wall_y = self.robot_y
        if(self.robot_dir==1): #RIGHT
            self.wall_x = self.robot_x
            self.wall_y = self.robot_y+3
        if(self.robot_dir==2): #DOWN
            self.wall_x=self.robot_x+3
            self.wall_y = self.robot_y+2
        if(self.robot_dir==3): #LEFT
            self.wall_x=self.robot_x+2
            self.wall_y = self.robot_y-1
        return self.matrizBase[self.wall_x][self.wall_y]

    def looking_right_obs(self):
        self.wall_x, self.wall_y = 0, 0
        if(self.robot_dir==0): #UP
            self.wall_x=self.robot_x-1
            self.wall_y = self.robot_y+2
        if(self.robot_dir==1): #RIGHT
            self.wall_x = self.robot_x+2
            self.wall_y = self.robot_y+3
        if(self.robot_dir==2): #DOWN
            self.wall_x=self.robot_x+3
            self.wall_y = self.robot_y
        if(self.robot_dir==3): #LEFT
            self.wall_x=self.robot_x
            self.wall_y = self.robot_y-1
        return self.matrizBase[self.wall_x][self.wall_y]
                
                   





    #Função que inicializa o fluxo de do robo na segunda etapa
    #Por enquanto não foram criadas as regras de produção, apenas um fluxo de entendimento
    #Para movimrntar, aperte a letra+ enter
    #CIMA - w
    #Direira - d
    #Edsquerda - a
    #Baixo - s


    def start_first_part(self):
        if(self.firstPart):
           # r = 0
            self.after(1000, self.start_first_part)
            #print(self.sensor_central(), self.sensor_left(), self.sensor_right())
            #print(self.looking_forward_obs())
            print(np.array(self.matrizBase))
            print(np.array(self.Matrix))
            if(self.sensor_central()==7 or self.sensor_left()==7 or self.sensor_right()==7):
                print("CHEGOU!!!!!")
                #r=0
                self.labelRegra.configure(text='Regra 1: O linha de chegada!')# = tk.Label(self, , borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.display_grid_second_part()
            elif((self.looking_forward_obs()==6 or self.looking_left_obs()==6 or self.looking_right_obs()==6) and self.desviando==2):
                #r=1
                self.labelRegra.configure(text='Regra 2: Contornando o comprimento do obstaculo...')#tk.Label(self, text='Regra 2: Contornando o comprimento do obstaculo...', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                print("contornando")
                self.turn_right()
                self.move_forward()
                self.turn_left()
                self.desviando=2
            elif((self.looking_forward_obs()==6 or self.looking_left_obs()==6 or self.looking_right_obs()==6)):
                #r=2
                self.labelRegra.configure(text='Regra 3: Contornando a largura do obstaculo...')#text='Regra 3: Contornando a largura do obstaculo...', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                print("obstacle")
                self.turn_right()
                self.move_forward()
                self.turn_left()
                self.desviando = 1
            elif(self.sensor_central()==1 and self.sensor_left()==0 and self.sensor_right()==0):
                #r=3
                self.labelRegra.configure(text='Regra 4: Sensores laterais livres, seguir em frente!')# text='Regra 4: Sensores laterais livres, seguir em frente!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
            elif(self.sensor_central()==1 and self.sensor_left()==1 and self.sensor_right()==0):
                #r=4
                self.labelRegra.configure(text='Regra 5: Sinal captado no sensor esquerdo, virar a esquerda!')#='Regra 5: Sinal captado no sensor esquerdo, virar a esquerda!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
                self.turn_left()
            elif(self.sensor_central()==1 and self.sensor_left()==0 and self.sensor_right()==1):
               #r=5
                self.labelRegra.configure(text='Regra 6: Sinal captado no sensor direito, virar a direita!')#t='Regra 6: Sinal captado no sensor direito, virar a direita!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
                self.turn_right()
            elif((self.sensor_central()==1 and self.sensor_left()==1 and self.sensor_right()==1) and self.desviando==2):
                #r=6
                self.labelRegra.configure(text='Regra 7: Linha reencontrada! Centralizando...')#='Regra 7: Linha reencontrada! Centralizando...', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
                self.turn_right()
                self.desviando=0
            elif(self.sensor_central()==1 and self.sensor_left()==1 and self.sensor_right()==1):
                #r=7
                self.labelRegra.configure(text='Regra 8: Encruzilhada encontrada, seguir em frente!')#'Regra 8: Encruzilhada encontrada, seguir em frente!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
            elif(self.desviando==1):
                #r=8
                self.labelRegra.configure(text='Regra 9: Checagem de largura completa. Hora de checar o comprimento!')#text='Regra 9: Checagem de largura completa. Hora de checar o comprimento!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.desviando=2
                self.move_forward()
                self.turn_left()
            else:
                #r=9
                self.labelRegra.configure(text='Regra 10: Na duvida, siga em frente!')#text='Regra 10: Na duvida, siga em frente!', borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
                self.move_forward()
            
            #labelRegra = tk.Label(self, text='Regra %s'%(r), borderwidth=1 ).grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
            self.labelRegra.grid(row=int(self.h+2),column=int(self.w/2), columnspan=20)
          

            #if(com=='f'):
            #    self.move_forward()
            #elif(com=='x'):
            #    self.turn_right()
            #elif(com=='z'):
            #    self.turn_left()
            #    
            #else:
            #   pass

    #def looking_right_obs(self):
    #    wall_x, wall_y = 0, 0
    #    if(self.robot_dir==0): #UP
    #        wall_x=self.robot_x-1
    #        wall_y = self.robot_y+2
    #    if(self.robot_dir==1): #RIGHT
    #        wall_x = self.robot_x+2
    #        wall_y = self.robot_y+3
    #    if(self.robot_dir==2): #DOWN
    #        wall_x=self.robot_x+3
    #        wall_y = self.robot_y
    #    if(self.robot_dir==3): #LEFT
    #        wall_x=self.robot_x
    #        wall_y = self.robot_y-1
    #    return self.matrizBase[wall_x][wall_y]
                

    #def desvia_parede(self):
    #    if(self.robot_dir == 0): #UP
    #        self.robot_dir = 1
    #
    #    if(self.robot_dir == 1): #RIGHT
    #        self.turn_right()
    #        for i in range(3):
    #            self.after(1000)
    #            if(self.looking_left() == self.looking_right() == self.looking_forward() == 6):
    #                self.turn_right()
    #                self.turn_right()
    #            else:
    #                self.move_forward()
    #
    #    if(self.robot_dir == 2): #DOWN
    #        self.robot_dir = 2
    #
    #    if(self.robot_dir == 3): #LEFT
    #        self.robot_dir = 0
    #    return
    #
    def on_start_button_first_part(self, event):
        self.matrizBase = list(map(list, self.Matrix))
        self.labelRegra=tk.Label(self, text='', borderwidth=1)
        self.start_first_part()

    def move_gmaps(self):
        self.Objects
        x = self.robot_x +1
        y = self.robot_y +1
        dist = []
        for i in self.Objects:
            dist_x = i[0] - x
            dist_y = i[1] - y
            dist.append((dist_x,dist_y))
        now = dist[0]
        print(now)
        if(self.SmallWall):
            p_x = 0
            p_y = 0
            if(now[0] < 0):
                if(self.h > (self.robot_x + 4)):
                    p_x = self.robot_x + 3
                    p_y = self.robot_y + now[1]
                elif(self.robot_x > 4):
                    p_x = self.robot_x - 3
                    p_y = self.robot_y + now[1]
                else:
                    p_x = int(self.x*random.random())
                    p_y = int(self.y*random.random())
            else:
                if(self.w > (self.robot_y + 4)):
                    p_y = self.robot_y + 3
                    p_x = self.robot_x + now[0] + 3
                elif(self.robot_y > 4):
                    p_y = self.robot_y - 3
                    p_x = self.robot_x + now[0] + 3
                else:
                    p_x = int(self.x*random.random())
                    p_y = int(self.y*random.random())
            if(self.ObjectsNum > len(self.Objects) + 1):
                self.Objects = self.Objects[2:]
            self.Objects = [(p_x,p_y)]+self.Objects
            print(self.Objects)

        if(now[1] == 0):
            if(now[0] == 0):
                self.Objects = self.Objects[1:]
            elif(now[0] < 0):
                self.labelRegra.configure(text='Regra 4: Objeto em cima. Suba!')
                while(self.robot_dir != 0):
                    self.turn_left()
            else:
                self.labelRegra.configure(text='Regra 5: Objeto embaixo. Desça!')
                while(self.robot_dir != 2):
                    self.turn_left()
        elif(now[1] > 0):
            self.labelRegra.configure(text='Regra 6: Objeto á direita.Vá a direita!')
            while(self.robot_dir != 1):
                self.turn_left()
        else:
            self.labelRegra.configure(text='Regra 7: Objeto á esquerda.Vá a esquerda')
            while(self.robot_dir != 3):
                self.turn_left()
        return
        

    #Função que inicia a parte 2
    def start_second_part(self):
        if(not self.firstPart):
            self.after(500, self.start_second_part)
            self.move_gmaps()
            if(self.looking_left_obs() == 6 and self.looking_right_obs() == 6 and self.looking_forward_obs() == 6):
                self.labelRegra.configure(text='Regra 1: Parede delimitadora da arena. Gire aleatoriamente para um lado!')
                print("PAREDE")
                choice = random.random()
                if(choice<=0.5):
                    self.turn_right()
                else:
                    self.turn_left()
            elif(self.looking_left_obs() == 6 or self.looking_right_obs() == 6 or self.looking_forward_obs() == 6):
                self.labelRegra.configure(text='Regra 2: Pequena Parede. Saia Aleatoriamente.')
                self.SmallWall = True
            elif(self.looking_left_obs() == 7):
                self.labelRegra.configure(text='Regra 3: Objeto a Frente. Siga em frente para coletar!')
                #self.turn_left()
                #self.move_forward()
                #self.turn_right()
                self.matrizBase[self.wall_x][self.wall_y] = 0
            elif(self.looking_right_obs() == 7):
                self.labelRegra.configure(text='Regra 3: Objeto a Frente. Siga em frente para coletar!')
                #self.turn_right()
                #self.move_forward()
                #self.turn_left()
                self.matrizBase[self.wall_x][self.wall_y] = 0
            elif(self.looking_forward_obs() == 7):
                self.labelRegra.configure(text='Regra 3: Objeto a Frente. Siga em frente para coletar!')
                #self.move_forward()
                #self.numberOfOjects += 1
                self.matrizBase[self.wall_x][self.wall_y] = 0
                print("OBJETO")
                self.ObjectsNum = self.ObjectsNum - 1
            else:
                self.SmallWall = False
                self.move_forward()
            


    def on_start_button_second_part(self, event):
        self.matrizBase = list(map(list, self.Matrix))
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
        #print("caaaaa")
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        x_ini ,y_ini = 1,1
        self.robot_x, self.robot_y, self.robot_dir = x_ini, y_ini, 1
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
        buttonStart.grid(row=int(self.h)+1, column=int(self.w/2)-5, columnspan=10)
        #buttonStart.place(x=1200, y=520)
        self.create_matriz_image(x_ini,y_ini,"right")
        self.display_image(x_ini,y_ini,90)
        #self.matrizBase = self.Matrix.copy()

    #Esta função inicia a segunda parte de identificações que o robo irá fazer
    #Nesta parte não tem linhas, apenas as paredes (em azul com valor de 6), e os objetos a serem coletados (em bege no valor de 7)
    #O robo começa na posição 1,1 na matriz geral, e sua matriz interna possui os valores de 2,3,4 para os sensores (esta parte esta em analise, já que na segunda etapa
    #   talvez nao precisemos desses valores e sim falar que existem apenas dois sensores, um ultrassonico e outro de cor para identificar os objetos), e o restante do corpo
    #   do robo possui 5 como valor, e todos em vermelho
    def display_grid_second_part(self):
        self.firstPart = False
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        x_ini ,y_ini = 1,1
        self.robot_x, self.robot_y, self.robot_dir = x_ini, y_ini, 1
        obstacles = []
        for i in range(2):
            x=random.randint(4, self.h-5)
            y=random.randint(4, self.w-5)
            obstacles.append((x,y)) 
            self.Matrix[x][y] = 6

        objects = []
        for i in range(5):
            x=random.randint(5, self.h-3)
            y=random.randint(5, self.w-3)
            objects.append((x,y)) 
            self.Matrix[x][y] = 7
        self.Objects = sorted(objects)
        self.ObjectsNum = len(self.Objects)
        print(self.Objects)

        for x in range(self.h):
            for y in range(self.w):
                button = tk.Button(self, text="", width=1, height=1)
                if(x==0 or y==0 or x==self.h-1 or y ==self.w-1):
                    self.Matrix[x][y] = 6
                    button = tk.Button(self, text="", width=1, height=1, bg="blue")
                elif(self.Matrix[x][y]==6):
                    button = tk.Button(self, text="", width=1, height=1, bg="blue")
                #elif(self.Matrix[x][y]==4 or self.Matrix[x][y]==3 or self.Matrix[x][y]==2 or self.Matrix[x][y]==5):
                #    button = tk.Button(self, text="", width=1, height=1, bg="red")
                elif(self.Matrix[x][y]==7):
                    button = tk.Button(self, text="", width=1, height=1, bg="peru")   
                button._coords = x, y
                button.grid(row=x, column=y)
        
        self.create_matriz_image(x_ini,y_ini,"right")
        self.display_image(x_ini,y_ini,90)
        #self.matrizBase = self.Matrix
        
        #self.on_start_button_second_part(x_ini,y_ini)
        buttonStart = tk.Button(self, text="START", width=10, height=1)
        buttonStart.bind("<Button-1>", self.on_start_button_second_part)
        buttonStart.grid(row=int(self.h)+1, column=int(self.w/2)-5, columnspan=10)
        #buttonStart.place(x=1200, y=520)

if __name__ == '__main__':
    App().mainloop()
