import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Anna") 

valge = (255, 255, 255)
must = (0, 0, 0)
oranž = (255, 165, 0)
sinine = (0, 0, 255)
pruun = (139, 69, 19)
punane = (255, 0, 0)
aken.fill(sinine)

# keha
pygame.draw.circle(aken, valge, (150, 220), 50) # нижний круг
pygame.draw.circle(aken, valge, (150, 150), 35) # средний круг
pygame.draw.circle(aken, valge, (150, 90), 30) # голова

# silmad
pygame.draw.circle(aken, must, (142, 85), 3)
pygame.draw.circle(aken, must, (158, 85), 3)

# naeratus
pygame.draw.circle(aken, must, (140, 105), 2)
pygame.draw.circle(aken, must, (145, 108), 2)
pygame.draw.circle(aken, must, (150, 109), 2)
pygame.draw.circle(aken, must, (155, 108), 2)
pygame.draw.circle(aken, must, (160, 105), 2)

#müts
pygame.draw.rect(aken, must, (120, 60, 60, 12)) 
pygame.draw.rect(aken, must, (130, 30, 40, 35)) 

#nupud
pygame.draw.circle(aken, must, (150, 140), 4)
pygame.draw.circle(aken, must, (150, 150), 4)
pygame.draw.circle(aken, must, (150, 160), 4)

#nina
pygame.draw.polygon(aken, oranž, [(150, 90), (150, 95), (180, 92)])

# käed
pygame.draw.line(aken, pruun, (120, 160), (80, 140), 5) 
pygame.draw.line(aken, pruun, (180, 160), (220, 140), 5)

# luud 
pygame.draw.line(aken, pruun, (220, 140), (230, 100), 4) # pulk
pygame.draw.rect(aken, pruun, (225, 90, 10, 20)) 

# sall 
pygame.draw.rect(aken, punane, (130, 115, 40, 10)) # вокруг 
pygame.draw.rect(aken, punane, (145, 125, 10, 20)) # конец шарфа вниз

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit