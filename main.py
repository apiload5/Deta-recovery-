from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: 'Tecno Data Recovery'
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H4'
        MDRaisedButton:
            text: 'Start Data Recovery'
            pos_hint: {'center_x': 0.5}
            on_release: app.start_data_recovery()
'''

class HomeScreen(Screen):
    pass

class TecnoDataRecoveryApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_data_recovery(self):
        # Add your data recovery logic here
        print("Data recovery started")

if __name__ == '__main__':
    TecnoDataRecoveryApp().run()
