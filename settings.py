class Settings:
	"""A large class to hold all game settings"""
	
	def __init__(self):
		"""Initialize the games settings"""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		"""Ship settings"""
		self.ship_speed = 6

		"""Bullet settings"""
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		""" Alien settings"""
		self.alien_speed = .125
		self.alien_drop_speed = 10.0
		# 1 means the fleet moves right, -1 means the fleet moves left
		self.fleet_direction = 1

