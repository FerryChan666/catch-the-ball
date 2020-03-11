import pygame

class Boy():
	"""男孩类"""
	def __init__(self, screen, my_settings):
		"""初始化"""
		#初始化变量———屏幕，设置
		self.screen = screen
		self.my_settings = my_settings
		#获取图像
		self.image = pygame.image.load('images/boy.png')
		#获得图像属性
		self.rect = self.image.get_rect()
		#获得屏幕属性
		self.screen_rect = screen.get_rect()
		#图像的初始位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		#存储移动距离的小数
		self.x = float(self.rect.centerx)
		
	def update(self):
		"""更新位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.my_settings.boy_speed_factor
			
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.my_settings.boy_speed_factor
		self.rect.centerx = self.x

	def blitme(self):
		"""将图像移动到指定位置"""
		self.screen.blit(self.image, self.rect)
