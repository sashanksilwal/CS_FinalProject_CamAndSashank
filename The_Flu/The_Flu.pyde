add_library('minim')
import os, time, random
player = Minim(this)
path=os.getcwd()


class Game():
    def __init__(self,w,h,g,l):
        self.gamestate= "menu"
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.time = 0
        self.pause = False
        self.level = l
        self.enemies = []
        self.platforms = []
        # inputFile = open(path+"/level"+l,"r")
        self.game_bground = loadImage(path+"/images/cloud.png")
        self.antidotes = []
        self.bgImgs = []
        self.germs = []
        self.platforms = []
        
        #adding the germs
        self.germs.append(Germ(300, 400, 35, self.g, "play.png", 70, 70, 5, 300, 800,800,1000,1))
        self.germs.append(Germ(300, 300, 35, self.g, "play.png", 70, 70, 5, 300, 800,1000,1000,1.5))
        self.germs.append(Germ(300, 200, 35, self.g, "play.png", 70, 70, 5, 300, 800,400,1000,0.6))
        self.germs.append(Germ(300, 100, 35, self.g, "play.png", 70, 70, 5, 300, 800,400,1000,2))
        
        self.antidotes.append(Antidote())
        
        self.doctor = Doctor(50,50, 40, self.g, "run.png", 82, 100, 6)
        
        self.platforms.append(Platform(170,420, 100, 20, "cloud.png"))
        self.platforms.append(Platform(500,400, 100, 20, "cloud.png"))
        self.platforms.append(Platform(750,350, 100, 20, "cloud.png"))
        
        # for line in inputFile:
            # line = line.strip().split(",")
            # if line[0] == "platform":
            #     self.platforms.append(Platform(int(line[1]),int(line[2]), int(line[3]), int(line[4]), line[5]))
        #     elif line[0] == "germ":
        #         self.enemies.append(Germ(int(line[1]),int(line[2]), int(line[3]), int(line[4]), line[5], int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10])))
        #     elif line[0] == "ground":
        #         self.g = int(line[2])
    
    def display(self):
        
        if self.gamestate == "play":
            background(0)
            # image(game.game_bground, 0,0,game.w,game.h)
            for p in self.platforms:
                p.display()
    
            for g in self.germs:
                g.display()
            self.doctor.display()


class Creature:
    def __init__(self, x, y, r, g, img, w, h, slices):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 0
        self.vx = 0
        self.img = loadImage(path + "/images/" + img)
        self.jmp_img = loadImage(path + "/images/jump.png")
        self.shoot_img = loadImage(path + "/images/shoot.png")
        self.w = w
        self.h = h
        self.direction = RIGHT
        self.slices = slices
        self.frame = 0
        self.frame_jump = 0
        self.xdirection = RIGHT
        self.ydirection = DOWN
    
    def gravity(self):
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y + self.r)
        
        for p in game.platforms:
            if self.y + self.r <= p.y and self.x+self.r >= p.x and self.x <= p.x+p.w:
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
        fill(255, 255, 255)
        stroke(0, 0, 0)
        
        if self.xdirection == RIGHT:
            if self.vy !=0:
                if self.shoot == True:
                    image(self.shoot_img, self.x-self.w//2 , self.y -self.h//2, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
                else:
                    image(self.jmp_img, self.x-self.w//2 , self.y -self.h//2, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
            else:
                if self.shoot == True:
                    image(self.shoot_img, self.x-self.w//2 , self.y -self.h//2, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
                else:
                    image(self.img, self.x-self.w//2 , self.y -self.h//2 , self.w, self.h, self.frame * self.w, 0, (self.frame +1) * self.w, self.h)
                
                                
        elif self.xdirection == LEFT:
            if self.vy !=0:
                if self.shoot == True:
                    image(self.shoot_img, self.x -self.w//2, self.y -self.h//2, self.w, self.h, (self.frame_jump +1) * 75, 0, self.frame_jump  * self.w, self.h)
                else:
                    image(self.jmp_img, self.x -self.w//2, self.y -self.h//2, self.w, self.h, (self.frame_jump +1) * 75, 0, self.frame_jump  * self.w, self.h)
            else:
                if self.shoot == True:
                    image(self.shoot_img, self.x-self.w//2, self.y -self.h//2, self.w, self.h, (self.frame_jump + 1)* self.w, 0, self.frame_jump * self.w, self.h)
                else:
                    image(self.img, self.x-self.w//2, self.y -self.h//2, self.w, self.h, (self.frame + 1)* self.w, 0, self.frame * self.w, self.h)
                    
                    
                
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
    
class Germ(Creature):
    def __init__(self, x, y, r, g, img, w, h, f, x1, y1, x2, y2, xspeed):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vx = xspeed
        self.vy = 0
        self.w = w
        self.h = h
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
        image(self.img, self.x , self.y, self.w, self.h)

        
class Doctor(Creature):
    def __init__(self, x, y, r, g, img, w, h, F):
        Creature.__init__(self,x, y, r, g, img, w, h, F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.germCnt = 0
        self.antiCnt = 0
        self.shoot = False
        
    def update(self):
        self.gravity()
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.xdirection = LEFT
        elif self.keyHandler[RIGHT]:
            self.vx = 8
            self.xdirection = RIGHT
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.ydirection = UP
        
            self.vy = -15
            
        if self.x - self.r < 0:
            self.x = self.r 
            
        if self.x + self.r >= game.w:
            self.x = game.w-self.r
        
        self.x += self.vx
        self.y += self.vy
        
        # if self.x >= game.w//2:
        #     game.x += self.vx
        
        if frameCount % 6 == 0 and self.vx != 0 and self.vy == 0:
            self.frame = (self.frame + 1) % self.slices
        if frameCount %20 == 0 :
            self.frame_jump = (self.frame_jump + 1) % 2

        # for s in germs.antidote:
            # if self.distance(s) <= self.r + s.r:
            #     g.stars.remove(s)
            #     self.antiCnt += 1    

        for e in game.germs:
            if self.distance(e) <= self.r + e.r:
                if self.vy > 0:
                    game.germs.remove(e)
                    del e
                    self.vy = -2
                    self.germCnt += 1
            # else:
            #     game.pause = True
                    
            
                # else:
                #     g.bgSound.pause()
                #     g.__init__(1280,720,585)
                
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
        

class Platform:
    def __init__(self,x,y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+"/images/"+img)

    
    def display(self):
        rect(self.x , self.y, self.w, self.h)
        image(self.img, self.x , self.y, self.w, self.h)
        pass
    
class Antidote:
    def __init__(self):
        pass
    
            
class Intro:
    def __init__(self):
        self.cloud = loadImage(path+"/images/cloud.png")
        self.bground = loadImage(path+"/images/intro_background.jpeg")
        self.inst_bground = loadImage(path+"/images/instructions_bground.jpeg")
        self.intro = loadImage(path+"/images/intro.png")
        self.play = loadImage(path+"/images/play.png")
        self.i = 0
        self.time = 1
        
    def menudisplay(self):
        image(self.bground,0,0,game.w, game.h)
        image(self.cloud,game.w//1.5,game.h//7,400,328)
        # image(self.play,100,210,300,200)
        image(self.intro,game.w//1.5,game.h//2,400,380,800*self.i,0,800*(self.i+1),600)
        fill(0)
        textSize(25)
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
        image(self.inst_bground,0,0)
        fill(0)
        
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            fill(0)
        else:
            fill(255,255,255)
        text("Back",50,650)
        
        
intro = Intro()
game = Game(1280,720,585,"1") 
   
def setup():
    size(game.w, game.h)
    background(255)

def draw():
    if not game.pause:
        # background(0,0,0)
        if game.gamestate == "menu":
            intro.menudisplay()
        elif game.gamestate == "instructions":
            intro.instructions()
        elif game.gamestate == "play":
            
            game.display()
                
def mouseClicked():
    if game.gamestate == "menu":
        if 240<= mouseX <= 350 and 160<= mouseY <= 160+70:
            game.gamestate = "play"

        elif 100<= mouseX <= 152 and 363<= mouseY <= 385:
            pass
        #     game.gamestate = "exit"
        elif 240<= mouseX <= 350 and 400<= mouseY <= 470:
            game.gamestate = "instructions"
            
    elif game.gamestate == "instructions":
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            game.gamestate = "menu"
        
def keyReleased():
    if keyCode == LEFT:
        game.doctor.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.doctor.keyHandler[RIGHT] = False
    elif keyCode == UP:
        game.doctor.keyHandler[UP] = False
        game.doctor.ydirection = DOWN   
        
    elif game.doctor.shoot == True:
        game.doctor.shoot = False
    
def keyPressed():
    #checking is game is paused
    if keyCode == 32:
        game.doctor.shoot = True
    elif keyCode == 80:
        if game.pause:
            game.pause = False
        else:
            game.pause = True
    elif keyCode == LEFT:
        game.doctor.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        game.doctor.keyHandler[RIGHT] = True
    elif keyCode == UP:
        game.doctor.keyHandler[UP] = True
    elif keyCode == 80:
        if game.pause:
            game.pause = False
        else:
            game.pause = True
            game.bgSound.pause()
