add_library('minim')
import os, time, random
player = Minim(this)
path=os.getcwd()


class Game():
    def __init__(self,w,h,g):
        self.gamestate1= "menu"
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
  
game = Game(1000,750,585)    
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
    size(600,780)
    background(205)
    


def draw():
    pass
    
 
# def keyPressed():
    # pass
        
# def keyReleased():
    # pass
    
    
