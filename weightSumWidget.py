#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import topsis

class WeightSumMaker():

    @staticmethod
    def run(data):

        def keyPressed(event, data, top):
            if len(data.weight) == data.cols:
                top.destroy()
                topsis.Topsis().run(data)

        def store(e, weightList):
            weightList.append(e.widget.get())

        top = Toplevel()
        top.title("Weighted Sum")
        top.bind("<Key>", lambda event:
            keyPressed(event, data, top))

        for i in range(len(data.attribute)):
            Label(top, text = "How Much Weight Would You Like to Assign to %s" % data.attribute[i]).grid(row = i, column = 0)
            b = Entry(top, text = "", width = 10)
            b.grid(row = i, column = 1)
            b.bind("<Return>", lambda e: store(e, data.weight))


            
