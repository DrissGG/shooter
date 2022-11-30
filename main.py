from game import Game

import pygame
pygame.init()



# generer la fenetre de notre jeu 
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer de charger  l'arriere plan de notre jeu 
background = pygame.image.load(('assets/bg.jpg'))

# charger le jeu 
game = Game()

# charger notre jeu 
# player = Player()


running = True

# boucle tant que  que cette condition est vrai
while running:
    # appliquer l'arriere plan de notre jeu 
    screen.blit(background, (0,-200))
    # appliquer l'image de mon joueur 
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur souhaite aller a gauche ou a droite 
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()


    print(game.pressed)

    # mettre a jour l'ecran 
    pygame.display.flip()

    # si le joueur ferme la fenetre 
    for event in pygame.event.get():
        # l'evenement de fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
           
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
            
             



