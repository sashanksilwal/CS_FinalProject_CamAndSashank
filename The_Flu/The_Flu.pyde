add_library('minim')
import os, time, random
player = Minim(this)
path=os.getcwd()


class Game():
    def __init__(self,w,h,g):
        self.gamestate= "menu"
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.time = 0
        self.pause = False
        # self.pauseSound = player.loadFile(path + "sounds/pause.mp3")
        # self.bgSound = player.loadFile(path + "sounds/background.mp3")
        # self.bgSound.play()
        # self.bgSound.loop()
        self.enemies = []
        self.platforms = []


class Creature():
    def __init__(self,x,y,g,img,w,h):
        self.x = x
        
        
class Doctor(Creature):
    def __init__(self):
        self.x = x
    
class Germs(Creature):
    def __init__(self):
        self


class Intro:
    def __init__(self):
        self.cloud = loadImage(path+"/images/cloud.png")
        self.bground = loadImage(path+"/images/baground_intro1.png")
        self.intro = loadImage(path+"/images/intro.png")
        self.play = loadImage(path+"/images/play.png")
        self.i = 0
        self.file = open(path+"/intro.txt","r")
        self.time = 1
        
    def menudisplay(self):
        image(self.bground,0,0,600,750)
        image(self.cloud,300,200,300,200)
        # image(self.play,100,210,300,200)
        image(self.intro,250,350,400,300,800*self.i,0,800*(self.i+1),600)
        fill(0)
        textSize(25)
        a = self.file.readline()
        # print(a)
        # self.time = 0
        if frameCount % 2 ==0:
            # self.time += 1
            # a = self.file.readline()
            # print(a)
            text(a,350,220)
        self.i = (self.i+1)%15
        # print(mouseX,mouseY)
        fill(255,0,255)
        if 100<= mouseX <= 157 and 294<= mouseY <= 312:
            fill(255,255,255)
        textSize(25)
        text("Start",100,310)
        fill(255,0,255)
        if 100<= mouseX <= 152 and 363<= mouseY <= 385:
            fill(255,255,255)
        textSize(25)
        text("Quit",100,380)
        fill(255,0,255)
        if 100<= mouseX <= 242 and 445<= mouseY <= 465:
            fill(255,255,255)
        textSize(25)
        text("Instructions",100,460)
        
    def instructions(self):
        image(self.bground,0,0,600,750)
        fill(0)
        rect(100,150,400,450)
        textSize(25)
        
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            fill(0)
        else:
            fill(255,255,255)
        text("Back",50,650)
        
        
intro = Intro()
game = Game(600,750,585) 
   
def setup():
    size(game.w, game.h)
    background(255)

def draw():
    # background(0,0,0)
    if game.gamestate == "menu":
        intro.menudisplay()
    elif game.gamestate == "instructions":
        intro.instructions()
    elif game.gamestate == "play":
        pass
                
def mouseClicked():
    if game.gamestate == "menu":
        if 100<= mouseX <= 157 and 294<= mouseY <= 312:
            pass
            # game.gamestate = "play"
        elif 100<= mouseX <= 152 and 363<= mouseY <= 385:
            pass
        #     game.gamestate = "exit"
        elif 100<= mouseX <= 242 and 445<= mouseY <= 465:
            game.gamestate = "instructions"
            
    elif game.gamestate == "instructions":
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            game.gamestate = "menu"
        
def keyReleased():
    game.gamestate = "menu"

    
def keyPressed():

   game.gamestate = "paused"

# def keyPressed():
    # pass
        
# def keyReleased():
    # pass
    
    
