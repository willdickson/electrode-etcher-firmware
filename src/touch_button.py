import copy
from M5 import Widgets
from constants import NAME_TO_FONT

class TouchButton:

    def __init__(self, param):
        self.param = copy.deepcopy(param)
        self.create_rect()
        self.create_label()
        self.create_image()
        self.visible = False 

    def create_rect(self):
        apos = self.param['apos']
        size = self.param['size']
        fg_color = self.param['fg_color']
        bg_color = self.param['bg_color']
        self.rect = Widgets.Rectangle(*apos, *size, fg_color, bg_color) 

    def create_label(self):
        try:
            label_param = self.param['label']
        except KeyError:
            self.label = None
            return
        rpos = label_param['rpos']
        text = label_param['text']
        font_size = label_param['font']['size']
        font_name = label_param['font']['name']
        font = NAME_TO_FONT[font_name]
        fg_color = label_param.get('color', self.param['fg_color'])
        bg_color = self.param['bg_color']
        apos = rpos_to_apos(self.param['apos'], rpos)
        self.label = Widgets.Label(text, *apos, font_size, fg_color, bg_color, font)

    def create_image(self):
        try:
            image_param = self.param['image']
        except KeyError:
            self.image = None
            return
        file = image_param['file']
        rpos = image_param['rpos']
        apos = rpos_to_apos(self.param['apos'], rpos)
        self.image = Widgets.Image(file, *apos)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self.rect.setVisible(value)
        if self.label is not None:
            self.label.setVisible(value)
        if self.image is not None:
            self.image.setVisible(value)
        self._visible = value

    def is_inside(self, x, y):
        sx, sy = self.param['size']
        x0, y0 = self.param['apos']
        x1, y1 = x0 + sx, y0 + sy
        return ((x>=x0) and (x<=x1)) and ((y>=y0) and (y<=y1))

# Utility functions
def rpos_to_apos(parent_apos, rpos):
    apos = rpos[0] + parent_apos[0], rpos[1] + parent_apos[1]
    return apos








