import json,random
from ui.material import Material
from game.player import Player
from game.enemy import Enemy
from constants import TILE_SIZE,SCREEN_COLUMNS,SCREEN_ROWS
class EntityHandler:
    def __init__(self,manager):
        self.manager = manager
        self.entities = []
        self.player_materials = self.get_materials('player_materials')
        self.enemy_materials = self.get_materials('enemy_materials')
        self.player = Player(self.get_random_spawn(self.manager.ui.maps[self.manager.ui.current_map_index]),self.player_materials["blob"])
        self.entities.append(Enemy(self.get_random_spawn(self.manager.ui.maps[self.manager.ui.current_map_index]),self.enemy_materials["angry_blob"],self.player))
        self.entities.append(Enemy(self.get_random_spawn(self.manager.ui.maps[self.manager.ui.current_map_index]),self.enemy_materials["angry_blob"],self.player))
        self.entities.append(Enemy(self.get_random_spawn(self.manager.ui.maps[self.manager.ui.current_map_index]),self.enemy_materials["angry_blob"],self.player))
        self.entities.append(self.player)
    
    def get_materials(self, type):
        materials = {}
        with open("assets/materials.json","r") as file:
            self.materials_list =  json.load(file)[type]
            for material in self.materials_list:
                images = self.manager.ui.get_images(f'assets/images/{material["material"]}.png',material['varieties'])
                materials[material['material']] = Material(material['material'],images,material['varieties'],material['traversable'])
        return materials


    def append(self, entity):
        self.entities.append(entity)
    
    def get_random_spawn(self,map):
        while True:
            x = random.randint(0,SCREEN_COLUMNS-1)
            y = random.randint(0,SCREEN_ROWS-1)
            if any([entity.rect.x//TILE_SIZE == x and entity.rect.y//TILE_SIZE == y for entity in self.entities]):
                continue
            if map.tiles[x][y].material.traversable:
                return (x * TILE_SIZE,y * TILE_SIZE)
        
    
    def update_all(self,screen,map):
        for entity in self.entities:
            if entity.enabled:
                entity.update(screen,map)
        
        for entity in self.entities:
            if entity.enabled:
                for other in self.entities:
                    if other.enabled and other != entity and entity.rect.colliderect(other.rect):
                        entity.collide(other)
    def draw_all(self, screen):
        for entity in self.entities:
            if entity.enabled:
                entity.draw(screen)