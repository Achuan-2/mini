import pygame.font
from func.ship import Ship
from pygame.sprite import Group

class Scoreboard():
	"""显示得分信息"""
	def __init__(self,ai_settings,screen,stats):
		"""初始化显示得分涉及的属性"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats
		#显示得分信息使用的字体设置
		self.text_color=(28,28,28)
		self.font=pygame.font.SysFont("SimHei",24)
		#准备初始得分图像
		self.prep_level()
		self.prep_high_score()
		self.prep_score()
		self.prep_ships()
		self.show_prompt()
		
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		round_score=round(self.stats.score,-1)
		score_str="{:,}".format(round_score)
		self.score_image=self.font.render(score_str,True,self.text_color,None)
		#将得分放在屏幕右上角
		self.score_rect=self.score_image.get_rect()
		self.score_rect.centerx=self.screen_rect.centerx+200
		self.score_rect.bottom=self.level_rect.bottom
		
	def prep_high_score(self):
		"""将最高得分转换为一幅渲染的图像"""
		high_score = round(int(self.stats.high_score), -1)
		high_score_str="{:,}".format(high_score)
		self.high_score_image=self.font.render(high_score_str,True,self.text_color,None)
		#将最高分放在屏幕顶部中央
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx-100
		self.high_score_rect.bottom=self.level_rect.bottom
		
	def prep_level(self):
		"""将登记转换为渲染的图像"""
		self.level_image=self.font.render(str(self.stats.level),True,self.text_color,None)
		#将等级放在得分下方
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.screen_rect.right-100
		self.level_rect.top=self.screen_rect.top+50
	
	def	prep_ships(self):
		self.ships=Group()
		for ship_number in range(self.stats.ships_left):
			ship=Ship(self.ai_settings,self.screen)
			ship.image=pygame.image.load('images/life.png')
			ship.rect.x=10+ship_number*ship.rect.width
			ship.rect.y=10
			self.ships.add(ship)
	def show_score(self):
		"""在屏幕上显示得分"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)
		self.show_prompt()
	def show_prompt(self):
		#分数名称显示
		self.score_prompt=self.font.render("SCORE",True,(92,167,186),None)
		self.score_prompt_rect=self.score_prompt.get_rect()
		self.score_prompt_rect.centerx=self.score_rect.centerx
		self.score_prompt_rect.top=self.screen_rect.top+20
		#最高分名称显示
		self.highscore_image=self.font.render("HIGHEST SCORE",True,(92,167,186),None)
		self.highscore_rect=self.highscore_image.get_rect()
		self.highscore_rect.centerx=self.high_score_rect.centerx
		self.highscore_rect.top=self.screen_rect.top+20
		#等级显示
		self.level_prompt=self.font.render("LEVEL",True,(92,167,186),None)
		self.level_prompt_rect=self.level_prompt.get_rect()
		self.level_prompt_rect.centerx=self.level_rect.centerx
		self.level_prompt_rect.top=self.screen_rect.top+20
		#绘制名称
		self.screen.blit(self.score_prompt,self.score_prompt_rect)
		self.screen.blit(self.highscore_image,self.highscore_rect)
		self.screen.blit(self.level_prompt,self.level_prompt_rect)
		
