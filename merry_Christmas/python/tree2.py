
"""
Author: Achuan-2
"""
import random
import os
import time
height = 11


def draw_color_tree(height):
    trunk = '[___]'
    bias=50
    print('\033[1;33m', end='')
    for i in range(2):
        print(" " * (height-i+bias), end='')
        print("★"*(2*i+1))
    print('\033[1;32m', end='')
    for i in range(2,height):
        print(" " * (height-i+bias), end='')
        for j in range((2*i)+1):
            if random.random() < 0.1:
                color = random.choice(
                    ['\033[31m', '\033[33m', '\033[34m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'])
                print(color,end='')
                shape = random.choice(['✦', '★', '❁', '●'])
                print(f"{shape}", end='')
            else:
                print('\033[32m', end='')
                print('*', end='')
        print()
    print(' '*(height-2+bias)+f'\033[32m[   ]\033[0m')
    print(' '*(height-2+bias)+f'\033[32m{trunk }\033[0m')

def main(height):
    while True:
        screen_width, _ = os.get_terminal_size()
        try:
            time.sleep(0.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            draw_color_tree(height)
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{'🎄!!Merry Christmas!!🎄':^{screen_width}}", end='\n\n')
            break


if __name__ == '__main__':
    main(height=30)
    # draw_color_tree(height=12)

