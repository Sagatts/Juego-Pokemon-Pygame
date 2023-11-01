import pygame 
import sys

pygame.init()
pygame.mixer.init()

size=(800,500)
#Crear ventana
screen=pygame.display.set_mode(size)

sound1=pygame.mixer.Sound('Sonido1.wav')

while True:
    for event in pygame.event.get():
        sound1.play()
        if event.type==pygame.QUIT:
            sys.exit()