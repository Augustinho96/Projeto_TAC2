import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.music_playing = True
        self.collision_sound = pygame.mixer.Sound('monster.wav')

    def som_de_fundo(self):
        pygame.mixer.music.load('space.wav')
        pygame.mixer.music.play(-1, 0.0)

    def parar_musica(self):
        if self.music_playing:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.play(-1, 0.0)
        self.music_playing = not self.music_playing

    def som_colisao(self):
        self.collision_sound.play()