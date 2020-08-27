from visualising.global_variables import Button, events_handler, render_text
import pygame as pg

if not pg.get_init():
    pg.init()


def draw_connections(surface, state, lines):
    if state != 'test_page':
        return surface
    for line in lines:
        pg.draw.line(surface, (240, 185, 153), line[0], line[1])
        pg.draw.circle(surface, (255, 100, 100), line[0], 5)
        pg.draw.circle(surface, (255, 100, 100), line[1], 5)
    return surface


if __name__ == '__main__':
    surface = pg.display.set_mode((400, 500))
    mouse = [0, 0]
    while True:
        pg.time.wait(100)
        variables = events_handler(mouse)
        draw_connections(surface, 'test_page', [[[0, 0], [100, 100]], [[0, 100], [100, 0]]])
        pg.display.update()

