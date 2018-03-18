import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

inp = None

# Frame for upcoming user reservations
class AllReviews(tk.Frame):

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
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)
        self.desc = tk.Label(self, text="You have upcoming reservations from the following restaurants:", wraplength=300)
        self.desc.grid(row=1, column=1)

        # Get restaurant license number from session variable?? dynamic??
        licensenumber = "mgao8505"
        
        # Connect to DB and select user's points
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT reviewdate, rating, comment FROM review WHERE licensenb='{0}';".format(licensenumber)
        result_set = conn.execute(query)  
        conn.close()

        #Putting all data from review table to arrays date, rating and comment
        date = []
        rating = []
        comment = []
        for r in result_set:
            date.append(r[0])
            rating.append(r[1])
            comment.append(r[2])

        #Print column names
        self.date = tk.Label(self, text="Date")
        self.date.grid(row=3, column=0)
        self.rating = tk.Label(self, text="Rating")
        self.rating.grid(row=3, column=1)
        self.comment = tk.Label(self, text="Comment")
        self.comment.grid(row=3, column=2)

        #Display data put in arrays date, rating and comment
        irow = 4
        i = 0
        for r in date:
            self.date = tk.Label(self, text=date[i])
            self.date.grid(row=irow, column=0)
            self.rating = tk.Label(self, text=rating[i])
            self.rating.grid(row=irow, column=1)
            self.comment = tk.Label(self, text=comment[i], wraplength = 300)
            self.comment.grid(row=irow, column=2)

            i += 1
            irow += 1

    #Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for upcoming user reservations
class MakeReview(tk.Frame):

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
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.intro = tk.Label(self, text="Write your comment here: ")
        self.intro.grid(row=0, column=1)
        
        self.text = tk.Text(self, borderwidth=3)
        self.text.grid(row=1, column=1)
        
        self.button = tk.Button(self, text="Submit comment", command=self.on_button)
        self.button.grid(row=2, column=2)


    def on_button(self):
        
        lines = self.text.get("1.0", tk.END).splitlines()
        stringComment = ""
        for line in lines:
            stringComment += line
            stringComment += " "

        print stringComment

        # Get restaurant license number from session variable?? dynamic??
        useremail = ''
        licensenumber = "mgao8505"
        

         # Connect to DB and select user's points
        db = DBconnection.connecting()
        conn = db.connect()
        cursor = db.cursor()
        query = "".format(licensenumber)
        cursor.execute(query)

        db.commit()
        conn.close()
            
            
        

    #Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
        
    
