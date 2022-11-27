from pygame import*
from random import randint
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
background=transform.scale(image.load("fon2.jpg"),(1200,700))
window = display.set_mode((1200, 700))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y = self.rect.y + self.speed
            


class Anemi(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.x <= -10:
            self.rect.x = 1250
            self.rect.y = randint(0, 700)
            

cube = Player("12.png",10, 560, 80, 80, 5)

lal = sprite.Group()
lol = sprite.Group()
font1 = font.SysFont("Arial",80)
font2 = font.SysFont("Arial", 40)
lose = font1.render("Game Over", True, (255,255,0))
for i in range(1,5):
    cube2 = Anemi("fireball.png",1000, -300, 150, 150, 7)
    lol.add(cube2)
for i in range(1,4):
    cube3 = Anemi("fireball3.png",1000, -500, 100, 100, 10)
    lal.add(cube3)


run = True
clock = time.Clock()
FPS = 60
finish  = False
life = 3


while run:
 
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:   
            if key == [K_UP]:
                cube.control(-steps, 0)
    
    if not finish:
        window.blit(background,(0,0))
        cube.reset()
        cube.update()
        lol.draw(window)
        lol.update()
        lal.draw(window)
        lal.update()

    
        

        if sprite.spritecollide(cube, lol, False) or sprite.spritecollide(cube, lal,False):
            sprite.spritecollide(cube,lol, True)
            sprite.spritecollide(cube,lal,True)
            life = life - 1
        if life == 0:
            finish = True
            window.blit(lose,(500,300))

              
        
        text_life = font2.render(str(life), True, (255,0,0))
        window.blit(text_life,(650,10))
        
    else:
        finish = False
        life = 3
        for cube2 in lol:
            cube2.kill()
        for cube3 in lal:
            cube3.kill()
        time.delay(500)
        for i in range(1,5):
            cube2 = Anemi("fireball.png",1000, -300, 150, 150, 7)
            lol.add(cube2)
        for i in range(1,4):
            cube3 = Anemi("fireball3.png",1000, - 500, 100, 100, 10)
            lal.add(cube3)  

    display.update()
    clock.tick(FPS)
