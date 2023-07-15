import pygame
from constants import TILE_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT
class Player:
    def __init__(self,x,y,images,index = 0):
        self.rect = pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
        self.images = images
        self.index = index
        self.velocity = (0,0)
    
    def update(self,screen,map):
        self.index += 1
        self.index %= len(self.images)
        if self.valid_move(screen,map):
            self.rect = self.rect.move(self.velocity[0],self.velocity[1])
    
    def valid_move(self,screen,map):
        new_rect = self.rect.move(self.velocity[0],self.velocity[1])
        if not screen.get_rect().contains(new_rect):
            return False

        tile = map.tiles[new_rect.x//TILE_SIZE][new_rect.y//TILE_SIZE]
        if not tile.material.traversable:
            return False
        return True
            

    def draw(self,screen):
        screen.blit(self.images[self.index],self.rect)