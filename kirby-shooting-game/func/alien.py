import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#加载外星人图像
		self.image=pygame.image.load('images/kabi.png')
		self.rect=self.image.get_rect()
		#外星人产生在左上角
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#存储外星人的位置
		self.x=float(self.rect.x)
	
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
	def check_edges(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
			
	def update(self):
		self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x=self.x

		
