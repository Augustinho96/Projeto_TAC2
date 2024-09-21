import pygame

class Player:
    def __init__(self):
        self.img = pygame.image.load('personagem.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 5, self.img.get_height() // 5))
        self.rect = self.img.get_rect(topleft=(50, 682))
        
        self.moviment = [False, False]
        self.vel_y = 0
        self.gravidade = 0.8
        self.no_chao = False

        self.mask = pygame.mask.from_surface(self.img)

    def move_left(self):
        self.moviment[0] = True

    def move_right(self):
        self.moviment[1] = True

    def stop_moving_left(self):
        self.moviment[0] = False

    def stop_moving_right(self):
        self.moviment[1] = False

    def jump(self):
        if self.no_chao:
            self.vel_y = -15
            self.no_chao = False

    def aplicar_gravidade(self):
        self.vel_y += self.gravidade
        self.rect.y += self.vel_y

        if self.rect.bottom >= 682: 
            self.rect.bottom = 682
            self.vel_y = 0 
            self.no_chao = True

    def update_position(self):
        self.rect.x += (self.moviment[1] - self.moviment[0]) * 5
        self.aplicar_gravidade()

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)


class Enemy:
    def __init__(self, x, y):
        self.img = pygame.image.load('enemy.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 4, self.img.get_height() // 4))
        self.rect = self.img.get_rect(topleft=(x, y))

        self.mask = pygame.mask.from_surface(self.img)
        self.vel_x = -1

    def move(self):
        self.rect.x += self.vel_x

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)