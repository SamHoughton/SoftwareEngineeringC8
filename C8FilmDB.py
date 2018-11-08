import requests
#response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")
#print(response.content)

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    

    def create_widgets(self):
        
        self.Search = tk.Entry()
        self.Search.pack()
        #self.SearchContents = StringVar()
        # set it to some value
        #self.SearchContents.set("Arrival")
        # tell the entry widget to watch this variable
        #self.Search["textvariable"] = self.SearchContents
        #self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self)
        self.MovieBtn["text"] = "Find a\n Random Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def MovieSearch(self):
        print(self.Search["textvariable"])
        #a = ["http://www.omdbapi.com/?t=" + (self.Search["textvariable"] + "&apikey=3f3265e5"
        #response = requests.get(a)
        #print(response.content)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
