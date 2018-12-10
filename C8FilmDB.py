# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:30:17 2018

@author: Student
"""

#============Importing the APIs==================#
import requests, json
response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")
movie_dictionary_info = json.loads(response.text)

import collections
import tkinter as tk

#------------Application Class-------------------#   

class Application(tk.Frame):
    
#------------Initialisation Function-------------#   
    
    def __init__(self, master=None):
        
#============Setting Up Everything===============#
        
        super().__init__(master, width=500)
        self.master = master
        self.pack()
        self.create_widgets()
        master.geometry("600x300+300+200")
        
        master.configure(background="#a1dbcd")
        
    def create_film_frames(self):
        
        #some for loop to count number of searched items
        
        #----------------------------------       
        #Film Frame
        self.FilmFrame = tk.Frame(bg="white")
        self.FilmFrame.pack(side = tk.TOP)
        
        #Info Frame
        self.InfoFrame = tk.Frame(self.FilmFrame,bg="white")
        self.InfoFrame.pack(pady = 10)
        
        #Title Frame - Info Frame
        TitleFrame = tk.Frame(self.InfoFrame,bg="white")
        TitleFrame.pack()
        
        #Year Frame - Info Frame
        YearFrame = tk.Frame(self.InfoFrame,bg="white")
        YearFrame.pack()
        
        #Director Frame - Info Frame
        DirectorFrame = tk.Frame(self.InfoFrame,bg="white")
        DirectorFrame.pack()
        
        #Genre Frame - Info Frame
        GenreFrame = tk.Frame(self.InfoFrame,bg="white")
        GenreFrame.pack()
        
        #Button Frame
        self.ButtonFrame = tk.Frame(self.FilmFrame,bg="white")
        self.ButtonFrame.pack(side = tk.BOTTOM)
        
        #============Labels for Movie Info==============#   
        
        #Title of the Movie
        #Label
        self.title = tk.Label(TitleFrame, padx=3, pady=3,bg="white")
        self.title.pack(side = tk.LEFT)
        self.title["text"] = "Title:"
        #Variable
        self.MovieTitle = tk.Label(TitleFrame, padx=3, pady=3,bg="white")
        self.MovieTitle.pack()
        self.MovieTitle["textvariable"] = self.LabelDefault
        
        #Year the Movie was Released
        #Label
        self.year = tk.Label(YearFrame, padx=3, pady=3,bg="white")
        self.year.pack(side = tk.LEFT)
        self.year["text"] = "Year:"
        #Variable
        self.MovieYear = tk.Label(YearFrame, padx=3, pady=3,bg="white")
        self.MovieYear.pack()
        self.MovieYear["textvariable"] = self.LabelDefault
        
        #The Director of the Movie
        #Label
        self.director = tk.Label(DirectorFrame, padx=3, pady=3,bg="white")
        self.director.pack(side = tk.LEFT)
        self.director["text"] = "Director:"
        #Variable
        self.MovieDirector = tk.Label(DirectorFrame, padx=3, pady=3,bg="white")
        self.MovieDirector.pack()
        self.MovieDirector["textvariable"] = self.LabelDefault
        
        #The Genre(s) of the Movie
        #Label
        self.genre = tk.Label(GenreFrame, padx=3, pady=3,bg="white")
        self.genre.pack(side = tk.LEFT)
        self.genre["text"] = "Genre:"
        #Variable
        self.MovieGenre = tk.Label(GenreFrame, padx=3, pady=3,bg="white")
        self.MovieGenre.pack()
        self.MovieGenre["textvariable"] = self.LabelDefault
        
#============Info and Add-to-Wishlist Buttons=========================#        
        
        add = tk.Button(self.ButtonFrame, text="Add to Wishlist", fg="white",bd=0, bg="#179184",width=20, height=2) # command=self.display_film) #creates button
        #remove["command"] = self.remove_film #create command when button is pressed
        add.pack(side="right", padx=50, pady=10)
        
        film = tk.Button(self.ButtonFrame, text="Show Film Info",fg="white", bd=0, bg="#179184",width=20, height=2) #, command=self.display_film) #creates button
        film["command"] = self.display_film #create command when button is pressed
        film.pack(side="right", padx=50, pady=10) #placement of button
        
        
        
                         
#------------Create Widgets Function-------------#   
        
    def create_widgets(self):
        
#============Labelling The Window================#   
        
        self.winfo_toplevel().title("Movie Information Client")
 
#============Frame Declarations==================#   
        
        #Search Frame
        self.SearchFrame = tk.Frame(bg="#a1dbcd")
        self.SearchFrame.pack(side = tk.TOP)

#============Default Declarations===============#   
        
        self.LabelDefault = tk.StringVar()
        self.LabelDefault.set("--")
 
#============Frame Declarations==================#   

        
     
        #Quit Frame
        self.QuitFrame = tk.Frame(bg="#a1dbcd")
        self.QuitFrame.pack(side = tk.BOTTOM)
        
#============Search Frame======================#
        
        wishlist = tk.Button(self.SearchFrame, text="Wishlist",fg="white", bd=0, bg="#179184", width=10, height=2) # command=self.master.destroy) #quit application button
        wishlist.pack(side="left", padx=120, pady=10) #placement of button
        
        #title = tk.Label(self.SearchFrame,fg="white", bg="#a1dbcd") #creates label
        #title["text"] = "FIND A FILM" #text on label
        #title.pack(side="left", padx=50, pady=10)
        
#============Search Widget======================#   
        
        self.Search = tk.Entry(self.SearchFrame)
        self.Search.pack(side = tk.RIGHT) #, fill=tk.X)
        
        self.SearchContents = tk.StringVar()
        self.SearchContents.set("Arrival")         
        # tell the entry widget to watch this variable
        self.Search["textvariable"] = self.SearchContents
        self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self.SearchFrame, fg="white", bd=0, bg="#179184",width=10, height=2)
        self.MovieBtn["text"] = "Find Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side = tk.RIGHT, padx=20)


#============Quit Button=========================#   
        
        self.quit = tk.Button(self.QuitFrame, text="QUIT", fg="white",bd=0, bg="#af1700", width=10, height=2,
                              command=self.master.destroy,)
        self.quit.pack(pady=10)
 
#------------Movie Search Function---------------#
    
    def MovieSearch(self, event=None):
        
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info)
          
#        movie = collections.defaultdict(list)
#        for i in movie_dictionary_info:
#            #dictionary = movie_dictionary_info.split('},')
#            movie[i['Title']].append(i)
#            
#        movie_list = list(movie.values())
        
        self.TitleX = tk.StringVar()
        self.TitleX.set(movie_dictionary_info.get("Title"))
        
        self.YearX = tk.StringVar()
        self.YearX.set(movie_dictionary_info.get("Year"))
        
        self.DirectorX = tk.StringVar()
        self.DirectorX.set(movie_dictionary_info.get("Director"))
        
        self.GenreX = tk.StringVar()
        self.GenreX.set(movie_dictionary_info.get("Genre"))
        
        self.create_film_frames()
        
        self.MovieTitle["textvariable"] = self.TitleX
        self.MovieYear["textvariable"] = self.YearX
        self.MovieDirector["textvariable"] = self.DirectorX
        self.MovieGenre["textvariable"] = self.GenreX
            
            
        
    def display_film(self): #display_film button command
        
        film_description = tk.Entry
        
        film_description = tk.Toplevel(root, bg="#a1dbcd")
        #film_description.geometry("300x150+300+300")
        
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        dictionary_info = json.loads(response.text)
        print(dictionary_info)
        
        self.TitleX = tk.StringVar()
        self.TitleX.set(dictionary_info.get("Title"))
        
        self.DateX = tk.StringVar()
        self.DateX.set(dictionary_info.get("Released"))
       
        self.DirectorX = tk.StringVar()
        self.DirectorX.set(dictionary_info.get("Director"))
        
        self.CastX = tk.StringVar()
        self.CastX.set(dictionary_info.get("Actors"))
        
        self.PlotX = tk.StringVar()
        self.PlotX.set(dictionary_info.get("Plot"))
        
        tk.Label(film_description, text='Film Title: %s\nDate of Release: %s\nDirector: %s\nCast: %s\nFilm Description: %s' % (self.TitleX.get(), self.DateX.get(), self.DirectorX.get(), self.CastX.get(), self.PlotX.get()), bg="#a1dbcd").pack(side="left", padx=30, pady=30)
        
#         #Title Frame - Info Frame
#        TitleFrameA = tk.Frame(self.InfoFrame,bg="white")
#        TitleFrameA.pack()
#        
#        #Year Frame - Info Frame
#        YearFrameA = tk.Frame(self.InfoFrame,bg="white")
#        YearFrameA.pack()
#        
#        #Director Frame - Info Frame
#        DirectorFrameA = tk.Frame(self.InfoFrame,bg="white")
#        DirectorFrameA.pack()
#        
#        #Genre Frame - Info Frame
#        GenreFrameA = tk.Frame(self.InfoFrame,bg="white")
#        GenreFrameA.pack()
#        
#        #Plot
#                 
#        self.titleA = tk.Label(TitleFrameA, padx=3, pady=3,bg="white")
#        self.titleA.pack(side = tk.LEFT)
#        self.titleA["text"] = "Title:"
#        #Variable
#        self.MovieTitleA = tk.Label(TitleFrameA, padx=3, pady=3,bg="white")
#        self.MovieTitleA.pack()
#        self.MovieTitleA["textvariable"] = self.TitleX
#        
#        #Year the Movie was Released
#        #Label
#        self.yearA = tk.Label(YearFrameA, padx=3, pady=3,bg="white")
#        self.yearA.pack(side = tk.LEFT)
#        self.yearA["text"] = "Year:"
#        #Variable
#        self.MovieYearA = tk.Label(YearFrameA, padx=3, pady=3,bg="white")
#        self.MovieYearA.pack()
#        self.MovieYearA["textvariable"] = self.YearX
#        
#        #The Director of the Movie
#        #Label
#        self.directorA = tk.Label(DirectorFrameA, padx=3, pady=3,bg="white")
#        self.directorA.pack(side = tk.LEFT)
#        self.directorA["text"] = "Director:"
#        #Variable
#        self.MovieDirectorA = tk.Label(DirectorFrameA, padx=3, pady=3,bg="white")
#        self.MovieDirectorA.pack()
#        self.MovieDirectorA["textvariable"] = self.DirectorX
#        
#        #The Genre(s) of the Movie
#        #Label
#        self.genreA = tk.Label(GenreFrameA, padx=3, pady=3,bg="white")
#        self.genreA.pack(side = tk.LEFT)
#        self.genreA["text"] = "Genre:"
#        #Variable
#        self.MovieGenreA = tk.Label(GenreFrameA, padx=3, pady=3,bg="white")
#        self.MovieGenreA.pack()
#        self.MovieGenreA["textvariable"] = self.GenreX
#        
#        #self.Plot = tk.Label(PlotFrameA)
#        self.Plot.pack(side = tk.LEFT)
#        self.Plot["text"] = "Plot:"
#    
#        
#        
#        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
#        movie_dictionary_info = json.loads(response.text)
#        print(movie_dictionary_info)
#        
#        self.PlotX = tk.StringVar()
#        self.PlotX.set(movie_dictionary_info.get("Plot"))
#        
#        #self.Plot = tk.Label(PlotFrameA)
#        self.Plot.pack()
#        self.Plot["textvariable"] = self.PlotX
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()