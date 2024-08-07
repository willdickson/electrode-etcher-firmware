import time
from M5 import Widgets
from utils import clamp
from utils import recursive_update
from events import Event
from value_label import ValueLabel
from touch_button import TouchButton
from constants import DEFAULT_FONT
from constants import DEFAULT_FG_COLOR
from constants import DEFAULT_BG_COLOR


default_param = { 
        'value': { 
            'min'     : 0,
            'max'     : 10,
            'default' : 0.0, 
            },
        'step' : {
            'slow'  : 0.001, 
            'fast'  : 0.01, 
            'first' : 0.1,
            },
        'dt' : {
            'mode_timeout' : 250, 
            'speed_change' : 3000,
            },
        'label' : {
            'text'     : 'Value',  
            'digits'   : 4, 
            'decimals' : 1,
            'apos'     : (25, 55),
            'fg_color' : DEFAULT_FG_COLOR, 
            'bg_color' : DEFAULT_BG_COLOR, 
            'font'     : DEFAULT_FONT, 
            }, 
        'button' :  { 
            'incr' : { 
                'apos'        : (200, 16),
                'size'        : (100, 100), 
                'fg_color'    : DEFAULT_BG_COLOR, 
                'bg_color'    : DEFAULT_BG_COLOR, 
                'image'  : {
                    'file' : '/flash/arrow_circle_up.png', 
                    'rpos' : (10,10), 
                    },
                }, 
            'decr' : { 
                'apos'        : (200, 127),
                'size'        : (100, 100), 
                'fg_color'    : DEFAULT_BG_COLOR, 
                'bg_color'    : DEFAULT_BG_COLOR, 
                'image'  : {
                    'file' : '/flash/arrow_circle_down.png', 
                    'rpos' : (10,10),
                    },
                },
            'done' : {
                'apos'        : (10, 127),
                'size'        : (100, 100), 
                'fg_color'    : DEFAULT_BG_COLOR, 
                'bg_color'    : DEFAULT_BG_COLOR, 
                'image'  : {
                    'file' : '/flash/check_circle.png', 
                    'rpos' : (10,10),
                    },
                }, 
            }
        }


class ValueEditorScreen:

    def __init__( self, param=None): 
        self.param = recursive_update(default_param, param)
        self.incr_button = None
        self.decr_button = None
        self.done_button = None
        self.value_label = None

        self.setup_touch_buttons()
        self.setup_value_label()
        self.visible = False

        self.is_first_incr = False
        self.is_first_decr = False
        self.t_last_incr = time.ticks_ms()
        self.t_last_decr = time.ticks_ms()
        self.t_start_incr = time.ticks_ms()
        self.t_start_decr = time.ticks_ms()
        self.value = self.param['value']['default']

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self.incr_button.visible = value
        self.decr_button.visible = value
        self.done_button.visible = value 
        self.value_label.visible = value
        self._visible = value

    def setup_touch_buttons(self):
        self.incr_button = TouchButton(self.param['button']['incr'])
        self.decr_button = TouchButton(self.param['button']['decr'])
        self.done_button = TouchButton(self.param['button']['done'])

    def setup_value_label(self):
        self.value_label = ValueLabel(
                value = self.param['value']['default'],
                param = self.param['label'], 
                )

    def update(self, elapsed_time, run_param):
        pass

    def on_button_event(self, t_now, touch_pos):
        step = 0
        step_sign = 0
        touched = False

        # Handle increment button presses
        if self.incr_button.is_inside(*touch_pos):
            touched = True
            step_sign = 1 
            if t_now - self.t_last_incr > self.param['dt']['mode_timeout']:
                self.t_start_incr = t_now
                self.is_first_incr = True
            if self.is_first_incr:
                step = self.param['step']['first']
            else:
                if t_now - self.t_start_incr > self.param['dt']['speed_change']:
                    step = self.param['step']['fast']
                else:
                    step = self.param['step']['slow']
            self.t_last_incr = t_now
            self.is_first_incr = False

        # Handle increment button presses
        if self.decr_button.is_inside(*touch_pos):
            touched = True
            step_sign = -1
            if t_now - self.t_last_decr > self.param['dt']['mode_timeout']:
                self.t_start_decr = t_now
                self.is_first_decr = True
            if self.is_first_decr:
                step = self.param['step']['first']
            else:
                if t_now - self.t_start_decr > self.param['dt']['speed_change']:
                    step = self.param['step']['fast']
                else:
                    step = self.param['step']['slow']
            self.t_last_decr = t_now
            self.is_first_decr = False

        # Update value based a cacluated step size and sign 
        if touched:
            max_value = self.param['value']['max']
            min_value = self.param['value']['min']
            self.value = clamp(self.value + step_sign*step, min_value, max_value)
            text = self.param['label']['text']
            self.value_label.value = self.value

        # Check to see if done is pressed
        if self.done_button.is_inside(*touch_pos):
            event = Event.DONE_PRESSED
        else:
            event = None

        return event



    

