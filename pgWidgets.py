'''
This file stores most of the GUI-related classes.
Such as nodes, buttons, arrowed lines, etc.
As for now, the hovering-color-inverse effect has been implemented.
Later, the drag and drop, node resize, etc. will be implemented.

This file will be imported in the UI_Tkinter_Playground file.
'''
import random

class PlayerNode():

    def __init__(self, playerName, cx, cy, r = 30):
        self.playerName = playerName
        self.cx = cx
        self.cy = cy
        self.r = r

    def draw(self, canvas, mouseX, mouseY, fill = "black", outline = "cyan"):
        self.vertexNW = (self.cx - self.r, self.cy - self.r)
        self.vertexSE = (self.cx + self.r, self.cy + self.r)
        self.borderN = (self.cx, self.cy - self.r)
        self.borderS = (self.cx, self.cy + self.r)
        self.borderW = (self.cx - self.r, self.cy)
        self.borderE = (self.cx + self.r, self.cy)
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            fill, outline = outline, fill
        canvas.create_oval(self.vertexNW, self.vertexSE, fill = fill, width = 3, outline = outline)
        canvas.create_text(self.cx, self.cy, text = self.playerName, fill = outline, font = "Helvetica 20 bold")
    
    def ifSingleClicked(self, canvas, playground, mouseX, mouseY, inPlayList):
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            if  (self.cx >= playground.vertexNW[0]
                and self.cx <= playground.vertexSE[0]
                and self.cy >= playground.vertexNW[1]
                and self.cy <= playground.vertexSE[1]):
                canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = None, outline = "cyan", width = 1)
            else:
                innerOffset = 50
                self.cx = random.randint(playground.vertexNW[0] + innerOffset, playground.vertexSE[0] - innerOffset)
                self.cy = random.randint(playground.vertexNW[1] + innerOffset ,playground.vertexSE[1] - innerOffset)
                inPlayList.append(self.playerName)

    def ifDoubleClicked(self, canvas, playground, mouseX, mouseY, sittingPlayerLoc, inPlayList):
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            if  (self.cx >= playground.vertexNW[0]
                and self.cx <= playground.vertexSE[0]
                and self.cy >= playground.vertexNW[1]
                and self.cy <= playground.vertexSE[1]):
                self.cx, self.cy = sittingPlayerLoc[self.playerName]
                inPlayList.remove(self.playerName)

    def ifDragged(self, canvas, playground, mouseX, mouseY):
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            if  (self.cx >= playground.vertexNW[0]
                and self.cx <= playground.vertexSE[0]
                and self.cy >= playground.vertexNW[1]
                and self.cy <= playground.vertexSE[1]):  
                self.cx, self.cy = mouseX, mouseY     
    
    def ifReleased(self, canvas, playground, mouseX, mouseY):
        PlayerNode.ifDragged(self,canvas, playground, mouseX, mouseY)

    
    def safeDistance(self, other, safeDist = 10):
        if (isinstance(other, PlayerNode)
            or isinstance(other, BeatNode)):
            eucliDist = ((other.cx - self.cx) ** 2 + (other.cx - self.cy) ** 2) ** 0.5
            while eucliDist <= self.r + other.r:
                self.cx += safeDist
                self.cy += safeDist


    def __eq__(self, other):
        return (str(other) == self.playerName)

    def getHashables(self):
        return (self.playerName, self.cx, self.cy, self.r)
    
    def __hash__(self):
        return hash(self.getHashables())

class Path():

    def __init__(self, dep, dest):
        self.dep = dep
        self.dest = dest
    
    def draw(self, canvas):
        canvas.create_line(self.dep, self.dest, fill = "cyan", width = 5, arrow = LAST, arrowshape = (20,20,5))

class BeatNode():

    def __init__(self, cx, cy, r, num):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.num = num
        self.vertexNW = (self.cx - self.s, self.cy - self.s)
        self.vertexSE = (self.cx + self.s, self.cy + self.s)
    
    def draw(self, canvas):
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = "black", outline = "cyan", width = 2)
        canvas.create_text(self.cx, self.cy, text = str(self.num), fill = "cyan")


class OperationButton():

    def __init__(self, prompt, cx, cy, w , h = 50):
        self.prompt = prompt
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.vertexNW = (self.cx - self.w//2, self.cy - self.h//2)
        self.vertexSE = (self.cx + self.w//2, self.cy + self.h//2)
    
    def draw(self, canvas, mouseX, mouseY, playground = None, fill = "black", outline = "cyan"):
        if (mouseX >= self.vertexNW[0]
             and mouseX <= self.vertexSE[0]
             and mouseY >= self.vertexNW[1]
             and mouseY <= self.vertexSE[1]):
             fill, outline = outline, fill
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3)
        canvas.create_text(self.cx, self.cy, text = self.prompt, font = "Helvetica 15 bold", fill = outline)

class HintButton(OperationButton):

    def __init__(self, prompt, cx, cy, w , h):
        super().__init__(prompt, cx, cy, w , h)
    
    def draw(self, canvas, mouseX, mouseY, playground, fill = "black", outline = "cyan"):
        if (mouseX >= self.vertexNW[0]
             and mouseX <= self.vertexSE[0]
             and mouseY >= self.vertexNW[1]
             and mouseY <= self.vertexSE[1]):
            kernelOffset = 20
            canvas.create_rectangle(playground.vertexNW[0] + kernelOffset, 
                                        playground.vertexNW[1] + kernelOffset, 
                                        playground.vertexSE[0] - kernelOffset, 
                                        playground.vertexSE[1] - kernelOffset,
                                        fill = fill, outline = outline, width = 3)
            canvas.create_text((playground.vertexNW[0] + playground.vertexSE[0])//2, 
                                (playground.vertexNW[1] + playground.vertexSE[1])//2,
                                text = "PlaceHolder Hint", font = "Helvetica 30 bold", fill = outline)
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3)
        canvas.create_text(self.cx, self.cy, text = self.prompt, font = "Helvetica 15 bold", fill = outline)                        


class Playground():

    def __init__(self, vertexNW, vertexSE):
        self.vertexNW = vertexNW
        self.vertexSE = vertexSE
        self.w = self.vertexSE[0] - self.vertexNW[0]
        self.h = self.vertexSE[1] - self.vertexNW[1]

    
    def draw(self, canvas, mouseX, mouseY, hightlightMargin, fill = "black", outline = "cyan"):
        if ((mouseX >= self.vertexNW[0] - hightlightMargin
            and mouseX <= self.vertexNW[0] + hightlightMargin)
            or (mouseX >= self.vertexSE[0] - hightlightMargin
            and mouseX <= self.vertexSE[0] + hightlightMargin)
            or (mouseY >= self.vertexNW[1] - hightlightMargin
            and mouseY <= self.vertexNW[1] + hightlightMargin)
            or (mouseY >= self.vertexSE[1] - hightlightMargin
            and mouseY <= self.vertexSE[1] + hightlightMargin)):
            outline = "white"
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3, dash = (7, 10, 1, 1))
