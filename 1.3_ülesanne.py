import pygame

pygame.init()
aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 1.3")

valge = (255, 255, 255)
must = (0, 0, 0)
sinine = (100, 100, 255)

taust = pygame.image.load("liblikas.png")
taust = pygame.transform.scale(taust, (640, 480))
aken.blit(taust, (0, 0))

kangelane = pygame.image.load("dedpull.png")
kangelane = pygame.transform.scale(kangelane, (200, 200))
aken.blit(kangelane, (220, 250))

# овал 
pygame.draw.ellipse(aken, valge, (100, 50, 440, 100)) # сам овал
pygame.draw.ellipse(aken, must, (100, 50, 440, 100), 3) # граница


font = pygame.font.SysFont("Comic Sans MS", 30)
tekst = font.render("Tere! Mina olen Anna", True, must)
aken.blit(tekst, (150, 90))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit
