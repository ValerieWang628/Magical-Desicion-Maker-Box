'''
This file stores most of the GUI-related classes.
Such as nodes, buttons, arrowed lines, etc.
As for now, the hovering-color-inverse effect has been implemented.
Later, the drag and drop, node resize, etc. will be implemented.

This file will be imported in the UI_Tkinter_Playground file.
'''
import random
import math
from collections import deque
import schulzeBeat

class PlayerNode():

    def __init__(self, playerName, cx, cy, isInSmith = False, r = 30):
        self.playerName = playerName
        self.cx = cx
        self.cy = cy
        self.r = r
        self.isInSmith = isInSmith

    def __eq__(self, other):
        return (isinstance(other, PlayerNode)
                and self.playerName == other.playerName)

    def draw(self, canvas, mouseX, mouseY, fill = "black", outline = "cyan"):
        self.vertexNW = (self.cx - self.r, self.cy - self.r)
        self.vertexSE = (self.cx + self.r, self.cy + self.r)
        self.borderN = (self.cx, self.cy - self.r)
        self.borderS = (self.cx, self.cy + self.r)
        self.borderW = (self.cx - self.r, self.cy)
        self.borderE = (self.cx + self.r, self.cy)
        self.borderNE = (self.cx + (self.r) * math.cos(math.pi/4), self.cy - (self.r) * math.sin(math.pi/4))
        self.borderSE = (self.cx + (self.r) * math.cos(math.pi/4), self.cy + (self.r) * math.sin(math.pi/4))
        self.borderNW = (self.cx - (self.r) * math.cos(math.pi/4), self.cy - (self.r) * math.sin(math.pi/4))
        self.borderSW = (self.cx + (self.r) * math.cos(math.pi/4), self.cy + (self.r) * math.sin(math.pi/4))
        self.connector = [self.borderE, self.borderN, self.borderS, self.borderW, self.borderNE, self.borderNW, self.borderSE, self.borderSW]
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            fill, outline = outline, fill
        canvas.create_oval(self.vertexNW, self.vertexSE, fill = fill, width = 3, outline = outline)
        canvas.create_text(self.cx, self.cy, text = self.playerName, fill = outline, font = "Helvetica 20 bold")
    
    @staticmethod
    def angleCalc(Ox, Oy, Ax, Ay, theta):
        AOx = Ay*1.0-Oy
        AOy = Ax*1.0-Ox
        R = math.sqrt(AOx**2+AOy**2)
        angleA = math.atan2(AOx, AOy)
        angleB = angleA + theta
        BOx = math.cos(angleB)*R
        BOy = math.sin(angleB)*R
        Bx = BOx+Ox
        By = BOy+Oy
        return (Bx, By)


    def showConnection(self, other, canvas, playground, scoreDict, twoWay):
        assert(type(other) == PlayerNode)
        bestConnect = None
        shortestConnection = 10000 #magic num
        for pointSelf in self.connector:
            for pointOther in other.connector:
                eucliDist = ((pointSelf[0] - pointOther[0]) ** 2 + (pointSelf[1] - pointOther[1]) ** 2) ** 0.5
                if eucliDist <= shortestConnection:
                    shortestConnection = eucliDist
                    bestConnect = (pointSelf, pointOther)
        if (bestConnect[0][0] >= playground.vertexNW[0]
            and bestConnect[0][0] <= playground.vertexSE[0]
            and bestConnect[1][0] >= playground.vertexNW[0]
            and bestConnect[1][0] <= playground.vertexSE[0]
            and bestConnect[0][1] >= playground.vertexNW[1]
            and bestConnect[0][1] <= playground.vertexSE[1]
            and bestConnect[1][1] >= playground.vertexNW[1]
            and bestConnect[1][1] <= playground.vertexSE[1]):
            connectionPath = Path(bestConnect[0], bestConnect[1])
            connectionPath.draw(canvas)    
            if not twoWay:
                beatScore = BeatNode((bestConnect[0][0]+bestConnect[1][0])//2, (bestConnect[0][1]+bestConnect[1][1])//2, scoreDict[self.playerName]) 
                beatScore.draw(canvas)
            else:                
                x1, y1, x2, y2 = bestConnect[0][0], bestConnect[0][1], bestConnect[1][0], bestConnect[1][1]
                t1, t2 = 1, 2 # trisection proportion
                x3, y3 = (t1*x2+t2*x1)/(t1+t2), (t1*y2+t2*y1)/(t1+t2)
                angleOffset = 50
                bx, by = PlayerNode.angleCalc(self.cx, self.cy, x1, y1, angleOffset)
                cx, cy = PlayerNode.angleCalc(other.cx, other.cy, x2, y2, angleOffset * (-1))
                x4, y4 = (t2*cx+t1*bx)/(t1+t2), (t2*cy+t1*by)/(t1+t2) 
                twoWayPath = Path((cx, cy),(bx, by))
                twoWayPath.draw(canvas, fill = "plum1")   
                beatScoreOneWay = BeatNode(x3, y3, scoreDict[self.playerName]) 
                beatScoreOneWay.draw(canvas)
                beatScoreTwoWay = BeatNode(x4, y4, scoreDict[other.playerName]) 
                beatScoreTwoWay.draw(canvas, outline = "plum1")


    def showPositivePath(self, other, canvas, playground, positiveScoreDict):
        assert(type(other) == PlayerNode)
        bestConnect = None
        shortestConnection = 10000 #magic num
        for pointSelf in self.connector:
            for pointOther in other.connector:
                eucliDist = ((pointSelf[0] - pointOther[0]) ** 2 + (pointSelf[1] - pointOther[1]) ** 2) ** 0.5
                if eucliDist <= shortestConnection:
                    shortestConnection = eucliDist
                    bestConnect = (pointSelf, pointOther)
        if (bestConnect[0][0] >= playground.vertexNW[0]
            and bestConnect[0][0] <= playground.vertexSE[0]
            and bestConnect[1][0] >= playground.vertexNW[0]
            and bestConnect[1][0] <= playground.vertexSE[0]
            and bestConnect[0][1] >= playground.vertexNW[1]
            and bestConnect[0][1] <= playground.vertexSE[1]
            and bestConnect[1][1] >= playground.vertexNW[1]
            and bestConnect[1][1] <= playground.vertexSE[1]):
            connectionPath = Path(bestConnect[0], bestConnect[1])
            connectionPath.draw(canvas, fill = "gold") 
            t1, t2 = 1, 2
            x1, y1, x2, y2 = bestConnect[0][0], bestConnect[0][1], bestConnect[1][0], bestConnect[1][1]
            x3, y3 = (t1*x2+t2*x1)/(t1+t2), (t1*y2+t2*y1)/(t1+t2)
            beatScore = BeatNode(x3, y3, positiveScoreDict[self.playerName]) 
            beatScore.draw(canvas)


            
    
    def ifSingleClicked(self, canvas, playground, mouseX, mouseY, inPlayList, mouseSelectionHist):
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            if  (self.cx >= playground.vertexNW[0]
                and self.cx <= playground.vertexSE[0]
                and self.cy >= playground.vertexNW[1]
                and self.cy <= playground.vertexSE[1]):
                canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = None, outline = "cyan", width = 1)
                mouseSelectionHist.append(self)
            else:
                innerOffset = 200
                self.cx = random.randint(playground.vertexNW[0] + innerOffset, playground.vertexSE[0] - innerOffset)
                self.cy = random.randint(playground.vertexNW[1] + innerOffset ,playground.vertexSE[1] - innerOffset)
                inPlayList.append(self)


    def ifDoubleClicked(self, canvas, playground, mouseX, mouseY, sittingPlayerLoc, inPlayList):
        eucliDist = ((mouseX - self.cx) ** 2 + (mouseY - self.cy) ** 2) ** 0.5
        if eucliDist <= self.r:
            if  (self.cx >= playground.vertexNW[0]
                and self.cx <= playground.vertexSE[0]
                and self.cy >= playground.vertexNW[1]
                and self.cy <= playground.vertexSE[1]):
                self.cx, self.cy = sittingPlayerLoc[self.playerName]
                inPlayList.remove(self)

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


    def getHashables(self):
        return (self.playerName, self.cx, self.cy, self.r)
    
    def __hash__(self):
        return hash(self.getHashables())

class Path():

    def __init__(self, dep, dest):
        self.dep = dep
        self.dest = dest
    
    def draw(self, canvas, fill = "cyan"):
        canvas.create_line(self.dep, self.dest, fill = fill, width = 3, arrow= "last", arrowshape = (20,20,5))
    
    def __eq__(self, other):
        return (isinstance(other, Path) 
                and ((self.dep == other.dep and self.dest == other.dest) 
                or (self.dep == other.dest and self.dest == other.dep)))
    
    def __hash__(self):
        return hash(self.getHashables())
    
    def getHashables(self):
        return (self.dep, self.dest)

class BeatNode():

    def __init__(self, cx, cy, num, r = 20):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.num = num
        self.vertexNW = (self.cx - self.r, self.cy - self.r)
        self.vertexSE = (self.cx + self.r, self.cy + self.r)
    
    def draw(self, canvas, outline = "cyan"):
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = "black", outline = outline, width = 2)
        canvas.create_text(self.cx, self.cy, text = str(self.num), fill = outline, font = "Helvetica 20 bold")


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

    def ifClicked(self, canvas, mouseX, mouseY, mouseSelectionHist, beatScoreList, playerNodeList, inPlayList, playground, matrix):
        pass


class SmithSetFinderButton(OperationButton):

    def ifClicked(self, canvas, mouseX, mouseY, mouseSelectionHist, beatScoreList, playerNodeList, inPlayList, playground, matrix):
        if (mouseX >= self.vertexNW[0]
            and mouseX <= self.vertexSE[0]
            and mouseY >= self.vertexNW[1]
            and mouseY <= self.vertexSE[1]):
            if (mouseSelectionHist == deque(maxlen = 1) 
                and inPlayList == []):
                ErrorPrompt("Please First Add a Player.").draw(canvas)
            else:
                inPlayName = [player.playerName for player in inPlayList] # extracting only attributes from objects
                smithSet = schulzeBeat.SmithSetFinder().findSmithSet(matrix, inPlayName)
                inPlaySet = set(inPlayName)
                inPlaySmith = inPlaySet & smithSet
                for playName in inPlaySmith:
                    for player in inPlayList:
                        if player.playerName == playName:
                            player.isInSmith = True
                for playerName in inPlaySet:
                    for score in beatScoreList:
                        if playerName in score and score[playerName] != 0:
                            pairWisePlayer = list(score.keys())
                            pairWisePlayer.remove(playerName)
                            theOtherPlayer = pairWisePlayer[0]
                            if theOtherPlayer in inPlayName:
                                confront, rival = None, None
                                for player in inPlayList:
                                    if player.playerName == theOtherPlayer:
                                        rival = player
                                    elif player.playerName == playerName:
                                        confront = player
                                confront.showPositivePath(rival, canvas, playground, score)
                ErrorPrompt("Now You Are Looking at by How Much a Winner Beats Another with Smith Set Players Highlighted.").draw(canvas)
        else:
            for player in inPlayList:
                player.isInSmith = False


class BeatDemoButton(OperationButton):

    def ifClicked(self, canvas, mouseX, mouseY, mouseSelectionHist, beatScoreList, playerNodeList, inPlayList, playground, matrix):
        if (mouseX >= self.vertexNW[0]
            and mouseX <= self.vertexSE[0]
            and mouseY >= self.vertexNW[1]
            and mouseY <= self.vertexSE[1]):
            pass


class ShowConnectionButton(OperationButton):

    def ifClicked(self, canvas, mouseX, mouseY, mouseSelectionHist, beatScoreList, playerNodeList, inPlayList, playground, matrix = None):
        if (mouseX >= self.vertexNW[0]
            and mouseX <= self.vertexSE[0]
            and mouseY >= self.vertexNW[1]
            and mouseY <= self.vertexSE[1]):
            if (mouseSelectionHist == deque(maxlen = 1) 
                and inPlayList == []):
                ErrorPrompt("Please First Add a Player.").draw(canvas)
            elif (mouseSelectionHist == deque(maxlen = 1) 
                and inPlayList != []):
                ErrorPrompt("Please First Select a Player by Clicking on It.").draw(canvas)
            elif len(inPlayList) < 2:
                ErrorPrompt("Please Drag at Least Two Players to the Playground.").draw(canvas)
            else:
                for score in beatScoreList:
                    selectedPlayer = mouseSelectionHist[-1]
                    if selectedPlayer.playerName in score:
                        pairWisePlayer = list(score.keys())
                        pairWisePlayer.remove(selectedPlayer.playerName)
                        theOtherPlayer = pairWisePlayer[0]
                        for player in playerNodeList:
                            if player.playerName == theOtherPlayer:
                                theOtherPlayer = player
                        if self.prompt == "Show One-Way Path":
                            selectedPlayer.showConnection(theOtherPlayer, canvas, playground, score, twoWay = False)
                            ErrorPrompt("Now You Are Looking at All One-way BeatPaths Departed from %s." % selectedPlayer.playerName).draw(canvas)
                        elif self.prompt == "Show Two-Way Path":
                            selectedPlayer.showConnection(theOtherPlayer, canvas, playground, score, twoWay = True)
                            ErrorPrompt("Now You Are Looking at All Two-way BeatPaths Departed from %s." % selectedPlayer.playerName).draw(canvas)


class ErrorPrompt():

    def __init__(self, prompt, cx = 550, cy = 25):
        self.prompt = prompt
        self.cx = cx
        self.cy = cy
 
    def draw(self, canvas, fill = "black", outline = "cyan"):
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
