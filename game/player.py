from game.entity import Entity
class Player(Entity):
    def __init__(self,position,material):
        super().__init__(position,material)
        self.tags.append('player')
    
    def collide(self,other):
        if 'enemy' in other.tags:
            self.health -= 1
            print(f'player health: {self.health}')
        super().collide(other)

        