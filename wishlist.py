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
        master.title("Movie Information Client - Wishlist")
        master.geometry("600x400+300+200")
        self.pack()
        self.create_widgets()
        master.configure(background="#a1dbcd")
        #self.master.geometry("400*600")
                         

    def create_widgets(self):
        
        #winfo_toplevel().title("Movie Information Client - Wishlist)
        
        title_frame = tk.Frame(root, bg="#a1dbcd")
        title_frame.pack(side="top", fill=tk.X)

        home = tk.Button(title_frame, text="Home",fg="white", bd=0, bg="#179184",width=10, height=2) # command=self.master.destroy) #quit application button
        home.pack(side="left", padx=80, pady=10) #placement of button
        
        wishlist = tk.Label(title_frame, bg="#a1dbcd") #creates label
        wishlist["text"] = "WISHLIST" #text on label
        wishlist.pack(side="left", padx=10, pady=10)
        wishlist.configure(font="titleFont")
        
        search_function = tk.Entry(title_frame, bg="white")
        search_function.pack(side="right", padx=50, pady=10)
        
        
   #     self.SearchContents = tk.StringVar()
   #     self.SearchContents.set("Arrival")         
   #     # tell the entry widget to watch this variable
   #     search_function["textvariable"] = self.SearchContents
   #     search_function.bind('<Key-Return>', self.MovieSearch)
   #     
   #     MovieBtn = tk.Button(self.SearchFrame, padx=3, pady=3)
   #     MovieBtn["text"] = "Find Movie"
   #     MovieBtn["command"] = self.MovieSearch
   #     MovieBtn.pack(side = tk.LEFT)
        
        
        main_frame = tk.Frame(root, bg="#a1dbcd")
        main_frame.pack(side="top", fill=tk.BOTH)
        
        bottom_frame = tk.Frame(main_frame, bg="#a1dbcd")
        bottom_frame.pack(side="bottom", fill=tk.X)
        
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side="right", fill=tk.Y)
        
        film_frame = tk.LabelFrame(main_frame, width=500, height=150, bg="white")
        film_frame.pack(side="top")
        
        info_frame = tk.Frame(film_frame, bg="white")
        info_frame.pack(side="top", fill=tk.X)
        
        title = tk.Label(info_frame, bg="white")
        title["text"] = "Film Title:"
        title.pack(side="top", padx=10, pady=10)
        
        date = tk.Label(info_frame, bg="white")
        date["text"] = "Date Added to Wishlist:"
        date.pack(side="top", padx=10, pady=10)
                      
                              
        mini_frame = tk.Frame(film_frame, bg="white")
        mini_frame.pack(side="bottom", fill=tk.X)
                              
        remove = tk.Button(mini_frame, text="Remove Film", fg="white",bd=0, bg="#179184",width=20, height=2, command=film_frame.destroy) #, command=self.display_film) #creates button
        #remove["command"] = self.remove_film #create command when button is pressed
        remove.pack(side="right", padx=50, pady=10)
        
        film = tk.Button(mini_frame, text="Show Film Info",fg="white", bd=0, bg="#179184",width=20, height=2) #, command=self.display_film) #creates button
        film["command"] = self.display_film #create command when button is pressed
        film.pack(side="right", padx=50, pady=10) #placement of button
        
        
        quit = tk.Button(bottom_frame, text="Close Application", fg="white",bd=0, bg="#af1700", width=20, height=2, command=self.master.destroy) #quit application button
        quit.pack(side="bottom", pady=10) #placement of button
        
        


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
    
    
    #------------Movie Search Function---------------#
    
  #  def MovieSearch(self):
        
        #print(self.SearchContents.get())
        #response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        #print(response.content)
        #print(omdb.get(title=self.SearchContents.get()))
        
  #      response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
  #      movie_dictionary_info = json.loads(response.text)
  #      print(movie_dictionary_info)
  #      
  #      self.TitleX = tk.StringVar()
  #      self.TitleX.set(movie_dictionary_info.get("Title"))
  #      
  #      self.YearX = tk.StringVar()
  #      self.YearX.set(movie_dictionary_info.get("Year"))
  #      
  #      self.DirectorX = tk.StringVar()
  #      self.DirectorX.set(movie_dictionary_info.get("Director"))
  #      
  #      self.GenreX = tk.StringVar()
  #      self.GenreX.set(movie_dictionary_info.get("Genre"))
  #      
  #      self.MovieTitle["textvariable"] = self.TitleX
  #      self.MovieYear["textvariable"] = self.YearX
  #      self.MovieDirector["textvariable"] = self.DirectorX
  #      self.MovieGenre["textvariable"] = self.GenreX
        
   # def text_update(film):
    #    film.text.delete(0, tk.END)
     #   film.text.insert(0, film) 
        #root = tk.Tk()
        
# run the GUI event loop          
                 
                 
        
app = Application(master=root)
app.mainloop()
