class Event:
    EDIT_PRESSED  = 0
    PLAY_PRESSED  = 1
    DONE_PRESSED  = 2
    STOP_PRESSED  = 3
    VALUE_CHANGED = 4
    MOTION_STOPPED = 5

event_to_str = {
        Event.EDIT_PRESSED   : 'edit pressed', 
        Event.PLAY_PRESSED   : 'play pressed', 
        Event.DONE_PRESSED   : 'done pressed', 
        Event.STOP_PRESSED   : 'stop pressed', 
        Event.VALUE_CHANGED  : 'value changed',
        Event.MOTION_STOPPED : 'motion stopped', 
        None                 : 'None', 
        }
