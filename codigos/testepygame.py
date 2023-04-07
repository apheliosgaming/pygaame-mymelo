import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('NewJeans')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surface = pygame.image.load('Skyy.png')
text_surface = test_font.render('NewJeans', False, 'Pink')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # desenhos serao feitos aqui
    # update everything
    screen.blit(test_surface,(0,0))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)


