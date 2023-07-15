import pygame,random
from constants import TILE_SIZE
class Tile:
    def __init__(self,x,y,material,variety=-1) -> None:
        if variety == -1:
            variety = random.randrange(0,material.varieties)
        self.variety = variety
        self.material = material
        self.rect = pygame.rect.Rect(x,y,TILE_SIZE,TILE_SIZE)
        self.map_pos = (x//TILE_SIZE,y//TILE_SIZE)
    
    def update_text_map(self,text_map):
        text_map[self.map_pos[0]][self.map_pos[1]] = f'{self.material.material}:{self.variety}'

    def draw(self,screen):
        image = self.material.images[self.variety]
        screen.blit(image,self.rect)
    
    def __str__(self):
        return str(self.rect)