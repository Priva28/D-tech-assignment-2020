from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


'''
    D-Tech Assignment Task 1
    Manipulating Text
    Christian P
    
    All you need to do is enter your name and year of birth.
    Go to the bottom of the page to choose a cli or a gui.
'''


# First we will construct the algorithm with basic Python.
def cli_version():
    name = input("Enter your name: ")  # User will enter their name.
    year_of_birth = input("Enter your year of birth: ")  # User will enter their year of birth.

    current_year = date.today().year  # Get the current year.

    # Try, except lets us catch errors so the program doesnt crash.
    try:
        # Calculate how old the user will turn, or has turned this year.
        age_this_year = str(current_year - int(year_of_birth))

        # Now we print a message with their name and age.
        print("Hello {name}, this year, you will turn {age}".format(name=name, age=age_this_year))
    except:
        print("There was an error. Enter a valid year of birth!")
        cli_version()


# Now above code can be made into a GUI with Tkinter.
def gui_version():
    root = Tk()
    root.geometry("600x150")
    root.title("Age Calculator")

    # Do something when the name entry changes.
    def name_entry_changed(name='', index='', mode=''):
        if name_entry.get() != "":
            if year_entry.get() != "":
                try:
                    age_this_year = str(current_year - int(year_entry.get()))
                    main_label.config(text="Hello " + name_entry.get() + "! This year you will turn " + age_this_year)
                except:
                    messagebox.showerror(title="Error!", message="There was an error calculating your age. "
                                                                 "Make sure that you enter a valid year of birth.")
                    year_entry.delete(0, "end")
            else:
                main_label.config(text="Hello " + name_entry.get() + "! This year you will turn --.")
        else:
            main_label.config(text="Hello! This year you will turn --.")

        root.geometry("{labelwidth}x150".format(labelwidth=str(main_label.winfo_width() + 60)))

    # Do something when the year of birth entry changes.
    def year_entry_changed(name='', index='', mode=''):
        if year_entry.get() != "":
            try:
                age_this_year = str(current_year - int(year_entry.get()))
                if name_entry.get() != "":
                    main_label.config(text="Hello " + name_entry.get() + "! This year you will turn " + age_this_year)
                else:
                    main_label.config(text="Hello! This year you will turn " + age_this_year)
            except:
                messagebox.showerror(title="Error!", message="There was an error calculating your age. "
                                                             "Make sure that you enter a valid year of birth.")
                year_entry.delete(0, "end")
        else:
            if name_entry.get() != "":
                main_label.config(text="Hello " + name_entry.get() + "! This year you will turn --.")
            else:
                main_label.config(text="Hello! This year you will turn --.")

    current_year = date.today().year

    # StringVars (They are used so we can call a function when it changes.)
    name = StringVar()
    name.trace_add("write", name_entry_changed)
    year_of_birth = StringVar()
    year_of_birth.trace_add("write", year_entry_changed)

    # Labels
    main_label = ttk.Label(text="Hello! This year you will turn --.", font=("default", 30, "bold"))
    direction_label = ttk.Label(text="Please enter your name and year of birth:", font=("default", 20))

    # Entry Labels
    name_entry_label = ttk.Label(text="Name: ")
    year_entry_label = ttk.Label(text="Year of birth: ")

    # Entries
    name_entry = ttk.Entry(root, width=50, textvariable=name)
    year_entry = ttk.Entry(root, width=50, textvariable=year_of_birth)

    # Grid System
    main_label.grid(sticky="w", row=0, column=0)
    direction_label.grid(sticky="w", row=1, column=0)

    name_entry_label.grid(sticky="w", row=2, column=0)
    name_entry.grid(sticky="w", row=2, column=0, padx=50)

    year_entry_label.grid(sticky="w", row=3, column=0)
    year_entry.grid(sticky="w", row=3, column=0, padx=90)

    root.mainloop()


# Choose your version, gui or cli
# cli_version()
gui_version()
