from visualising.global_variables import Button, events_handler, render_text
import pygame as pg

if not pg.get_init():
    pg.init()


def draw_connections(surface, lines, dots):
    for line in lines:
        pg.draw.line(surface, (240, 185, 153), line[0], line[1])
    for type, dot_set in dots.items():
        for dot in dot_set:
            if type == 'original':
                pg.draw.circle(surface, (255, 100, 100), dot, 7)
            elif type == 'shteins':
                pg.draw.circle(surface, (100, 100, 255), dot, 7)
    return surface


def render_result_page(surface, state, mouse, mouse_on_click, lines, dots):
    if state != 'result_page':
        return surface, state
    surface = draw_connections(surface, lines, dots)
    return surface, state


if __name__ == '__main__':
    surface = pg.display.set_mode((400, 500))
    mouse = [0, 0]
    mouse_on_click = [[0, 0], 0]
    lines = [[[0, 0], [100, 100]], [[0, 100], [100, 0]]]
    while True:
        pg.time.wait(100)
        variables = events_handler(mouse)
        mouse = variables['mouse']
        mouse_on_click = variables['mouse_on_click']
        keys = variables['keys']
        render_result_page(surface, 'main_page', mouse, mouse_on_click, lines)
        pg.display.update()

