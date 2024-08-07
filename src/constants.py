from M5 import Widgets

DEFAULT_TIME = 10.0
DEFAULT_FREQ = 1.0
DEFAULT_DIST = 5.0

I2C_ADDR = 0x25
I2C_FREQ = 100000
I2C_SCL_PIN_NUM = 8
I2C_SDA_PIN_NUM = 9

SERVO_CHANNEL = 0
SERVO_PULSE_MIN = 1050
SERVO_PULSE_MAX = 1950
SERVO_PULSE_MS_PER_MM = (1650-1350)/10.0

DISPLAY_BRIGHTNESS = 127
DISPLAY_FADE_DT = 0.001

COLORS = {
        'black'  : 0x000000,  
        'white'  : 0xffffff, 
        'green'  : 0x66FF66,
        'yellow' : 0xffff31,
        'blue'   : 0x1974d2,
        'amber'  : 0xffbf00,
        }

DEFAULT_FG_COLOR = COLORS['green']
DEFAULT_BG_COLOR = COLORS['black']

UPPERCASE_DELTA = '\u0394'

DEFAULT_TIME = 0.5 
TIME_MIN_VALUE = 0.1
TIME_MAX_VALUE = 60.0
TIME_DIGITS = 4
TIME_DECIMALS = 1
TIME_VALUE_TEXT = f't(min)'
TIME_STEP_SLOW = 0.001
TIME_STEP_FAST = 0.01
TIME_STEP_FIRST = 0.1

DEFAULT_FREQ = 0.1
FREQ_MIN_VALUE = 0.01
FREQ_MAX_VALUE = 1.0
FREQ_DIGITS = 4
FREQ_DECIMALS = 2
FREQ_STEP_SLOW = 0.0001
FREQ_STEP_FAST = 0.001
FREQ_STEP_FIRST = 0.01
FREQ_VALUE_TEXT = f'f(Hz) '

DEFAULT_DIST = 10.0
DIST_MIN_VALUE = 1.0
DIST_MAX_VALUE = 30.0
DIST_DIGITS = 4
DIST_DECIMALS = 1
DIST_VALUE_TEXT = f'{UPPERCASE_DELTA}(mm) '
DIST_STEP_SLOW = 0.001
DIST_STEP_FAST = 0.01
DIST_STEP_FIRST = 0.1

TIME_SCREEN_PARAM = {
        'value' : {
            'min'     : TIME_MIN_VALUE, 
            'max'     : TIME_MAX_VALUE, 
            'default' : DEFAULT_TIME, 
            },
        'label': {
            'text'     : TIME_VALUE_TEXT,
            'digits'   : TIME_DIGITS,
            'decimals' : TIME_DECIMALS,
            },
        'step' : {
            'slow'  : TIME_STEP_SLOW, 
            'fast'  : TIME_STEP_FAST, 
            'first' : TIME_STEP_FIRST ,
            },
        }

FREQ_SCREEN_PARAM = {
        'value' : {
            'min'     : FREQ_MIN_VALUE, 
            'max'     : FREQ_MAX_VALUE, 
            'default' : DEFAULT_FREQ, 
            },
        'label': {
            'text'     : FREQ_VALUE_TEXT, 
            'digits'   : FREQ_DIGITS,
            'decimals' : FREQ_DECIMALS,
            },
        'step' : {
            'slow'  : FREQ_STEP_SLOW, 
            'fast'  : FREQ_STEP_FAST, 
            'first' : FREQ_STEP_FIRST ,
            },
        }

DIST_SCREEN_PARAM = {
        'value' : {
            'min'     : DIST_MIN_VALUE, 
            'max'     : DIST_MAX_VALUE, 
            'default' : DEFAULT_DIST, 
            },
        'label': {
            'text'     : DIST_VALUE_TEXT, 
            'digits'   : DIST_DIGITS,
            'decimals' : DIST_DECIMALS,
            },
       'step' : {
            'slow'  : DIST_STEP_SLOW, 
            'fast'  : DIST_STEP_FAST, 
            'first' : DIST_STEP_FIRST ,
            },
        }

DEFAULT_FONT = { 
        'name' : 'EFontKR24',
        'size' : 1.2, 
        }

NAME_TO_FONT = { 
        'ASCII7'    : Widgets.FONTS.ASCII7,
        'DejaVu12'  : Widgets.FONTS.DejaVu12,
        'DejaVu18'  : Widgets.FONTS.DejaVu18,
        'DejaVu24'  : Widgets.FONTS.DejaVu24,
        'DejaVu40'  : Widgets.FONTS.DejaVu40,
        'DejaVu56'  : Widgets.FONTS.DejaVu56,
        'DejaVu72'  : Widgets.FONTS.DejaVu72,
        'DejaVu9'   : Widgets.FONTS.DejaVu9,
        'EFontCN24' : Widgets.FONTS.EFontCN24,
        'EFontJA24' : Widgets.FONTS.EFontJA24,
        'EFontKR24' : Widgets.FONTS.EFontKR24,
        }
