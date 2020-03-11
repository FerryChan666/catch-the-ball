import pygame
import sys
from ball import Ball
from boy import Boy

def check_events(boy):
	"""检查事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#左右移动
		elif event.type == pygame.KEYDOWN:
			check_key_down(event, boy)
		elif event.type == pygame.KEYUP:
			check_key_up(event, boy)
	
def check_key_down(event, boy):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		boy.moving_right = True
	if event.key == pygame.K_LEFT:
		boy.moving_left = True
		
def check_key_up(event, boy):
	"""响应松键"""
	if event.key == pygame.K_RIGHT:
		boy.moving_right = False
	if event.key == pygame.K_LEFT:
		boy.moving_left = False
	


def update_boy(screen, my_settings, boy):
	"""更新男孩位置"""
	boy.update()

def create_ball(screen, my_settings, balls):
	"""创造球"""
	new_ball = Ball(screen, my_settings)
	balls.add(new_ball)
	
def update_ball(screen, my_settings, balls, boy):
	"""更新球"""
	if len(balls) < my_settings.ball_limit:
		create_ball(screen, my_settings, balls)
	balls.update()
	for ball in balls.copy():
		if ball.rect.top > ball.screen_rect.bottom:
			balls.remove(ball)
	check_ball_boy_collision(my_settings, screen, boy, balls, ball)
	
def check_ball_boy_collision(my_settings, screen, boy, balls, ball):
	"""检测是否有球和男孩的碰撞"""
	#如果这样，删除球
	if pygame.sprite.spritecollideany(boy, balls):
		balls.remove(ball)
			
def update_screen(screen, my_settins, boy, balls):
	"""更新屏幕"""
	#填充颜色
	screen.fill(my_settins.bg_color)
	
	#显示男孩
	boy.blitme()
	
	#显示球
	balls.draw(screen)
	#显示最近绘制的屏幕
	pygame.display.flip()
	


