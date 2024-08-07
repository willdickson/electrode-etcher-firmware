import math
import time
import machine
import unit.servos8

from utils import s_to_ms
from utils import ms_to_s
from utils import s_to_min
from utils import min_to_ms
from utils import pulse_mm_to_ms
from utils import pulse_ms_to_mm
from utils import sawtooth

from constants import I2C_FREQ
from constants import I2C_ADDR
from constants import I2C_SCL_PIN_NUM 
from constants import I2C_SDA_PIN_NUM
from constants import SERVO_CHANNEL
from constants import SERVO_PULSE_MIN
from constants import SERVO_PULSE_MAX

class MotionController:

    def __init__(self):
        scl_pin = machine.Pin(I2C_SCL_PIN_NUM)
        sda_pin = machine.Pin(I2C_SDA_PIN_NUM)
        self.i2c = machine.I2C(0, scl=scl_pin, sda=sda_pin, freq=I2C_FREQ)
        self.servo = unit.servos8.Servos8Unit(self.i2c, address=I2C_ADDR)
        self.servo.set_mode(unit.servos8.SERVO_CTRL_MODE, SERVO_CHANNEL)

        self.running = False
        self.time_start_ms = 0.0
        self.time_done_ms = 0.0
        self.dist_mm = 0.0
        self.freq_hz = 0.0

    def move_to_zero(self):
        self.servo.set_servo_pulse(SERVO_PULSE_MIN, SERVO_CHANNEL)

    def is_done(self,t):
        done = False 
        if self.running: 
            done = self.elapsed_time_ms(t) >= self.time_done_ms
        return done

    def start(self, t, run_param):
        self.running = True
        self.time_start_ms = t
        self.time_done_ms = min_to_ms(run_param['time'])
        self.dist_mm = run_param['dist']
        self.freq_hz = run_param['freq']

    def stop(self):
        self.running = False
        self.move_to_zero()

    def elapsed_time_ms(self,t_ms):
        if self.running:
            return t_ms - self.time_start_ms
        else:
            return 0.0

    def elapsed_time_s(self,t):
        return ms_to_s(self.elapsed_time_ms(t))

    def elapsed_time_min(self,t):
        return s_to_min(self.elapsed_time_s(t))

    def update(self, t_ms):
        if self.running:
            elapsed_time_s = self.elapsed_time_s(t_ms)
            position_mm = sawtooth(elapsed_time_s, self.dist_mm, self.freq_hz)
            position_ms = int(pulse_mm_to_ms(position_mm)) + SERVO_PULSE_MIN
            self.servo.set_servo_pulse(position_ms, SERVO_CHANNEL)
            if self.is_done(t_ms):
                self.stop()


    
