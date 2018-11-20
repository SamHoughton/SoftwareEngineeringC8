# -*- coding: utf-8 -*-
#"""
#Spyder Editor

#This is a temporary script file.
#"""

import tkinter as tk
from tkinter import font


root = tk.Tk()
titleFont = font.Font(family = "Helvetica", size = 36, weight = "bold")
font.families()


class Application(tk.Frame):
    
    root = tk.Tk()
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.films = [0]
        self.master.configure(background="#a1dbcd")
        

    def create_widgets(self):

        self.quit = tk.Button(self, text="Close Application", fg="red", bg="#a1dbcd",
                              command=self.master.destroy) #quit application button
        self.quit.pack(side="bottom") #placement of button
        
        self.wishlist = tk.Label(self, bg="#a1dbcd") #creates label
        self.wishlist["text"] = "WISHLIST" #text on label
        self.wishlist.pack(side="top")
        self.wishlist.configure(font="titleFont")
        
        #self.frame = tk.LabelFrame(self, text="Help please")
        #self.frame.pack(fill = "both", expand = "yes", side="top")
        #self.left = tk.LabelFrame(frame, text = "Inside the LabelFrame")
        #self.left.pack()
        
        self.film = tk.Button(self, text="will be a film title", bg="#a1dbcd") #, command=self.display_film) #creates button
        #self.film["text"] = "will be a film title?" #creates text on button
        self.film["command"] = self.display_film #create command when button is pressed
        self.film.pack(side="top") #placement of button

    def display_film(self): #display_film button command
        film_description = tk.Toplevel(self.root)
        film_description.title(self.films[0])
        tk.Label(film_description, text='Film Title:\nDate of Release:\nDirector:\nCast:\nDate Added to Wishlist:\nFilm Description:', anchor='w').pack(fill='both') #(padx=10, pady=10)
        #tk.Button(film_description)
        
        #self.quit = tk.Button(self, text="Close Application", fg="red", command=self.master.destroy) #quit application button
        #self.quit.pack(side="bottom") #placement of button #just adds another button on to main window
        
        
        #self.film_description["text"] = "Film title??"
        #self.print("Help pls")
        #root.title("hello")
        #top = Toplevel()
        #top.title("Python")
        
        #print("hi there, everyone!") #when hello world button pressed, print text


#root = tk.Tk()
app = Application(master=root)
app.mainloop()
#backgroundColour = background
#titleFont = font.Font(family = "Helvetica", size = 36, weight = "bold")
#font.families()
