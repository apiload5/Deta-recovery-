from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class RecoveryApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Press to scan deleted videos")
        self.add_widget(self.label)

        self.scan_btn = Button(text="Scan Videos")
        self.scan_btn.bind(on_press=self.scan_deleted_videos)
        self.add_widget(self.scan_btn)

    def scan_deleted_videos(self, instance):
        self.label.text = "Scanning..."
        possible_paths = [
            "/sdcard/DCIM/.thumbnails",
            "/sdcard/Movies",
            "/sdcard/WhatsApp/Media/WhatsApp Video"
        ]
        found = []
        for path in possible_paths:
            if os.path.exists(path):
                for f in os.listdir(path):
                    if f.endswith((".mp4", ".3gp")):
                        found.append(os.path.join(path, f))

        if found:
            self.label.text = f"Found {len(found)} videos."
        else:
            self.label.text = "No deleted videos found."

class TicnoRecoveryApp(App):
    def build(self):
        return RecoveryApp()

if __name__ == '__main__':
    TicnoRecoveryApp().run()
            
