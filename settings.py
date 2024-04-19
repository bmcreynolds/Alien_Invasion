class Settings:
	"""A large class to hold all game settings"""
	
	def __init__(self):
		"""Initialize the games STATIC settings"""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		"""Ship settings"""
		self.ship_limit = 3

		"""Bullet settings"""
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		""" Alien settings"""
		self.alien_drop_speed = 10.0

		# How fast the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		'''Set the settings that change as the game goes on'''
	# Ship speed
		self.ship_speed = 3
	# Alien speed
		self.alien_speed = 1
	# Bullet speed
		self.bullet_speed = 2
 
	# Fleet direction (1 = right, -1 = left)
		self.fleet_direction = 1

	def increase_speed(self):
		'''Increase all the dynamic speeds for aliens, ships, and bullets when called'''
		self.ship_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
