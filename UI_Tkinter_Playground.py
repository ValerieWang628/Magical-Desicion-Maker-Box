
import pgWidgets

'''
This file is the main GUI file for the playground interaction.
The UI effects will be implemented first and then, connected to the calculated matrix.
'''


from tkinter import *

def init(data):
    data.playerList = ['A','B','C','D']
    data.margin = 50
    data.mouseMotion = (-1, -1)
    data.mouseSelection = (-1, -1)
    data.playerNode = []
    loadSittingPlayers(data)
    data.operationButton = []
    loadOperationButton(data)

def loadOperationButton(data):
    horizontalAlign = (2 * data.height - 3 * data.margin)//2 
    data.operationButton.append(pgWidgets.OperationButton("Show Connections",100, horizontalAlign))


def loadSittingPlayers(data):
    heightOffset = 1.5 * data.margin
    verticalAlign = ((data.width - 3 * data.margin) + data.width)//2
    for i in range(len(data.playerList)):
        data.playerNode.append(pgWidgets.PlayerNode(data.playerList[i], verticalAlign, heightOffset + data.margin * i * 2))

def mousePressed(event, data):
    data.mouseSelection = (event.x, event.y)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def drawPlaygroundBG(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

def drawPlaygroundField(canvas, data):
    corners = (data.margin, data.margin, data.width - 3 * data.margin, data.height - 3 * data.margin)
    canvas.create_rectangle(corners, fill = "black", outline = "cyan", width = 3, dash = (7, 10, 1, 1))

def drawPlayerNode(canvas, data):
    mouseX, mouseY = data.mouseMotion
    for node in data.playerNode:
        node.draw(canvas, mouseX, mouseY)
        print(node.cx, node.cy)

def drawOperationButton(canvas, data):
    mouseX, mouseY = data.mouseMotion
    for button in data.operationButton:
        button.draw(canvas, mouseX, mouseY)

def redrawAll(canvas, data):
    drawPlaygroundBG(canvas, data)
    drawPlaygroundField(canvas, data)
    drawPlayerNode(canvas, data)
    drawOperationButton(canvas, data)

def mouseTracker(event, data):
    data.mouseMotion = (event.x, event.y)

def run(width=300, height=300):
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
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.title("Magic Desicion Maker Box")
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event:
                            mouseTrackerWrapper(event, data))  
    # root.bind("<ButtonRelease-1>")
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)
