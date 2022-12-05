import pygame
import math

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT =  800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 1

for i in range(1,4):
	bgs.append(pygame.image.load(f'assets/bgs/{i}.png'))
	banners.append(pygame.image.load(f'assets/banners/{i}.png'))
	guns.append(pygame.image.load(f'assets/guns/{i}.png'))

run = True
while run:
	timer.tick(fps)

	screen.fill('black')
	screen.blit(bgs[level - 1], (0, 0))
	screen.blit(banners[level - 1], (0, HEIGHT - 200))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.flip()
pygame.quit()