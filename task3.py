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

        if mark_pct >= 90:
            print(str(mark_pct) + "% is a satisfactory mark. A. PASS")
        elif mark_pct >=80 and mark_pct <= 89:
            print(str(mark_pct) + "% is a satisfactory mark. B. PASS")
        elif mark_pct >=70 and mark_pct <= 79:
            print(str(mark_pct) + "% is a satisfactory mark. C. PASS")
        elif mark_pct >=60 and mark_pct <= 69:
            print(str(mark_pct) + "% is a satisfactory mark. D. PASS")
        elif mark_pct >=0 and mark_pct <= 60:
            print(str(mark_pct) + "% is an unsatisfactory mark. F. FAIL")
        else:
            print("Error calculation mark. Retry:")
            cli_version()

    except:
        print("Error input valid integers.")
        cli_version()





num = 1

def gui_version():

    root = Tk()
    root.geometry("500x200")
    root.title("Mark Calculator")

    markWindow = Toplevel(root)
    markWindow.geometry("0x0")

    mark_label = Label(markWindow, text=".", font=("default", 100, "bold"))
    mark_label.pack()

    def animateView():
        global num

        try:
            mark_pct = (int(num1_entry.get()) / int(num2_entry.get())) * 100

            print(mark_pct)

            if mark_pct >= 90 and mark_pct <= 100:
                mark_label.config(text = "🏅 A 🏅")
            elif mark_pct >= 80 and mark_pct <= 89:
                mark_label.config(text = "🥈 B 🥈")
            elif mark_pct >= 70 and mark_pct <= 79:
                mark_label.config(text = "✅ C ✅")
            elif mark_pct >= 60 and mark_pct <= 69:
                mark_label.config(text = "🆗 D 🆗")
            elif mark_pct >= 0 and mark_pct <= 60:
                mark_label.config(text = "⛔ F ⛔")
            else:
                messagebox.showerror(title="Error!", message="There was an error calculating. "
                                                             "Make sure that you enter a valid number.")
                num1_entry.delete(0, "end")
                num2_entry.delete(0, "end")


            if num < 400:
                markWindow.geometry("{w}x{h}+600+600".format(w = num * 2, h = num))
                num = num + 10
                print(num)
                root.after(1, animateView)
        except:
            messagebox.showerror(title="Error!", message="There was an error calculating. "
                                                         "Make sure that you enter a valid number.")
            num1_entry.delete(0, "end")
            num2_entry.delete(0, "end")

    # Labels
    title_label = ttk.Label(text="Mark Calculator", font=("default", 30, "bold"))
    direction_label = ttk.Label(text="Enter your mark and the amount of possible marks.", font=("default", 20))

    # Entry Labels
    num1_entry_label = ttk.Label(text="Mark: ")
    num2_entry_label = ttk.Label(text="Out of: ")

    # Entries
    num1_entry = ttk.Entry(root, width=30)
    num2_entry = ttk.Entry(root, width=30)

    # Button
    enter_button = ttk.Button(root, text="Enter", command=animateView)

    title_label.grid(sticky="w", row = 0, column = 0)
    direction_label.grid(row = 1, column = 0)

    num1_entry_label.grid(sticky="w", row=2, column=0)
    num2_entry_label.grid(sticky="w", row=3, column=0)

    num1_entry.grid(sticky="w", row=2, column=0, padx=80)
    num2_entry.grid(sticky="w", row=3, column=0, padx=80)

    enter_button.grid(sticky="w", row=4, column=0, pady=20)

    root.mainloop()

gui_version()