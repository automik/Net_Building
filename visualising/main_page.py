from visualising.global_variables import Button, events_handler
import pygame as pg

if not pg.get_init():
    pg.init()
start_button = Button()


def main_page_prepare_rendering(surface):
    w, h = surface.get_size()
    global start_button
    start_button = Button(w // 2 - w // 6, h // 2 - h // 10, w // 3, h // 5, (50, 200, 75), (25, 100, 50), (0, 0, 0),
                          'START')


def main_page_render(surface, state, mouse, mouse_on_click):
    if state != 'main_page':
        return surface
    global start_button
    surface = start_button.render_itself(surface, mouse, mouse_on_click)
    return surface


if __name__ == '__main__':
    surface = pg.display.set_mode((400, 500))
    print(surface.get_size())
    mouse = [0, 0]
    mouse_on_click = [[0, 0], 0]
    main_page_prepare_rendering(surface)
    while True:
        pg.time.wait(100)
        variables = events_handler(mouse)
        mouse = variables['mouse']
        mouse_on_click = variables['mouse_on_click']
        keys = variables['keys']
        main_page_render(surface, 'main_page', mouse, mouse_on_click)
        pg.display.update()
