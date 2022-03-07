import pygame


class inputHandler:
    def __init__(self):
        self.held=False
        self.character=""
        self.quit=False
        self.K_arrows={
            "left":False,
            "right":False,
            "up":False,
            "down":False
        }
        self.K_a=False
        self.K_b=False
        self.K_c=False
        self.K_d=False
        self.K_e=False
        self.K_f=False
        self.K_g=False
        self.K_h=False
        self.K_i=False
        self.K_j=False
        self.K_k=False
        self.K_l=False
        self.K_m=False
        self.K_n=False
        self.K_o=False
        self.K_p=False
        self.K_q=False
        self.K_r=False
        self.K_s=False
        self.K_t=False
        self.K_u=False
        self.K_v=False
        self.K_w=False
        self.K_x=False
        self.K_y=False
        self.K_z=False
        self.K_0=False
        self.K_1=False
        self.K_2=False
        self.K_3=False
        self.K_4=False
        self.K_5=False
        self.K_6=False
        self.K_7=False
        self.K_8=False
        self.K_9=False
        self.K_period=False
    def getInput(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.quit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.K_arrows["left"]=True
                if event.key==pygame.K_RIGHT:
                    self.K_arrows["right"]=True
                if event.key==pygame.K_UP:
                    self.K_arrows["up"]=True
                if event.key==pygame.K_DOWN:
                    self.K_arrows["down"]=True
                if event.key==pygame.K_a:
                    self.K_a=True
                if event.key==pygame.K_b:
                    self.K_b=True
                if event.key==pygame.K_c:
                    self.K_c=True
                if event.key==pygame.K_d:
                    self.K_d=True
                if event.key==pygame.K_e:
                    self.K_e=True
                if event.key==pygame.K_f:
                    self.K_f=True
                if event.key==pygame.K_g:
                    self.K_g=True
                if event.key==pygame.K_h:
                    self.K_h=True
                if event.key==pygame.K_i:
                    self.K_i=True
                if event.key==pygame.K_j:
                    self.K_j=True
                if event.key==pygame.K_k:
                    self.K_k=True
                if event.key==pygame.K_l:
                    self.K_l=True
                if event.key==pygame.K_m:
                    self.K_m=True
                if event.key==pygame.K_n:
                    self.K_n=True
                if event.key==pygame.K_o:
                    self.K_o=True
                if event.key==pygame.K_p:
                    self.K_p=True
                if event.key==pygame.K_q:
                    self.K_q=True
                if event.key==pygame.K_r:
                    self.K_r=True
                if event.key==pygame.K_s:
                    self.K_s=True
                if event.key==pygame.K_t:
                    self.K_t=True
                if event.key==pygame.K_t:
                    self.K_t=True
                if event.key==pygame.K_u:
                    self.K_u=True
                if event.key==pygame.K_v:
                    self.K_v=True
                if event.key==pygame.K_w:
                    self.K_w=True
                if event.key==pygame.K_x:
                    self.K_x=True
                if event.key==pygame.K_y:
                    self.K_y=True
                if event.key==pygame.K_z:
                    self.K_z=True
                if event.key==pygame.K_0:
                    self.K_0=True
                if event.key==pygame.K_1:
                    self.K_1=True
                if event.key==pygame.K_2:
                    self.K_2=True
                if event.key==pygame.K_3:
                    self.K_3=True
                if event.key==pygame.K_4:
                    self.K_4=True
                if event.key==pygame.K_5:
                    self.K_5=True
                if event.key==pygame.K_6:
                    self.K_6=True
                if event.key==pygame.K_7:
                    self.K_7=True
                if event.key==pygame.K_8:
                    self.K_8=True
                if event.key==pygame.K_9:
                    self.K_9=True
                if event.key==pygame.K_PERIOD:
                    self.K_period=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.K_arrows["left"]=False
                    self.held=False
                if event.key==pygame.K_RIGHT:
                    self.K_arrows["right"]=False
                    self.held=False
                if event.key==pygame.K_UP:
                    self.K_arrows["up"]=False
                    self.held=False
                if event.key==pygame.K_DOWN:
                    self.K_arrows["down"]=False
                    self.held=False
                if event.key==pygame.K_a:
                    self.K_a=False
                    self.held=False
                if event.key==pygame.K_b:
                    self.K_b=False
                    self.held=False
                if event.key==pygame.K_c:
                    self.K_c=False
                    self.held=False
                if event.key==pygame.K_d:
                    self.K_d=False
                    self.held=False
                if event.key==pygame.K_e:
                    self.K_e=False
                    self.held=False
                if event.key==pygame.K_f:
                    self.K_f=False
                    self.held=False
                if event.key==pygame.K_g:
                    self.K_g=False
                    self.held=False
                if event.key==pygame.K_h:
                    self.K_h=False
                    self.held=False
                if event.key==pygame.K_i:
                    self.K_i=False
                    self.held=False
                if event.key==pygame.K_j:
                    self.K_j=False
                    self.held=False
                if event.key==pygame.K_k:
                    self.K_k=False
                    self.held=False
                if event.key==pygame.K_l:
                    self.K_l=False
                    self.held=False
                if event.key==pygame.K_m:
                    self.K_m=False
                    self.held=False
                if event.key==pygame.K_n:
                    self.K_n=False
                    self.held=False
                if event.key==pygame.K_o:
                    self.K_o=False
                    self.held=False
                if event.key==pygame.K_p:
                    self.K_p=False
                    self.held=False
                if event.key==pygame.K_q:
                    self.K_q=False
                    self.held=False
                if event.key==pygame.K_r:
                    self.K_r=False
                    self.held=False
                if event.key==pygame.K_s:
                    self.K_s=False
                    self.held=False
                if event.key==pygame.K_t:
                    self.K_t=False
                    self.held=False
                if event.key==pygame.K_t:
                    self.K_t=False
                    self.held=False
                if event.key==pygame.K_u:
                    self.K_u=False
                    self.held=False
                if event.key==pygame.K_v:
                    self.K_v=False
                    self.held=False
                if event.key==pygame.K_w:
                    self.K_w=False
                    self.held=False
                if event.key==pygame.K_x:
                    self.K_x=False
                    self.held=False
                if event.key==pygame.K_y:
                    self.K_y=False
                    self.held=False
                if event.key==pygame.K_z:
                    self.K_z=False
                    self.held=False
                if event.key==pygame.K_0:
                    self.K_0=False
                    self.held=False
                if event.key==pygame.K_1:
                    self.K_1=False
                    self.held=False
                if event.key==pygame.K_2:
                    self.K_2=False
                    self.held=False
                if event.key==pygame.K_3:
                    self.K_3=False
                    self.held=False
                if event.key==pygame.K_4:
                    self.K_4=False
                    self.held=False
                if event.key==pygame.K_5:
                    self.K_5=False
                    self.held=False
                if event.key==pygame.K_6:
                    self.K_6=False
                    self.held=False
                if event.key==pygame.K_7:
                    self.K_7=False
                    self.held=False
                if event.key==pygame.K_8:
                    self.K_8=False
                    self.held=False
                if event.key==pygame.K_9:
                    self.K_9=False
                    self.held=False
                if event.key==pygame.K_PERIOD:
                    self.K_period=False
                    self.held=False
    def getStringInput(self):
        if not self.held:
            if self.K_a:
                self.character="a"
                self.held=True
            elif self.K_b:
                self.character="b"
                self.held=True
            elif self.K_c:
                self.character="c"
                self.held=True
            elif self.K_d:
                self.character="d"
                self.held=True
            elif self.K_e:
                self.character="e"
                self.held=True
            elif self.K_f:
                self.character="f"
                self.held=True
            elif self.K_g:
                self.character="g"
                self.held=True
            elif self.K_h:
                self.character="h"
                self.held=True
            elif self.K_i:
                self.character="i"
                self.held=True
            elif self.K_j:
                self.character="j"
                self.held=True
            elif self.K_k:
                self.character="k"
                self.held=True
            elif self.K_l:
                self.character="l"
                self.held=True
            elif self.K_m:
                self.character="m"
                self.held=True
            elif self.K_n:
                self.character="n"
                self.held=True
            elif self.K_o:
                self.character="o"
                self.held=True
            elif self.K_p:
                self.character="p"
                self.held=True
            elif self.K_q:
                self.character="q"
                self.held=True
            elif self.K_r:
                self.character="r"
                self.held=True
            elif self.K_s:
                self.character="s"
                self.held=True
            elif self.K_t:
                self.character="t"
                self.held=True
            elif self.K_u:
                self.character="u"
                self.held=True
            elif self.K_v:
                self.character="v"
                self.held=True
            elif self.K_w:
                self.character="w"
                self.held=True
            elif self.K_x:
                self.character="x"
                self.held=True
            elif self.K_y:
                self.character="y"
                self.held=True
            elif self.K_z:
                self.character="z"
                self.held=True
            elif self.K_0:
                self.character="0"
                self.held=True
            elif self.K_1:
                self.character="1"
                self.held=True
            elif self.K_2:
                self.character="2"
                self.held=True
            elif self.K_3:
                self.character="3"
                self.held=True
            elif self.K_4:
                self.character="4"
                self.held=True
            elif self.K_5:
                self.character="5"
                self.held=True
            elif self.K_6:
                self.character="6"
                self.held=True
            elif self.K_7:
                self.character="7"
                self.held=True
            elif self.K_8:
                self.character="8"
                self.held=True
            elif self.K_9:
                self.character="9"
                self.held=True
            elif self.K_period:
                self.character="."
                self.held=True
            return
        self.character=""
