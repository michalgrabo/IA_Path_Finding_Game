
import pickle

#Ask about whether it is adequate to use pickle
"""
level_map = [
    "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "xx                      x",
    "xx                      x",
    "xxxx                   xx",
    "xxxxp    e             xx",
    "xxxxxxxxxxxxxxxxxxxxxxxxx",
]
"""
level_map = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "xx                                                    x",
    "xx                                                    x",
    "xx                                                    x",
    "xx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx           x",
    "xx   x                           x                    x",
    "xx   x       xxxxxxx             x              e     x",
    "xx   x       x                   x                    x",
    "xx   x       x    xxxxxxxxxxxx   xxxxxxxxxxxxxx       x",
    "xx   x       x            x   x              x        x",
    "xx        x       x       x       x          x        x",
    "xx   x       x            x   x              x        x",
    "xx   xxxxx   xxxxx        x   xxxxx          xxxxxxxxxx",
    "xx        x       x       x       x          x        x",
    "xx        x       x       x       x          x        x",
    "xx        x       x       x       x          x        x",
    "xx        x       x       x       xxxxxxxx   xxxxxxx  x",
    "xx        x       xxxxx   xxxxx            x x     x  x",
    "xxxxxxxxxxx           x      x             x   x   x  x",
    "xx           xxxxxxxxxxxx      xxxxxxxxxxxxx x     x  x",
    "xx                                 p            x  x  x",
    "xx                                                    x",
    "xx                                                    x",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]

tile_size = 25
screen_width =  len(level_map[0]) * tile_size
screen_height = len(level_map) * tile_size
fps = 60
level_map_grid = []
file_name = "game_map"
speed = 1

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

def visibility_field(size, pos):
    field_grid = []
    for i in range(size, -size - 1, -1):
        for j in range(-size, size + 1):
            field_grid.append((j, i))
    actual_field = []
    #print(field_grid)
    for i in range(len(field_grid)):
        real_pos_x = field_grid[i][0] + convert_grid(pos.x)
        real_pos_y = field_grid[i][1] + convert_grid(pos.y)
        actual_field.append((real_pos_x, real_pos_y))
    return actual_field

def convert_grid(value):
    return int(value/tile_size)



