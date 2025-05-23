import pygame
import random

pygame.init()

kollane = (255, 255, 0)
hall = (150, 150, 150)
roheline = (0, 255, 0)
sinine = (135, 206, 235)
lilla = (160, 32, 240)
must = (0, 0, 0)
valge = (255, 255, 255)

ekraan = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tere tulemast!")


mesilane_pilt = pygame.image.load("mesilane.png")
mesilane_pilt = pygame.transform.scale(mesilane_pilt, (50, 50))


def paike():
    x = 200
    y = 0
    for i in range(30):
        pygame.draw.line(ekraan, kollane, (0, 0), (x, y), 5)
        x -= 7
        y += 7
        if i in range(10, 20):
            pygame.draw.line(ekraan, kollane, (0, 0), (x + i, y), 5)
        else:
            pygame.draw.line(ekraan, kollane, (0, 0), (x, y), 5)

def joonista_lill(ekraan, x, y):
    pygame.draw.line(ekraan, roheline, (x, y), (x, y + 60), 4)
    pygame.draw.circle(ekraan, lilla, (x - 10, y), 10)
    pygame.draw.circle(ekraan, lilla, (x + 10, y), 10)
    pygame.draw.circle(ekraan, lilla, (x, y - 10), 10)
    pygame.draw.circle(ekraan, lilla, (x, y + 10), 10)
    pygame.draw.circle(ekraan, valge, (x, y), 7)

def joonista_pilv(ekraan, x, y):
    pygame.draw.circle(ekraan, hall, (x, y), 20)
    pygame.draw.circle(ekraan, hall, (x + 20, y), 25)
    pygame.draw.circle(ekraan, hall, (x + 40, y), 20)
    pygame.draw.circle(ekraan, hall, (x + 10, y - 10), 18)
    pygame.draw.circle(ekraan, hall, (x + 30, y - 10), 18)

def joonista_mesilane(ekraan, x, y):
    ekraan.blit(mesilane_pilt, (x, y))



ekraan.fill(sinine) # небо
pygame.draw.rect(ekraan, roheline, (0, 400, 800, 200)) # трава

paike()
for _ in range(10):
    x = random.randint(20, 780)
    y = random.randint(420, 580) 
    joonista_lill(ekraan, x, y)
joonista_lill(ekraan, 200, 450)
joonista_lill(ekraan, 250, 470)
joonista_pilv(ekraan, 400, 100)
joonista_pilv(ekraan, 600, 80)
joonista_mesilane(ekraan, 300, 200)
joonista_mesilane(ekraan, 350, 250)


font = pygame.font.SysFont("Arial", 48)
tekst = font.render("Tere tulemast!", True, valge)
ekraan.blit(tekst, (500, 20))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit