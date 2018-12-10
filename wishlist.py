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

UPDATE_RATE = 10000

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        master = master
        master.title("Movie Information Client - Wishlist")
        master.geometry("600x1000+300+200")
        self.pack()
        
        #============Core Frame Refresh==================#

        title_frame, main_frame, bottom_frame = self.create_frames()
                    
        self.create_widgets(title_frame, main_frame, bottom_frame)
        master.configure(background="#a1dbcd")
#        self.updater(title_frame, main_frame, bottom_frame)

          
#------------File Read Function------------------#
                       
    def FileRead(self):
        
        wishlist_file= open("movie_wishlist.txt","r+")
        contents = wishlist_file.readlines()
        count=0
        for each in contents:
            count += 1
        wishlist_file.close()
        return count
        
#------------Create Frames Function--------------#
        
    def create_frames(self):
               
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
                
        return title_frame, main_frame, bottom_frame
        
#------------Frame Reset Function----------------#
        
    def frame_reset(self, main_frame, title_frame, bottom_frame):

#============Frame Reset=========================# 

        main_frame.destroy()
        title_frame.destroy()
        bottom_frame.destroy()
        self.updater()
        
#------------Create Film Frames Function---------#
        
    def create_film_frames(self, main_frame):
       
        count = self.FileRead()

#============Film Frame with Objects=============#   
         
        for i in range(count):
        
            film_frame = tk.LabelFrame(main_frame, width=300, height=100, bg="white")
            film_frame.pack(side="top")
            
            info_frame = tk.Frame(film_frame, bg="white")
            info_frame.pack(side="top", fill=tk.X)
                                  
            mini_frame = tk.Frame(film_frame, bg="white")
            mini_frame.pack(side="bottom", fill=tk.X)
                
            title = tk.Label(info_frame, bg="white")
            title["text"] = "Film Title:"
            title.pack(side="top", padx=5, pady=5)
            #Variable
            self.MovieTitle = tk.Label(info_frame, padx=3, pady=3, bg="white")
            self.MovieTitle.pack()
            self.MovieTitle["textvariable"] = self.LabelDefault
            
            date = tk.Label(info_frame, bg="white")
            date["text"] = "Date Added to Wishlist:"
            date.pack(side="top", padx=5, pady=5)
            #Variable
            self.DateAdded = tk.Label(info_frame, padx=3, pady=3, bg="white")
            self.DateAdded.pack()
            self.DateAdded["textvariable"] = self.LabelDefault
            
            #creates button
            remove = tk.Button(mini_frame, text="Remove Film", fg="white",bd=0, bg="#179184",width=20, height=2)
            remove['command'] = (lambda i=i: self.RemoveFilm(i, film_frame))
            #placement of button
            remove.pack(side="right", padx=25, pady=5)
            
            #creates button
            film = tk.Button(mini_frame, text="Show Film Info",fg="white", bd=0, bg="#179184",width=20, height=2) 
            #create command when button is pressed
            film["command"] = lambda i=i: self.display_film(i) 
            #placement of button
            film.pack(side="right", padx=25, pady=5) 
            
            self.InfoDisplay(i)





        
#------------Create Widgets Function-------------#
        
    def create_widgets(self, title_frame, main_frame, bottom_frame):

##============Search Widget=======================#   
#        
#        search_function = tk.Entry(title_frame, bg="white")
#        search_function.pack(side="right", padx=50, pady=10)
#        self.SearchContents = tk.StringVar()
#        self.SearchContents.set("Search Here")         
#        # tell the entry widget to watch this variable
#        search_function["textvariable"] = self.SearchContents
#        search_function.bind('<Key-Return>', self.MovieSearch, self.frame_reset)
                
#============Default Declarations================#   
        
        self.LabelDefault = tk.StringVar()
        self.LabelDefault.set("--")
                
#============Create Film Frames==================# 
        
        self.create_film_frames(main_frame)
   
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
        
#------------Display Info Function---------------#
        
    def InfoDisplay(self, i):
        
        with open("movie_wishlist.txt","r+") as wishlist_file:
            for idx, line in enumerate(wishlist_file):
                if idx == i:
                    wishlist = line.split(',')
                    wishlist_data = wishlist[0]
                    date_data = wishlist[1]

                    response = requests.get(wishlist_data)
                    dictionary_info = json.loads(response.text)
                
                    self.TitleX = tk.StringVar()
                    self.TitleX.set(dictionary_info.get("Title"))
                    self.MovieTitle["textvariable"] = self.TitleX
                    
                    self.DateX = tk.StringVar()
                    self.DateX.set(date_data)
                    self.DateAdded["textvariable"] = self.DateX                
                
        wishlist_file.close()

#------------Display Film Function---------------#

    #display_film button command
    def display_film(self, i): 
        
        film_description = tk.Entry
        film_description = tk.Toplevel(root, bg="#a1dbcd")
                
        with open("movie_wishlist.txt","r+") as wishlist_file:
            for idx, line in enumerate(wishlist_file):
                if idx == i:
                    wishlist = line.split(',')
                    wishlist_data = wishlist[0]
                    #date_data = wishlist[1]
                    
                    
                    
                    dictionary_info = json.loads(response.text)
                
                    self.TitleX = tk.StringVar()
                    self.TitleX.set(dictionary_info.get("Title"))
                    #self.MovieTitle["textvariable"] = self.TitleX
                    
                    self.DateX = tk.StringVar()
                    self.DateX.set(dictionary_info.get("Released"))
                   # self.DateRelease["textvariable"] = self.DateX
                   
                    self.DirectorX = tk.StringVar()
                    self.DirectorX.set(dictionary_info.get("Director"))
                    
                    self.CastX = tk.StringVar()
                    self.CastX.set(dictionary_info.get("Actors"))
                    
                    self.PlotX = tk.StringVar()
                    self.PlotX.set(dictionary_info.get("Plot"))
                    
                    tk.Label(film_description, text='Film Title: %s\nDate of Release: %s\nDirector: %s\nCast: %s\nFilm Description: %s' % (self.TitleX.get(), self.DateX.get(), self.DirectorX.get(), self.CastX.get(), self.PlotX.get()), bg="#a1dbcd").pack(side="left", padx=30, pady=30)
                
                
        wishlist_file.close()
        print(i)
        f = 'floccinaucinihilipilification'
        print(f)
    
##------------Movie Search Function---------------#
#    
#    def MovieSearch(self, event=None):
#            
#        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
#        movie_dictionary_info = json.loads(response.text)
#        print(movie_dictionary_info)
#        
#        self.IMDbID = tk.StringVar()
#        self.IMDbID.set(movie_dictionary_info.get("imdbID"))
#        
#        wishlist_file= open("movie_wishlist.txt","a+")
#        wishlist_file.write("\nhttp://www.omdbapi.com/?i=%s&apikey=3f3265e5" % self.IMDbID.get())
#        wishlist_file.close()
#        
#        self.DateAddedAppend()
#        
##------------Date Append Function----------------#
#             
#    def DateAddedAppend(self):
#         
#        wishlist_file= open("movie_wishlist.txt","a+")
#        wishlist_file.write(now.strftime(",%d:%m:%Y"))
#        wishlist_file.close()
#             
#------------Remove Film Function----------------#
        
# run the GUI event loop          
    def RemoveFilm(self, i, film_frame):
        print('in')
        wishlist = open("movie_wishlist.txt","r")
        lines = wishlist.readlines()
        wishlist.close()
        wishlist = open("movie_wishlist.txt","w")
        idx = 0
        for line in lines:
            if idx != i:
                wishlist.write(line)
            idx=idx+1
        wishlist.close()
        film_frame.destroy()
        
app = Application(master=root)
app.mainloop()
