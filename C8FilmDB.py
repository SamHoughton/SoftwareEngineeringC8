import requests
response = requests.get("http://www.omdbapi.com/?t=blade&apikey=3f3265e5")
#print(response.content)

#import omdb

#res = omdb.request(t='Lion King', y=1994, r='json')
#xml_content = res.content
#print(omdb.search(t='Lion King') )



import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        tk.geometry("500x500")
        
    def create_widgets(self):
        
        self.winfo_toplevel().title("Movie Information Client")
        
        self.Search = tk.Entry()
        self.Search.pack()
        self.SearchContents = tk.StringVar()
        
        # set it to some value
        self.SearchContents.set("Arrival")
        
        # tell the entry widget to watch this variable
        self.Search["textvariable"] = self.SearchContents
        self.Search.bind('<Key-Return>', self.MovieSearch)
        
        self.MovieBtn = tk.Button(self)
        self.MovieBtn["text"] = "Find a\n Random Movie"
        self.MovieBtn["command"] = self.MovieSearch
        self.MovieBtn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def MovieSearch(self):
        print(self.SearchContents.get())
        response = requests.get("http://www.omdbapi.com/?t=%s&apikey=3f3265e5" % (self.SearchContents.get()))
        print(response.content)
        print("")
        
        #self.TitleLabel
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
