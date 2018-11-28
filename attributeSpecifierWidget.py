#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import gridMakerWidget

class AttributeSpecifier():

    @staticmethod
    def run(data):

        def keyPressed(event, data, top):
            if len(data.attribute) == data.cols:
                top.destroy()
                gridMakerWidget.GridLayer().run(data)

        def store(e, data):
            data.attribute.append(e.widget.get())

        top = Toplevel()
        top.title("Please Enter Attributes.")
        top.geometry("500x500+300+0")
        top.bind("<Key>", lambda event:
            keyPressed(event, data, top))
        Label(top, text = "\n",font = "Helvetica 15").grid(row = 0, columnspan = 2,column = 1, sticky = W)
        Label(top, text = " We Would Love to Know What Attributes You Have in Mind.").grid(row = 1, columnspan = 2, sticky = W)
        Label(top, text = " Please Enter Consider Quantitative Attributes Only.").grid(row = 2, columnspan = 2, sticky = W)
        Label(top, text = "\n",font = "Helvetica 15").grid(row = 3, columnspan = 2,column = 1, sticky = W)

        for i in range(data.cols):
            Label(top, text = "Attribute %s" % str(i+1) ).grid(row = i+5, column = 0)
            b = Entry(top, text = "", width = 20)
            b.grid(row = i+5, column = 1)
            b.bind("<Return>", lambda e: store(e, data))

