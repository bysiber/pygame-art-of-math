import pygame,sys
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
            y = math.sin(alpha+i/counter)*math.cos(alpha+i-counter2)*300
            x = math.sin(alpha-i/counter)*math.sin(alpha+i-counter2)*300 
            
            p = i*255/counter # transparent !!!
            pygame.draw.aaline(screen,[255-p,255-p,255-p],(int(200+x),int(200+y)),(int(600+x),int(400+y)))
            

        pygame.time.wait(5)
        pygame.display.update()

                      
