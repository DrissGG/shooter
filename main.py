from game import Game
import math
import pygame
pygame.init()



# generer la fenetre de notre jeu 
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 700))

# importer de charger  l'arriere plan de notre jeu 
background = pygame.image.load(('assets/bg.jpg'))

# importe charger notre banniere 
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x =  math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)
# charger le jeu 
game = Game()

# charger notre jeu 
# player = Player()


running = True

# boucle tant que  que cette condition est vrai
while running:
    # appliquer l'arriere plan de notre jeu 
    screen.blit(background, (0, -200))
    
    # verifier si notre jeu a commencé ou non 
    if game.is_playing:
        # declencher les instructions de la partie 
        game.update(screen)
    # verifier si notre jeu n'a pas commencer
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect) 
       
    

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifie pour savoir si la souris est en collision avec le bouton 
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer 
                game.start()

            
            
             



