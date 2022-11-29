import pygame
pygame.init()

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# impoerter de charger  l'arriere plan de notre jeu 
background = pygame.image.load(('assets/bg.jpg'))
running = True

# boucle tant que  que cette condition est vrai
while running:
    # appliquer l'arriere plan de notre jeu 
    screen.blit(background, (0,-200))
    # mettre a jour l'ecran 
    pygame.display.flip()

    # si le joueur ferme la fenetre 
    for event in pygame.event.get():
        # l'evenement de fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

