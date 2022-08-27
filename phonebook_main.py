
#PhoneBook Demo. Demonstrating OOP, Tkinter GUI module,
#using Thinter parent and child relationships



from tkinter import *
import tkinter as tk


# be sure to import other modules
# so we can have access to them

import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration

        self.master = master
        self.master.minsize(500,300) #height and weight
        self.master.maxsize(500,300)
        # This CenterWindow method will center out app on the users screeen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter PhoneBook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda:phonebook_func.ask_quit(self))
        arg = self.master

        #load in GUI widget from a seperate module,
        #keeping your code comparmentalized and clutter free



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
