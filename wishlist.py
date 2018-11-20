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
        #self.master.geometry("400*600")
                         

    def create_widgets(self):
        
        #winfo_toplevel().title("Movie Information Client - Wishlist)
        
        title_frame = tk.Frame(root, bg="#a1dbcd")
        title_frame.pack(side="top")

        home = tk.Button(title_frame, text="Home", bg="#a1dbcd") # command=self.master.destroy) #quit application button
        home.pack(side="left", padx=50, pady=10) #placement of button
        
        wishlist = tk.Label(title_frame, bg="#a1dbcd") #creates label
        wishlist["text"] = "WISHLIST" #text on label
        wishlist.pack(side="left", padx=10, pady=10)
        wishlist.configure(font="titleFont")
        
        search_function = tk.Entry(title_frame, bg="white")
        search_function.pack(side="left", padx=10, pady=10)
        
        main_frame = tk.Frame(root, bg="#a1dbcd")
        main_frame.pack(side="bottom")
        
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side="right", fill=tk.Y)
        
        quit = tk.Button(main_frame, text="Close Application", fg="red", bg="#a1dbcd", command=self.master.destroy) #quit application button
        quit.pack(side="bottom") #placement of button
        
        film_frame = tk.LabelFrame(main_frame, width=500, height=150, bg="#a1dbcd", command=self.master.destroy)
        film_frame.pack(side="bottom")
        
        info_frame = tk.Frame(film_frame, bg="#a1dbcd")
        info_frame.pack(side="top", fill=tk.X)
        
        title = tk.Label(info_frame, bg="#a1dbcd")
        title["text"] = "Film Title:"
        title.pack(side="top", padx=10, pady=10)
        
        date = tk.Label(info_frame, bg="#a1dbcd")
        date["text"] = "Date Added to Wishlist:"
        date.pack(side="top", padx=10, pady=10)
                      
                              
        mini_frame = tk.Frame(film_frame, bg="#a1dbcd")
        mini_frame.pack(side="bottom", fill=tk.X)
                              
        remove = tk.Button(mini_frame, text="Remove Film", fg="red", bg="#a1dbcd") #, command=self.display_film) #creates button
        #remove["command"] = self.remove_film #create command when button is pressed
        remove.pack(side="right", padx=50)
        
        film = tk.Button(mini_frame, text="Show Film Info", bg="#a1dbcd") #, command=self.display_film) #creates button
        film["command"] = self.display_film #create command when button is pressed
        film.pack(side="right", padx=50) #placement of button


        #text = tk.Entry(root, width=35, bg="#a1dbcd")
        #text.pack(side="top") 
        #btn_dict = {}
        #col = 0 
        #words = ["Dog", "Cat", "Pig", "Cow", "Rat"] 
    
        #for animal in words:
    # pass each button's text to a function
         #   action = lambda x = animal: self.text_update(x)
    # create the buttons and assign to animal:button-object dict pair
          #  btn_dict[animal] = tk.Button(root, text=animal, command=action) 
            #btn_dict[animal].grid(row=1, column=col, pady=5) 
           # col += 1

    #def remove_film(self): #removes film frame from wishlist
        
        #self.film_frame(self.master.destroy)


    def display_film(self): #display_film button command
        
        film_description = tk.Entry
        
        film_description = tk.Toplevel(root, bg="#a1dbcd")
        
        tk.Label(film_description, text='Film Title:\nDate of Release:\nDirector:\nCast:\nDate Added to Wishlist:\nFilm Description:', bg="#a1dbcd").pack(side="left", padx=30, pady=30)
    
        
   # def text_update(film):
    #    film.text.delete(0, tk.END)
     #   film.text.insert(0, film) 
        #root = tk.Tk()
        
# run the GUI event loop          
                 
                 
        
app = Application(master=root)
app.mainloop()
