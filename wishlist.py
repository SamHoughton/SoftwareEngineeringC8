# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:36:42 2018

@author: Student
"""
#============Importing the APIs==================#
import requests, json, datetime

now = datetime.datetime.now()
import tkinter as tk
from tkinter import font

root = tk.Tk()
titleFont = font.Font(family = "Helvetica", size = 36, weight = "bold")
font.families()


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        master = master
        master.title("Movie Information Client - Wishlist")
        master.geometry("600x400+300+200")
        self.pack()
        self.create_widgets()
        master.configure(background="#a1dbcd")
        #self.master.geometry("400*600")

                 
    def FileRead(self):
        
        wishlist_file= open("movie_wishlist.txt","r+")
        contents = wishlist_file.readlines()
        count=0
        for each in contents:
            count += 1
        return count
    
    def CreateMovieFrame(self):
#============Film Frame with Objects=============#   
        
        for i in range(count):
        
            film_frame = tk.LabelFrame(main_frame, width=500, height=150, bg="white")
            film_frame.pack(side="top")
            
            info_frame = tk.Frame(film_frame, bg="white")
            info_frame.pack(side="top", fill=tk.X)
                                  
            mini_frame = tk.Frame(film_frame, bg="white")
            mini_frame.pack(side="bottom", fill=tk.X)
                
            title = tk.Label(info_frame, bg="white")
            title["text"] = "Film Title:"
            title.pack(side="top", padx=10, pady=10)
            #Variable
            self.MovieTitle = tk.Label(info_frame, padx=3, pady=3, bg="white")
            self.MovieTitle.pack()
            self.MovieTitle["textvariable"] = self.LabelDefault
            
            date = tk.Label(info_frame, bg="white")
            date["text"] = "Date Added to Wishlist:"
            date.pack(side="top", padx=10, pady=10)
            #Variable
            self.DateAdded = tk.Label(info_frame, padx=3, pady=3, bg="white")
            self.DateAdded.pack()
            self.DateAdded["textvariable"] = self.LabelDefault
            
            #creates button
            remove = tk.Button(mini_frame, text="Remove Film", fg="white",bd=0, bg="#179184",width=20, height=2, command=film_frame.destroy) 
            #placement of button
            remove.pack(side="right", padx=50, pady=10)
            
            #creates button
            film = tk.Button(mini_frame, text="Show Film Info",fg="white", bd=0, bg="#179184",width=20, height=2) 
            #create command when button is pressed
            film["command"] = self.display_film 
            #placement of button
            film.pack(side="right", padx=50, pady=10) 
   

    def create_widgets(self):
        
        #winfo_toplevel().title("Movie Information Client - Wishlist)

#============Frame Declarations==================# 
        
        title_frame = tk.Frame(root, bg="#a1dbcd")
        title_frame.pack(side="top", fill=tk.X)
         
        main_frame = tk.Frame(root, bg="#a1dbcd")
        main_frame.pack(side="top", fill=tk.BOTH)
        
        #Scrollbar
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side="right", fill=tk.Y)
        #main_frame.configure(tk.yscrollcommand=scrollbar.set)
        
        bottom_frame = tk.Frame(bg="#a1dbcd")
        bottom_frame.pack(side="bottom", fill=tk.X)
        
        count = self.FileRead()

#============Search Widget=======================#   
        
        search_function = tk.Entry(title_frame, bg="white")
        search_function.pack(side="right", padx=50, pady=10)
        self.SearchContents = tk.StringVar()
        self.SearchContents.set("Search Here")         
        # tell the entry widget to watch this variable
        search_function["textvariable"] = self.SearchContents
        if search_function.bind('<Key-Return>', self.MovieSearch):
            count=+1
        
#============Default Declarations================#   
        
        self.LabelDefault = tk.StringVar()
        self.LabelDefault.set("--")
  

        self.CreateMovieFrame(count, main_frame)

#============Labels and Buttons==================#
        
        home = tk.Button(title_frame, text="Home",fg="white", bd=0, bg="#179184",width=10, height=2)
        #placement of button
        home.pack(side="left", padx=80, pady=10)
        
        #creates label
        wishlist = tk.Label(title_frame, bg="#a1dbcd")
        #text on label
        wishlist["text"] = "WISHLIST"
        wishlist.pack(side="left", padx=10, pady=10)
        wishlist.configure(font="titleFont")
        
        #quit application button
        quit = tk.Button(bottom_frame, text="Quit", fg="white",bd=0, bg="#af1700", width=10, height=2, command=self.master.destroy)
        #placement of button
        quit.pack(pady=30) 

#------------Display Film Function---------------#

    #display_film button command
    def display_film(self): 
        
        film_description = tk.Entry
        film_description = tk.Toplevel(root, bg="#a1dbcd")
        
        tk.Label(film_description, text='Film Title:\nDate of Release:\nDirector:\nCast:\nDate Added to Wishlist:\nFilm Description:', bg="#a1dbcd").pack(side="left", padx=30, pady=30)
    
    
#------------Movie Search Function---------------#
    
    def MovieSearch(self, event=None):
                
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info)
        
        self.TitleX = tk.StringVar()
        self.TitleX.set(movie_dictionary_info.get("Title"))
        self.MovieTitle["textvariable"] = self.TitleX
        
        self.DateX = tk.StringVar()
        self.DateX.set(now.strftime("%d:%m:%Y"))
        self.DateAdded["textvariable"] = self.DateX
        
        
# run the GUI event loop          

                     
        
app = Application(master=root)
app.mainloop()
