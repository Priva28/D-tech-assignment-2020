from tkinter import *
from tkinter import ttk
from tkinter import messagebox


'''
    D-Tech Assignment Task 2
    Manipulating Numbers
    Christian P

    All you need to do is enter 2 numbers.
    Go to the bottom of the page to choose a cli or a gui.
'''


def cli_version():
    # Get 2 numbers
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    try:
        total = int(num1) + int(num2)  # Add them together
        average = total / 2  # Calculate the average

        # Print the results
        print("Total: " + str(total))
        print("Average: " + str(average))
    except:
        print("Error calculating, enter 2 valid integers.")
        cli_version()


def gui_version():
    root = Tk()
    root.geometry("500x150")
    root.title("Total / Average Calculator")

    def num_changed(name='', index='', mode=''):
        if num1_entry.get() != "" and num2_entry.get() != "":
            try:
                total = int(num1_entry.get()) + int(num2_entry.get())
                avg = total / 2
                total_label.config(text="Total: " + str(total))
                avg_label.config(text="Average: " + str(avg))
            except:
                messagebox.showerror(title="Error!", message="There was an error calculating. "
                                                             "Make sure that you enter a valid number.")
                total_label.config(text="Total: ")
                avg_label.config(text="Average: ")
                num1_entry.delete(0, "end")
                num2_entry.delete(0, "end")

    # StringVars (They are used so we can call a function when it changes.)
    num1 = StringVar()
    num1.trace_add("write", num_changed)
    num2 = StringVar()
    num2.trace_add("write", num_changed)

    # Labels
    total_label = ttk.Label(text="Total: ", font=("default", 30, "bold"))
    avg_label = ttk.Label(text="Average: ", font=("default", 30, "bold"))

    # Entry Labels
    num1_entry_label = ttk.Label(text="Number 1: ")
    num2_entry_label = ttk.Label(text="Number 2: ")

    # Entries
    num1_entry = ttk.Entry(root, width=30, textvariable=num1)
    num2_entry = ttk.Entry(root, width=30, textvariable=num2)

    # Grid System
    total_label.grid(sticky="w", row=0, column=0)
    avg_label.grid(sticky="w", row=1, column=0)

    num1_entry_label.grid(sticky="w", row=2, column=0)
    num2_entry_label.grid(sticky="w", row=3, column=0)

    num1_entry.grid(sticky="w", row=2, column=0, padx=80)
    num2_entry.grid(sticky="w", row=3, column=0, padx=80)

    root.mainloop()

# Choose your version, gui or cli
# cli_version()
gui_version()