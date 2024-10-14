import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.priority = 0
        self.parent_pointer = None

    def __lt__(self, other):
        return self.f_score < other.f_score

    def update_scores(self, goal_x, goal_y, old_g):
        self.h_score = math.sqrt((goal_x - self.x)**2 + (goal_y - self.y)**2)
        self.g_score = old_g + 1
        self.f_score = self.g_score + self.h_score

    def update_parent_pointer(self, parent):
        self.parent_pointer = parent

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
