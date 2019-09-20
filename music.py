import pygame.midi
import time
import random

pygame.midi.init()
player = pygame.midi.Output(0)

player.set_instrument(1)

for x in range(65,67):
	for x in range(65,75):
		z=random.randint(64,70)
		player.note_on(z,127)
		time.sleep(0.3)
		player.note_off(z,127)
	time.sleep(0.3)