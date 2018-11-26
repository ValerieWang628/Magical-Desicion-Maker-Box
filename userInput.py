from tkinter import *
import userInputWidget
import gridMakerWidget

class UserInput():

    @staticmethod
    def initUserInput(data):
        data.hintButton = userInputWidget.HintButton()
        data.decisionPrompt = []
        UserInput.loadPrompt(data)
        data.inputBox = []
        UserInput.loadInputBox(data)

        data.doneButton = []
        UserInput.loadDoneButton(data)
        data.stringInput1 = ""
        data.stringInput2 = ""
        data.stringInput3 = ""
        data.done1Pressed = False
        data.done2Pressed = False
        data.done3Pressed = False
    
    @staticmethod
    def loadPrompt(data):
        whatDecisionPrompt = userInputWidget.QuestionPrompt("Hi %s, What Decision Are You Making Today?" % data.userName, data.width//2, 200, 30)
        data.decisionPrompt.append(whatDecisionPrompt)
        howManyAlternativesPrompt = userInputWidget.QuestionPrompt("How Many Alternatives Do You Have?", data.width//2, 400, 30)
        data.decisionPrompt.append(howManyAlternativesPrompt)
        howManyAttributesPrompt = userInputWidget.QuestionPrompt("How Many Attributes Do You Care About?", data.width//2, 600, 30)
        data.decisionPrompt.append(howManyAttributesPrompt)

    @staticmethod
    def loadInputBox(data):
        data.decisionInput = userInputWidget.InputBox(data.width//2, 300, 600, 50)
        data.inputBox.append(data.decisionInput)
        data.optionInput = userInputWidget.InputBox(data.width//2, 500, 100, 50)
        data.inputBox.append(data.optionInput)
        data.attributeInput = userInputWidget.InputBox(data.width//2, 700, 100, 50)
        data.inputBox.append(data.attributeInput)

    @staticmethod
    def loadDoneButton(data):
        data.done1 = userInputWidget.DoneButton(900, 300, 50, 50)
        data.doneButton.append(data.done1)
        data.done2 = userInputWidget.DoneButton(700, 500, 50, 50)
        data.doneButton.append(data.done2)
        data.done3 = userInputWidget.DoneButton(700, 700, 50, 50)
        data.doneButton.append(data.done3)

    @staticmethod
    def mousePressed(event, data, top):
        data.mouseSelection = (event.x, event.y)
        if (event.x >= data.done1.vertexNW[0]
            and event.x <= data.done1.vertexSE[0]
            and event.y >= data.done1.vertexNW[1]
            and event.y <= data.done1.vertexSE[1]):
            data.done1Pressed = True
        elif (event.x >= data.done2.vertexNW[0]
            and event.x <= data.done2.vertexSE[0]
            and event.y >= data.done2.vertexNW[1]
            and event.y <= data.done2.vertexSE[1]):
            data.done2Pressed = True
        elif (event.x >= data.done3.vertexNW[0]
            and event.x <= data.done3.vertexSE[0]
            and event.y >= data.done3.vertexNW[1]
            and event.y <= data.done3.vertexSE[1]):
            data.done3Pressed = True
        if (data.done1Pressed
            and data.done2Pressed
            and data.done3Pressed):
            top.destroy()
            gridMakerWidget.GridLayer().run(data)

    @staticmethod
    def mouseTracker(event, data):
        data.mouseMotion = (event.x, event.y)

    @staticmethod   
    def keyPressed(event, data):
        if (not data.done1Pressed
            and not data.done2Pressed
            and not data.done3Pressed):
            if (event.keysym == "BackSpace" 
                and data.stringInput1 != ""):
                data.stringInput1 = data.stringInput1[:-1]
            data.stringInput1 += event.char
        elif (data.done1Pressed 
            and not data.done2Pressed
            and not data.done3Pressed):
            if (event.keysym == "BackSpace" 
                and data.stringInput2 != ""):
                data.stringInput2 = data.stringInput2[:-1]
            data.stringInput2 += event.char
        elif (data.done1Pressed
            and data.done2Pressed
            and not data.done3Pressed):
            if (event.keysym == "BackSpace" 
                and data.stringInput1 != ""):
                data.stringInput3 = data.stringInput3[:-1]
            data.stringInput3 += event.char

    @staticmethod
    def drawFieldInput(canvas, data):
        canvas.create_text(data.decisionInput.cx, data.decisionInput.cy, text = data.stringInput1, font = "Helvetica 20 bold", fill = "black")
        canvas.create_text(data.optionInput.cx, data.optionInput.cy, text = data.stringInput2, font = "Helvetica 20 bold", fill = "black")
        canvas.create_text(data.attributeInput.cx, data.attributeInput.cy, text = data.stringInput3, font = "Helvetica 20 bold", fill = "black")
        

    @staticmethod
    def drawPrompt(canvas, data):
        for prompt in data.decisionPrompt:
            prompt.draw(canvas)

    @staticmethod
    def drawDoneButton(canvas, data, mouseX, mouseY):
        for done in data.doneButton:
            done.draw(canvas, mouseX, mouseY)

    @staticmethod
    def drawInputBox(canvas, data, mouseX, mouseY):
        for box in data.inputBox:
            box.draw(canvas, mouseX, mouseY)

    @staticmethod
    def drawUserInputBG(canvas, data):
        canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

    @staticmethod
    def redrawAll(canvas, data):
        UserInput.drawUserInputBG(canvas, data)
        mouseMotionX, mouseMotionY = data.mouseMotion
        data.hintButton.draw(data, canvas, mouseMotionX, mouseMotionY)
        UserInput.drawPrompt(canvas, data)
        UserInput.drawInputBox(canvas, data, mouseMotionX, mouseMotionY)
        UserInput.drawDoneButton(canvas, data, mouseMotionX, mouseMotionY)
        UserInput.drawFieldInput(canvas, data)


    @staticmethod
    def timerFired(data):
        pass
    
    @staticmethod
    def run(data):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            UserInput.redrawAll(canvas, data)
            canvas.update()    

        def timerFiredWrapper(canvas, data):
            UserInput.timerFired(data)
            redrawAllWrapper(canvas, data)
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
        def mousePressedWrapper(event, canvas, data, top):
            UserInput.mousePressed(event, data, top)
            redrawAllWrapper(canvas, data)

        def mouseTrackerWrapper(event, data):
            UserInput.mouseTracker(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            UserInput.keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        
        top = Toplevel()
        top.title("User Input")
        top.geometry("1200x800+100+0")
        UserInput.initUserInput(data)
        data.mouseMotion = (-1, -1)
        data.mouseSelection = (-1, -1)
        data.entryStorage = []
        data.attribute = ['ph_a','ph_b']
        data.alternative = ['ph1', 'ph2', 'ph3']
        data.weight = []
        canvas = Canvas(top, width=data.width, height=data.height)
        canvas.configure(bd=0, highlightthickness=0)
        canvas.pack()
        top.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data, top))
        top.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
        top.bind("<Motion>", lambda event:
                            mouseTrackerWrapper(event, data))  
        timerFiredWrapper(canvas, data)
