#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import attributeSpecifierWidget

class AlternativeSpecifier():

    @staticmethod
    def run(data):
        data.rows = int(data.stringInput2)
        data.cols = int(data.stringInput3)

        def keyPressed(event, data, top):
            if len(data.alternative) == data.rows:
                top.destroy()
                attributeSpecifierWidget.AttributeSpecifier().run(data)

        def store(e, data):
            data.alternative.append(e.widget.get())

        top = Toplevel()
        top.title("Please Enter Alternatives.")
        top.geometry("500x300+300+0")
        top.bind("<Key>", lambda event:
            keyPressed(event, data, top))
        Label(top, text = "\n",font = "Helvetica 15").grid(row = 0, columnspan = 2, column = 1, sticky = W)
        Label(top, text = " We Would Love to Know What Alternatives You Have in Mind.",font = "Helvetica 15").grid(row = 2, columnspan = 2, column = 1, sticky = W)
        Label(top, text = " Please Use A Capitalized Letter to Represent The Options. ",font = "Helvetica 15").grid(row = 3, columnspan = 2,column = 1, sticky = W)
        Label(top, text = "\n",font = "Helvetica 15").grid(row = 3, columnspan = 2,column = 1, sticky = W)
        
        for i in range(data.rows):
            Label(top, text = "Alternative %s" % str(i+1),font = "Helvetica 13").grid(row = i+7, column = 1)
            b = Entry(top, text = "", width = 20)
            b.grid(row = i+7, column = 2)
            b.bind("<Return>", lambda e: store(e, data))

