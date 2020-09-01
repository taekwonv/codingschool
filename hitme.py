import sys
import pygame as pg
from random import randrange

def main():
	info = pg.display.Info()
	screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
	screen_rect = screen.get_rect()
	font = pg.font.Font(None, 100)
	clock = pg.time.Clock()
	done = False
	freeze = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					done = True
				elif event.key == pg.K_SPACE:
					freeze = True
				elif event.key == pg.K_RETURN:
					freeze = False

		if freeze == False:
			color = (randrange(256), randrange(256), randrange(256))
			txt = font.render(str(randrange(100)), True, color)

		screen.fill((30, 30, 30))
		screen.blit(txt, txt.get_rect(center=screen_rect.center))
		pg.display.flip()
		clock.tick(10)
		

if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()