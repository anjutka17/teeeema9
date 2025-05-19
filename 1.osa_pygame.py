import pygame
from pygame.font import SysFont
def paike():
    x=200
    y=0
    for i in range(30):
        pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y), 5)
        x-=7
        y+=7
        if i in range(10, 20):
            pygame.draw.line(ekraani_pind, kollane, (0, 0), (x+i, y), 5)
        else:
            pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y), 5)



pygame.init() 
kollane=[255, 255, 0]
punane=[255, 0, 0]
sinine=[0, 0, 255]
hall=[128, 128, 128]
roheline=[139, 69, 19]

ekraani_pind=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(hall)    #заливка
#päike
pygame.draw.rect(ekraani_pind, kollane, (0, 0, 100, 100))
paike()
pygame.draw.circle(ekraani_pind, punane, (400, 300), 50)
pygame.draw.polygon(ekraani_pind, sinine, [(600, 100), (700, 100), (650, 50)])
pygame.draw.line(ekraani_pind, roheline, (100, 500), (700, 500), 10)


pilt1=pygame.image.load("rediska.jpg")
pilt1=pygame.transform.scale(pilt1, (100, 100))
ekraani_pind.blit(pilt1, (300, 400))
ekraani_pind.blit(pilt1, (500, 400))
# tekst
font=pygame.font.SysFont("Arial", 50)
sõnum="Tere tulemast!"
tekti_lisamine=font.render(sõnum, True, punane)
ekraani_pind.blit(tekti_lisamine, (500, 500))

#polygon - треугольник
pygame.display.flip()#отобразить на экране
while True:
    event=pygame.event.poll()#poll- проверяет что нашли
    if event.type==pygame.QUIT: break
pygame.quit