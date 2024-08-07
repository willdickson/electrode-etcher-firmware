from events import Event
from utils import recursive_update
from value_label import ValueLabel
from touch_button import TouchButton

from constants import DEFAULT_TIME
from constants import TIME_DIGITS
from constants import TIME_DECIMALS
from constants import TIME_VALUE_TEXT

from constants import DEFAULT_FREQ
from constants import FREQ_DIGITS
from constants import FREQ_DECIMALS
from constants import FREQ_VALUE_TEXT

from constants import DEFAULT_DIST
from constants import DIST_DIGITS
from constants import DIST_DECIMALS 
from constants import DIST_VALUE_TEXT

from constants import DEFAULT_FONT
from constants import DEFAULT_FG_COLOR
from constants import DEFAULT_BG_COLOR
from constants import UPPERCASE_DELTA

default_param = {
        'value' : {
            'dist' : DEFAULT_DIST, 
            'freq' : DEFAULT_FREQ,
            'time' : DEFAULT_TIME,
            }, 
        'label' : {
            'time' : {
                'text'     : TIME_VALUE_TEXT,
                'digits'   : TIME_DIGITS, 
                'decimals' : TIME_DECIMALS,
                'apos'     : (10, 50),
                'fg_color' : DEFAULT_FG_COLOR, 
                'bg_color' : DEFAULT_BG_COLOR, 
                'font'     : DEFAULT_FONT, 
                },
            'freq' : {
                'text'     : FREQ_VALUE_TEXT,
                'digits'   : FREQ_DIGITS, 
                'decimals' : FREQ_DECIMALS,
                'apos'     : (10, 100),
                'fg_color' : DEFAULT_FG_COLOR, 
                'bg_color' : DEFAULT_BG_COLOR, 
                'font'     : DEFAULT_FONT, 
                }, 
            'dist' : {
                'text'     : DIST_VALUE_TEXT,
                'digits'   : DIST_DIGITS, 
                'decimals' : DIST_DECIMALS,
                'apos'     : (10, 150),
                'fg_color' : DEFAULT_FG_COLOR, 
                'bg_color' : DEFAULT_BG_COLOR, 
                'font'     : DEFAULT_FONT, 
                },
            }, 
        'button' : {
            'edit' : { 
                'apos'        : (200, 16),
                'size'        : (100, 100), 
                'fg_color'    : DEFAULT_BG_COLOR, 
                'bg_color'    : DEFAULT_BG_COLOR, 
                'image'  : {
                    'file' : '/flash/edit_circle.png', 
                    'rpos' : (10,10), 
                    },
                }, 
            'play' : { 
                'apos'        : (200, 127),
                'size'        : (100, 100), 
                'fg_color'    : DEFAULT_BG_COLOR, 
                'bg_color'    : DEFAULT_BG_COLOR, 
                'image'  : {
                    'file' : '/flash/play_circle.png', 
                    'rpos' : (10,10),
                    },
                },

            },
        }

class StoppedScreen:

    def __init__(self, param=None):
        self.param = recursive_update(default_param, param)
        self.edit_button = None
        self.play_button = None
        self.setup_touch_buttons()
        self.setup_value_labels()
        self.visible = False

    def setup_touch_buttons(self):
        self.edit_button = TouchButton(self.param['button']['edit'])
        self.play_button = TouchButton(self.param['button']['play'])

    def setup_value_labels(self):
        dist_value = self.param['value']['dist']
        dist_label_param = self.param['label']['dist']
        self.dist_label = ValueLabel(dist_value, dist_label_param) 

        freq_value = self.param['value']['freq']
        freq_label_param = self.param['label']['freq']
        self.freq_label = ValueLabel(freq_value, freq_label_param)

        time_value = self.param['value']['time']
        time_label_param = self.param['label']['time']
        self.time_label = ValueLabel(time_value, time_label_param)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self.edit_button.visible = value
        self.play_button.visible = value
        self.dist_label.visible = value
        self.freq_label.visible = value
        self.time_label.visible = value
        self._visible = value

    def set_value_labels(self, values):
        self.dist_label.value = values['dist']
        self.freq_label.value = values['freq']
        self.time_label.value = values['time']

    def update(self, elapsed_time, run_param):
        self.set_value_labels(run_param)

    def on_button_event(self, t_now, touch_pos):
        if self.edit_button.is_inside(*touch_pos):
            return Event.EDIT_PRESSED
        elif self.play_button.is_inside(*touch_pos):
            return Event.PLAY_PRESSED
        else:
            return None
