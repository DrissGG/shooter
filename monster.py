import pygame





# creeer une classe qui va gérer la notion de monstre sur notre jeu

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        

    def forward(self):
        # le deplacement ce fait que si il n'ya pas de collission avec un groupe de joueur
        if not self.game.check_collisioon(self, self.game.all_players):
            self.rect.x  -= self.velocity

    


