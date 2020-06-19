"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: pygamer.py
@time: 2020-5-16 下午 5:22

I'm a green hand
"""

import pygame

def game():
    pygame.init()

    secreen = pygame.display.set_mode((800,600))

    pygame.display.set_caption('haha')

    running =True
    while running:
        for enent in pygame.event.get():
            if enent.type == pygame.QUIT:
                running = False
if __name__ == '__main__':
    game()