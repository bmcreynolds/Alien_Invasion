import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Represents a single alien in the enemy fleet"""
	
	def __init__(self, ai_game):
		"""Initialize the aliens and set starting postition (x and y)"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#Load the alien image and set it's rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Starts each new alien at top left of the screen
		# this expression sets the rect.x to be a rect.width value's distance from the left side of the screen, so one aliens width
		self.rect.x = self.rect.width
		# this does the same as above, but with one aliens height from the top
		self.rect.y = self.rect.height

		#Store the alien's horizontal position as a float (Horizontal speed will be more precise than vertical, so float is needed)
		self.x = float(self.rect.x)

	def update(self):
		"""Moves alien to the right"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x


	def check_edges(self):
		"""Return true if an alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.x >= screen_rect.right or self.rect.left <= 0:
			return True