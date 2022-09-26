class GameStats():
	def __init__(self,ai_settings):
		self.ai_settings=ai_settings
		self.reset_stats()
		self.game_active = False
		self.level=1
		filename = 'high_score.txt'
		with open(filename) as f:
			self.high_score = f.read()
	def reset_stats(self):
		self.ships_left=self.ai_settings.ship_limit 
		self.score=0
		self.level=1

	
