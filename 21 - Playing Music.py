'''PLAYING MUSIC

Create a program that opens and plays audio from an MP3 file '''


import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/Users/lidianegarcia/PycharmProjects/100 Tiny Python Projects for Beginners/.venv/music01.mp3')
pygame.mixer.music.play()
input('Press enter to stop')
pygame.mixer.music.stop()
