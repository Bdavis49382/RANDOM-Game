from ui.tile import Tile
from constants import TILE_SIZE,SCREEN_COLUMNS,SCREEN_ROWS,SCREEN_HEIGHT,SCREEN_WIDTH,TILE_SIZE
import pygame,random,json
class Map:
    def __init__(self,text_map,materials):
        self.tiles = []

        self.materials = materials
        self.text_map = text_map
        for x in range(0,SCREEN_WIDTH,TILE_SIZE): 
            row = []
            for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
                text = self.text_map[x//TILE_SIZE][y//TILE_SIZE]
                if text.find(":") == -1:
                    row.append(Tile(x,y,self.materials[self.text_map[x//TILE_SIZE][y//TILE_SIZE]]))
                else:
                    material,variety = text.split(":")
                    row.append(Tile(x,y,self.materials[material],int(variety)))
            self.tiles.append(row)
    
    
    def check_tiles(self,point:tuple):
        for column in self.tiles:
            for tile in column:
                if tile.rect.collidepoint(point):
                    return tile
    

    
    def draw(self,screen):
        '''Draws all tiles onto the screen.'''
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)