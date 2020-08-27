from visualising.global_variables import Button, events_handler, render_text, InputPlace
import pygame as pg

if not pg.get_init():
    pg.init()
start_button = Button()
number_of_dots_input = InputPlace()


def change_phase_to_results(state):
    return 'result_page'


def prepare_rendering_main_page(surface, state):
    w, h = surface.get_size()
    global start_button, number_of_dots_input
    start_button = Button(w // 2 - w // 6, h // 2 - h // 5, w // 3, h // 5, (50, 200, 75), (25, 100, 50), (0, 0, 0),
                          'START', change_phase_to_results, state)
    number_of_dots_input = InputPlace(True, w//2 - w//8, h//2 + h//8, w//4, h//6)


def render_main_page(surface, state, mouse, mouse_on_click, keys, number):
    if state != 'main_page':
        return surface, state, number
    global start_button, number_of_dots_input
    surface, state = start_button.render_itself(surface, mouse, mouse_on_click)
    number_of_dots_input.render_itself(surface, keys)
    if number_of_dots_input.text.isdigit():
        number = int(number_of_dots_input.text)
    else:
        number = 0
    print(surface, state, number)
    return surface, state, number


if __name__ == '__main__':
    surface = pg.display.set_mode((400, 500))
    mouse = [0, 0]
    mouse_on_click = [[0, 0], 0]
    prepare_rendering_main_page(surface)
    while True:
        pg.time.wait(100)
        variables = events_handler(mouse)
        mouse = variables['mouse']
        mouse_on_click = variables['mouse_on_click']
        keys = variables['keys']
        render_main_page(surface, 'main_page', mouse, mouse_on_click)

        pg.display.update()
