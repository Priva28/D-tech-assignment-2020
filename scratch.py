from typing import Any

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep

'''
    D-Tech Assignment Task 3
    Decisions
    Christian P

    Enter the highest possible mark and a mark. 
    The percentage will be output and satisfactory if above 50% or unsatisfactory if below.
    Go to the bottom of the page to choose a cli or a gui.
'''


def cli_version():
    possible_marks = input("Highest possible mark: ")
    mark = input("Mark: ")

    try:
        mark_pct = (int(mark) / int(possible_marks)) * 100

        if mark_pct > 50:
            print(str(mark_pct) + "% is a satisfactory mark. PASS")
        else:
            print(str(mark_pct) + "% is an unsatisfactory mark. FAIL")
    except:
        print("Error input valid integers.")
        cli_version()



root = Tk()
root.geometry("1x1")
root.title("Mark Calculator")

num = 1

def button():
    global num

    if num < 400:
        root.geometry("{num}x{num}".format(num = num))
        num = num + 30
        print(num)
        root.after(1, button)

root.after(0, button)
root.mainloop()