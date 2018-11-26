#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *


class GridLayer():

    @staticmethod
    def run(data):
        top = Toplevel()
        top.title("GridMaker")
        col = int(data.stringInput2)
        row = int(data.stringInput3)
        entries = []
        for i in range(row): 
            newrow = []
            for j in range(col): 
                b = Entry(top, text="",width=8)
                b.grid(row=i, column=j)
                newrow.append(b)
            entries.append(newrow)
