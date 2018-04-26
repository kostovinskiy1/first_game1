
import pygame
import os
import random
#import image

# it is better to have an extra variable, than an extremely long line.
img_path = os.path.join('C:\\Users\\user\\PycharmProjects\\homeWork', 'car.png')
img_path1 = os.path.join('C:\\Users\\user\\PycharmProjects\\homeWork', 'mario.png')
img_path2 = os.path.join('C:\\Users\\user\\PycharmProjects\\homeWork', 'gameover.png')
class Car(object):
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image,(100,200))
        # the car position
        self.x = 400
        self.y = 400

    def handle_keys(self):

        key = pygame.key.get_pressed()
        dist = 7
        if (key[pygame.K_RIGHT]) and (self.x<800-25*dist):
            self.x += dist
        elif (key[pygame.K_LEFT]) and (self.x>5*dist):
            self.x -= dist

    def draw(self, surface):

        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load(img_path1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = random.randint(0+35,800-25*7)
        self.y = 0
        self.speed=10

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class GameOver(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load(img_path2)
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.x = 0
        self.y = 0


    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))


def intersection(x1,y1,xd,yd,x2,y2,xdd,ydd):

    if  ((xdd+x2>xd) and (xdd+x2<xd+x1) and (ydd-y2<yd)  and (ydd-y2>yd-y1)) or  ((xdd>xd) and (xdd<xd+x1) and (ydd-y2<yd) and (ydd-y2>yd-y2)):
        a=True
        return a


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Crazy Race")
car = Car() # create an instance
enemy = Enemy() # create Enemy Mario

clock = pygame.time.Clock()
enemy.draw(screen)
running = True

while running:
    enemy.y = enemy.y + enemy.speed
    if enemy.y>car.y+10*enemy.speed:
        enemy=Enemy()
    if intersection(car.image.get_width(),car.image.get_height(),car.x,car.y,enemy.image.get_width(),car.image.get_height(),enemy.x,enemy.y)==True:
        enemy.speed=0
        pygame.quit()
        gameover=GameOver()
        gameover.draw(gameover.image)
        pygame.display.update()
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    car.handle_keys() # handle the keys

    screen.fill((100,100,100))
    car.draw(screen) # draw the car to the screen
    enemy.draw(screen) # draw the enemy
    pygame.display.update() # update the screen

    clock.tick(40)