import copy
from constants import SERVO_PULSE_MS_PER_MM

def sawtooth(t, amplitude, frequency):
    """ 
    Output sawtooth waveform at given time point for given amplitudelitude and
    frequencyuency. Sawtooth is assumed to go from 0 to amplitude and back. 

    Parameters 
    ----------
    t : float
        time in seconds

    amplitude : float
        peak-to-peak amplitudelitude of sawtooth waveform

    frequency : float
         frequencyuency of sawtooth waveform

    Returns
    -------

    value : float
        value of sawtooth waveform at time t

    """
    period = 1.0/frequency
    tmod = t % period
    if tmod <= period/2:
        slope = 2.0*amplitude/period
        offset = 0.0
    else:
        slope = -2.0*amplitude/period
        offset = 2.0*amplitude 
    value = slope*tmod + offset
    return value


def clamp(val, min_val, max_val):
    """ Clamp value, val,  between min_val and max_val """
    return max(min(val, max_val), min_val)


def recursive_update(a, b):
    """ Recursively update dict a with dict b """
    a_copy = copy.deepcopy(a)
    if b is not None:
        for k, v in b.items():
            if type(v) == dict:
                a_copy[k] = recursive_update(a_copy.get(k, dict()), v)
            else:
                a_copy[k] = copy.deepcopy(v)
    return a_copy


def pulse_ms_to_mm(value_ms):
    """ convert ms of ms of servo pulse width to mm of servo position """
    return value_ms/SERVO_PULSE_MS_PER_MM


def pulse_mm_to_ms(value_mm):
    """ convert mm of servo position to ms of servo pulse width """
    return value_mm*SERVO_PULSE_MS_PER_MM


def s_to_ms(val):
    """ Convert seconds to milliseconds """
    return val*1.0e3

def ms_to_s(val):
    """ Convert milliseconds to seconds """
    return val*1.0e-3

def s_to_min(val):
    """ Convert seconds to minutes """
    return val/60.0

def min_to_s(val):
    """ Convert minutes to seconds """
    return val*60.0

def min_to_ms(val):
    """ Convert minutes to milliseconds """
    return s_to_ms(min_to_s(val))

def ms_to_min(val):
    """ Convert milliseconds to minutes """
    return s_to_min(ms_to_s(val))

