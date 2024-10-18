
import pickle

#Ask about whether it is adequate to use pickle

level_map = [
    "bbbbbbbbbbbbbbbbbbbbbbbbb",
    "bx                      b",
    "bx                      b",
    "bxxx                   xb",
    "bxxxp     e            xb",
    "bbbbbbbbbbbbbbbbbbbbbbbbb",
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

def convert_grid(value):
    return int(value/tile_size)



