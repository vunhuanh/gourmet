import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Frame for buying event tickets
class Reserve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)

        # Display
        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=0, column=4)
        
    # Display page contents
    def display(self, event):
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Make a reservation", wraplength=400)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT licensenb, restaurantname FROM restaurant ORDER BY restaurantname;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])

        # Print relevant info
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.ures = tk.Button(self, text="Reserve")
            self.ures.bind('<Button-1>', self.mkres)
            self.ures.grid(row=irow, column=2)

            i += 1 
            irow += 1

    def mkres(self, event):
        print "MakeReservation"

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
