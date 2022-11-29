import pygame
pygame.init()

# creer une seconde classe qui va representer notre jeu
class Game:
    def __init__(self):
        # generer notre joueur 
         self.player = Player()

# creer une premiere classe qui va representer notre joueur 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400 
        self.rect.y = 500

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

    # mettre a jour l'ecran 
    pygame.display.flip()

    # si le joueur ferme la fenetre 
    for event in pygame.event.get():
        # l'evenement de fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

