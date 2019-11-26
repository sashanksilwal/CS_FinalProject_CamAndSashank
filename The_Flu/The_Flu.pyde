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


class Creature:
    def __init__(self, x, y, r, g, img, w, h, slices):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 0
        self.vx = 0
        self.img = loadImage(path + "/images/" + img)
        self.w = w
        self.h = h
        self.slices = slices
        self.frame = 0
        self.xdirection = RIGHT
        self.ydirection = UP
    
    def gravity(self):
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y + self.r)
        
        for p in game.platforms:
            if self.y + self.r <= p.y and self.x + self.r >= p.x and self.x - self.r <= p.x + p.w:
                self.g = p.y
                break
            else:
                self.g = game.g
        
    def update(self):
        self.gravity()
        
        self.y += self.vy
        self.x += self.vx
        
    def display(self):
        self.update()
        # fill(255, 255, 255)
        # stroke(0, 0, 0)
        # circle(self.x, self.y, self.r * 2)
        
        if self.direction == RIGHT:
            image(self.img, self.x - self.img_w//2, self.y -self.img_h//2, self.img_w, self.img_h, self.frame * self.img_w, 0, (self.frame +1) * self.img_w, self.img_h)
        elif self.direction == LEFT:
            image(self.img, self.x - self.img_w//2, self.y -self.img_h//2, self.img_w, self.img_h, (self.frame + 1)* self.img_w, 0, self.frame * self.img_w, self.img_h)
            
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
        
        

    
    
class Germ(Creature):
    def __init__(self, x, y, r, g, img, w, h, f, x1, y1, x2, y2):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vx = 0
        self.vy = 0
        self.xdirection = RIGHT
        self.ydirection = RIGHT
        
    def update(self):
        # no gravity, only motion -- polymorphism, so we don't call it here (I don't know how we can make this more beautiful)
        # x movements
        if self.x < self.x1:
            self.xdirection = RIGHT
            self.vx *= -1
        elif self.x > self.x2:
            self.xdirection = LEFT
            self.vx *= -1
        
        # y movements
        if self.y < self.y1:
            self.ydirection = DOWN
            self.vy *= -1
        elif self.y > self.y2:
            self.ydirection = UP
            self.vy *= -1
             
             
        if frameCount % 5 == 0:
            self.frame = (self.frame + 1) % self.slices
            
        self.y += self.vy
        self.x += self.vx
        
            
    def display(self):
        self.update()

        
class Doctor(Creature):
    def __init__(self):
        self.x = x


class Intro:
    def __init__(self):
        self.cloud = loadImage(path+"/images/cloud.png")
        self.bground = loadImage(path+"/images/intro_background.jpeg")
        self.intro = loadImage(path+"/images/intro.png")
        self.play = loadImage(path+"/images/play.png")
        self.info = loadImage(path+"/images/info.jpg")
        self.i = 0
        self.file = open(path+"/intro.txt","r")
        self.time = 1
        
    def menudisplay(self):
        image(self.bground,0,0,game.w, game.h)
        image(self.cloud,game.w//1.5,game.h//7,400,328)
        # image(self.play,100,210,300,200)
        image(self.intro,game.w//1.5,game.h//2,400,380,800*self.i,0,800*(self.i+1),600)
        fill(0)
        textSize(25)
        a = self.file.readline()
        # print(a)
        # self.time = 0
        
            # self.time += 1
            # a = self.file.readline()
            # print(a)
            # text(a,350,220)
        if frameCount % 3 ==0:
            self.i = (self.i+1)%15
        # print(mouseX,mouseY)
        image(self.play,240,160,105,60)
        image(self.play,240,400,105,60)
        image(self.play,240,280,105,60)
        fill(255,255,255)
        if 240<= mouseX <= 240+115 and 160<= mouseY <= 160+70:
            image(self.play,240,160,115,70)
        
        
        elif 240<= mouseX <= 240+115 and 280<= mouseY <= 350:
            image(self.play,240,280,115,70)
        
        
        elif 240<= mouseX <= 240+115 and 400<= mouseY <= 470:
            image(self.play,240,400,115,70)

        
    def instructions(self):
        image(self.bground,0,0)
        fill(0)
        image(self.info,game.w/8,game.h/8,game.w/1.2, game.h/1.2)
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            fill(0)
        else:
            fill(255,255,255)
        text("Back",50,650)
        
        
intro = Intro()
game = Game(1280,720,585) 
   
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
        elif 240<= mouseX <= 350 and 400<= mouseY <= 470:
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
    
    
