# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:36:42 2018

@author: Student
"""

import tkinter as tk
from tkinter import font


root = tk.Tk()
titleFont = font.Font(family = "Helvetica", size = 36, weight = "bold")
font.families()


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        master = master
        self.pack()
        self.create_widgets()
        master.configure(background="#a1dbcd")
        

    def create_widgets(self):

        home = tk.Button(text="Home", bg="#a1dbcd") # command=self.master.destroy) #quit application button
        home.pack(side="left", padx=10, pady=10) #placement of button
        
        wishlist = tk.Label(bg="#a1dbcd") #creates label
        wishlist["text"] = "WISHLIST" #text on label
        wishlist.pack(side="left", padx=10, pady=10)
        wishlist.configure(font="titleFont")
        
       
        film = tk.Button(text="will be a film title", bg="#a1dbcd") #, command=self.display_film) #creates button
        film["command"] = self.display_film #create command when button is pressed
        film.pack(side="bottom") #placement of button

        quit = tk.Button(text="Close Application", fg="red", bg="#a1dbcd", command=self.master.destroy) #quit application button
        quit.pack(side="bottom") #placement of button


    def display_film(self): #display_film button command
        
        
        film_description = tk.Toplevel(root, bg="#a1dbcd")
        
        tk.Label(film_description, text='Film Title:\nDate of Release:\nDirector:\nCast:\nDate Added to Wishlist:\nFilm Description:', bg="#a1dbcd").pack(side="left", padx=30, pady=30)
    
        
        
app = Application(master=root)
app.mainloop()
