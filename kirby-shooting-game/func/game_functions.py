import sys
from time import sleep
import pygame
from func.bullet import Bullet
from func.alien import Alien

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
				sys.exit()
		elif event.type==pygame.KEYDOWN:#Keydown是键盘按下的意思
			check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		elif event.type==pygame.KEYUP:#Keyup是键盘松开的意思
			check_keyup_events(event,ship)
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环都重绘屏幕
	screen.fill(ai_settings.bg_color)
	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	for alien in aliens.sprites():
		alien.blitme()
	sb.show_score()
	if not stats.game_active:
		play_button.draw_button()
    #让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	check_bullet_alien_collisons(ai_settings,screen,stats,sb,ship,aliens,bullets)
	
def check_high_score(stats,sb):
	"""检查是否诞生了新的最高得分"""
	if stats.score>int(stats.high_score):
		stats.high_score=stats.score
		filename = 'high_score.txt'
		with open(filename, 'w') as f:
			f.write(str(stats.high_score))
		sb.prep_high_score()
			
def check_bullet_alien_collisons(ai_settings,screen,stats,sb,ship,aliens,bullets):
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score +=ai_settings.alien_points*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
	if len(aliens)==0:
		bullets.empty()
		ai_settings.increase_speed()
		#提高等级
		stats.level+=1
		sb.prep_level()
		create_fleet(ai_settings,screen,ship,aliens)
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed:
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
def get_number_aliens_x(ai_settings,alien_width):
	#算一行可容纳多少
	available_space_x=ai_settings.screen_width-2*alien_width
	number_aliens_x=int(available_space_x/(2*alien_width)) #保证为整数
	return number_aliens_x

	
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number+10
    aliens.add(alien)
    
		
def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)


def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed
	ai_settings.fleet_direction*=-1
	
def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
	if stats.ships_left > 0:
		stats.ships_left -=1
		#更新记分牌
		sb.prep_ships()
		aliens.empty()
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		sleep(0.5)			
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
	# 检查是否有外星人到达屏幕底端
	check_aliens_bottom(ai_settings, screen,stats, sb,ship, aliens, bullets)	
	
def check_aliens_bottom(ai_settings,screen,stats,sb,ship, aliens, bullets):
	"""检查是否有外星人到达了屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 像飞船被撞到一样进行处理
			ship_hit(ai_settings,screen,stats,sb,ship, aliens, bullets)
			break


def check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_UP:
		ship.moving_top=True
	elif event.key==pygame.K_DOWN:
		ship.moving_bottom=True
	elif event.key==pygame.K_SPACE:
		ai_settings.bullet_width=5
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_k:
		ai_settings.bullet_width=300
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_ESCAPE:
		sys.exit()
	elif event.key==pygame.K_p or event.key==pygame.K_RETURN:
		if  not stats.game_active:
			restart_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
	elif event.key==pygame.K_q:
		stats.game_active=False
		
		
		
				
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
			ship.moving_right=False
	elif event.key==pygame.K_LEFT:
			ship.moving_left=False
	elif event.key==pygame.K_UP:
			ship.moving_top=False
	elif event.key==pygame.K_DOWN:
			ship.moving_bottom=False
			
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	"""在玩家单机Play按钮时开始游戏"""
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		restart_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		
def restart_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
		stats.reset_stats()
		stats.game_active=True
		#隐藏光标
		pygame.mouse.set_visible(False)
		#重置游戏设置
		ai_settings.initialize_dynamic_settings()
		#重置记分牌图像
		sb.prep_high_score()
		sb.prep_score()
		sb.prep_level()
		sb.prep_ships()
		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()
		#创建一群新的外星人，并让飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
