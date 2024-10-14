"""
import pickle

Ask about whether it is adequate to use pickle
file_name = "game_map"
with open(filename, "wb") as outfile:
    pickle.dump(level_map, outfile)

with open(filename, "rb") as infile:
    level_map_2 = pickle.load(infile)
"""
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



