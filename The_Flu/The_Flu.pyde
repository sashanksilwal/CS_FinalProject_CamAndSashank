add_library('minim')
import os, time, random

player = Minim(this)

path=os.getcwd()

#loading the images as it was lagging loading it inside the class
platformimg = loadImage(path + "/images/platform.png")
germ = loadImage(path + "/images/germ.png")
germ1 = loadImage(path + "/images/germ1.png")
germ2 = loadImage(path + "/images/coin.png")
villian = loadImage(path + "/images/antagonistic.png")
# play_bground = loadImage(path+"/images/play_bground.png")
fire_img = loadImage(path + "/images/pew.png")
checkpoint = loadImage(path + "/images/checkpoint.png")
img = loadImage(path + "/images/run.png")
jmp_img = loadImage(path + "/images/jump.png")
shoot_img = loadImage(path + "/images/shoot.png")
antidote_img = loadImage(path + "/images/antidote.png")
info = loadImage(path + "/images/info.jpeg")

germ_img = []
germ_img.append(germ)
germ_img.append(germ1)
germ_img.append(germ2)

class Game:
    def __init__(self, w, h, g, l,lives):
        self.gamestate = "menu"
        self.shoot_once = True
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.time = 0
        self.pause = False
        self.y_shift = 0
        self.level = l
        
        self.speed = 0
        inputFile = open(path + "/level"+l+".csv","r")
        
        self.antidotes = []
        self.bgImgs = []
        self.germs = []
        self.fires = []
        self.platforms = []
        self.villians = []
        # self.a = 0
        
        self.doctor = Doctor(150,500, 40, self.g, "run.png", 82, 100, 6, lives)
        self.detonator = Detonator(0,1000,20,"cloud.png")

        for line in inputFile:
            line = line.strip().split(",")
            if line[0] == "platform":
                self.platforms.append(Platform(int(line[1]),int(line[2]), int(line[3]), int(line[4]), int(line[6])))
            elif line[0] == "germ":
                self.germs.append(Germ(int(line[1]),int(line[2]), int(line[3]), self.g, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), int(line[12]), float(line[13]), float(line[14])))
            elif line[0] == "antidotes":
                self.antidotes.append(Antidote(int(line[1]),int(line[2]), int(line[3]), self.g, line[5], int(line[6]), int(line[7]), int(line[8])))
            elif line[0] == "speed":
                self.speed_temp = float(line[1])
            elif line[0] == "checkpoint":
                self.checkpoint = Checkpoint(int(line[1]),int(line[2]), int(line[3]), self.g, line[5], int(line[6]), int(line[7]),int(line[8]))
            elif line[0] == "villian":
                self.villians = Villian(int(line[1]),int(line[2]), int(line[3]), self.g, line[5], int(line[6]), int(line[7]),int(line[8]))
        
    def update(self):
        
        if self.doctor.antiCnt>0:
            self.fires.append(Fire(game.doctor.x, game.doctor.y, 15, game.g, "pew.png", 40, 30, 0))
            self.doctor.antiCnt -= 1
            game.doctor.shootsound.rewind()
            game.doctor.shootsound.play()
            
    
    def display(self):
        
        if self.gamestate == "play":
            # image(play_bground,0,0,game.w, game.h)
            background(0)
            if frameRate % 2 == 0:
                fill(255,0,0)
            else:
                fill(255,0,0)
            rect(0,675,1280,5)
            for p in self.platforms:
                p.display()
    
            for g in self.germs:
                g.display()
                
            for a in self.antidotes:
                a.display()
            self.checkpoint.display()   
            self.doctor.display()
            
            fill(255,255,255)
            textSize(20)
            # self.a += 1
            # print(self.a)
            text("Antidotes: " + str(self.doctor.antiCnt), 1000, 50)
            text("Lives Remaining: " + str(self.doctor.lives), 1000, 80) 
            text("Germs Killed: " + str(self.doctor.germCnt), 1000, 110) 
            # self.fire = Fire(game.doctor.x, game.doctor.y, 50, game.g, "pew.png", 40, 30, 0)

            for f in self.fires:
                f.display()
        if self.gamestate == "info":
            image(info,0,0)
                

class Creature:
    
    def __init__(self, x, y, r, g, img, w, h, slices):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 0
        self.vx = 0
        self.img = img
        self.w = w
        self.h = h
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
        if game.gamestate == "play":
            if self.xdirection == RIGHT:
                if self.vy !=0:
                    if self.shoot == True and game.doctor.antiCnt >0 :
                        image(shoot_img, self.x-self.w//2 , self.y -self.h//2-game.y_shift, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
                    else:
                        image(jmp_img, self.x-self.w//2 , self.y -self.h//2-game.y_shift, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
                else:
                    if self.shoot == True and game.doctor.antiCnt >0:
                        image(shoot_img, self.x-self.w//2 , self.y -self.h//2-game.y_shift, self.w, self.h, self.frame_jump * self.w, 0, (self.frame_jump +1) * 75, self.h)
                    else:
                        image(img, self.x-self.w//2 , self.y -self.h//2 -game.y_shift, self.w, self.h, self.frame * self.w, 0, (self.frame +1) * self.w, self.h)
                    
                                    
            elif self.xdirection == LEFT:
                if self.vy !=0:
                    if self.shoot == True and game.doctor.antiCnt >0:
                        image(shoot_img, self.x -self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, (self.frame_jump +1) * 75, 0, self.frame_jump  * self.w, self.h)
                    else:
                        image(jmp_img, self.x -self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, (self.frame_jump +1) * 75, 0, self.frame_jump  * self.w, self.h)
                else:
                    if self.shoot == True and game.doctor.antiCnt >0:
                        image(shoot_img, self.x-self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, (self.frame_jump + 1)* self.w, 0, self.frame_jump * self.w, self.h)
                    else:
                        image(img, self.x-self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, (self.frame + 1)* self.w, 0, self.frame * self.w, self.h)
                        
                    
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
    
    
class Antidote(Creature):
    def __init__(self, x, y, r, g, img, w, h, f):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        self.frame = 1
    
    def update(self):
        if frameCount % 20 == 0:
            self.frame = (self.frame + 1) % 5
    
    def display(self):
        self.update()
        image(antidote_img,self.x-self.w//2,self.y-game.y_shift-self.h//2,self.w, self.h,self.frame * 250, 0, (self.frame+1) * 250, 250)
        
        
class Germ(Creature):
    def __init__(self, x, y, r, g, img, w, h, f, x1, y1, x2, y2, xspeed,yspeed):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vx = xspeed
        self.vy = yspeed
        self.w = w
        self.h = h
        self.xdirection = RIGHT
        self.ydirection = UP # why is this right? 
        
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
        
        if frameCount % 2 == 0:
            self.frame = (self.frame + 1) % self.slices
            
        self.y += self.vy
        self.x += self.vx
        
    def display(self):
        self.update()
        # image(self.img, self.x -self.w//2, self.y-game.y_shift-self.h//2, self.w, self.h)
        image(germ_img[self.img], self.x-self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, self.frame * 500, 0, (self.frame+1) * 500, 500)
        # image(self.img, self.x-self.w//2 , self.y -self.h//2-game.y_shift, self.w, self.h, (self.frame+1) * 500, 0, (self.frame +1) * 500, 500)
        
class Villian(Germ):
    def __init__(self, x, y, r, g, img, w, h, f, x1, y1, x2, y2, xspeed, yspeed, lives):
        Germ.__init__(self, x, y, r, g, img, w, h, f, x1, y1, x2, y2, xspeed, yspeed)
        self.lives = lives
        
    def update(self):
        if self.distance <= game.doctor.r + self.r:
            self.lives -= 1
    
    def display(self):
        # if self.lives == 0:
            # end game
        self.update()
        image(villian, self.x-self.w//2, self.y -self.h//2-game.y_shift, self.w, self.h, self.frame * 500, 0, (self.frame+1) * 500, 500)
        
    
class Fire(Creature):
    def __init__(self, x, y, r, g, img, w, h, f):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        
        if game.doctor.xdirection == RIGHT:
            self.direction = RIGHT
        elif game.doctor.xdirection == LEFT: 
            self.direction = LEFT
            
        if self.direction == RIGHT:
            self.vx = 3
        elif self.direction == LEFT:
            self.vx = -3
        
        
    def update(self):    
        self.x += self.vx
        if self.x<0 or self.x>game.w:
            game.fires.remove(self)
        # game.y_shift += -0.3
        
        for e in game.germs:
            if self.distance(e) <= self.r + e.r:
                game.germs.remove(e)
                game.fires.remove(self)
                del e
                game.doctor.germCnt += 1
        
        
    def display(self):
        self.update()
        
        if self.direction == RIGHT:
            image(fire_img, self.x-self.w//2, self.y-game.y_shift+5-self.h//2, self.w, self.h)
        elif self.direction == LEFT:
            image(fire_img, self.x-self.w-self.w//2, self.y-game.y_shift+5-self.h//2, self.w, self.h,200,150,0,0)
            
        
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5 
        
              
class Doctor(Creature):
    def __init__(self, x, y, r, g, img, w, h, F,lives):
        Creature.__init__(self, x, y, r, g, img, w, h, F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.shootsound = player.loadFile(path + "/sounds/shoot.mp3")
        self.inst_bground = loadImage(path+"/images/instructions_bground.jpeg")
        self.germCnt = 0
        self.antiCnt = 5
        self.lives = lives
        self.vy1 = -0.3
        self.shoot = False
        self.over = 645
        self.xdirection = RIGHT
        self.ydirection = DOWN
        
    def update(self):
        global game
        self.gravity()
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.xdirection = LEFT
        elif self.keyHandler[RIGHT]:
            self.vx = 5
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
        
        game.y_shift -= game.speed
        self.over -= game.speed
    
        if self.y > self.over:
            if self.lives > 0:
                change_level(game.level, self.lives - 1, "play")
            else:
                game.gamestate = "over"
                text("Game Over",500,400)
                text("Press anywhere to restart the game.", 500, 440)
    
        if frameCount % 6 == 0 and self.vx != 0 and self.vy == 0:
            self.frame = (self.frame + 1) % self.slices
            
        if frameCount %40 == 0:
            self.frame_jump = (self.frame_jump + 1) % 2

        for s in game.antidotes:
            if self.distance(s) <= self.r + s.r:
                game.antidotes.remove(s)
                self.antiCnt += 1    

        for e in game.germs:
            
            if self.distance(e) <= self.r + e.r:
                if self.vy > 0 and self.antiCnt>0:
                    game.germs.remove(e)
                    del e
                    self.vy = -2
                    self.germCnt += 1
                else:
                    if self.lives > 0:
                        change_level(game.level,self.lives-1,"play")
                        #work left
                    else:
                        game.gamestate = "over"
                        text("Game Over",500,400)
                        text("Press anywhere to restart the game.",500,440)
                    
        if self.distance(game.checkpoint) <= self.r + game.checkpoint.r:
        
            game.gamestate = "info"
            # if game.level<=2:
            # game = Game(1280,720,650,str(int(game.level)+1),game.doctor.lives) 
            
            # game.gamestate = "play"
                
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
        

class Platform:
    def __init__(self,x,y, w, h, slice):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # self.img = loadImage(path+"/images/"+img)
        self.frame = 0
        self.slice = slice
    
    def update(self):
        if frameCount % 5 ==0:
            self.frame = (self.frame+1)%self.slice
        
    def display(self):
        self.update()
        # rect(self.x , self.y-game.y_shift, self.w, self.h)
        image(platformimg, self.x , self.y-game.y_shift, self.w, self.h,self.frame * 1200, 350, (self.frame+1) * 1200, 960)        
        
    
class Checkpoint(Creature):
    def __init__(self, x, y, r, g, img, w, h, f):
        Creature.__init__(self, x, y, r, g, img, w, h, f)
        
    def display(self):
        # if self.y <= 100:
        image(checkpoint, self.x -self.w//2, self.y-game.y_shift-self.h//2, self.w, self.h)


class Detonator(Creature):
    def __init__(self, x, y, r,  img):
        # Creature.__init__(self, x, y, r, g, img, w, h, F)
        pass
    
    def display(self):
        # if self.y <= 100:
        image(self.img, self.x -self.w//2, self.y-game.y_shift-self.h//2, self.w, self.h)
        
        
# class LevelChange():
#     def __init__(self):
#         self.intro = loadImage(path+"/images/instructions_bground.jpeg")
#         image(self.intro,0,0)
#         self.display()
        
#     def display(self):
        
#         time.sleep(5)    
    
            
class Intro:
    def __init__(self):
        self.cloud = loadImage(path+"/images/cloud.png")
        self.bground = loadImage(path+"/images/intro_background.jpeg")
        self.inst_bground = loadImage(path+"/images/instructions_bground.jpeg")
        # self.game_bground  = loadImage(path+"/images/play_bground.jpg")
        self.intro = loadImage(path+"/images/intro.png")
        self.play = loadImage(path+"/images/play.png")
        self.quit = loadImage(path+"/images/quit.png")
        self.instructions = loadImage(path+"/images/instructions.png")
        
        self.bground_m =  player.loadFile(path + "/sounds/bground.mp3")

        self.i = 0
        self.time = 1
        
    def menudisplay(self):
        image(self.bground, 0, 0, game.w, game.h)
        image(self.cloud, game.w // 1.5, game.h // 7, 400, 328)
        # image(self.play,100,210,300,200)
        image(self.intro, game.w // 1.5, game.h // 2, 400, 380, 800 * self.i, 0, 800 * (self.i+1), 600)
         
        if frameCount % 3 == 0:
            self.i = (self.i+1) % 15
        # print(mouseX,mouseY)
        image(self.play, 240, 160, 105, 60)
        image(self.quit, 240, 280, 105, 60)
        image(self.instructions, 240, 400, 150, 70)
        fill(0)
        textSize(15)
        a="Hey! The evil doctor has taken over.\n It's our final opportunity to save the planet.\n Suit up doc!"
        text(a,game.w // 1.5 + 40, game.h // 7 + 60)
        fill(255, 255, 255)
        # image with greater width and height 
        if 240 <= mouseX <= 240 + 115 and 160 <= mouseY <= 160 + 70:
            image(self.play, 240, 160, 115, 70)
        
        elif 240 <= mouseX <= 240 + 115 and 280 <= mouseY <= 350:
            image(self.quit, 240, 280, 115, 70)
    
        elif 240 <= mouseX <= 240 + 160 and 400 <= mouseY <= 470:
            image(self.instructions, 240, 400, 160, 80)
    
    def instruction(self):
        
        # self.bground_m.play()
        # self.bground_m.rewind()
        
        image(self.inst_bground,0,0)
        fill(0)
        
        if 50 <= mouseX <= 105 and 635 <= mouseY <= 655:
            fill(0)
        else:
            fill(255, 255, 255)
        text("Back", 50, 650)
        
        
intro = Intro()
game = Game(1280,720,650,"1",3) 


def change_level(level,life,state):
    global game
    # del game
    game = Game(1280,720,650,str(level),life) 
    game.gamestate = state
    
   
def setup():
    size(game.w, game.h)
    background(255)


def draw():
    if not game.pause:
        # background(0,0,0)
        if game.gamestate == "menu":
            intro.menudisplay()
        elif game.gamestate == "instructions":
            intro.instruction()
        elif game.gamestate == "play":
            # intro.bground_m.close()
            game.display()
  
def mouseClicked():
    if game.gamestate == "menu":
        if 240<= mouseX <= 350 and 160<= mouseY <= 160+70:
            game.gamestate = "play"

        elif 240<= mouseX <= 350 and 280<= mouseY <= 350:
             exit()
        elif 240<= mouseX <= 350 and 400<= mouseY <= 470:
            game.gamestate = "instructions"
            
    elif game.gamestate == "instructions":
        if 50<= mouseX <= 105 and 635<= mouseY <= 655:
            game.gamestate = "menu"
            
    elif game.gamestate == "over":
        change_level("1",3,"menu")
        
        
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

    # elif  keyCode == 32 and game.doctor.shoot:
    #     game.doctor.shoot = False
    
def checkpoint_reached():
    global game
    game = Game(1280,720,650,str(int(game.level)+1),game.doctor.lives)     
    game.gamestate = "play"       
    
def keyPressed():
    if game.speed == 0:
        game.speed = game.speed_temp
    #checking is game is paused
    if keyCode == 32 and game.gamestate == "play": #checks if space bar 
        game.doctor.shoot = True
        game.update()
    if keyCode == 32 and game.gamestate == "info":
        checkpoint_reached()
        #need to add a function: class is called fire -- call that class fire, creates what is being shot and then change the value of x with right or left direction 
        
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
