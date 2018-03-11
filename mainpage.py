import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Frame for main page
class Mainpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside mainpage
    def create_widgets(self):
        # Set width to column 0
        self.grid_columnconfigure(0, minsize=100)
        
        # Header
        self.title = tk.Label(self, text="GOURMET")
        self.title.grid(row=0, column=1)
        self.desc = tk.Label(self, text="Gourmet is an application which lets you reserve tables in our partnered restaurants, as well as buy event tickets and food.\n\n", wraplength=500)
        self.desc.grid(row=1, column=1, sticky=tk.E)

        # Buttons
        self.signup_btn = tk.Button(self, text="Sign up")
        self.signup_btn.bind('<Button-1>', self.signup)
        self.signup_btn.grid(row=2, column=1, sticky=tk.W)

        self.login_btn = tk.Button(self, text="Log in")
        self.login_btn.bind('<Button-1>', self.login)
        self.login_btn.grid(row=2, column=1, sticky=tk.E)

        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=3, column=1)

    # Signup
    def signup(self, event):
        hp = signup.display(self)

    # Login
    def login(self, event):
        hp = login.display(self)
        # Once logged in, display the homepage.py frame

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("homepage")
        