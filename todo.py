"""

To do Application

Tkinter GUI Application Development
""" 

from Tkinter import *
import ttk
#import sqlite3


class ToDo:
    def __init__(self, master):

        fr = LabelFrame(master, text = 'Create New Task')
        fr.grid(row = 0, column=1, padx=8,pady=8, sticky='ew')

        self.tree = ttk.Treeview(height=5, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=W)
        self.tree.heading(2, text='Phone Number', anchor=W)

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
        self.combobox = ttk.Combobox(fr, values = [u"none",u"Low",u"Medium",u"High",u"Critical"],height=5)
        self.combobox.set(u"none")
        self.combobox.grid(row=2, column=3, sticky=W, padx=5, pady=2)

        #Add task button
        ttk.Button(fr, text = 'Add task').grid(row=2, column=4, sticky=E,padx=5, pady=2)
    
root = Tk()
application = ToDo(root)
root.mainloop()
