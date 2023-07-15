import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,BLACK,GREEN,TILE_SIZE,UPDATE_DELAY,KEY_MAP
from ui.map import Map
from game.player import Player
from ui.ui import UI
class Manager:
    def __init__(self):
        self.ui = UI(self)

        self.player = Player(4*TILE_SIZE, 4*TILE_SIZE,self.ui.get_images('assets/images/blob.png',4))
        self.clock = pygame.time.Clock()
        self.edit_mode = False
        
        self.run_game()
        self.ui.save_text_maps()
    

        
    def run_game(self):
        current_time = pygame.time.get_ticks()
        update_time = current_time + UPDATE_DELAY
        while True:
            self.clock.tick(60)
            self.ui.draw(self.player)

            if not self.edit_mode:
                current_time = pygame.time.get_ticks()
                if current_time > update_time:
                    self.player.update(self.ui.screen,self.ui.maps[self.ui.current_map_index])
                    update_time = current_time + UPDATE_DELAY

            if not self.handle_events():
                break
            
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key in KEY_MAP.keys():
                    self.player.velocity = KEY_MAP[event.key]
                elif event.key == pygame.K_m:
                    self.edit_mode = not self.edit_mode
                elif event.key == pygame.K_l and self.edit_mode:
                    self.ui.current_map_index = (self.ui.current_map_index + 1) % len(self.ui.maps)
            if event.type == pygame.KEYUP:
                if event.key in KEY_MAP.keys():
                    self.player.velocity = (0,0)
            if event.type == pygame.MOUSEBUTTONDOWN and self.edit_mode:
                mouse_pos = pygame.mouse.get_pos()
                tile =  self.ui.maps[self.ui.current_map_index].check_tiles(mouse_pos)
                if tile:
                    if event.button == 1:
                        tile.variety += 1
                        if tile.variety == len(tile.material.images):
                            tile.variety = 0
                        tile.update_text_map(self.ui.text_maps[self.ui.current_map_index])
                    if event.button == 3:
                        for i,material in enumerate(self.ui.materials_list):
                            if tile.material.material == material["material"]:
                                if i < len(self.ui.materials_list)-1:
                                    tile.material = self.ui.materials[self.ui.materials_list[i+1]['material']]
                                else:
                                    tile.material = self.ui.materials[self.ui.materials_list[0]['material']]
                                tile.variety = 0
                                tile.update_text_map(self.ui.text_maps[self.ui.current_map_index])
                                break
        return True