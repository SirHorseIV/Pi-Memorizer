class camera:
    def __init__(self,startPos,smooth,WINDOW_SIZE):
        self.smoothScroll=startPos
        self.WINDOW_SIZE=WINDOW_SIZE
        if smooth<=0:
            self.smooth=1
        else:
            self.smooth=1/smooth
        self.shaking=False
        self.shakeTimer=0
        self.shakeTime=10
        self.shakeOffset=2
    def update(self,focus):
        self.scroll=[self.WINDOW_SIZE[0]/2-focus[0],self.WINDOW_SIZE[1]/2-focus[1]]
        self.smoothScroll=[self.smoothScroll[0]+(self.scroll[0]-self.smoothScroll[0])*self.smooth,
                           self.smoothScroll[1]+(self.scroll[1]-self.smoothScroll[1])*self.smooth]
