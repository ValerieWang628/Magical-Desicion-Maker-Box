from tkinter import *
import copy
import pgWidgets
from collections import deque
import schulzeBeat
import scoreCalc

class Playground():


    @staticmethod
    def initPlayground(data):
        data.matrix = Playground.matrixMaker(data.entryStorageTrans)
        data.playerList = data.alternative
        data.inPlayList = []
        data.beatScoreList = schulzeBeat.PathIdentifier().pathIdentifier(data.matrix, data.playerList)
        data.positiveBeatScoreList = schulzeBeat.PositiveBeatFinder().positiveBeatFinder(data.matrix, data.playerList)
        data.smithSolution = schulzeBeat.SmithSetFinder().findSmithSet(data.matrix, data.playerList)
        data.strongestPathList =[]
        data.margin = 50
        data.mouseMotion = (-1, -1)
        data.mouseSelection = (-1, -1)
        data.mouseSelectionHist = deque(maxlen = 1)
        data.clickHist = deque(maxlen = 2)
        data.doubleClickSelection = (-1,-1)
        data.mouseHeldPosition = (-1, -1)
        data.selectionRect = deque(maxlen = 1)
        data.playerNode = []
        data.playerNodeSep = data.height//len(data.playerList)
        data.sittingPlayerLoc = {}
        Playground.loadSittingPlayers(data)
        data.beatNodeSet = set()
        data.nodeDep = None
        data.nodeDest = None
        data.operationButton = []
        data.buttonNum = 4
        data.buttonWidth = 160
        data.buttonSep = (data.width - 4 * data.margin)//data.buttonNum + 30
        Playground.loadOperationButton(data)
        data.playground = None
        Playground.loadPlayground(data)
    
    @staticmethod
    def partialInit(data):
        data.inPlayList = []
        data.mouseSelectionHist = deque(maxlen = 1)
        data.clickHist = deque(maxlen = 2)
        data.selectionRect = deque(maxlen = 1)
        data.playerNode = []
        data.playerNodeSep = data.height//len(data.playerList)
        data.sittingPlayerLoc = {}
        Playground.loadSittingPlayers(data)
        data.beatNodeSet = set()
        data.nodeDep = None
        data.nodeDest = None
        data.operationButton = []
        data.buttonNum = 4
        data.buttonWidth = 160
        data.buttonSep = (data.width - 4 * data.margin)//data.buttonNum + 30
        Playground.loadOperationButton(data)
    
    @staticmethod
    def matrixMaker(l):
        newList = []
        for row in l:
            newList.append(row[1:])
        rows, cols = len(newList), len(newList[0])
        newList.pop(0)
        return newList

    @staticmethod
    def loadPlayground(data):
        vertexNW, vertexSE = (data.margin, data.margin), (data.width - 3 * data.margin, data.height - 3 * data.margin)
        data.playground = pgWidgets.Playground(vertexNW,vertexSE)

    @staticmethod
    def loadSittingPlayers(data):
        heightOffset = 1.5 * data.margin
        verticalAlign = ((data.width - 3 * data.margin) + data.width)//2
        for i in range(len(data.playerList)):
            player = pgWidgets.PlayerNode(data.playerList[i], verticalAlign, heightOffset + i * data.playerNodeSep)
            data.playerNode.append(player)
            data.sittingPlayerLoc[player.playerName] = (player.cx, player.cy)
    
    @staticmethod
    def loadOperationButton(data):
        horizontalAlign = (2 * data.height - 3 * data.margin)//2 
        data.button1 = pgWidgets.ShowConnectionButton("Show One-Way Path", data.margin + data.buttonWidth//2, horizontalAlign, data.buttonWidth)
        data.operationButton.append(data.button1)
        data.button2 = pgWidgets.ShowConnectionButton("Show Two-Way Path", data.margin + data.buttonWidth//2 + data.buttonSep, horizontalAlign, data.buttonWidth)
        data.operationButton.append(data.button2)
        data.button3 = pgWidgets.SmithSetFinderButton("Show Smith Set", data.margin + data.buttonWidth//2 + data.buttonSep * 2, horizontalAlign, data.buttonWidth)
        data.operationButton.append(data.button3)
        data.button4 = pgWidgets.BeatDemoButton("Beat Path Demo", data.margin + data.buttonWidth//2 + data.buttonSep * 3, horizontalAlign, data.buttonWidth)
        data.operationButton.append(data.button4)
        button5 = pgWidgets.HintButton("Hint", data.margin//2 + 5, data.margin//2 + 5, 40, 40)
        data.operationButton.append(button5)

    @staticmethod
    def mousePressed(event, data):
        data.mouseSelection = (event.x, event.y)
        for player in data.inPlayList:
            eucliDist = ((event.x- player.cx) ** 2 + (event.y - player.cy) ** 2) ** 0.5
            if eucliDist <= player.r:
                if  (player.cx >= data.playground.vertexNW[0]
                    and player.cx <= data.playground.vertexSE[0]
                    and player.cy >= data.playground.vertexNW[1]
                    and player.cy <= data.playground.vertexSE[1]):
                    data.clickHist.append(player)
                    selectionRect = pgWidgets.SelectionRect(player.vertexNW, player.vertexSE, player.r)
                    data.selectionRect.append(selectionRect)
        for beatNode in data.beatNodeSet:
            if beatNode.ifClicked(event.x, event.y):
                data.nodeDep = beatNode.dep
                data.nodeDest = beatNode.dest
                scoreCalc.ScoreCalc.run(data)
        


    @staticmethod
    def mouseTracker(event, data):
        data.mouseMotion = (event.x, event.y)

    @staticmethod
    def mouseDoublePressed(event, data):
        data.doubleClickSelection = (event.x, event.y)

    @staticmethod
    def mouseHeld(event, data):
        data.mouseHeldPosition = (event.x, event.y)

    @staticmethod   
    def keyPressed(event, data):
        pass

    @staticmethod
    def drawPlaygroundBG(canvas, data):
        canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

    @staticmethod
    def drawPlaygroundField(canvas, data, mouseMotionX, mouseMotionY):
        data.playground.draw(canvas, mouseMotionX, mouseMotionY, 20)
    

    @staticmethod
    def drawPlayerNode(canvas, data):
        mouseX, mouseY = data.mouseMotion
        mousePressedX, mousePressedY = data.mouseSelection
        mouseDoublePressedX, mouseDoublePressedY = data.doubleClickSelection
        mouseHeldX, mouseHeldY = data.mouseHeldPosition
        for node in data.playerNode:
            node.ifSingleClicked(canvas, data.playground, mousePressedX, mousePressedY, data.inPlayList, data.mouseSelectionHist)
            node.ifDoubleClicked(canvas, data.playground, mouseDoublePressedX, mouseDoublePressedY, data.sittingPlayerLoc, data.inPlayList)
            node.ifDragged(canvas, data.playground, mouseHeldX, mouseHeldY)
            if not node.isInSmith:
                node.draw(canvas, mouseX, mouseY)
            else:
                node.draw(canvas, mouseX, mouseY, outline = "gold")

    @staticmethod
    def drawOperationButton(canvas, data):
        mouseX, mouseY = data.mouseMotion
        mousePressedX, mousePressedY = data.mouseSelection
        for button in data.operationButton:
            button.ifClicked(canvas, data, mousePressedX, mousePressedY, Playground.partialInit)
            button.draw(canvas, mouseX, mouseY, data.playground)

    @staticmethod
    def redrawAll(canvas, data):
        pass
        mouseMotionX, mouseMotionY = data.mouseMotion
        Playground.drawPlaygroundBG(canvas, data)
        Playground.drawPlaygroundField(canvas, data, mouseMotionX, mouseMotionY)
        Playground.drawPlayerNode(canvas, data)
        Playground.drawOperationButton(canvas, data)

    @staticmethod
    def timerFired(data):
        pass
    
    @staticmethod
    def run(data):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            Playground.redrawAll(canvas, data)
            canvas.update()    

        def timerFiredWrapper(canvas, data):
            Playground.timerFired(data)
            redrawAllWrapper(canvas, data)
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

        def mousePressedWrapper(event, canvas, data):
            Playground.mousePressed(event, data)
            redrawAllWrapper(canvas, data)

        def mouseTrackerWrapper(event, data):
            Playground.mouseTracker(event, data)
            redrawAllWrapper(canvas, data)
        
        def mouseDoublePressedWrapper(event, canvas, data):
            Playground.mouseDoublePressed(event, data)
            redrawAllWrapper(canvas, data)
    
        def mouseHeldWrapper(event, canvas, data):
            Playground.mouseHeld(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            Playground.keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        
        top = Toplevel()
        top.title("Welcome to the Beat Path Playground!")
        top.geometry("1200x800+100+0")
        Playground.initPlayground(data)
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
        top.bind("<Double-Button-1>", lambda event:
                            mouseDoublePressedWrapper(event, canvas, data))
        top.bind("<B1-Motion>", lambda event:
                            mouseHeldWrapper(event, canvas, data)) 
        timerFiredWrapper(canvas, data)
