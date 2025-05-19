import pygame

pygame.init()
aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 1.3")

valge = (255, 255, 255)
must = (0, 0, 0)
sinine = (100, 100, 255)

taust = pygame.image.load("taust.png")
taust = pygame.transform.scale(taust, (640, 480))
aken.blit(taust, (0, 0))

kangelane = pygame.image.load("hero.png")
kangelane = pygame.transform.scale(kangelane, (100, 100))
aken.blit(kangelane, (100, 300))

pygame.draw.polygon(aken, valge, [(220, 270), (500, 270), (500, 200), (400, 180), (300, 200), (220, 200)])

font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Tere! Mina olen Anna", True, must)
aken.blit(tekst, (230, 210))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
