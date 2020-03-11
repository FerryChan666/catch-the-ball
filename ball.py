import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
	"""球类"""
	def __init__(self, screen, my_settings):
		super().__init__()
		self.screen = screen
		self.my_settings = my_settings
		#获取图像
		self.image = pygame.image.load('images/ball.png')
		#获取图像，屏幕属性
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#确定图像位置
		self.rect.centerx = randint(0, self.screen_rect.right)
		self.rect.top = self.screen_rect.top
		#设置可存储小数的变量
		self.y = float(self.rect.top)
		
	def update(self):
		"""更新球的位置"""
		self.y += self.my_settings.ball_speed_factor
		self.rect.top = self.y
		

		
