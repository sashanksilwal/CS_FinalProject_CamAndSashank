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
  
game = Game(1000,800,585)    
def setup():
    size(game.w, game.h)
    background(255)
        
def keyPressed():
    pass
def keyReleased():
    pass
    
def mouseClicked():
   pass
def setup():
    size(600,750)
    background(205)
    

i = 0


def menu():
    global i
    a = "Hello"
    cloud = loadImage("images/cloud.png")
    bground = loadImage("images/baground_intro1.png")
    intro = loadImage("images/intro.png")
    image(bground,0,0,600,750)
    image(cloud,300,200,300,200)
    image(intro,250,350,400,300,800*i,0,800*(i+1),600)
    fill(0)
    textSize(15)
    text(a,350,220)
    i = (i+1)%15
    print(mouseX,mouseY)
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
        
    
def draw():
    background(0,0,0)
    if game.gamestate == "menu":
        menu()
    elif game.gamestate == "instructions":
        instructions()
        
    
 
# def keyPressed():
    # pass
        
# def keyReleased():
    # pass
    
    
