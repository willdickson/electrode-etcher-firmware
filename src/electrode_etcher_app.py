import time
import M5
from events import Event
from events import event_to_str

from state_machine import State
from state_machine import StateMachine
from state_machine import state_to_str
from motion_controller import MotionController
from stopped_screen import StoppedScreen
from running_screen import RunningScreen
from value_editor_screen import ValueEditorScreen

from constants import COLORS
from constants import DEFAULT_TIME
from constants import DEFAULT_FREQ
from constants import DEFAULT_DIST
from constants import DISPLAY_BRIGHTNESS
from constants import DISPLAY_FADE_DT
from constants import DIST_SCREEN_PARAM
from constants import FREQ_SCREEN_PARAM
from constants import TIME_SCREEN_PARAM


class ElectrodeEtcherApp:

    def __init__(self):

        # Initialize M5 and display
        M5.begin()
        M5.Display.clear()
        M5.Widgets.fillScreen(COLORS['black'])
        M5.Display.setBrightness(0)

        # Create screens
        self.stopped_screen = StoppedScreen()
        self.running_screen = RunningScreen()
        self.time_edit_screen = ValueEditorScreen(TIME_SCREEN_PARAM)
        self.freq_edit_screen = ValueEditorScreen(FREQ_SCREEN_PARAM)
        self.dist_edit_screen = ValueEditorScreen(DIST_SCREEN_PARAM)
        self.state_to_screen = {
                State.STOPPED   : self.stopped_screen, 
                State.RUNNING   : self.running_screen, 
                State.TIME_EDIT : self.time_edit_screen, 
                State.FREQ_EDIT : self.freq_edit_screen,
                State.DIST_EDIT : self.dist_edit_screen, 
                }
        self.current_screen = None
        self.state_machine = StateMachine()
        self.state_machine.state = State.STOPPED
        self.change_screen()

        # Setup motion controller
        self.motion_controller = MotionController()
        self.motion_controller.move_to_zero()

    @property
    def run_param(self):
        run_param = {
                'time': self.time_edit_screen.value, 
                'freq': self.freq_edit_screen.value, 
                'dist': self.dist_edit_screen.value,
                }
        return run_param

    def change_screen(self):
        self.display_fade_out()
        if self.current_screen is not None:
            self.current_screen.visible = False
        self.current_screen = self.state_to_screen[self.state_machine.state]
        M5.Display.clear()
        self.current_screen.visible = True
        self.display_fade_in()

    def display_fade_in(self):
        for i in range(DISPLAY_BRIGHTNESS+1):
            M5.Display.setBrightness(i)
            time.sleep(DISPLAY_FADE_DT)

    def display_fade_out(self):
        for i in range(DISPLAY_BRIGHTNESS,-1,-1):
            M5.Display.setBrightness(i)
            time.sleep(DISPLAY_FADE_DT)

    def check_for_touch(self):
        pos = None
        if M5.Touch.getCount() > 0:
            x = M5.Touch.getX()
            y = M5.Touch.getY()
            pos = x,y
        return pos

    def handle_button_events(self,t): 
        pos = self.check_for_touch()
        if pos is None:
            return
        event = self.current_screen.on_button_event(t, pos)
        if self.state_machine.update(event):
            self.clear_touch_events()
            self.change_screen()
            if self.state_machine.state == State.RUNNING:
                self.motion_controller.start(time.ticks_ms(), self.run_param)
            elif self.state_machine.state == State.STOPPED:
                self.motion_controller.stop()

    def clear_touch_events(self):
        while M5.Touch.getCount() > 0:
            M5.update()

    def update(self): 
        M5.update()
        self.handle_button_events(time.ticks_ms())
        self.motion_controller.update(time.ticks_ms())
        if self.state_machine.state == State.RUNNING: 
            if self.motion_controller.running == False:
                self.state_machine.update(Event.MOTION_STOPPED)
                self.change_screen()
        elapsed_time_min = self.motion_controller.elapsed_time_min(time.ticks_ms())
        self.current_screen.update(elapsed_time_min, self.run_param)

    def run(self):
        while True:
            self.update()

