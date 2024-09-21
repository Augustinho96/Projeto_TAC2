import pygame
from pygame.locals import *
import sys
from sprites import Player, Enemy
from sounds import SoundManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Super Adventure')
        
        self.carregar_recursos()
        self.inicializar_objetos()
        
        self.sounds = SoundManager()
        self.sounds.som_de_fundo()

    def carregar_recursos(self):
        info_tela = pygame.display.Info()
        self.LARGURAJANELA = info_tela.current_w
        self.ALTURAJANELA = info_tela.current_h
        self.tela = pygame.display.set_mode((self.LARGURAJANELA, self.ALTURAJANELA), pygame.FULLSCREEN)

        self.imagemFundo = pygame.image.load('fundo.jpg')
        self.imagemFundo = pygame.transform.scale(self.imagemFundo, (self.LARGURAJANELA, self.ALTURAJANELA))
        self.clock = pygame.time.Clock()

    def inicializar_objetos(self):
        self.player = Player()
        self.enemies = [Enemy(600, 605), Enemy(900, 605), Enemy(1200, 605)]

    def run(self):
        while True:
            self.moverJogador()
            self.atualizar_posicoes()
            self.checar_colisoes()
            self.carregar_fundo()
            pygame.display.update()
            self.clock.tick(60)

    def moverJogador(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                if event.key == pygame.K_m:
                    self.sounds.parar_musica()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.stop_moving_left()
                if event.key == pygame.K_RIGHT:
                    self.player.stop_moving_right()

    def atualizar_posicoes(self):
        self.player.update_position()
        for enemy in self.enemies:
            enemy.move()

    def checar_colisoes(self):
        for enemy in self.enemies:
            offset = (enemy.rect.x - self.player.rect.x, enemy.rect.y - self.player.rect.y)
            if self.player.mask.overlap(enemy.mask, offset):
                self.fim_de_jogo()

    def carregar_fundo(self):
        self.tela.blit(self.imagemFundo, (0, 0))
        self.player.draw(self.tela)
        for enemy in self.enemies:
            enemy.draw(self.tela)

    def fim_de_jogo(self):
        self.sounds.som_colisao()

        font = pygame.font.Font(None, 74)
        text = font.render('Fim de Jogo', True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.LARGURAJANELA / 2, self.ALTURAJANELA / 2))

        pygame.mixer.music.stop()
        self.tela.blit(text, text_rect)
        pygame.display.update()

        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    from main import start_game
    start_game()