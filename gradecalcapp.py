from tkinter import *
from tkinter import ttk

class GradeCalculator:
    def __init__(self, root):
        root.geometry('500x500')
        root.title("Grade Calculator")

        content = ttk.Frame(root, padding=(3,3,12,12))
        mainframe = ttk.Frame(content)
        content.grid(column=0, row=0, sticky=(N, S, E, W))
        mainframe.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Labels
        assignlabel = ttk.Label(content, text= "Grade Category")
        percentlabel = ttk.Label(content, text= "Grade (%)")
        weightlabel = ttk.Label(content, text= "Weight")
        gradelabel = ttk.Label(content, text="Final Grade:")
        gradelabel = ttk.Label(content, text="Final Grade:")
        gradedisplaylabel = ttk.Label(content, text="")

        # Assigning widgets to a grid
        assignlabel.grid(column=0, row=0)
        percentlabel.grid(column=1, row=0)
        weightlabel.grid(column=2, row=0)
        gradelabel.grid(column=1, row=7)
        gradedisplaylabel.grid(column=1, row=8)

        ae1 = StringVar()
        ae2 = StringVar()
        ae3 = StringVar()

        pe1 = StringVar()
        pe2 = StringVar()
        pe3 = StringVar()

        we1 = StringVar()
        we2 = StringVar()
        we3 = StringVar()

        def calc():
            sum = (float(we1.get()) * float(pe1.get()) / 100) + (float(we2.get()) * float(pe2.get()) / 100) + (float(we3.get()) * float(pe3.get()) / 100)
            # Use get to get the string value from the StringVar class that the entries have, and then use float to convert to a double.
            letterGrade(sum)

        def letterGrade(finalgrade):
            letter = ""
            if(0 <= finalgrade < 60):
                letter = "F"
            elif(60 <= finalgrade < 70):
                letter = "D"
            elif(70 <= finalgrade < 80):
                letter = "C"
            elif(80 <= finalgrade < 90):
                letter = "B"
            elif(90 <= finalgrade <= 100):
                letter = "A"
            gradedisplaylabel.config(text=str(finalgrade)+ " " + letter)

        # Entries, set up like this for testing. These would at least be the base entries available on launch.
        assignentry1 = ttk.Entry(content, textvariable= ae1)
        assignentry2 = ttk.Entry(content, textvariable= ae2)
        assignentry3 = ttk.Entry(content, textvariable= ae3)

        percententry1 = ttk.Entry(content, textvariable= pe1)
        percententry2 = ttk.Entry(content, textvariable= pe2)
        percententry3 = ttk.Entry(content, textvariable= pe3)

        weightentry1 = ttk.Entry(content, textvariable= we1)
        weightentry2 = ttk.Entry(content, textvariable= we2)
        weightentry3 = ttk.Entry(content, textvariable= we3)

        assignentry1.grid(column=0, row=1)
        assignentry2.grid(column=0, row=2)
        assignentry3.grid(column=0, row=3)

        percententry1.grid(column=1, row=1)
        percententry2.grid(column=1, row=2)
        percententry3.grid(column=1, row=3)

        weightentry1.grid(column=2, row=1)
        weightentry2.grid(column=2, row=2)
        weightentry3.grid(column=2, row=3)

        # Buttons
        calcButton = ttk.Button(content, text="Calculate", command=calc)
        calcButton.grid(column=1, row=6)

        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.rowconfigure(0, pad=25) # Label row space
        content.rowconfigure(1, pad=10) # Entry row 1 space
        content.rowconfigure(2, pad=10) # Entry row 2 space
        content.rowconfigure(3, pad=10) # Entry row 3 space
        content.rowconfigure(6, pad=50) # Calculate button space

root = Tk()
GradeCalculator(root)
root.mainloop()