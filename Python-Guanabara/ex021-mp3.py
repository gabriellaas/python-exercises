import pygame

pygame.init()
pygame.mixer.music.load('')  # substituir a string vazia pelo nome do arquivo mp3
pygame.mixer.music.play()
pygame.event.wait()
