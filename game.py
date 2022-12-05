from player import Player
from monster import Monster

import pygame



# creer une seconde classe qui va representer notre jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commence ou non
        self.is_playing = False
        # generer notre joueur 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #  group de monstre 
        self.all_monsters = pygame.sprite.Group()
        self.pressed ={}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # remettre le jeu a neuf, retirer les monstres, remttre le joueur a 100 DE VIE, JEU en  ATTENTE
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        # appliquer l'image de mon joueur 
        screen.blit(self.player.image, self.player.rect)

        # recuperer les projectiles du joueuer
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupere les monstres de notre jeu 
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            

        # applique l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)


        # appliquer de images de mon groupe de monstre 
        self.all_monsters.draw(screen)

        self.player.update_health_bar(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collisioon(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

   
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
