import pygame,sys
from game.manager import Manager

if __name__ == '__main__':
    pygame.init()
    Manager()
    pygame.quit()
    sys.exit()