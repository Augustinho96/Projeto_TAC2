import pygame

class Player:
    def __init__(self):
        self.img = pygame.image.load('personagem.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 5, self.img.get_height() // 5))
        self.rect = self.img.get_rect(topleft=(10, 290))
        self.moviment = [False, False, False, False]  # [cima, baixo, esquerda, direita]

    def move_up(self):
        self.moviment[0] = True

    def move_down(self):
        self.moviment[1] = True

    def move_left(self):
        self.moviment[2] = True

    def move_right(self):
        self.moviment[3] = True

    def stop_moving_up(self):
        self.moviment[0] = False

    def stop_moving_down(self):
        self.moviment[1] = False

    def stop_moving_left(self):
        self.moviment[2] = False

    def stop_moving_right(self):
        self.moviment[3] = False

    def update_position(self):
        self.rect.y += (self.moviment[1] - self.moviment[0]) * 4
        self.rect.x += (self.moviment[3] - self.moviment[2]) * 4

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)

class Enemy:
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 4, self.img.get_height() // 4))
        self.rect = self.img.get_rect(topleft=(400, 310))

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)