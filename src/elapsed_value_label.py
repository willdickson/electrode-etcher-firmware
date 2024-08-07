from M5 import Widgets
from utils import recursive_update
from constants import DEFAULT_FONT
from constants import NAME_TO_FONT
from constants import DEFAULT_FG_COLOR
from constants import DEFAULT_BG_COLOR

default_param = { 
        'text'     : 'value',
        'digits'   : 4, 
        'decimals' : 1,
        'apos'     : (0, 20),
        'fg_color' : DEFAULT_FG_COLOR, 
        'bg_color' : DEFAULT_BG_COLOR, 
        'font'     : DEFAULT_FONT, 
        }

class ElapsedValueLabel:

    def __init__(self, value=0.0, done_value=0.0, param=None):
        self.param = recursive_update(default_param, param)
        self.value = value
        self.done_value = done_value
        
        if param is not None:
            recursive_update(self.param, param)
        self.setup_label()
        self.visible = False

    def setup_label(self):
        font_name = self.param['font']['name']
        font = NAME_TO_FONT[font_name]
        self.label = Widgets.Label(
                self.label_str(self.value, self.done_value),
                *self.param['apos'], 
                self.param['font']['size'], 
                self.param['fg_color'],
                self.param['bg_color'],
                font,
                )

    def label_str(self, value, done_value):
        text = self.param['text']
        digits = self.param['digits']
        decimals = self.param['decimals']
        return f'{text} {value:{digits}.{decimals}f}/{done_value:{digits}.{decimals}f}' 

    def update(self, value, done_value):
        self.label.setText(self.label_str(value, done_value))

    def value_str(self, ):
        text = self.param['text']
        digits = self.param['digits']
        decimals = self.param['decimals']
        return f'{text} {self._value:{digits}.{decimals}f}' 

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self.label.setVisible(value)
        self._visible = value

