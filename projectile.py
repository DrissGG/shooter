import pygame

# definir la classe qui va gerer le projectile de notre joueur 

class Projectile(pygame.sprite.Sprite):

    # definir le constructeur 
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0 

    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def rotate(self):
        # tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un  monstre
        for monster in  self.player.game.check_collisioon(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger des degats 
            monster.damage(self.player.attack)

        # verifier si notre projectile n'est plus présent sur l'écran 
        if self.rect.x > 1080:
            # supprimer le projectile (en dehors de l'ecran) pour ne pas tuer les autres monstres
            self.remove()
            print('projectile supprime')
