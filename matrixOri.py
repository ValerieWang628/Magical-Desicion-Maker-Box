from tkinter import *
import copy
import matrixOriWidget

class MatrixOri():

    @staticmethod
    def entryListOrganizer(data):
        l = data.entryStorage
        folded = []
        for i in range(0, len(l), data.cols):
            folded.append(l[i:i+data.cols])
        attribute = [data.attribute.copy()]
        attribute.extend(folded)
        folded = attribute
        for i in range(1, len(folded)):
            folded[i].insert(0, data.alternative[i-1])
        weight = ["weight"]
        weight.extend(data.weight.copy())
        blank = [" "]
        blank.extend(folded[0])
        folded[0] = blank
        folded.insert(1, weight)
        return folded

    @staticmethod
    def entryListTransformer(data):
        pass

    @staticmethod
    def initTopsis(data):
        data.entryStorage = MatrixOri.entryListOrganizer(data)
        data.entryStorageTrans = MatrixOri.entryListTransformer(data)
        data.matrixOriList = []
        data.matrixTransList = []
        MatrixOri.createOriMatrixCell(data)

    @staticmethod
    def locateCellBounds(data, row, col, marginW, marginH, s, left = True):   
        if left: 
            x0 = marginW + col * s
            x1 = marginW + (col+1) * s
        else:
            x0 = marginW + col * s + data.width//2
            x1 = marginW + (col+1) * s + data.width//2
        y0 = marginH + row * s
        y1 = marginH + (row+1) * s
        return (x0, y0, x1, y1)

    @staticmethod
    def createOriMatrixCell(data):
        rows, cols = len(data.entryStorage), len(data.entryStorage[0])
        marginW = 50
        marginH = 100
        w = data.width//2 - 2 * marginW
        h = data.height - 2 * marginH
        s = min(w, h)//max(rows, cols)
        for row in range(rows):
            for col in range(cols):
                loc = MatrixOri.locateCellBounds(data, row, col, marginW, marginH, s)
                vertexNW, vertexSE = (loc[0], loc[1]), (loc[2], loc[3])
                cell = matrixOriWidget.Cell(vertexNW, vertexSE, data.entryStorage[row][col])
                data.matrixOriList.append(cell)

    @staticmethod
    def createTransMatrixCell(data):
        rows, cols = len(data.entryStorage), len(data.entryStorage[0])
        marginW = 50
        marginH = 100
        w = data.width//2 - 2 * marginW
        h = data.height - 2 * marginH
        s = min(w, h)//max(rows, cols)
        for row in range(rows):
            for col in range(cols):
                loc = MatrixOri.locateCellBounds(data, row, col, marginW, marginH, s, left = False)
                vertexNW, vertexSE = (loc[0], loc[1]), (loc[2], loc[3])
                cell = matrixOriWidget.Cell(vertexNW, vertexSE, data.entryStorageTrans[row][col])
                data.matrixTransList.append(cell)


    @staticmethod
    def loadPrompt(data):
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
    def drawPrompt(canvas, data):
        pass

    @staticmethod
    def drawCellOri(canvas, data):
        for cell in data.matrixOriList:
            cell.draw(canvas)
    
    @staticmethod
    def drawCellTrans(canvas, data):
        for cell in data.matrixTransList:
            cell.draw(canvas)

    @staticmethod
    def redrawAll(canvas, data):
        canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
        MatrixOri.drawCellOri(canvas, data)
        MatrixOri.drawCellTrans(canvas, data)


    @staticmethod
    def timerFired(data):
        pass
    
    @staticmethod
    def run(data):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            MatrixOri.redrawAll(canvas, data)
            canvas.update()    

        def timerFiredWrapper(canvas, data):
            MatrixOri.timerFired(data)
            redrawAllWrapper(canvas, data)
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
        def mousePressedWrapper(event, canvas, data):
            MatrixOri.mousePressed(event, data)
            redrawAllWrapper(canvas, data)

        def mouseTrackerWrapper(event, data):
            MatrixOri.mouseTracker(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            MatrixOri.keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        
        top = Toplevel()
        top.title("Matrix")
        top.geometry("1200x800+100+0")
        MatrixOri.initTopsis(data)
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
