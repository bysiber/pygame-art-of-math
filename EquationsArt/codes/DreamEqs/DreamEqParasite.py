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
            counter += 1
            counter2 += 0.1

        alpha += 0.01

        screen.fill([0,0,0])
        for i in range(counter):
            n = i+1
            z = 2*math.pi/(counter)
            y = math.cos(alpha-i)**3*i
            x = math.sin(alpha*i)**3*i

            pygame.draw.aaline(screen,[255,255,255],(int(411+x),int(411+y)),(int(400+x),int(400+y)))
            

        pygame.time.wait(5)
        pygame.display.update()

                      