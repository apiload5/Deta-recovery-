from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.filechooser import FileChooserListView
import os
import time

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Voice Recorder"
        elevation: 10

    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10

        MDLabel:
            id: status_label
            text: "Press Record to start recording"
            halign: 'center'

        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: None
            height: '48dp'

            MDRaisedButton:
                id: record_button
                text: "Record"
                on_press: app.start_recording()

            MDRaisedButton:
                id: stop_button
                text: "Stop"
                disabled: True
                on_press: app.stop_recording()

            MDRaisedButton:
                id: play_button
                text: "Play"
                disabled: True
                on_press: app.play_recording()
'''

class VoiceRecorderApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_recording(self):
        self.root.ids.status_label.text = "Recording..."
        self.root.ids.record_button.disabled = True
        self.root.ids.stop_button.disabled = False
        self.root.ids.play_button.disabled = True

        # Simulate recording (replace with actual recording code)
        self.recording_file = "recording_" + str(time.time()) + ".wav"
        self.recording = True
        Clock.schedule_interval(self.update_recording, 1)

    def stop_recording(self):
        self.root.ids.status_label.text = "Recording stopped"
        self.root.ids.record_button.disabled = False
        self.root.ids.stop_button.disabled = True
        self.root.ids.play_button.disabled = False

        # Stop recording (replace with actual stop recording code)
        self.recording = False
        Clock.unschedule(self.update_recording)

    def play_recording(self):
        if hasattr(self, 'recording_file') and os.path.exists(self.recording_file):
            self.sound = SoundLoader.load(self.recording_file)
            if self.sound:
                self.sound.play()
                self.root.ids.status_label.text = "Playing recording..."
            else:
                self.root.ids.status_label.text = "Error playing recording"
        else:
            self.root.ids.status_label.text = "No recording found"

    def update_recording(self, dt):
        if self.recording:
            # Simulate recording (replace with actual recording code)
            self.root.ids.status_label.text = "Recording... " + str(int(time.time() % 60)) + "s"

if __name__ == '__main__':
    VoiceRecorderApp().run()
