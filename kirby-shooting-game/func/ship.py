import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings #获取settings里的速度因子
		self.image=pygame.image.load('images/kabi1.png')
		self.rect=self.image.get_rect()#处理矩形
		self.screen_rect=screen.get_rect()
		#放在底部中央
		self.rect.centerx=self.screen_rect.centerx     #centerx是指x轴中心
		self.rect.bottom=self.screen_rect.bottom
		#center
		self.centerx=float(self.rect.centerx)
		self.centery=float(self.rect.centery)
		#移动标志
		self.moving_right=False
		self.moving_left=False
		self.moving_top=False
		self.moving_bottom=False
	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.centerx +=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.centerx -=self.ai_settings.ship_speed_factor
		if self.moving_top and self.rect.top>self.screen_rect.top:
			self.centery -=self.ai_settings.ship_speed_factor
		if self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
			self.centery +=self.ai_settings.ship_speed_factor
		self.rect.centerx=self.centerx
		self.rect.centery=self.centery
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.centerx = self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		self.centery=self.rect.centery
		
