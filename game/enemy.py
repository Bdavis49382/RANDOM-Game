from game.entity import Entity
from constants import SCREEN_COLUMNS,SCREEN_ROWS,TILE_SIZE
import random
class Enemy(Entity):
    def __init__(self,position,material,player):
        super().__init__(position,material)
        self.player = player
        self.tags.append("enemy")

    
    def update(self,screen,map):
        super().update(screen,map)
        self.velocity =  self.get_next_step(map)
    
    def collide(self,other):
        if 'player' in other.tags:
            self.health -= 1
        super().collide(other)
    
    def valid_move(self, screen, map):
        if random.randint(0,100) < 50:
            return False
        return super().valid_move(screen, map)

    def get_next_step(self,map):
        player_pos = self.player.rect.x//TILE_SIZE,self.player.rect.y//TILE_SIZE
        # path_map = self.path(player_pos,self.rect.x//TILE_SIZE,self.rect.y//TILE_SIZE,map)
        steps,path_map = self.path(player_pos,map)
        
        # rows = []
        # for i in range(SCREEN_ROWS):
        #     row = []
        #     for column in path_map:
        #         row.append(column[i])
        #     rows.append(row)
        # for row in rows:
        #     print(row)
        
        # print(path_map[player_pos[0]][player_pos[1]])
        path_point = player_pos
        for i in range(len(steps)-2,0,-1):
            for point in steps[i]:
                differencex = abs(path_point[0] - point[0])
                differencey = abs(path_point[1] - point[1])
                if differencex + differencey == 1:
                    path_point = point
                    break
        return path_point[0] * TILE_SIZE - self.rect.x,path_point[1] * TILE_SIZE - self.rect.y

            
            
    def path(self,player_pos,map):
        start_x,start_y = self.rect.x//TILE_SIZE,self.rect.y//TILE_SIZE
        steps = [[(start_x,start_y)]]
        path_map =  [[-1 for _ in range(SCREEN_ROWS)] for _ in range(SCREEN_COLUMNS)]
        path_map[start_x][start_y] = 0
        step = 0
        while True:
            if player_pos in steps[step]:
                return steps,path_map
            steps.append([])
            for x,y in steps[step]:
                options = [(-1,0),(1,0),(0,-1),(0,1)]                
                for option in options:
                    new_x,new_y = x+option[0],y+option[1]
                    if new_x < 0 or new_x >= SCREEN_COLUMNS or new_y < 0 or new_y >= SCREEN_ROWS:
                        continue
                    elif not map.tiles[new_x][new_y].material.traversable:
                        path_map[new_x][new_y] = -5
                        continue
                    elif path_map[new_x][new_y]!= -1:
                        continue
                    else:
                        steps[step+1].append((new_x,new_y))
                        path_map[new_x][new_y] = step+1
            step += 1