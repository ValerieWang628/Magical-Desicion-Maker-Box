#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import topsis
import weightSumWidget
import gridMakerWidget

class AttributeSpecifier():

    @staticmethod
    def run(data):

        def keyPressed(event, data, top):
            if len(data.attribute) == data.cols:
                top.destroy()
                gridMakerWidget.GridLayer().run(data)
                # weightSumWidget.WeightSumMaker().run(data)


        def store(e, data):
            data.attribute.append(e.widget.get())

        top = Toplevel()
        top.title("Weighted Sum")
        top.bind("<Key>", lambda event:
            keyPressed(event, data, top))

        for i in range(data.cols):
            Label(top, text = "Attribute %s" % str(i+1) ).grid(row = i, column = 0)
            b = Entry(top, text = "", width = 10)
            b.grid(row = i, column = 1)
            b.bind("<Return>", lambda e: store(e, data))


            
