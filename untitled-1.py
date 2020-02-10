#! GabrielBreeding
#  2/10/2020

import tkinter as tk
import pickle 
from tkinter import scrolledtext

if __name__ == "__main__":
    datafile = open("gamelib.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close    
    
    root = tk.Tk()
    root.geometry("350x400")
    root.title("Gabriel's Game Library!")
    
    class StartScreen(tk.Frame):
    
        def __init__(self):
            tk.Frame.__init__(self)
            
            self.lbl_welcome = tk.Label(self, text = "Welcome To Gabriel's Game Library!", fg = "blue")
            self.lbl_welcome.grid(row = 0, column = 0, columnspan = 2 , sticky = "news")
            
            self.btn_start = tk.Button(self, text = "Add / Edit", bg = "green")
            self.btn_start.grid(row = 1, column = 0, columnspan = 2, sticky = "news")          
            
            self.btn_start = tk.Button(self, text = "Print All Games", bg = "green")
            self.btn_start.grid(row = 2, column = 0, columnspan = 2, sticky = "news")    
            
            self.btn_start = tk.Button(self, text = "Search For A Game", bg = "green")
            self.btn_start.grid(row = 3, column = 0, columnspan = 2, sticky = "news")   
            
            self.btn_start = tk.Button(self, text = "Remove A Game", bg = "green")
            self.btn_start.grid(row = 4, column = 0, columnspan = 2, sticky = "news")   
            
            self.btn_start = tk.Button(self, text = "Save", bg = "green")
            self.btn_start.grid(row = 5, column = 0, columnspan = 2, sticky = "news")               
        
    startscreen = StartScreen()
    startscreen.grid(row = 0, column = 0, sticky = "news")
    
    
    
    
    root.mainloop()
