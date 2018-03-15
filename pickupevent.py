import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData


# Frame for making pickups
class Pickup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Restaurants available for food pickup", wraplength=400)
        self.desc.grid(row=1, column=1)

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT r.licensenb, r.restaurantname FROM food_menu f, restaurant r WHERE f.licensenb = r.licensenb;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
        
        irow = 3
        i = 0
        for r in restau:
            self.vmenu = tk.Button(self, text="View menu")
            self.vmenu.bind('<Button-1>', lambda event, arg=licensenb[i]: self.menu(event, arg))
            self.vmenu.grid(row=irow, column=0)

            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  

            i += 1 
            irow += 1

    # Go to menu page
    def menu(self, event, arg):
        print(arg)

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for buying event tickets
class Event(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Restaurants that are hosting events soon", wraplength=400)
        self.desc.grid(row=1, column=1)

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT licensenb, restaurantname, eventname, eventdate, eventprice FROM upcomingevents;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        event = []
        date = []
        price = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
            event.append(r[2])
            date.append(r[3])
            price.append(r[4])

        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)
        self.event = tk.Label(self, text="Event")
        self.event.grid(row=3, column=2)
        self.date = tk.Label(self, text="Date")
        self.date.grid(row=3, column=3)
        self.price = tk.Label(self, text="Price (CAD)")
        self.price.grid(row=3, column=4)

        irow = 4
        i = 0
        for r in restau:
            self.tic = tk.Button(self, text="Buy tickets")
            self.tic.bind('<Button-1>', self.ticket)
            self.tic.grid(row=irow, column=0)

            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.event = tk.Label(self, text=event[i])
            self.event.grid(row=irow, column=2)
            self.date = tk.Label(self, text=date[i])
            self.date.grid(row=irow, column=3)
            self.price = tk.Label(self, text=price[i])
            self.price.grid(row=irow, column=4)
            
            i += 1 
            irow += 1

    # Go to menu page
    def ticket(self, event):
        print "ticket"

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")


