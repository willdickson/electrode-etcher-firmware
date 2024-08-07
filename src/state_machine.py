from events import Event

class State:
    STOPPED = 0
    RUNNING = 1
    DIST_EDIT = 2
    FREQ_EDIT = 3
    TIME_EDIT = 4

state_to_str = {
        State.STOPPED   : 'stopped', 
        State.RUNNING   : 'running', 
        State.DIST_EDIT : 'dist edit', 
        State.FREQ_EDIT : 'freq edit', 
        State.TIME_EDIT : 'time edit', 
        }


class StateMachine:

    TABLE = {
            State.STOPPED :  {
                Event.EDIT_PRESSED : State.TIME_EDIT,
                Event.PLAY_PRESSED : State.RUNNING, 
                },
            State.RUNNING : {
                Event.STOP_PRESSED   : State.STOPPED, 
                Event.MOTION_STOPPED : State.STOPPED,
                },
            State.TIME_EDIT : {
                Event.DONE_PRESSED : State.FREQ_EDIT,
                },
            State.FREQ_EDIT : {
                Event.DONE_PRESSED : State.DIST_EDIT,
                },
            State.DIST_EDIT : {
                Event.DONE_PRESSED : State.STOPPED,
                },
            }

    def __init__(self):
        self.state = State.STOPPED

    def update(self, event):
        try:
            self.state = self.TABLE[self.state][event]
            changed = True
        except KeyError:
            changed = False
        return changed



        
