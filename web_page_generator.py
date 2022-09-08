import tkinter as tk
from tkinter import *
import webbrowser
import tkinter.simpledialog




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web page Generator")
        self.btn=Button(self.master, text="Default HTML Page", width=30, height=2, command = self.defaultHTML)
        self.btn.grid(row= 1, column= 0,padx=(10,10), pady=(10,10))

        self.CustomText_btn = Button(text="Submit Custom Text", width=30,height=2, command=self.CustomText)
        self.CustomText_btn.grid(row = 1, column = 1, padx=(10,10), pady=(10,10))

        self.textEntry=Entry(self.master)
        self.textEntry.grid(row =0, column = 0,columnspan = 3, padx = (10,10), pady=(10,10))
        self.btn = Button(self.master, text="Enter Custom Text or click the Default HTML page button", width=70, command = self.defaultHTML)
        
                            
        

    def CustomText():
        CustomText= self.textEntry.get()
        htmlText= CustomText
        htmlFile=open("index.html","w")
        htmlContent="<html>\n<body>\n<h1>"+ htmlText+ "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        

     


    def defaultHTML(self):
        htmlText= "Hello and Thank you for Being too lazy to type anything :)!"
        htmlFile=open("index.html","w")
        htmlContent="<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()




































if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
    
