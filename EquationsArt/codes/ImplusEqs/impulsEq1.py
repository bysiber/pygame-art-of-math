import pygame,sys
import Equations as eqs
import math
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 800
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
alpha = 0
counter = 1
counter2 = 1

Tur = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[0]:
            Tur = True
            screen.fill([0,0,0])

    while Tur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if alpha >= 2*math.pi :
            alpha = 0.01

        if pygame.mouse.get_pressed()[0]:
            counter += 0.1
            counter2 += 0.1

        alpha += 0.01

        screen.fill([0,0,0])
        counter = 800
        for i in range(counter):
            n = i+1
            z = 2*math.pi/(counter)
            x = math.sin(alpha+(i+1)*(2*math.pi/(counter2)))*100*math.cos(alpha+(i+1))*3
            y = math.cos(alpha+(i+1)*(2*math.pi/(counter2)))*math.cos(alpha+(i+1))*300
            
            p = i*255/counter # transparent !!!
            pygame.draw.circle(screen,[p,p,255-p],(int(400+x),int(400+y)),p/16,0)
            

        pygame.time.wait(5)
        pygame.display.update()

                      