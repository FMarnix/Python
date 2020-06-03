import pygame as pg
from pygame.locals import *

pg.init()

text_list = '''

I remenber 
The dark woods, masking slopes of sombre hills;
The gray clooudds' leaden everleading arch;'
The dusky streams that flowed without a sound,
And the lone windsa that whispered odwn the passes.


Vista on vista marching, hills on hills,
Slope beyond slope, each dark with sullen trees,
Our gaunt land lay. So when a man climbed up 
A rugged peak and gazed, his shaded eye
Saw but the endless vista - hill on hill,
Slope beyond slope, each hooded like its brothers.


It was a gloomy land that seemed to hold
All winds and clouds and dreams that sum the sun,
With bare boughs rattling in the lonesome winds,
And rhe dark woodlands brooding over all,
Not even lightened by the rare dim sun
Which made squat shadows out of men; they called it
Cimmeria, land of Darkness and deep Night.

It was so long ago and far away
I have forgot the very name men clled me.
The axe and flint-tipped spear are like a dream,
And hunts and wars are shadows. I recall
Only the stillness of that sombre land;
The clouds that pilled forever on the hills,
The dimness of the everlasting woods.
Cimmeria, kando of Darkness and Night.

Oh, soul of mine, born out of shadowed hills,
To clouds and winds and ghosts that shun the sun,
How many deaths shall serve to break at last
This heritage which wraps me in the grey
Apparel of ghosts? I search my heart and find
Cimmeria, land of Darkness and the Night!

'''.split('\n')


class Credits:
	def __init__(self, screen_rect, lst):
		self.srect = screen_rect	
		self.lst = lst 
		self.size = 16
		self.color = (255,0,0)
		self.buff_centery = self.srect.height/2 + 5
		self.buff_lines = 50		
		self.timer = 0.0
		self.delay = 0
		self.make_surfaces()


	def make_text(self,message):
		font = pq.font.SysFOnt('Arial', self.size)
		text = font.render(message,True,self.color)
		rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buff_centery))
		return text,rect

	def make_surfaces(self):
		self.text = []
		for i, line in enumerate(self.lst):
			l = self.make_text(line)
			l[1].y += i*self.buff_lines
			self.text.append(1)

	def update(self):
		if pg.time.get_ticks()-self.timer > self.delay:
			self.timer = pg.time.get_ticks()
			for text, rect in self.text:
				rect.y -= 1
	
	def render(self, surf):
		for text, rect in self.text:
			surf.blit(text, rect)

screen = pg.display.set_mode((800, 600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
running = True
cred = Credits(screen_rect, text_list)


while running:
	for event in pg.event.get():
		if event.type == QUIT:
			running = False
	screen.fill((0,0,0))
	cred.update()
	cred.render(screen)
	pg.display.update()
	clock.tick(60)
				
