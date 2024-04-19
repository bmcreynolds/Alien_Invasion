import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
	###Overall class to manage the game assets and behavior###

	def __init__(self):
		"""initialize the game and create the game resources"""
		pygame.init()
		""" initialize Settings class and apply it here"""
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Initialize an instance of game stats
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()	
		self.aliens = pygame.sprite.Group()	

		self._create_fleet()

		# Make the play button
		self.play_button = Button(self, "Play")

	def run_game(self):
		###Start the main loop for the game and runs helper methods defined below###
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()	
				self._update_aliens()
				
			self._update_screen()

	def _check_events(self):
		"""Watch for and respond to keyboard and mouse events (HELPER METHOD)"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			# Start game if mouse is clicked over 'play' button
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		'''Check if the posistion of the mouse is inside the play button'''
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset game stats to start again.
			self.stats.reset_stats()
			# Reset speeds to original values
			self.settings.initialize_dynamic_settings()
			
			self.stats.game_active = True

			# Get rid of aliens and bullets
			self.aliens.empty()
			self.bullets.empty()
			
			# Create a new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			# Hide the mouse
			pygame.mouse.set_visible(False)
			

	def _check_keydown_events(self, event):
		"""Respond to key presses"""
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				self.ship.moving_left = True
			elif event.key == pygame.K_SPACE:
				self._fire_bullet()
			elif event.key == pygame.K_q:
				sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to key release"""
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.ship.moving_left = False
			elif event.key == pygame.K_RIGHT:
				self.ship.moving_right = False

	def _fire_bullet(self):
		"""Creates the new bullet and draws it to the screen"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update the positition and remove old bullets"""
		self.bullets.update()

		#Get rid of old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		'''Responnd to collisions between bullet and alient'''
		# Check for collisions
		collions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		
		# Check if there are any more alien in the fleet
		if not self.aliens:
			# Destroy the remaining bullets and create a new fleet
			self.bullets.empty()
			self._create_fleet()
			# Change the speeds for the next round
			self.settings.increase_speed()


	def _ship_hit(self):
		'''Responds to a ship being hit'''
		# If there are lives remaining:
		if self.settings.ship_limit > 0:
			# Remove a 'life'
			self.settings.ship_limit -= 1

			# Get rid of existing aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			# Pause to let player reorient
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		'''Responds to aliens hitting the bottom of the screen'''
		# Establih the dimensions of the screen
		screen_rect = self.screen.get_rect()

		#Loop through each alien in the group and check if the bottom of the alien sprite hits the bottom of the screen
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Respond the same as if the ship is hit
				self._ship_hit()
				break


	def _create_fleet(self):
		# Actually adds the alien to the fleet and places then correctly
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)
		available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
		number_rows = available_space_y // (2 * alien_height)
		
		for row in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row)

	def _create_alien(self, alien_number, row):
		""" Defines alien and then finds how many can fit on the screen"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2* alien.rect.height * row
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		'''Respond appropriately if any aliens have reached an edge'''
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction ()
				break

	def _change_fleet_direction(self):
		'''Drop the entire fleet by the set amount and change the fleet direction'''
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.alien_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		"""Redraws the screen during each pass through the loop and uses Settings to color it, and draws the ship (HELPER METHOD) """
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Draw some aliends
		self.aliens.draw(self.screen)

		# Draw the play button if the game is not active
		if not self.stats.game_active:
			self.play_button.draw_button()
		
		# Make the most recently drawn screen visible.
		pygame.display.flip()

	def _update_aliens(self):
		"""Check if an alien is at the edge adjust the y axis, and then updates the position of aliens"""
		self._check_fleet_edges()
		self.aliens.update()

		# Check if any alien collides with the ship
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Check if any aliens reach the bottom
		self._check_aliens_bottom()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()