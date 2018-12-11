#============Importing the APIs==================#
import requests, json
response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")
movie_dictionary_info = json.loads(response.text)

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
        add["command"] = self.WishAdd #create command when button is pressed
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
        
        self.create_film_frames()
     
        #Quit Frame
        self.QuitFrame = tk.Frame(bg="#a1dbcd")
        self.QuitFrame.pack(side = tk.BOTTOM)
        
#============Search Frame======================#
        
        wishlist = tk.Button(self.SearchFrame, text="Wishlist",fg="white", bd=0, bg="#179184", width=10, height=2) # command=self.master.destroy) #quit application button
        wishlist.pack(side="left", padx=10, pady=10) #placement of button
        
        TMDbBtn = tk.Button(self.SearchFrame, fg="white", bd=0, bg="#179184",width=10, height=2)
        TMDbBtn["text"] = "TMDb Movie"
        TMDbBtn["command"] = self.TMDbSearch
        TMDbBtn.pack(side="right", padx=10, pady=10)
        
#============Search Widget======================#   
        
        self.Search = tk.Entry(self.SearchFrame,width=20)
        self.Search.pack(side = tk.LEFT, padx=10) #, fill=tk.X)
        
        self.SearchContents = tk.StringVar()
        self.SearchContents.set("Search")         
        # tell the entry widget to watch this variable
        self.Search["textvariable"] = self.SearchContents
        self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self.SearchFrame, fg="white", bd=0, bg="#179184",width=10, height=2)
        self.MovieBtn["text"] = "OMDb Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side = tk.RIGHT, padx=10)
        


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
        
        
        self.MovieTitle["textvariable"] = self.TitleX
        self.MovieYear["textvariable"] = self.YearX
        self.MovieDirector["textvariable"] = self.DirectorX
        self.MovieGenre["textvariable"] = self.GenreX
            
#------------Movie Search Function---------------#
    
    def TMDbSearch(self, event=None):
        
        response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=60e497d583523b256a66a41c0c9bf116&query=%s" % (self.SearchContents.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info['results'][0]['id'])
        
        self.IdX = tk.StringVar()
        self.IdX.set(movie_dictionary_info['results'][0]['id'])
        print("This is it %s" % self.IdX.get())
        
        response = requests.get("https://api.themoviedb.org/3/movie/%s?api_key=60e497d583523b256a66a41c0c9bf116" % (self.IdX.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info)
        
        self.imdb_IdX = tk.StringVar()
        self.imdb_IdX.set(movie_dictionary_info.get("imdb_id"))
        
        response = requests.get("http://www.omdbapi.com/?i=%s&apikey=3f3265e5" % (self.imdb_IdX.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info)
        
        self.TitleX = tk.StringVar()
        self.TitleX.set(movie_dictionary_info.get("Title"))
        
        self.YearX = tk.StringVar()
        self.YearX.set(movie_dictionary_info.get("Year"))
        
        self.DirectorX = tk.StringVar()
        self.DirectorX.set(movie_dictionary_info.get("Director"))
        
        self.GenreX = tk.StringVar()
        self.GenreX.set(movie_dictionary_info.get("Genre"))
        

        self.MovieTitle["textvariable"] = self.TitleX
        self.MovieYear["textvariable"] = self.YearX
        self.MovieDirector["textvariable"] = self.DirectorX
        self.MovieGenre["textvariable"] = self.GenreX
            
            
        
    def display_film(self): #display_film button command
        
        film_description = tk.Entry
        
        film_description = tk.Toplevel(root, bg="#a1dbcd")
        
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
       
        
#------------Add to Wishlist Function------------#
    
    def WishAdd(self, event=None):
            
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        movie_dictionary_info = json.loads(response.text)
        print(movie_dictionary_info)
        
        self.IMDbID = tk.StringVar()
        self.IMDbID.set(movie_dictionary_info.get("imdbID"))
        
        wishlist_file= open("movie_wishlist.txt","a+")
        wishlist_file.write("\nhttp://www.omdbapi.com/?i=%s&apikey=3f3265e5" % self.IMDbID.get())
        wishlist_file.close()
        
        self.DateAddedAppend()
        
#------------Date Append Function----------------#
             
    def DateAddedAppend(self):
         
        wishlist_file= open("movie_wishlist.txt","a+")
        wishlist_file.write(now.strftime(",%d:%m:%Y"))
        wishlist_file.close()
             
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()

#============Importing the APIs==================#

import requests, json, datetime

now = datetime.datetime.now()
import tkinter as tk
from tkinter import font

root = tk.Tk()
titleFont = font.Font(family = "Helvetica", size = 36, weight = "bold")
font.families()

class Wishlist(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        master = master
        master.title("Movie Information Client - Wishlist")
        master.geometry("600x600+300+200")
        self.pack()
        
        #============Core Frame Refresh==================#

        title_frame, main_frame, bottom_frame = self.wish_frames()
                    
        self.wish_widgets_main(title_frame, main_frame, bottom_frame)
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
        
    def wish_frames(self):
               
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

#------------Create Widgets Function-------------#
        
    def wish_widgets_main(self, title_frame, main_frame, bottom_frame):
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
            film["command"] = lambda i=i: self.film_info(i) 
            #placement of button
            film.pack(side="right", padx=25, pady=5) 
            
            self.InfoDisplay(i)
       
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

    #Film Info button command
    def film_info(self, i): 
        
        film_description = tk.Entry
        film_description = tk.Toplevel(root, bg="#a1dbcd")
                
        with open("movie_wishlist.txt","r+") as wishlist_file:
            for idx, line in enumerate(wishlist_file):
                if idx == i:
                    wishlist = line.split(',')
                    wishlist_data = wishlist[0]
                    #date_data = wishlist[1]
                                        
                    response = requests.get(wishlist_data)
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
        
app = Wishlist(master=root)
app.mainloop()
