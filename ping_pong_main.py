from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width-80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width-80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if sprite.collide_rect(racket1, self) or sprite.collide_rect(racket2, self):
            if self.rect.x > racket2.rect.centerx-25 or self.rect.x < racket1.rect.centerx-25:
                pass
            else:
                self.speed_x *= -1

        if self.rect.y > win_height-50 or self.rect.y < 0:
            self.speed_y *= -1

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 50, 150, 4)
racket2 = Player("racket.png", 520, 200, 50, 150, 4)
ball = Ball("tenis_ball.png", 200, 200, 50, 50, 4)

font.init()
font = font.SysFont("Arial", 35)
lose1 = font.render("Player 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("Player 2 LOSE!", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))

        racket1.reset()
        racket2.reset()
        ball.reset()
    else:
        finish = False
        time.delay(2000)
        ball.kill()
        ball = Ball("tenis_ball.png", 200, 200, 50, 50, 4)

    display.update()
    clock.tick(FPS)
