#cited from https://stackoverflow.com/questions/44996633/accessing-entry-widget-created-using-for-loop
from tkinter import *
import topsis
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
        top.title("Alternative Specifier")
        top.bind("<Key>", lambda event:
            keyPressed(event, data, top))
        Label(top, text = "We Would Love to Know What Alternatives You Have in Mind.").grid(row = 0, columnspan = 2, sticky = W)
        Label(top, text = "Please Use A Capitalized Letter to Represent The Options. ").grid(row = 1, columnspan = 2, sticky = W)
        
        for i in range(data.rows):
            Label(top, text = "Alternative %s" % str(i+1)).grid(row = i+2, column = 0)
            b = Entry(top, text = "", width = 20)
            b.grid(row = i+2, column = 1)
            b.bind("<Return>", lambda e: store(e, data))

