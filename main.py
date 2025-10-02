from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
import os
from datetime import datetime

class FileCard(BoxLayout):
    def __init__(self, file_name, file_size, file_type, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.padding = [10, 5]
        
        # File icon based on type
        icon_path = self.get_icon_path(file_type)
        icon = Image(
            source=icon_path,
            size_hint_x=None,
            width=40
        )
        
        # File info
        info_layout = BoxLayout(orientation='vertical')
        name_label = Label(
            text=file_name,
            size_hint_y=0.6,
            halign='left',
            text_size=(200, None)
        )
        size_label = Label(
            text=f"Size: {file_size}",
            size_hint_y=0.4,
            font_size='12sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        
        info_layout.add_widget(name_label)
        info_layout.add_widget(size_label)
        
        # Select button
        self.select_btn = ToggleButton(
            text='Select',
            size_hint_x=None,
            width=80
        )
        
        self.add_widget(icon)
        self.add_widget(info_layout)
        self.add_widget(self.select_btn)
    
    def get_icon_path(self, file_type):
        icons = {
            'video': 'assets/icons/video_icon.png',
            'image': 'assets/icons/image_icon.png',
            'audio': 'assets/icons/audio_icon.png',
            'document': 'assets/icons/doc_icon.png'
        }
        return icons.get(file_type, 'assets/icons/file_icon.png')

class DataRecoveryApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        self.title = "ایڈوانسڈ موبائل ڈیٹا ریکوری"
        self.scanned_files = []
        
        return self.create_main_ui()
    
    def create_main_ui(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Header
        header = self.create_header()
        main_layout.add_widget(header)
        
        # Control buttons
        controls = self.create_control_buttons()
        main_layout.add_widget(controls)
        
        # Progress section
        progress_section = self.create_progress_section()
        main_layout.add_widget(progress_section)
        
        # Files list
        files_section = self.create_files_section()
        main_layout.add_widget(files_section)
        
        # Action buttons
        actions = self.create_action_buttons()
        main_layout.add_widget(actions)
        
        return main_layout
    
    def create_header(self):
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=80
        )
        
        # App icon and title
        icon = Image(
            source='assets/icons/recovery_icon.png',
            size_hint_x=None,
            width=60
        )
        
        title_layout = BoxLayout(orientation='vertical')
        main_title = Label(
            text='ایڈوانسڈ ڈیٹا ریکوری',
            font_size='24sp',
            bold=True,
            color=(0.2, 0.4, 0.8, 1)
        )
        sub_title = Label(
            text='اپنا ڈیلیٹڈ ڈیٹا واپس پائیں',
            font_size='14sp',
            color=(0.5, 0.5, 0.5, 1)
        )
        
        title_layout.add_widget(main_title)
        title_layout.add_widget(sub_title)
        
        header_layout.add_widget(icon)
        header_layout.add_widget(title_layout)
        
        return header_layout
    
    def create_control_buttons(self):
        layout = GridLayout(cols=3, spacing=10, size_hint_y=None, height=70)
        
        buttons_config = [
            ('فوری اسکین', (0.2, 0.6, 1, 1), self.quick_scan),
            ('گہری اسکین', (0.3, 0.8, 0.3, 1), self.deep_scan),
            ('صرف ویڈیوز', (0.9, 0.5, 0.1, 1), self.video_scan)
        ]
        
        for text, color, callback in buttons_config:
            btn = Button(
                text=text,
                background_color=color,
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=callback)
            layout.add_widget(btn)
        
        return layout
    
    def create_progress_section(self):
        layout = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        
        self.progress_label = Label(
            text='تیار ہے۔ اسکین شروع کریں۔',
            size_hint_y=None,
            height=30
        )
        
        self.progress_bar = ProgressBar(
            max=100,
            size_hint_y=None,
            height=25
        )
        
        self.stats_label = Label(
            text='ملے ہوئے فائلز: 0',
            size_hint_y=None,
            height=25,
            font_size='12sp'
        )
        
        layout.add_widget(self.progress_label)
        layout.add_widget(self.progress_bar)
        layout.add_widget(self.stats_label)
        
        return layout
    
    def create_files_section(self):
        # Scrollable files list
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=1)
        
        files_label = Label(
            text='ملے ہوئے فائلز:',
            size_hint_y=None,
            height=30,
            bold=True
        )
        scroll_layout.add_widget(files_label)
        
        # Files grid
        self.files_grid = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None
        )
        self.files_grid.bind(minimum_height=self.files_grid.setter('height'))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.files_grid)
        scroll_layout.add_widget(scroll_view)
        
        return scroll_layout
    
    def create_action_buttons(self):
        layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint_y=None,
            height=70
        )
        
        self.select_all_btn = Button(
            text='سب سلیکٹ کریں',
            background_color=(0.5, 0.5, 0.5, 1)
        )
        self.select_all_btn.bind(on_press=self.select_all_files)
        
        self.recover_btn = Button(
            text='سلیکٹڈ فائلز ریکور کریں',
            background_color=(0.3, 0.8, 0.3, 1)
        )
        self.recover_btn.bind(on_press=self.recover_selected_files)
        
        layout.add_widget(self.select_all_btn)
        layout.add_widget(self.recover_btn)
        
        return layout
    
    def quick_scan(self, instance):
        self.start_scanning('quick')
    
    def deep_scan(self, instance):
        self.start_scanning('deep')
    
    def video_scan(self, instance):
        self.start_scanning('video')
    
    def start_scanning(self, scan_type):
        self.progress_label.text = f'{scan_type} اسکین شروع ہو رہی ہے...'
        self.progress_bar.value = 0
        self.files_grid.clear_widgets()
        
        # Simulate scanning process
        Clock.schedule_interval(lambda dt: self.update_scan_progress(scan_type), 0.05)
    
    def update_scan_progress(self, scan_type):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 2
            
            # Add sample files at certain progress points
            if self.progress_bar.value in [20, 40, 60, 80]:
                self.add_sample_files()
                
        else:
            Clock.unschedule(self.update_scan_progress)
            self.progress_label.text = 'اسکین مکمل!'
            self.stats_label.text = f'ملے ہوئے فائلز: {len(self.scanned_files)}'
    
    def add_sample_files(self):
        # Sample files for demonstration
        sample_files = [
            {'name': 'video_001.mp4', 'size': '15.2 MB', 'type': 'video'},
            {'name': 'photo_123.jpg', 'size': '2.1 MB', 'type': 'image'},
            {'name': 'document.pdf', 'size': '0.8 MB', 'type': 'document'},
            {'name': 'audio_track.mp3', 'size': '3.4 MB', 'type': 'audio'}
        ]
        
        for file_info in sample_files:
            file_card = FileCard(
                file_info['name'],
                file_info['size'],
                file_info['type']
            )
            self.files_grid.add_widget(file_card)
            self.scanned_files.append(file_info)
    
    def select_all_files(self, instance):
        for child in self.files_grid.children:
            if hasattr(child, 'select_btn'):
                child.select_btn.state = 'down'
    
    def recover_selected_files(self, instance):
        selected_count = sum(1 for child in self.files_grid.children 
                           if hasattr(child, 'select_btn') and child.select_btn.state == 'down')
        
        self.progress_label.text = f'{selected_count} فائلز ریکور ہو رہی ہیں...'
        self.progress_bar.value = 0
        
        Clock.schedule_interval(self.update_recovery_progress, 0.1)
    
    def update_recovery_progress(self, dt):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 5
        else:
            Clock.unschedule(self.update_recovery_progress)
            self.progress_label.text = 'ریکوری مکمل!'
            
            # Show success message
            success_layout = BoxLayout(orientation='vertical', padding=20)
            success_label = Label(
                text='✅ تمام سلیکٹڈ فائلز کامیابی سے ریکور ہو گئیں!',
                color=(0, 0.7, 0, 1),
                font_size='18sp'
            )
            success_layout.add_widget(success_label)
            
            # You can add this to a popup

if __name__ == '__main__':
    DataRecoveryApp().run()
