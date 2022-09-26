class Settings():
	"""A class to store all settings for Alien Invasion."""#注意缩进
	def __init__(self):  #两个下划线！
		"""Initialize the game's settings."""
	    # Screen settings.
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(200,230,236)#设置背景色
		#ship
		self.ship_limit=3
		self.ship_speed_factor=1.5
		#bullet
		self.bullet_width=5
		self.bullet_height=15
		self.bullet_speed_factor=3
		self.bullet_color=(230,60,60)
		self.bullets_allowed=3
		#aliens
		self.fleet_drop_speed=10
		self.alien_speed_factor=1
		#以什么样的速度加快游戏节奏
		self.speedup_scale=1.1
		#外星人点数的提高速度
		self.score_scale=1.5
		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行变化的设置"""
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor=1
		#fleet_direction为1表示向右，为-1表示向左
		self.fleet_direction=1
		self.alien_points=50
	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *=self.speedup_scale
		self.bullet_speed_factor *=self.speedup_scale
		self.alien_speed_factor *=self.speedup_scale
		self.alien_points=int (self.alien_points*self.score_scale)
		
		
	
