import pygame.font

class Button():
	def __init__(self,ai_settings,screen,msg):
		"""初始化按钮的属性"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		#设置按钮的尺寸和其他属性
		self.width,self.height=300,100
		self.button_color=(252,157,154)
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont('msyh',30)
		
		#创建按钮的rec对象，并使其居中
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		#按钮的文本
		self.prep_msg(msg)
		self.prep_prompt()
	def prep_msg(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		self.msg_image_rect.centery=self.rect.centery-20
	def prep_prompt(self):
		self.prompt_image=self.font.render("Click Here or Press Enter",True,(252,199,154),self.button_color)
		self.prompt_rect=self.prompt_image.get_rect()
		self.prompt_rect.centerx=self.rect.centerx
		self.prompt_rect.centery=self.rect.centery+20
	def draw_button(self):
		#绘制一个用颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color,self.rect)#颜色填充的按钮
		self.screen.blit(self.msg_image,self.msg_image_rect)#绘制文本	
		self.screen.blit(self.prompt_image,self.prompt_rect)#绘制提示
	
