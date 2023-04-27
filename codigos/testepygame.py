import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('NewJeans')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surface = pygame.image.load('Skyy.png')
text_surface = test_font.render('NewJeans', False, 'Pink')
text_rect = text_surface.get_rect(center = (350, 50))

melo_surf = pygame.image.load('mymelosprite.png').convert_alpha()
melo_rect = melo_surf.get_rect(midbottom = (80,300))

pressed = pygame.key.get_pressed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print('mousew up')
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_RIGHT:
            
                melo_rect.left += 10
            if event.key == pygame.K_LEFT:
                melo_rect.left -= 10
        
    # desenhos serao feitos aqui
    # update everything
    screen.blit(test_surface,(0,0))
    screen.blit(text_surface,(300,50))

    # pygame.draw.rect(screen,'Pink', text_rect,10)

    # pygame.draw.line(screen, 'Gold', (0,0), (800,400),10)

    # keys = pygame.key.get_pressed()
    # keys[pygame.K_RIGHT]

    # melo_rect.left += 1
    screen.blit(melo_surf,melo_rect)

    pygame.display.update()
    clock.tick(60)



