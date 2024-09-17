import pygame

class Player:
    def __init__(self):
        self.img = pygame.image.load('personagem.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 5, self.img.get_height() // 5))
        self.rect = self.img.get_rect(topleft=(10, 290))  # Posição inicial do jogador
        
        self.moviment = [False, False]  # [esquerda, direita]
        self.vel_y = 0  # Velocidade vertical
        self.gravidade = 0.8  # Gravidade aplicada
        self.no_chao = False  # Verifica se o jogador está no chão

        # Cria a máscara baseada na imagem do jogador
        self.mask = pygame.mask.from_surface(self.img)

    def move_left(self):
        self.moviment[0] = True  # Iniciar movimento para a esquerda

    def move_right(self):
        self.moviment[1] = True  # Iniciar movimento para a direita

    def stop_moving_left(self):
        self.moviment[0] = False  # Parar movimento para a esquerda

    def stop_moving_right(self):
        self.moviment[1] = False  # Parar movimento para a direita

    def jump(self):
        if self.no_chao:  # Só pode pular se estiver no chão
            self.vel_y = -15  # Velocidade de pulo inicial
            self.no_chao = False  # Não está mais no chão após o pulo

    def aplicar_gravidade(self):
        self.vel_y += self.gravidade  # Aplicando a gravidade continuamente
        self.rect.y += self.vel_y  # Atualizando a posição vertical do jogador

        # Limitar a posição vertical (não permitir que o jogador caia abaixo do chão)
        if self.rect.bottom >= 390:  # Ajuste a altura do chão conforme necessário
            self.rect.bottom = 390  # Definir a posição do chão
            self.vel_y = 0  # Resetar a velocidade vertical
            self.no_chao = True  # Jogador está no chão novamente

    def update_position(self):
        # Movimento horizontal
        self.rect.x += (self.moviment[1] - self.moviment[0]) * 5  # Controlar movimento esquerdo/direito

        # Aplicar gravidade (movimento vertical)
        self.aplicar_gravidade()

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)  # Desenhar o jogador na tela


class Enemy:
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() // 4, self.img.get_height() // 4))
        self.rect = self.img.get_rect(topleft=(620, 308))  # Posição inicial do inimigo

        # Cria a máscara baseada na imagem do inimigo
        self.mask = pygame.mask.from_surface(self.img)
        self.vel_x = -1  # Velocidade de movimento para a esquerda (lenta, porque é uma lesma)

    def move(self):
        self.rect.x += self.vel_x  # Mover lentamente para a esquerda

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)  # Desenhar o inimigo na tela