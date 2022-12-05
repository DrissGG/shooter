import pygame
import random



# creer une classe qui va gérer la notion de monstre sur notre jeu

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)

    def damage(self, amount):
        # infliger les degats 
        self.health -= amount

        # verifier si son nouveau nombre de points de vie est inferieur ou egale a 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre 
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,2)
            self.health = self.max_health



    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (57, 235, 22)
        # definir une couleur pour l'arriere plan de la jauge (gris foncé)
        back_bar_color = (61, 61, 59)

        # definir la position de notre jauge de vie que sa largeur et son épaisseur
        bar_position = [self.rect.x + 12, self.rect.y -20, self.health, 5]
        # definir la position de l'arrière plan de notre jauge de vie 
        back_bar_position = [self.rect.x + 12, self.rect.y -20, self.max_health, 5]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position) 
        pygame.draw.rect(surface, bar_color, bar_position)
        


    def forward(self):
        # le deplacement ce fait que si il n'ya pas de collission avec un groupe de joueur
        if not self.game.check_collisioon(self, self.game.all_players):
            self.rect.x  -= self.velocity

        # si le monstre est en collision avec le joueur
        else:
            # infliger les degtas (au joueur )
            self.game.player.damage(self.attack)

    


