import pygame as pg


def display_update(surface):
    pg.display.update()
    surface.fill((0, 0, 0))


def events_handler(mouse=None):
    """
    This function handle all events in pygame
    :param mouse: current mouse position
    :return: those updated mouse and mouse_on_click
    """
    mouse_on_click = [[0, 0], 0]
    if mouse is None:
        mouse = [0, 0]
    keys = []
    if pg.get_init():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type == pg.MOUSEMOTION:
                mouse = event.pos
            if event.type == pg.MOUSEBUTTONUP:
                mouse_on_click = [event.pos, event.button]
            if event.type == pg.KEYUP:
                if chr(event.key) == '\x1b':
                    raise SystemExit
                keys.append(chr(event.key))
        variables_dict = {'mouse': mouse,
                          'mouse_on_click': mouse_on_click,
                          'keys': keys
                          }
        return variables_dict


def render_text(surface, text, x, y, w, h, rect_col, text_col):
    pg.draw.rect(surface, rect_col, (x, y, w, h))
    if len(text) == 0:
        return surface
    font_size = int(w // len(text))
    my_font = pg.font.SysFont("Calibri", font_size)
    my_text = my_font.render(text, 1, text_col)
    surface.blit(my_text, ((x + w // 2) - my_text.get_width() // 2,
                          (y + h // 2) - my_text.get_height() // 2))
    return surface


class Button:
    def __init__(self, x=0, y=0, w=100, h=100, a_col=(150, 150, 150),
                 i_col=(100, 100, 100), text_col=(0, 0, 0), text='', action=None, var=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.a_col = a_col
        self.i_col = i_col
        self.text_col = text_col
        self.text = text
        self.action = action
        self.var = var

    def check_mouse_position(self, mouse):
        if (self.x <= mouse[0] <= self.x+self.w) and (self.y <= mouse[1] <= self.y+self.h):
            return True

    def functionality(self, mouse_on_click):
        if self.check_mouse_position(mouse_on_click[0]):
            if (mouse_on_click[1] == 1) and (self.action is not None):
                self.var = self.action(self.var)

    def render_itself(self, surface, mouse, mouse_on_click):
        self.surface = surface
        if self.check_mouse_position(mouse):
            self.surface = render_text(self.surface, self.text, self.x, self.y, self.w, self.h, self.a_col, self.text_col)
        else:
            self.surface = render_text(self.surface, self.text, self.x, self.y, self.w, self.h, self.i_col, self.text_col)
        self.functionality(mouse_on_click)
        return self.surface, self.var


class InputPlace:
    def __init__(self, only_numbers=False, x=0, y=0, w=100, h=100, col=(150, 150, 150), text_col=(0, 0, 0)):
        self.only_numbers = only_numbers
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.text_col = text_col
        self.text = ''

    def functionality(self, keys):
        for key in keys:
            if key == '\x08':
                self.text = self.text[:-1]
                if len(self.text) == 0:
                    self.text = ''
                continue
            if self.only_numbers:
                if key.isdigit():
                    self.text += key
                    continue
            self.text += key

    def render_itself(self, surface, keys):
        self.surface = surface
        self.functionality(keys)
        self.suface = render_text(self.surface, self.text, self.x, self.y, self.w, self.h, self.col, self.text_col)
        return surface

    def get_result(self):
        return self.text


# test of the basic system
def simple_action():
    print('it\'s working, it\'s ALIVE!!!')


if __name__ == '__main__':
    pg.init()
    surface = pg.display.set_mode((500, 500))
    main_button = Button(250, 250, 100, 100, (150, 150, 0), (50, 50, 0), (255, 255, 255), 'MAIN', simple_action)
    main_input = InputPlace()
    mouse = [0, 0]
    mouse_on_click = [[0, 0], 0]
    while True:
        pg.time.wait(100)
        variables = events_handler(mouse)
        mouse = variables['mouse']
        mouse_on_click = variables['mouse_on_click']
        keys = variables['keys']
        main_button.render_itself(surface, mouse, mouse_on_click)
        main_input.render_itself(surface, keys)
        pg.display.update()
