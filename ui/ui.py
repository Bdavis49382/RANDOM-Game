import json,pygame
from constants import TILE_SIZE,SPRITE_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT,BLACK
from ui.map import Map
from ui.material import Material
class UI:
    def __init__(self,manager):
        self.manager = manager
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("the RANDOM Game")
        self.current_map_index = 0

        # self.images = {}
        self.materials = self.get_materials()
        # for material in self.materials:
        #     self.images[material['material']] = self.get_images(f'assets/images/{material["material"]}.png',material['varieties'])

        self.text_maps = self.get_text_maps()
        self.maps = [Map(text_map,self.materials) for text_map in self.text_maps]

    def save_text_maps(self):
        with open("assets/saved_maps.json","w") as file:
            json.dump(self.text_maps,file)

    def draw(self,player):
        self.screen.fill(BLACK)
        self.maps[self.current_map_index].draw(self.screen)
        player.draw(self.screen)

    def get_text_maps(self):
        with open("assets/saved_maps.json","r") as file:
            return json.load(file)
    
    def get_materials(self):
        materials = {}
        with open("assets/sheets.json","r") as file:
            self.materials_list =  json.load(file)['materials']
            for material in self.materials_list:
                images = self.get_images(f'assets/images/{material["material"]}.png',material['varieties'])
                materials[material['material']] = Material(material['material'],images,material['varieties'],material['traversable'])
        return materials

            
    
    def get_images(self,file_name,number):
        '''Returns a list of images for a material'''
        images = []
        sheet =  pygame.image.load(file_name).convert_alpha()
        sheet.set_alpha(255)
        counter = 1
        for y in range(0,2):
            for x in range(0,2):
                if counter > number:
                    break
                counter += 1
                rect = pygame.Rect(x*SPRITE_SIZE,y*SPRITE_SIZE,SPRITE_SIZE,SPRITE_SIZE)
                image = pygame.Surface(rect.size).convert()
                image.blit(sheet,(0,0), rect)
                image.set_colorkey((0,0,0))
                images.append(pygame.transform.scale(image,(TILE_SIZE,TILE_SIZE)).convert_alpha())
            if counter > number:
                break
        return images