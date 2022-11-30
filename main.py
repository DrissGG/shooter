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

    # recuperer les projectiles du joueuer
    for projectile in game.player.all_projectiles:
        projectile.move()

    # applique l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw((screen))

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
         game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x) 
    

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

        # detecter si la touche espace est declanche 
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
            
             



