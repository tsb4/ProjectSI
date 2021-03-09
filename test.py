

import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.w, self.h = 30, 30
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        self.Matrix[0][0] = 2
        self.Matrix[1][0] = 3
        self.Matrix[2][0] = 4 
        #self.butto
        #self.display_grid()
        self.display_grid_second_part()

    def on_button_1_click(self, event):
        print('on_button_1_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 1
        #event.widget.color_change = "black"
        #self.display_grid()
        button = tk.Button(self, text="", width=1, height=1, bg="black")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-1>", self.on_button_3_click)
        print(self.Matrix)

    
    def on_button_2_click(self, event):
        print('on_button_2_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 5
        #event.widget.color_change = "black"
        #self.display_grid()
        button = tk.Button(self, text="", width=1, height=1, bg="blue")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-3>", self.on_button_2_click)
        print(self.Matrix)
    
    def on_button_3_click(self, event):
        print('on_button_3_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]=6
        #event.widget.color_change = "black"
        #self.display_grid()
        button = tk.Button(self, text="", width=1, height=1, bg="peru")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-1>", self.on_button_3_click)
        print(self.Matrix)
    
    def display_grid(self):
      for x in range(self.h):
          for y in range(self.w):
              if(self.Matrix[x][y]==2 or self.Matrix[x][y]==3 or self.Matrix[x][y]==4):
                  button = tk.Button(self, text="", width=1, height=1, bg="red")
              else:
                  button = tk.Button(self, text="", width=1, height=1)

              button._coords = x, y
              button.grid(row=x, column=y)
              button.bind("<Button-1>", self.on_button_1_click)
              button.bind("<Button-3>", self.on_button_2_click)
    
    def display_grid_second_part(self):
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        for i in range(3):
            for j in range(3):
                self.Matrix[1+i][1+j]=4 
        objects = []
        for i in range(3):
            x=random.randint(5, self.h-3)
            y=random.randint(5, self.w-3)
            objects.append((x,y)) 
            self.Matrix[x][y] = 6
        

        for x in range(self.h):
            for y in range(self.w):
                button = tk.Button(self, text="", width=1, height=1)
                if(x==0 or y==0 or x==self.h-1 or y ==self.w-1):
                    self.Matrix[x][y] = 5
                    button = tk.Button(self, text="", width=1, height=1, bg="blue")
                elif(self.Matrix[x][y]==4):
                    button = tk.Button(self, text="", width=1, height=1, bg="red")
                elif(self.Matrix[x][y]==6):
                    button = tk.Button(self, text="", width=1, height=1, bg="peru")   



                button._coords = x, y
                button.grid(row=x, column=y)
                button.bind("<Button-1>", self.on_button_1_click)
                button.bind("<Button-3>", self.on_button_2_click)

if __name__ == '__main__':
    App().mainloop()
