import pygame as pg
from visualising.main_page import prepare_rendering_main_page, render_main_page
from visualising.global_variables import events_handler, display_update
from visualising.result_page import render_result_page
pg.init()


class Visualise:
    def __init__(self, lines=None, dots=None, phase=None):
        self.lines = lines
        self.dots = dots
        self.phase = phase
        self.variables = None
        if self.phase is None:
            self.phase = 'main_page'
        self.surface = pg.display.set_mode((800, 800))
        self.w, self.h = self.surface.get_size()
        self.mouse = [0, 0]
        self.mouse_on_click = [[0, 0], 0]
        self.keys = None
        self.number_of_dots = 0
        prepare_rendering_main_page(self.surface, self.phase)
        if self.lines is None:
            self.lines = [[[self.w // 2 - 50, self.h // 2 - 50], [self.w // 2 + 50, self.h // 2 + 50]],
                          [[self.w // 2 - 50, self.h // 2 + 50], [self.w // 2 + 50, self.h // 2 - 50]]]

    def render(self, dots=None, lines=None, number_of_dots=None):
        if dots is not None:
            self.dots = dots
        if lines is not None:
            self.lines = lines
        pg.time.wait(100)
        self.variables = events_handler(self.mouse)
        self.mouse = self.variables['mouse']
        self.mouse_on_click = self.variables['mouse_on_click']
        self.keys = self.variables['keys']
        (self.surface, self.phase, self.number_of_dots) = render_main_page(self.surface, self.phase,
                                                                           self.mouse, self.mouse_on_click,
                                                                           self.keys, self.number_of_dots)
        (self.surface, self.phase) = render_result_page(self.surface, self.phase, self.mouse,
                                                        self.mouse_on_click, self.lines, self.dots)
        display_update(self.surface)
        return self.number_of_dots, self.phase


if __name__ == '__main__':
    visual_system = Visualise()

    while True:
        visual_system.render()