import pygame
from constants import TILE_SIZE
class Entity:
    def __init__(self,position,material,index = 0,health = 10):
        self.rect = pygame.Rect(position[0],position[1],TILE_SIZE,TILE_SIZE)
        self.material = material
        self.index = index
        self.health = health
        self.velocity = (0,0)
        self.tags = []
        self.enabled = True
    
    def update(self,screen,map):
        self.index += 1
        self.index %= self.material.varieties
        if self.valid_move(screen,map):
            self.rect = self.rect.move(self.velocity[0],self.velocity[1])
        

    def collide(self,other):
        if self.health <= 0:
            self.enabled = False
    
    def add_velocity(self,vector):
        self.velocity = self.velocity[0] + vector[0],self.velocity[1] + vector[1]
    
    def valid_move(self,screen,map):
        new_rect = self.rect.move(self.velocity[0],self.velocity[1])
        if not screen.get_rect().contains(new_rect):
            return False

        tile = map.tiles[new_rect.x//TILE_SIZE][new_rect.y//TILE_SIZE]
        if not tile.material.traversable:
            return False
        return True
            

    def draw(self,screen):
        screen.blit(self.material.images[self.index],self.rect)