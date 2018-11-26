


class OperationButton():

    def __init__(self, prompt, cx, cy, w, h = 50):
        self.prompt = prompt
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.vertexNW = (self.cx - self.w//2, self.cy - self.h//2)
        self.vertexSE = (self.cx + self.w//2, self.cy + self.h//2)
    
    def draw(self, canvas, mouseX, mouseY, fill = "black", outline = "cyan"):
        if (mouseX >= self.vertexNW[0]
             and mouseX <= self.vertexSE[0]
             and mouseY >= self.vertexNW[1]
             and mouseY <= self.vertexSE[1]):
             fill, outline = outline, fill
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3)
        canvas.create_text(self.cx, self.cy, text = self.prompt, font = "Helvetica 15 bold", fill = outline)


class DoneButton(OperationButton):
    
    def __init__(self, cx, cy, w, h, prompt = "Done"):
        super().__init__(prompt, cx, cy, w, h)
        self.vertexNW = (self.cx - self.w//2, self.cy - self.h//2)
        self.vertexSE = (self.cx + self.w//2, self.cy + self.h//2)
    
    def draw(self, canvas, mouseX, mouseY, fill = "black", outline = "cyan"):
        super().draw(canvas, mouseX, mouseY, fill, outline)


class ErrorPrompt():

    def __init__(self, prompt, cx = 550, cy = 25, fontSize = 15):
        self.prompt = prompt
        self.cx = cx
        self.cy = cy
        self.fontSize = fontSize
 
    def draw(self, canvas, fill = "black", outline = "cyan"):
        canvas.create_text(self.cx, self.cy, text = self.prompt, font = "Helvetica " + str(self.fontSize) + " bold", fill = outline)


class QuestionPrompt(ErrorPrompt):
    pass



class InputBox():

    def __init__(self, cx, cy, w, h):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.vertexNW = (self.cx - self.w//2, self.cy - self.h//2)
        self.vertexSE = (self.cx + self.w//2, self.cy + self.h//2)
    
    def draw(self, canvas, mouseX, mouseY, fill = "lavender", outline = "cyan"):
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3)
        if (mouseX >= self.vertexNW[0]
             and mouseX <= self.vertexSE[0]
             and mouseY >= self.vertexNW[1]
             and mouseY <= self.vertexSE[1]):
             canvas.create_line((self.vertexNW[0] + self.vertexSE[0])//2, 
                                self.vertexNW[1] + 1,
                                (self.vertexNW[0] + self.vertexSE[0])//2,
                                self.vertexSE[1] - 1,
                                fill = "grey",
                                width = 3)




class HintButton(OperationButton):

    def __init__(self, prompt = "Hint", cx = 30, cy = 30, w = 40, h = 40):
        super().__init__(prompt, cx, cy, w , h)
    
    def draw(self, data, canvas, mouseX, mouseY, fill = "black", outline = "cyan"):
        if (mouseX >= self.vertexNW[0]
             and mouseX <= self.vertexSE[0]
             and mouseY >= self.vertexNW[1]
             and mouseY <= self.vertexSE[1]):
            offset = self.cx + self.cy 
            canvas.create_rectangle(offset, offset, data.width - offset, data.height - offset, fill = fill, outline = outline, width = 3)
            canvas.create_text(data.width//2, data.height//2,
                                text = "PlaceHolder Hint", font = "Helvetica 30 bold", fill = outline)
        canvas.create_rectangle(self.vertexNW, self.vertexSE, fill = fill, outline = outline, width = 3)
        canvas.create_text(self.cx, self.cy, text = self.prompt, font = "Helvetica 15 bold", fill = outline)  