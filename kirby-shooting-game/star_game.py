import pygame
from pygame.sprite import Group

from func.settings import Settings
from func.ship import Ship
import func.game_functions as gf
from func.game_stats import GameStats
from func.button import Button
from func.scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("卡比射击 by 风渡巛")
    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play ")
    #创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏的循环

    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)


run_game()
