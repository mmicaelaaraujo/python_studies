# Áudio MP3

import pygame
pygame.init()
pygame.mixer.music.load('testeex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
