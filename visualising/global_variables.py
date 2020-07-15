import pygame as pg


def handle_events(mouse=None):
    """
    This function handle all events in pygame
    :param mouse: current mouse position
    :return: those updated mouse and mouse_on_click
    """
    mouse_on_click = None
    if mouse_on_click is None:
        mouse_on_click = [[0, 0], 0]
    if mouse is None:
        mouse = [0, 0]
    if pg.get_init():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type == pg.MOUSEMOTION:
                mouse = event.pos
            if event.type == pg.MOUSEBUTTONUP:
                mouse_on_click = [event.pos, event.button]
        variables_dict = {'mouse': mouse,
                          'mouse_on_click': mouse_on_click
                          }
        return variables_dict


class Button:
    def __init__(self, surface, x, y, w, h, a_col, i_col, text_col, text, action):
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.a_col = a_col
        self.i_col = i_col
        self.text_col = text_col
        self.text = text
        self.action = action

    def check_mouse_position(self, mouse):
        if (self.x <= mouse[0] <= self.x+self.w) and (self.y <= mouse[1] <= self.y+self.h):
            return True

    def functionality(self, mouse_on_click):
        if self.check_mouse_position(mouse_on_click[0]):
            if (mouse_on_click[1] == 1) and (self.action is not None):
                self.action()

    def draw_rectangular(self, mouse):
        if self.check_mouse_position(mouse):
            pg.draw.rect(self.surface, self.a_col, (self.x, self.y, self.w, self.h))
        else:
            pg.draw.rect(self.surface, self.i_col, (self.x, self.y, self.w, self.h))

    def draw_text(self):
        font_size = int(self.w // len(self.text))
        my_font = pg.font.SysFont("Calibri", font_size)
        my_text = my_font.render(self.text, 1, self.text_col)
        self.surface.blit(my_text, ((self.x + self.w // 2) - my_text.get_width() // 2,
                                   (self.y + self.h // 2) - my_text.get_height() // 2))

    def render_button(self, mouse, surface, mouse_on_click):
        self.surface = surface
        self.draw_rectangular(mouse)
        self.draw_text()
        self.functionality(mouse_on_click)
        return self.surface


# test of the basic system
def simple_action():
    print('it\'s working, it\'s ALIVE!!!')


if __name__ == '__main__':
    pg.init()
    surface = pg.display.set_mode((500, 500))
    main_button = Button(surface, 250, 250, 100, 100, (150, 150, 0), (50, 50, 0), (255, 255, 255), 'MAIN', simple_action)
    mouse = [0, 0]
    mouse_on_click = [[0, 0], 0]
    while True:
        pg.time.wait(100)
        variables = handle_events(mouse)
        mouse = variables['mouse']
        mouse_on_click = variables['mouse_on_click']
        main_button.render_button(mouse, surface, mouse_on_click)
        pg.display.update()
