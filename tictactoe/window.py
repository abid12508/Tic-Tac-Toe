import tkinter as tk
from tkinter import ttk 
from tkinter import font
import game

class window:
    def __init__(self):
        
        #initialize win
        self.win = tk.Tk()
        #initialize canvas
        self.canvas = tk.Canvas(self.win, width=500, height=300)
        self.canvas.pack()
        #initialize font
        self.font = font.Font(family='Helvetica', size=38)
        #initialize buttonlist to store all buttons
        self.buttonlist = []
        #include game script
        self.game = game.Game(self.buttonlist)

    def customize_Win(self):
        # Set the size of the tkinter window
        self.win.geometry("300x300")
        self.win.resizable(False, False)
    #make buttons
    def buttons(self):
        #Place buttons on frame and move frame alltogether
        button_Frame = ttk.Frame()
        #make 9 buttons and add buttons to list
        for i in range(9):
            button = tk.Button(button_Frame, text=" ", borderwidth=1, font=self.font, 
                                width=3, command=lambda idx=i: self.game.mark(self.buttonlist, idx))
            button.grid(row=i//3, column=i%3)
            self.buttonlist.append(button)
            
        #Position all buttons
        button_Frame.place(x=3)


    
#assemble everything
def everything():
    win_Class = window()
    win_Class.customize_Win()
    win_Class.buttons()
    win_Class.win.mainloop()
    