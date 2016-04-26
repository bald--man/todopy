"""

To do Application

Tkinter GUI Application Development
""" 

from Tkinter import *
import ttk
import sqlite3


class ToDo:
    def __init__(self, master):

        fr = LabelFrame(master, text = 'Create New Task')
        fr.grid(row = 0, column=1, padx=8,pady=8, sticky='ew')

        #Add task field
        Label(fr, text='Task:').grid(row=1, column=1, sticky=W, pady=2)
        self.name = StringVar()
        self.namefield = Entry(fr, textvariable = self.name)
        self.namefield.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        #Add due date field
        Label(fr, text='Due Date:').grid(row=1, column=2, sticky=W, pady=2)
        self.name = StringVar()
        self.namefield = Entry(fr, textvariable = self.name)
        self.namefield.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        #Add priority field
        Label(fr, text='Priority:').grid(row=1, column=3, sticky=W, pady=2)
        self.name = StringVar()
        self.namefield = Entry(fr, textvariable = self.name)
        self.namefield.grid(row=2, column=3, sticky=W, padx=5, pady=2)
        #Add task button
        ttk.Button(fr, text = 'Add task').grid(row=2, column=4, sticky=E,padx=5, pady=2)
    
    
root = Tk()
application = ToDo(root)
root.mainloop()