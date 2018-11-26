from tkinter import *
import userInputWidget
import gridMakerWidget

class Topsis():

    @staticmethod
    def initTopsis(data):
        pass
    
    @staticmethod
    def loadPrompt(data):
        pass

    @staticmethod
    def loadInputBox(data):
        pass

    @staticmethod
    def loadDoneButton(data):
        pass

    @staticmethod
    def mousePressed(event, data):
        data.mouseSelection = (event.x, event.y)
        pass

    @staticmethod
    def mouseTracker(event, data):
        data.mouseMotion = (event.x, event.y)

    @staticmethod   
    def keyPressed(event, data):
        pass

    @staticmethod
    def drawFieldInput(canvas, data):
        pass
        

    @staticmethod
    def drawPrompt(canvas, data):
        pass

    @staticmethod
    def drawDoneButton(canvas, data, mouseX, mouseY):
        pass

    @staticmethod
    def drawInputBox(canvas, data, mouseX, mouseY):
        pass

    @staticmethod
    def drawUserInputBG(canvas, data):
        pass

    @staticmethod
    def redrawAll(canvas, data):
        canvas.create_rectangle(0,0,data.width, data.height, fill = "black")


    @staticmethod
    def timerFired(data):
        pass
    
    @staticmethod
    def run(data):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            Topsis.redrawAll(canvas, data)
            canvas.update()    

        def timerFiredWrapper(canvas, data):
            Topsis.timerFired(data)
            redrawAllWrapper(canvas, data)
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
        def mousePressedWrapper(event, canvas, data):
            Topsis.mousePressed(event, data)
            redrawAllWrapper(canvas, data)

        def mouseTrackerWrapper(event, data):
            Topsis.mouseTracker(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            Topsis.keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        
        top = Toplevel()
        top.title("TOPSIS")
        top.geometry("1200x800+100+0")
        Topsis.initTopsis(data)
        data.mouseMotion = (-1, -1)
        data.mouseSelection = (-1, -1)
        canvas = Canvas(top, width=data.width, height=data.height)
        canvas.configure(bd=0, highlightthickness=0)
        canvas.pack()
        top.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
        top.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
        top.bind("<Motion>", lambda event:
                            mouseTrackerWrapper(event, data))  
        timerFiredWrapper(canvas, data)
