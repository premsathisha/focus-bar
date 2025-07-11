import rumps
import time
import threading
from datetime import timedelta

class MyFocusBar(rumps.App):
    def __init__(self):
        super(MyFocusBar, self).__init__("Focus Bar")

        self.icon = "icons.icns"

        # Set default time duration
        self.default_duration = 20 * 60
        self.remaining = self.default_duration

        # App state
        self.timer_thread = None
        self.is_active = False

        # Define the menu structure with items
        self.menu = [
            rumps.MenuItem("Start", callback = self.start_timer, key = "s"),
            rumps.MenuItem("Pause", callback = self.pause_timer, key = "p"),
            rumps.MenuItem("Reset", callback = self.reset_timer, key = "r"),
            rumps.MenuItem("Set Timer", callback = None, dimensions = (160, 30)),
            None
        ]

        # Add preset timer options
        for mins in [20, 30, 40, 50, 60, 90, 120]:
            label = f"{mins} mins"
            self.menu["Set Timer"].add(rumps.MenuItem(label, callback = self.set_timer))

    def start_timer(self, _):
        pass

    def pause_timer(self, _):
        pass

    def reset_timer(self, _):
        pass

    def set_timer(self, _):
        pass

# Run the app
if __name__ == "__main__":
    MyFocusBar().run()
