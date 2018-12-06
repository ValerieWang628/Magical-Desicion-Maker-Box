from tkinter import *
import copy
import matrixOriWidget
import playground

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
        weight = ["w"]
        weight.extend(data.weight.copy())
        blank = [" "]
        blank.extend(folded[0])
        folded[0] = blank
        folded.insert(1, weight)
        return folded
    
    @staticmethod
    def fill(newTemp, ind, col, row, indList, matrix):
        if ind not in indList:
            newTemp[ind+2][col] = matrix[row][0]
            indList.append(ind)
        else:
            MatrixOri.fill(newTemp, ind+1, col, row, indList, matrix)

    @staticmethod
    def entryListTransformer(data):
        matrix = copy.deepcopy(data.entryStorage)
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col].isdigit():
                    matrix[row][col] = int(matrix[row][col])
        newTemp = copy.deepcopy(matrix)
        for row in range(2,rows):
            for col in range(1,cols):
                newTemp[row][col] = 0
        for col in range(1, cols):
            colList = [matrix[r][col] for r in range(len(matrix))][2:]
            colList = sorted(colList, reverse = True)
            indList = []
            for row in range(2, rows):
                ind = colList.index(matrix[row][col])
                MatrixOri.fill(newTemp, ind, col, row, indList, matrix)
        for row in range(2,rows):
            newTemp[row][0] = "r " + str(row-1)
        return newTemp

    @staticmethod
    def initMatrix(data):
        data.transformed = False
        data.entryStorage = MatrixOri.entryListOrganizer(data)
        data.entryStorageTrans = MatrixOri.entryListTransformer(data)
        data.matrixOriList = []
        data.matrixTransList = []
        MatrixOri.createOriMatrixCell(data)
        data.transformButton = matrixOriWidget.TransformButton("Transform to Rank Based Matrix!", 300, 700, 450, 100)
        data.matrixButton = [data.transformButton]

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
                cell = matrixOriWidget.Cell(vertexNW, vertexSE, data.entryStorage[row][col], row, col)
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
                cell = matrixOriWidget.Cell(vertexNW, vertexSE, data.entryStorageTrans[row][col], row, col)
                data.matrixTransList.append(cell)


    @staticmethod
    def loadPrompt(data):
        pass


    @staticmethod
    def mousePressed(event, data, top):
        data.mouseSelection = (event.x, event.y)
        if (event.x >= data.transformButton.vertexNW[0]
            and event.x <= data.transformButton.vertexSE[0]
            and event.y >= data.transformButton.vertexNW[1]
            and event.y <= data.transformButton.vertexSE[1]):
            MatrixOri.createTransMatrixCell(data)
            data.transformed = True
            data.goRankButton = matrixOriWidget.GoRankButton("Let's Go to Beat Path Playground!", 900, 700, 450, 100)
            data.matrixButton.append(data.goRankButton)
        if (event.x >= data.goRankButton.vertexNW[0]
            and event.x <= data.goRankButton.vertexSE[0]
            and event.y >= data.goRankButton.vertexNW[1]
            and event.y <= data.goRankButton.vertexSE[1]):
            top.destroy()
            playground.Playground.run(data)


    @staticmethod
    def mouseTracker(event, data):
        data.mouseMotion = (event.x, event.y)

    @staticmethod   
    def keyPressed(event, data):
        pass

    
    @staticmethod
    def pairFinderBeforeAfter(data, row, col):
        altName = data.entryStorage[row][0]
        for r in range(2, len(data.entryStorageTrans)):
            if data.entryStorageTrans[r][col] == altName:
                return r, col


    @staticmethod
    def drawPrompt(canvas, data):
        pass


    @staticmethod
    def drawCell(data, canvas, mouseX, mouseY):
        if data.transformed:
            for cell in data.matrixOriList:
                if (cell.row >= 2
                    and cell.col >= 1
                    and cell.ifHovered(mouseX, mouseY)):
                    row, col = MatrixOri.pairFinderBeforeAfter(data, cell.row, cell.col)
                    for cellT in data.matrixTransList:
                        if cellT.row == row and cellT.col == col:
                            cellT.draw(mouseX, mouseY, canvas, fill = "cyan", outline = "black")
                cell.draw(mouseX, mouseY, canvas)

    @staticmethod
    def drawCellOri(canvas, data, mouseX, mouseY):
        for cell in data.matrixOriList:
            cell.draw(mouseX, mouseY, canvas)
    
    @staticmethod
    def drawCellTrans(canvas, data, mouseX, mouseY):
        for cell in data.matrixTransList:
            cell.draw(mouseX, mouseY, canvas)

    @staticmethod
    def drawButton(canvas, data, mouseMotionX, mouseMotionY):
        for but in data.matrixButton:
            but.draw(canvas, mouseMotionX, mouseMotionY)

    @staticmethod
    def redrawAll(canvas, data):
        mouseMotionX, mouseMotionY = data.mouseMotion
        canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
        MatrixOri.drawCellOri(canvas, data, mouseMotionX, mouseMotionY)
        MatrixOri.drawCellTrans(canvas, data, mouseMotionX, mouseMotionY)
        MatrixOri.drawCell(data, canvas, mouseMotionX, mouseMotionY)
        MatrixOri.drawButton(canvas, data, mouseMotionX, mouseMotionY)


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
        
        def mousePressedWrapper(event, canvas, data, top):
            MatrixOri.mousePressed(event, data, top)
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
        MatrixOri.initMatrix(data)
        data.mouseMotion = (-1, -1)
        data.mouseSelection = (-1, -1)
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
