#============Importing the APIs==================#
import requests
response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")

import omdb
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
        
        self.SearchFrame = tk.Frame()
        self.SearchFrame.pack(side = tk.TOP)
        
        self.InfoFrame = tk.Frame()
        self.InfoFrame.pack()
        
        TitleFrame = tk.Frame(self.InfoFrame)
        TitleFrame.pack()
        
        YearFrame = tk.Frame(self.InfoFrame)
        YearFrame.pack()
        
        DirectorFrame = tk.Frame(self.InfoFrame)
        DirectorFrame.pack()
        
        GenreFrame = tk.Frame(self.InfoFrame)
        GenreFrame.pack()
        
        self.QuitFrame = tk.Frame()
        self.QuitFrame.pack(side = tk.BOTTOM)

#============Default Declarations===============#   
        
        self.LabelDefault = "--"
        
#============Search Widget======================#   
        
        self.Search = tk.Entry(self.SearchFrame)
        self.Search.pack(side = tk.RIGHT, fill=tk.X)
        self.SearchContents = tk.StringVar()
        self.SearchContents.set("Arrival")         
        # tell the entry widget to watch this variable
        self.Search["textvariable"] = self.SearchContents
        self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self.SearchFrame, padx=3, pady=3)
        self.MovieBtn["text"] = "Find a Random Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side = tk.LEFT)

#============Labels for Movie Info==============#   
        
        self.title = tk.Label(TitleFrame, padx=3, pady=3)
        self.title.pack(side = tk.LEFT)
        self.title["text"] = "Title:"
        
        self.MovieTitle = tk.Label(TitleFrame, padx=3, pady=3)
        self.MovieTitle.pack()
        self.MovieTitle["textvariable"] = self.LabelDefault
        
        self.year = tk.Label(YearFrame, padx=3, pady=3)
        self.year.pack(side = tk.LEFT)
        self.year["text"] = "Year:"
        
        self.MovieYear = tk.Label(YearFrame, padx=3, pady=3)
        self.MovieYear.pack()
        
        self.MovieYear["textvariable"] = self.LabelDefault
        
        self.director = tk.Label(DirectorFrame, padx=3, pady=3)
        self.director.pack(side = tk.LEFT)
        self.director["text"] = "Director:"
        
        self.MovieDirector = tk.Label(DirectorFrame, padx=3, pady=3)
        self.MovieDirector.pack()
        
        self.MovieDirector["textvariable"] = self.LabelDefault
        
        self.genre = tk.Label(GenreFrame, padx=3, pady=3)
        self.genre.pack(side = tk.LEFT)
        self.genre["text"] = "Genre:"
        
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
        
        print(omdb.get(title=self.SearchContents.get()))
        
        
        #self.TitleLabel

root = tk.Tk()
app = Application(master=root)
app.mainloop()
