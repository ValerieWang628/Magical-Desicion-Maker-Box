
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
    data.doubleClickSelection = (-1,-1)
    data.playerNode = []
    data.playerNodeSep = data.height//len(data.playerList)
    data.sittingPlayerLoc = {}
    loadSittingPlayers(data)
    data.operationButton = []
    data.buttonNum = 4
    data.buttonWidth = 160
    data.buttonSep = (data.width - 4 * data.margin)//data.buttonNum + 30
    loadOperationButton(data)
    data.playground = None

def loadOperationButton(data):
    horizontalAlign = (2 * data.height - 3 * data.margin)//2 
    button1 = pgWidgets.OperationButton("Show Connections", data.margin + data.buttonWidth//2, horizontalAlign, data.buttonWidth)
    data.operationButton.append(button1)
    button2 = pgWidgets.OperationButton("Hide Connections", data.margin + data.buttonWidth//2 + data.buttonSep, horizontalAlign, data.buttonWidth)
    data.operationButton.append(button2)
    button3 = pgWidgets.OperationButton("Show Smith Set", data.margin + data.buttonWidth//2 + data.buttonSep * 2, horizontalAlign, data.buttonWidth)
    data.operationButton.append(button3)
    button4 = pgWidgets.OperationButton("Beatpath Demo", data.margin + data.buttonWidth//2 + data.buttonSep * 3, horizontalAlign, data.buttonWidth)
    data.operationButton.append(button4)

def loadSittingPlayers(data):
    heightOffset = 1.5 * data.margin
    verticalAlign = ((data.width - 3 * data.margin) + data.width)//2
    for i in range(len(data.playerList)):
        player = pgWidgets.PlayerNode(data.playerList[i], verticalAlign, heightOffset + i * data.playerNodeSep)
        data.playerNode.append(player)
        data.sittingPlayerLoc[player.playerName] = (player.cx, player.cy)
    print(data.sittingPlayerLoc)

def mousePressed(event, data):
    data.mouseSelection = (event.x, event.y)

def mouseDoublePressed(event, data):
    data.doubleClickSelection = (event.x, event.y)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def drawPlaygroundBG(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

def drawPlaygroundField(canvas, data):
    mouseX, mouseY = data.mouseMotion
    vertexNW, vertexSE = (data.margin, data.margin), (data.width - 3 * data.margin, data.height - 3 * data.margin)
    data.playground = pgWidgets.Playground(vertexNW,vertexSE)
    data.playground.draw(canvas, mouseX, mouseY, 20)

def drawPlayerNode(canvas, data):
    mouseX, mouseY = data.mouseMotion
    mousePressedX, mousePressedY = data.mouseSelection
    mouseDoublePressedX, mouseDoublePressedY = data.doubleClickSelection
    for node in data.playerNode:
        node.ifSingleClicked(canvas, data.playground, mousePressedX, mousePressedY)
        node.ifDoubleClicked(canvas, data.playground, mouseDoublePressedX, mouseDoublePressedY, data.sittingPlayerLoc)
        node.draw(canvas, mouseX, mouseY)

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
    
    def mouseDoublePressedWrapper(event, canvas, data):
        mouseDoublePressed(event, data)
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
    root.bind("<Double-Button-1>", lambda event:
                            mouseDoublePressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)
