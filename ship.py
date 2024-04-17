import pygame

class Ship:
	""" First class for basic ship """

	def __init__(self, ai_game):
		"""Initialize the ship on the screen and sets original placement"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		"""Loads the image of a ship and shapes it"""
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		"""Starts each new ship at the bottom center of the screen"""
		self.rect.midbottom = self.screen_rect.midbottom

		#Convert rect x position to float
		self.x = float(self.rect.x)

		"""Movement flags for continuous motion"""
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ships position according to mvmnt flags and settings option instead of rect value"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#Convert self.x back into rect position
		self.rect.x = self.x

	def blitme(self):
		"""Draws the ship at it's current location"""
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		'''Center the ship after getting merced'''
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)