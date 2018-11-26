#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import topsis
import weightSumWidget

class GridLayer():

    @staticmethod
    def run(data):

        def keyPressed(event, data, top):
            if len(data.entryStorage) == data.rows * data.cols:
                top.destroy()
                # topsis.Topsis().run(data)
                weightSumWidget.WeightSumMaker().run(data)

        def store(e, storageList):
            storageList.append(e.widget.get())

        top = Toplevel()
        top.title("GridMaker")
        top.bind("<Key>", lambda event:
                    keyPressed(event, data, top))
        data.cols = int(data.stringInput2)
        data.rows = int(data.stringInput3)
        entries = []
        for i in range(1, data.rows+1):
            Label(top, text = str(i)).grid(row = i)
        for j in range(1, data.cols+1):
            Label(top, text = str(j)).grid(row = 0, column = j)
        for i in range(data.rows): 
            newrow = []
            for j in range(data.cols): 
                b = Entry(top, text="",width=15)
                b.grid(row=i+1, column=j+1)
                b.bind("<Return>", lambda e: store(e, data.entryStorage))
                newrow.append(b)
            entries.append(newrow)


