from constants import TILE_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT
import random,json
def add_random_text_map():
    with open("assets/saved_maps.json","r") as file:
        text_maps = json.load(file)
    with open("assets/sheets.json","r") as file:
        materials_list = json.load(file)['materials']
    text_map = []
    for _ in range(0,SCREEN_WIDTH,TILE_SIZE): 
        rows = []
        for _ in range(0,SCREEN_HEIGHT,TILE_SIZE):
            material = random.choice(materials_list)
            rows.append(f'{material["material"]}:{random.randrange(material["varieties"])}')
        text_map.append(rows)
    with open("assets/saved_maps.json","w") as file:
        text_maps.append(text_map)
        json.dump(text_maps,file)

if __name__ == "__main__":
    add_random_text_map()