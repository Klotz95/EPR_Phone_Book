""" This module contains the UI of phonebook

"""

__author__ = "6345060: Nico Kotlenga"
__copyright__ = "Copyright 2016 – EPR-Goethe-Uni"
__email__ = "nico.kotlenga@stud.uni-frankfurt.de"

import tkinter as tk
import IO
import logic
from tkinter import filedialog
class Application(tk.Frame):
    """ This class contains methods to generate the UI

    """
    def __init__(self, master = None):
        """ This method will be called during the initialisation

        """

        tk.Frame.__init__(self, master)
        self.grid()
        self.phone_book = logic.PhoneBook(None)
        self.create_Components()
    def create_Components(self):
        """This method draws the components to the view

        """
        # buttons

        self.first_name_button = tk.Button(self, text = "first name")
        self.last_name_button = tk.Button(self, text = "last name")
        self.city_button = tk.Button(self, text= "city")
        self.zip_button = tk.Button(self, text = "zip code")
        self.street_button = tk.Button(self, text = "street")
        self.phone_button = tk.Button(self, text = "phone")

        self.first_name_button.grid(column = 0 , row = 0)
        self.last_name_button.grid(column = 1, row = 0)
        self.city_button.grid(column = 2 , row = 0)
        self.zip_button.grid(column = 3, row = 0)
        self.street_button.grid(column = 4, row = 0)
        self.phone_button.grid(column = 5, row = 0)

        # listboxs

        self.first_name_list = tk.Listbox(self)
        self.last_name_list = tk.Listbox(self, state = "disabled")
        self.city_list = tk.Listbox(self, state = "disabled")
        self.zip_list = tk.Listbox(self , state = "disabled")
        self.street_list = tk.Listbox(self, state = "disabled")
        self.phone_list = tk.Listbox(self, state = "disabled")

        self.first_name_list.grid(column = 0, row = 1)
        self.last_name_list.grid(column = 1, row = 1)
        self.city_list.grid(column = 2, row = 1)
        self.zip_list.grid(column = 3, row = 1)
        self.street_list.grid(column = 4, row = 1)
        self.phone_list.grid(column = 5, row = 1)

        # control elements

        self.edit_button = tk.Button(self, text = "edit", state = "disabled")
        self.add_button = tk.Button(self, text = "new", command = \
        lambda: self.create_new_entry())
        self.save_button = tk.Button(self, text = "save", command = \
        lambda: self.save_file())
        self.load_button = tk.Button(self, text = "load", command = \
        lambda: self.load_file())
        self.search_button = tk.Button(self, text = "search")
        self.clear_button = tk.Button(self, text= "clear")
        self.search_field = tk.Entry(self)
        self.delete_button = tk.Button(self, text ="delete", state = "disabled")

        self.edit_button.grid(column = 1, row = 2)
        self.add_button.grid(column = 0, row = 2)
        self.save_button.grid(column = 0, row = 3)
        self.load_button.grid(column = 1, row = 3)
        self.delete_button.grid(column = 2, row = 2)
        self.search_field.grid(column = 3, row = 2, columnspan = 2)
        self.search_button.grid(column = 5, row = 2)
        self.clear_button.grid(column = 5, row = 3)
    def create_new_entry(self):
        # open the dialog
        dialog = tk.Toplevel(self)
        dialog.title("About this State:")
        first_name_label = tk.Label(dialog, text = "First Name: ")
        first_name_entry = tk.Entry(dialog)
        first_name_label.grid(column = 0, row = 0)
        first_name_entry.grid(column = 1, row = 0)

    def load_file(self):
        """ This method will open a file dialog and load the content of the
            selected file

        """
        path = filedialog.askopenfilename()
        cur_manager = IO.FileManager()
        cur_entries = cur_manager.load(path)
        self.phone_book = logic.PhoneBook(cur_entries)
    def save_file(self):
        """This method will opene a file dialog and save the phonebook in the
           given position
        """
        path = filedialog.asksaveasfilename()
        cur_manager = IO.FileManager()
        cur_manager.save(path, self.phone_book.phonebook)

app = Application()
app.master.title = "EPR Phonebook"
app.mainloop()
