# -*- coding: utf-8 -*-
#"""
#Spyder Editor

#This is a temporary script file.
#"""

import tkinter as tk
from tkinter import font


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):

        self.quit = tk.Button(self, text="Close Application", fg="red",
                              command=self.master.destroy) #quit application button
        self.quit.pack(side="bottom") #placement of button
        
        self.wishlist = tk.Label(self) #creates label
        self.wishlist["text"] = "WISHLIST" #text on label
        self.wishlist.pack(side="top")
        self.wishlist.configure(font="titleFont")
        
        
        #self.hi_there = tk.Button(self) #creates button
        #self.hi_there["text"] = "Hello World\n(click me)" #creates text on button
        #self.hi_there["command"] = self.say_hi #create command when button is pressed
        #self.hi_there.pack(side="top") #placement of button

    def say_hi(self): #hi_there button command
        print("hi there, everyone!") #when hello world button pressed, print text


root = tk.Tk()
app = Application(master=root)
app.mainloop()
titleFont = font.Font(family='MS Serif Symbol', size=20)
font.families()