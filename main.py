from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

import recoverpy

KV = '''
ScreenManager:
    MainScreen:
    RecoveryScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDLabel:
            text: 'Ticno Data Recovery'
            halign: 'center'
            font_style: 'H4'

        MDRectangleFlatButton:
            text: 'Recover Data'
            on_release: root.manager.current = 'recovery'

<RecoveryScreen>:
    name: 'recovery'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDLabel:
            text: 'Recover Deleted Files'
            halign: 'center'
            font_style: 'H4'

        MDTextField:
            id: path_input
            hint_text: 'Enter Path to Recover'

        MDRectangleFlatButton:
            text: 'Start Recovery'
            on_release: root.start_recovery()

        MDLabel:
            id: status_label
            text: ''
            halign: 'center'
'''

class MainScreen(Screen):
    pass

class RecoveryScreen(Screen):
    def start_recovery(self):
        path = self.ids.path_input.text
        if path:
            try:
                recoverpy.recover(path)
                self.ids.status_label.text = 'Recovery Started!'
            except Exception as e:
                self.ids.status_label.text = f'Error: {str(e)}'
        else:
            self.ids.status_label.text = 'Please enter a valid path.'

class TicnoDataRecoveryApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    TicnoDataRecoveryApp().run()
