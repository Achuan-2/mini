def draw_simple_tree(height):
    print('\033[1;32m', end='')
    for i in range(height):
        print((' '*(height-i))+("*"*(2*i+1)))
    print(' '*(height-2)+f'\033[32m[   ]\033[0m')
    print(' '*(height-2)+f'\033[32m[___]\033[0m')
if __name__=="__main__":
    draw_simple_tree(height=35)
