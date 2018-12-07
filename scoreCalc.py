from tkinter import *
import scoreCalcWidget
import matrixOriWidget

class ScoreCalc():

    @staticmethod
    def initScoreCalc(data):
        data.newMatrixTrans = []
        ScoreCalc.createMatrixCell(data)
        data.depStr = ""
        data.destStr = ""
        ScoreCalc.calcFormula(data)
        data.calcPrompt = []
        ScoreCalc.loadCalcPrompt(data)

    
    @staticmethod
    def loadCalcPrompt(data):
        depPrompt = scoreCalcWidget.CalcPrompt(data.depStr, 450, 180, 15)
        destPrompt = scoreCalcWidget.CalcPrompt(data.destStr, 450, 220, 15)
        data.calcPrompt.append(depPrompt)
        data.calcPrompt.append(destPrompt)

    @staticmethod
    def loadInputBox(data):
        pass


    @staticmethod
    def mousePressed(event, data, top):
        data.mouseSelection = (event.x, event.y)


    @staticmethod
    def mouseTracker(event, data):
        data.mouseMotion = (event.x, event.y)

    @staticmethod   
    def keyPressed(event, data):
        pass
        

    @staticmethod
    def drawPrompt(canvas, data):
        for prompt in data.calcPrompt:
            prompt.draw(canvas)

    @staticmethod
    def locateCellBounds(data, row, col, margin, s):   
        x0 = margin + col * s
        x1 = margin + (col+1) * s
        y0 = margin + row * s
        y1 = margin + (row+1) * s
        return (x0, y0, x1, y1)

    @staticmethod
    def createMatrixCell(data):
        rows, cols = len(data.entryStorage), len(data.entryStorage[0])
        margin = 50
        w = data.newWidth - 2 * margin
        h = data.newHeight - 2 * margin
        s = min(w, h)//max(rows, cols)
        for row in range(rows):
            for col in range(cols):
                loc = ScoreCalc.locateCellBounds(data, row, col, margin, s)
                vertexNW, vertexSE = (loc[0], loc[1]), (loc[2], loc[3])
                cell = matrixOriWidget.Cell(vertexNW, vertexSE, data.entryStorageTrans[row][col], row, col)
                data.newMatrixTrans.append(cell)
    
    @staticmethod
    def calcFormula(data):
        depList = [data.nodeDep]
        destList = [data.nodeDest]
        depStr = data.nodeDep + "'s Score = "
        destStr = data.nodeDest + "'s Score = "
        for col in range(1, len(data.entryStorageTrans[0])):
            for row in range(2, len(data.entryStorageTrans)):
                if data.entryStorageTrans[row][col] == data.nodeDep:
                    depList.append(str(data.entryStorageTrans[1][col]))
                    destList.append("0")
                    break
                elif data.entryStorageTrans[row][col] == data.nodeDest:
                    destList.append(str(data.entryStorageTrans[1][col]))
                    depList.append("0")
                    break
        depRightHandSide = " +  ".join(depList[1:])
        destRightHandSide = " +  ".join(destList[1:])
        depStr += depRightHandSide
        destStr += destRightHandSide
        data.depStr, data.destStr = depStr, destStr


    @staticmethod
    def drawScoreCalcBg(canvas, data):
        canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    @staticmethod
    def drawCellTrans(canvas, data, mouseX, mouseY):
        for cell in data.newMatrixTrans:
            cell.draw(mouseX, mouseY, canvas)

    @staticmethod
    def redrawAll(canvas, data):
        mouseMotionX, mouseMotionY = data.mouseMotion
        ScoreCalc.drawScoreCalcBg(canvas, data)
        ScoreCalc.drawCellTrans(canvas, data, mouseMotionX, mouseMotionY)
        ScoreCalc.drawPrompt(canvas, data)


    @staticmethod
    def timerFired(data):
        pass
    
    @staticmethod
    def run(data):
        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            ScoreCalc.redrawAll(canvas, data)
            canvas.update()    

        def timerFiredWrapper(canvas, data):
            ScoreCalc.timerFired(data)
            redrawAllWrapper(canvas, data)
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
        def mousePressedWrapper(event, canvas, data, top):
            ScoreCalc.mousePressed(event, data, top)
            redrawAllWrapper(canvas, data)

        def mouseTrackerWrapper(event, data):
            ScoreCalc.mouseTracker(event, data)
            redrawAllWrapper(canvas, data)

        def keyPressedWrapper(event, canvas, data):
            ScoreCalc.keyPressed(event, data)
            redrawAllWrapper(canvas, data)

        
        top = Toplevel()
        top.title("Score Calculation")
        top.geometry("600x400+100+200")
        data.newWidth = 600
        data.newHeight = 400
        ScoreCalc.initScoreCalc(data)
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
