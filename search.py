import math
import queue
from node import Node

def get_neighbours(star_node, map):
    neighbours = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #chat gpt
    for x, y in directions:
        new_x = star_node.x + x
        new_y = star_node.y + y
        if new_x <= len(map[0]) -1 and new_x >= 0 and new_y <= len(map) -1 and new_y >= 0 and map[new_y][new_x] != 1:
            neighbouring_node = Node(new_x, new_y)
            neighbours.append(neighbouring_node)
    return neighbours

def reconstruct(current, path):
    path.append(current)
    if current.parent_pointer.parent_pointer == None:
        #print(current.x, current.y)
        return None
    reconstruct(current.parent_pointer, path)
    return path[::-1] #need to reverse this path afterwards

def a_search (start, target, map):
    open_set = queue.PriorityQueue()
    open_set_nodes = []
    closed_set = []
    path = []
    start.g_score = 0
    start.update_scores(target.x, target.y, 0)
    open_set.put((start.f_score, start))
    open_set_nodes.append((start.x, start.y))
    #open_set.append(current)
    #while open_set.qsize() != 0:
    while open_set.qsize() != 0:
        current = open_set.get()[1]
        open_set_nodes.remove((current.x, current.y))
        if current.x == target.x and current.y == target.y:#Ask Mr T about memory address java similarity
            return reconstruct(current, path)
        else:
            closed_set.append((current.x, current.y))
            neighbours = get_neighbours(current, map)
            for neighbour in neighbours:
                if neighbour in closed_set:
                    continue
                hypothetic_g = neighbour.g_score + 1
                neighbour.update_scores(target.x, target.y, current.g_score)
                neighbour.update_parent_pointer(current)
                if (neighbour.x, neighbour.y) not in open_set_nodes:
                    neighbour.update_scores(target.x, target.y, current.g_score)
                    neighbour.update_parent_pointer(current)
                    open_set.put((neighbour.f_score, neighbour))
                    open_set_nodes.append((neighbour.x, neighbour.y))
                if hypothetic_g > neighbour.g_score:
                    neighbour.update_scores(target.x, target.y, current.g_score)
                    neighbour.update_parent_pointer(current)
    return None
