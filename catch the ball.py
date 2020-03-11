import pygame
from settings import Settings
import game_functions as gf
from boy import Boy
from ball import Ball
from pygame.sprite import Group

def run_game():
	"""运行游戏"""
	#初始化
	pygame.init()
	#导入设置
	my_settings = Settings()
	#创建屏幕实例
	screen = pygame.display.set_mode(
		(my_settings.screen_width, my_settings.screen_height))
	#创建男孩实例
	boy = Boy(screen, my_settings)
	#创建球的编组
	balls = Group()
	
	while True:
		#检查按键
		gf.check_events(boy)
		#boy更新
		gf.update_boy(screen, my_settings, boy)
		#ball更新
		gf.update_ball(screen, my_settings, balls, boy)
		#刷新屏幕
		gf.update_screen(screen, my_settings, boy, balls)
		
run_game()

