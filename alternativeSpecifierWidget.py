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

        for i in range(data.rows):
            Label(top, text = "Alternative %s" % str(i+1)).grid(row = i, column = 0)
            b = Entry(top, text = "", width = 10)
            b.grid(row = i, column = 1)
            b.bind("<Return>", lambda e: store(e, data))
        print(data.alternative)

