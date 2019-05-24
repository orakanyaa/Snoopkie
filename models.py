import arcade
import arcade.key
from random import randint

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class Cookie(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__("images/cookie.png",0.5)
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self):
        self.center_y -= self.speed

class Bomb(arcade.Sprite):
    def __init__(self, x, y, speed):
        super().__init__("images/bombb.png",0.75)
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self):
        self.center_y -= self.speed        

class Snoopy(arcade.Sprite):
    def __init__(self, link, size):
        super().__init__(link, size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 100
        self.change_x = 0
        self.direc = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x = -5
            self.direc = False
        if key == arcade.key.RIGHT:
            self.change_x = 5
            self.direc = True
        if key == arcade.key.SPACE:
            if self.direc :
                self.change_x = 8
            else :
                self.change_x = -8
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.SPACE:
            self.change_x = 0
    
    def is_end(self):
        if self.center_x > 680 :
            self.center_x = 680
        elif self.center_x < 20 :
            self.center_x = 20

    def update(self):
        super().draw()
        self.is_end()
        self.center_x += self.change_x           

class Monster(arcade.Sprite):
    def __init__(self, link,size, Snoopy):
        super().__init__(link,size)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT - 100
        self.Snoopy = Snoopy
        self.speed = 3
        self.Cookie = []
        self.Bomb = []
        self.score = 0
        self.throw = 0
        
    def movement(self):
        if self.center_x > 660 or self.center_x < 20:
            self.speed *= -1
        self.center_x += self.speed

    def create(self):
        if self.score > 100:
            time = randint(5,10)
        else : 
            time = randint(0,10)
        if time > 3:
            if self.score > 100:
                self.Cookie.append(Cookie(self.center_x,self.center_y,randint(3,10)))     
            else :
                self.Cookie.append(Cookie(self.center_x,self.center_y,randint(2,4))) 
        if time > 7:
            if self.score > 150:
                self.Bomb.append(Bomb(self.center_x,self.center_y,randint(5,9)))
            else:
                self.Bomb.append(Bomb(self.center_x,self.center_y,randint(1,4)))

    def update(self):
        if self.score < 0 :
            return
        else :
            self.throw += 1
            self.movement()
            if self.throw == 30:     
                self.create()
                self.throw = 0
            for Cookie in self.Cookie:
                if arcade.check_for_collision(Cookie,self.Snoopy):
                    self.Cookie.remove(Cookie)
                    if self.score > 100:
                        self.score += 2
                    else :
                        self.score += 2
                if Cookie.center_y < 0:
                    self.Cookie.remove(Cookie)
                Cookie.update()
            for Bomb in self.Bomb:
                if arcade.check_for_collision(Bomb,self.Snoopy):
                    self.Bomb.remove(Bomb)
                    if self.score > 100 :
                        # self.score -= randint(35,115)
                        self.score -= 5
                    else :
                        # self.score -= randint(15,40)
                        self.score -= 5
                if Bomb.center_y < 0:
                    self.Bomb.remove(Bomb)
                Bomb.update()
      
    def on_draw(self):
        super().draw()
        for Cookie in self.Cookie:
            Cookie.draw()
        for Bomb in self.Bomb:
            Bomb.draw()
