from tkinter import *
import welcomeWidget
import userInput

def initWelcome(data):
    data.userName = ""
    data.startButton = welcomeWidget.StartButton("Start", data.width//2, 4 * data.height//5, 200, 80)
    data.prompt = []
    loadPrompt(data)

def loadPrompt(data):
    hiPrompt = welcomeWidget.GreetingPrompt("Hi.", data.width//2, data.height//5, 50)
    data.prompt.append(hiPrompt)
    welcomePrompt = welcomeWidget.GreetingPrompt("Welcome to The Magic Desicion Maker Box.", data.width//2, data.height//3, 30)
    data.prompt.append(welcomePrompt)
    namePrompt = welcomeWidget.GreetingPrompt("What is Your Name?", data.width//2, data.height//2, 30)
    data.prompt.append(namePrompt)


def mousePressed(event, data):
    data.mouseSelection = (event.x, event.y)
    if (event.x >= data.startButton.vertexNW[0]
        and event.x <= data.startButton.vertexSE[0]
        and event.y >= data.startButton.vertexNW[1]
        and event.y <= data.startButton.vertexSE[1]):
        if data.userName == "":
            nameEnterPrompt = welcomeWidget.ErrorPrompt("We Would Like to Know Your Name First :)", data.width//2, 7 * data.height//8)
            data.prompt.append(nameEnterPrompt)
        else:
            userInput.UserInput().run(data)

def mouseTracker(event, data):
    data.mouseMotion = (event.x, event.y)

def keyPressed(event, data):
    if (event.keysym == "BackSpace" 
        and data.userName != ""):
        data.userName = data.userName[:-1]
    data.userName += event.char

def drawWelcomeBG(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

def drawStartButton(canvas, data):
    mouseMotionX, mouseMotionY = data.mouseMotion
    data.startButton.draw(canvas, mouseMotionX, mouseMotionY)

def drawPrompt(canvas, data):
    for prompt in data.prompt:
        prompt.draw(canvas)

def drawNameInput(canvas, data):
    mouseMotionX, mouseMotionY = data.mouseMotion
    inputBox = welcomeWidget.InputBox(data.width//2, data.height//1.6, 150, 30)
    inputBox.draw(canvas, mouseMotionX, mouseMotionY)
    canvas.create_text(inputBox.cx, inputBox.cy, text = data.userName, font = "Helvetica 20 bold", fill = "black")
    

def drawStringInput(canvas, data):
    pass

def redrawAll(canvas, data):
    drawWelcomeBG(canvas, data)
    drawStartButton(canvas, data)
    drawNameInput(canvas, data)
    drawPrompt(canvas, data)
    

def timerFired(data):
    pass

def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def mouseTrackerWrapper(event, data):
        mouseTracker(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10
    data.mouseMotion = (-1, -1)
    data.mouseSelection = (-1, -1)
    root = Tk()
    root.title("Magic Desicion Maker Box")
    root.resizable(width=False, height=False)
    initWelcome(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseTrackerWrapper(event, data))  

    timerFiredWrapper(canvas, data)
    root.geometry("1200x800+100+0")

    root.mainloop()

run(1200, 800)
