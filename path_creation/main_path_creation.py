import math
import random


def distance(dot1, dot2):
    x = dot2[0] - dot1[0]
    y = dot2[1] - dot1[1]
    dist = math.sqrt(x**2+y**2)
    return dist


def create_path(dots=None):
    connections = []
    if dots is None:
        dots = {
            'original': [[0, 0], [50, 100], [100, 0]],
            'shteins': [[50, 50]]
        }
    if len(dots['original'])-2 == len(dots['shteins']):
        shteins_dots = []
        tree_dots = []
        connections = []
        tree_connections = []
        for dot in dots['shteins']:
            shteins_dots.append([dot, 0, False])
        tree_dots.append(shteins_dots[0])
        for i in range(0, len(shteins_dots)-1):
            min_dist = 99999999
            min_dot1 = [[]]
            min_dot2 = [[]]
            for dot1 in tree_dots:
                for dot2 in shteins_dots:
                    dist = distance(dot1[0], dot2[0])
                    if (dist < min_dist) and (dot1[1] < 3) and (dot2[1] < 3) and (dist != 0) and (dot2 not in tree_dots):
                        min_dist = dist
                        min_dot1 = dot1
                        min_dot2 = dot2
            min_dot1[1] += 1
            min_dot2[1] += 1
            if min_dot1 not in tree_dots:
                tree_dots.append(min_dot1)
            if min_dot2 not in tree_dots:
                tree_dots.append(min_dot2)
            tree_connections.append([min_dot1[0], min_dot2[0]])

        connections = tree_connections
        for dot in dots['original']:
            min_dist = 99999999
            min_dot = []
            for shtein_dot in shteins_dots:
                dist = distance(dot, shtein_dot[0])
                if (dist < min_dist) and (shtein_dot[1] < 3):
                    min_dist = dist
                    min_dot = shtein_dot
            min_dot[1] += 1
            connections.append([dot, min_dot[0]])

        for dot in shteins_dots:
            if dot[1] !=3:
                print('fuuuuuuuk')

    else:
        print('wrong dots, dumbass')
    return connections


if __name__ == '__main__':
    dots = {
        'original': [[0,0], [100,100]],
        'shteins': [[20,20]]
    }
    lines = create_path(dots)
