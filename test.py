

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.w, self.h = 15, 15
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)] 
        #self.butto

        self.display_grid()

    def on_button_1_click(self, event):
        print('on_button_1_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 1
        #event.widget.color_change = "black"
        #self.display_grid()
        button = tk.Button(self, text="", width=4, height=2, bg="black")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-1>", self.on_button_1_click)
        print(self.Matrix)

    
    def on_button_2_click(self, event):
        print('on_button_2_click:{}'.format(event.widget._coords))
        self.Matrix[event.widget._coords[0]][event.widget._coords[1]]= 2
        #event.widget.color_change = "black"
        #self.display_grid()
        button = tk.Button(self, text="", width=4, height=2, bg="blue")
        x = event.widget._coords[0]
        y = event.widget._coords[1]
        button._coords = x, y
        button.grid(row=x, column=y)
        button.bind("<Button-3>", self.on_button_2_click)
        print(self.Matrix)
    
    def display_grid(self):
      for x in range(self.h):
          for y in range(self.w):
              button = tk.Button(self, text="", width=4, height=2)
              button._coords = x, y
              button.grid(row=x, column=y)
              button.bind("<Button-1>", self.on_button_1_click)
              button.bind("<Button-3>", self.on_button_2_click)


if __name__ == '__main__':
    App().mainloop()
