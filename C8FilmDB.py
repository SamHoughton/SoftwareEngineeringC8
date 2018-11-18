#============Importing the APIs==================#
import requests, json, omdb
response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")
movie_dictionary_info = json.loads(response.text)

omdb.set_default('apikey', '3f3265e5')
res = omdb.request(t='Lion King', y=1994, r='xml')
xml_content = res.content

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
        
#------------Create Widgets Function-------------#   
        
    def create_widgets(self):
        
#============Labelling The Window================#   
        
        self.winfo_toplevel().title("Movie Information Client")
 
#============Frame Declarations==================#   
        
        #Search Frame
        self.SearchFrame = tk.Frame()
        self.SearchFrame.pack(side = tk.TOP)
        
        #Info Frame
        self.InfoFrame = tk.Frame()
        self.InfoFrame.pack()
        
        #Title Frame - Info Frame
        TitleFrame = tk.Frame(self.InfoFrame)
        TitleFrame.pack()
        
        #Year Frame - Info Frame
        YearFrame = tk.Frame(self.InfoFrame)
        YearFrame.pack()
        
        #Year Frame - Info Frame
        DirectorFrame = tk.Frame(self.InfoFrame)
        DirectorFrame.pack()
        
        #Genre Frame - Info Frame
        GenreFrame = tk.Frame(self.InfoFrame)
        GenreFrame.pack()
        
        #Quit Frame
        self.QuitFrame = tk.Frame()
        self.QuitFrame.pack(side = tk.BOTTOM)

#============Default Declarations===============#   
        
        self.LabelDefault = tk.StringVar()
        self.LabelDefault.set("--")
        
#============Search Widget======================#   
        
        self.Search = tk.Entry(self.SearchFrame)
        self.Search.pack(side = tk.RIGHT, fill=tk.X)
        self.SearchContents = tk.StringVar()
        self.SearchContents.set("Arrival")         
        # tell the entry widget to watch this variable
        self.Search["textvariable"] = self.SearchContents
        self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self.SearchFrame, padx=3, pady=3)
        self.MovieBtn["text"] = "Find Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side = tk.LEFT)

#============Labels for Movie Info==============#   
        
        #Title of the Movie
        #Label
        self.title = tk.Label(TitleFrame, padx=3, pady=3)
        self.title.pack(side = tk.LEFT)
        self.title["text"] = "Title:"
        #Variable
        self.MovieTitle = tk.Label(TitleFrame, padx=3, pady=3)
        self.MovieTitle.pack()
        self.MovieTitle["textvariable"] = self.LabelDefault
        
        #Year the Movie was Released
        #Label
        self.year = tk.Label(YearFrame, padx=3, pady=3)
        self.year.pack(side = tk.LEFT)
        self.year["text"] = "Year:"
        #Variable
        self.MovieYear = tk.Label(YearFrame, padx=3, pady=3)
        self.MovieYear.pack()
        self.MovieYear["textvariable"] = self.LabelDefault
        
        #The Director of the Movie
        #Label
        self.director = tk.Label(DirectorFrame, padx=3, pady=3)
        self.director.pack(side = tk.LEFT)
        self.director["text"] = "Director:"
        #Variable
        self.MovieDirector = tk.Label(DirectorFrame, padx=3, pady=3)
        self.MovieDirector.pack()
        self.MovieDirector["textvariable"] = self.LabelDefault
        
        #The Genre(s) of the Movie
        #Label
        self.genre = tk.Label(GenreFrame, padx=3, pady=3)
        self.genre.pack(side = tk.LEFT)
        self.genre["text"] = "Genre:"
        #Variable
        self.MovieGenre = tk.Label(GenreFrame, padx=3, pady=3)
        self.MovieGenre.pack()
        self.MovieGenre["textvariable"] = self.LabelDefault
        
#============Quit Button=========================#   
        
        self.quit = tk.Button(self.QuitFrame, text="QUIT", fg="red",
                              command=self.master.destroy, padx=3, pady=3)
        self.quit.pack()
 
#------------Movie Search Function---------------#
    
    def MovieSearch(self):
        
        #print(self.SearchContents.get())
        #response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        #print(response.content)
        #print(omdb.get(title=self.SearchContents.get()))
        
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
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
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
