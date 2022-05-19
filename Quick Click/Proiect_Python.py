import pygame
import random
from random import randrange
pygame.init()

Red = (197,55,48)
Red2 = (161, 35, 35)
Red3 = (133, 27, 27)
Red4 = (89, 15, 15)
White = (255, 255, 255)
Gray = (10, 10, 10)
Black = (0, 0, 0)

font = pygame.font.Font("Pixellari.ttf", 80)
font2 = pygame.font.Font("Pixellari.ttf", 150)

timer = 30000
dt = 0

fnr = str(0)
T = int((timer-dt)/1000)
realtime = str(T)
K = 0
realscore = str(K)

score = font.render('Score: ', True, White, None)
nr = font.render(realscore, True, White, None)
time = font.render("Time: ", True, White, None)
sec = font.render(realtime, True, White, None)
final = font2.render("Final score: ", True, White, None)
finalnr = font2.render(fnr, True, White, None)

scoreRect = score.get_rect()
scoreRect.topleft = (10, 10)

nrRect = nr.get_rect()
nrRect.topleft = (250, 10)

finalRect = final.get_rect()
finalRect.center = (560, 300)

finalnrRect = finalnr.get_rect()
finalnrRect.center = (1050, 300)

timeRect = time.get_rect()
timeRect.topright = (1000, 10)

secRect = sec.get_rect()
secRect.topright = (1100, 10)

img = pygame.image.load("spacebg.jpg")
img = pygame.transform.scale(img, (1280, 720))

start_img = pygame.image.load('start_btn.png')
start_img = pygame.transform.scale(start_img, (385, 150))

quit_img = pygame.image.load('exit_btn.jpg')
quit_img = pygame.transform.scale(quit_img, (385, 150))

#fereastra jocului
screen=pygame.display.set_mode((1280,720))
screen.blit(img,(0,0))
pygame.display.set_caption("Quick Click")

clock=pygame.time.Clock()
FPS=60

class Border():
    def __init__(self):
        self.x = 0
        self.y = 0
    def draw(self):
        self.bord = pygame.draw.rect(screen, Black, pygame.Rect(0, 0, 1280, 100))

#buton de start
class ButtonStart():
    def __init__(self):       
        self.image=start_img
        self.x = 440
        self.y = 300
    def drawrect (self):
        self.rect = pygame.Rect((self.x, self.y), (385, 150))
    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))
buttonstart=ButtonStart()

#buton de iesire din joc
class ButtonQuit():
    def __init__(self):       
        self.image=quit_img
        self.x = 440
        self.y = 500
    def drawrect (self):
        self.rect = pygame.Rect((self.x, self.y), (385, 150))
    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))
buttonquit=ButtonQuit()

#cercul pe care se va da click, fiecare cerc nou va avea coordonate random
class Ball():
    def __init__(self):
        self.x = randrange(100, 1200)
        self.y = randrange(200, 650)
    def drawrect (self):
        self.rect = pygame.Rect((self.x-75, self.y-75), (147, 147))
    def draw(self):
        pygame.draw.circle(screen, Gray, (self.x,self.y), 75)
        pygame.draw.circle(screen, Red4, (self.x,self.y), 71)
        pygame.draw.circle(screen, Red3, (self.x,self.y), 52)
        pygame.draw.circle(screen, Red2, (self.x,self.y), 32)
        pygame.draw.circle(screen, Red, (self.x,self.y), 15)
    
#jocul propriu-zis
def game():
    border=Border()
    img = pygame.image.load("spacebg.jpg")
    img = pygame.transform.scale(img, (1280, 720))
    screen=pygame.display.set_mode((1280, 720))
    screen.blit(img, (0, 0))
    pygame.display.set_caption("Quick Click")
    border.draw()
    pygame.display.update()

    timer=30000
    dt=0
    T = int((timer-dt)/1000)
    realtime = str(T)
    current_time=0
    button_press_time=0
    ball=Ball()
    K = 0
    realscore = str(K)
    sec = font.render(realtime, True, White, None)
    nr = font.render(realscore, True, White, None)
    first = True

    while True: 
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.rect.collidepoint(pygame.mouse.get_pos()):
                    if (first == True):
                        button_press_time = pygame.time.get_ticks()
                        first = False

                    screen.blit(img, (0, 0))
                    ball=Ball()
                    ball.draw()
                    ball.drawrect()

                    K+=1
                    realscore = str(K)
                    nr = font.render(realscore, True, White, None)

                    screen.blit(score, scoreRect)
                    screen.blit(nr, nrRect)
                    screen.blit(time, timeRect)
                    pygame.display.update()

        current_time=pygame.time.get_ticks()

        if(button_press_time != 0):
            dt = current_time-button_press_time
            T = int((timer-dt)/1000)
            realtime=str(T)  
            sec = font.render(realtime, True, White, None)
            border.draw()
            screen.blit(score, scoreRect)
            screen.blit(nr, nrRect)
            screen.blit(time, timeRect)
            screen.blit(sec, secRect)
            pygame.display.update()

        if(T == 0):
            finalnr = font2.render(realscore, True, White, None)
            screen.blit(img, (0, 0))

            screen.blit(final, finalRect)
            screen.blit(finalnr, finalnrRect)

            pygame.display.update()
            pygame.time.delay(5000)
            return
        
        screen.blit(score, scoreRect)
        screen.blit(nr, nrRect)
        screen.blit(sec, secRect)
        screen.blit(time, timeRect)
        ball.draw()
        ball.drawrect()
        clock.tick(FPS)

#meniul principal
def mainmenu():
    pygame.display.set_caption("Menu")

    while True:
        #apar butoanele Start si Quit
        screen = pygame.display.set_mode((1280, 720))
        screen.blit(img, (0, 0))
        menu_text = font2.render("Quick Click", True, White)
        menu_rect = menu_text.get_rect(center=(640, 150))
        buttonstart = ButtonStart()
        buttonstart.drawrect()
        buttonstart.draw()
        buttonquit = ButtonQuit()
        buttonquit.drawrect()
        buttonquit.draw()
        screen.blit(menu_text, menu_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonstart.rect.collidepoint(pygame.mouse.get_pos()):
                    game()
                if buttonquit.rect.collidepoint(pygame.mouse.get_pos()):
                    return
mainmenu()
pygame.quit()
