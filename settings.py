
import pickle

#Ask about whether it is adequate to use pickle

level_map = [
    "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "xx                      x",
    "xx                      x",
    "xxxx                   xx",
    "xxxxp     e            xx",
    "xxxxxxxxxxxxxxxxxxxxxxxxx",
]
tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
fps = 60
level_map_grid = []
file_name = "game_map"
with open(file_name, "wb") as outfile:
    pickle.dump(level_map, outfile)

with open(file_name, "rb") as infile:
    level_map_2 = pickle.load(infile)

for row in level_map_2:
    row_list = []
    for character in row:
        if character == "x":
            row_list.append(1)
        else:
            row_list.append(0)
    level_map_grid.append(row_list)

def convert(pos1):
    grid_pos = (pos1.x/tile_size, pos1.y/tile_size)
    return grid_pos



