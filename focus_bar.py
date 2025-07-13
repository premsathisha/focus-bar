import rumps
import time
import threading
from datetime import timedelta

class MyFocusBar(rumps.App):
    def __init__(self):
        super(MyFocusBar, self).__init__("Focus Bar")

        # Set default time duration
        self.default_duration = 20 * 60
        self.remaining = self.default_duration

        # App state
        self.timer_thread = None
        self.is_active = False

        # Define the menu structure with items
        self.menu = [
            rumps.MenuItem("Start", callback = self.start_timer),
            rumps.MenuItem("Pause", callback = self.pause_timer),
            rumps.MenuItem("Reset", callback = self.reset_timer),
            rumps.MenuItem("Set Timer", callback = None, dimensions = (160, 30)),
            None
        ]

        # Add preset timer options
        for mins in [20, 30, 40, 50, 60, 90, 120]:
            label = f"{mins} mins"
            self.menu["Set Timer"].add(rumps.MenuItem(label, callback = self.set_timer))

        self.update_title()
    
    def update_title(self):
        minutes = self.remaining // 60
        seconds = self.remaining % 60
        self.title = f"{minutes:02d}:{seconds:02d}" # Show MM:SS on menu bar

    def start_timer(self, _):
        if not self.is_active:
            self.is_active = True
            self.timer_thread = threading.Thread(target = self.run_timer)
            self.timer_thread.daemon = True # Allows thread to exit when app quits
            self.timer_thread.start()

    def pause_timer(self, _):
        if self.is_active:
            self.is_active = False

    def reset_timer(self, _):
        self.is_active = False
        self.remaining = self.default_duration
        self.update_title()

    def set_timer(self, sender):
        if not self.is_active:
            minutes = int(sender.title.split()[0]) # Get minutes from menu item title
            self.default_duration = minutes * 60
            self.remaining = self.default_duration
            self.update_title()

    def run_timer(self):
        while self.is_active and self.remaining > 0:
            time.sleep(1)

            if not self.is_active:
                break # Stop counting down if paused or reset

            self.remaining -= 1

            try:
                self.update_title()
            except Exception:
                pass

        # If time is up, notify and reset
        if self.remaining <= 0 and self.is_active:
            self.is_active = False
            rumps.notification("Focus Bar", "Time's Up!", "Your focus session is complete!")
            self.remaining = self.default_duration
            try:
                self.update_title()
            except Exception:
                pass

# Run the app
if __name__ == "__main__":
    MyFocusBar().run()
