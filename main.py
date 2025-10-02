from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Rectangle

class FileCard(BoxLayout):
    def __init__(self, file_info, **kwargs):
        super().__init__(**kwargs)
        self.file_info = file_info
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 70
        self.padding = [10, 5]
        self.spacing = 10
        
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.create_widgets()
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def create_widgets(self):
        # File icon
        icon = Image(
            source=self.get_icon_path(),
            size_hint_x=None,
            width=40
        )
        
        # File information
        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        
        name_label = Label(
            text=self.file_info['name'],
            size_hint_y=0.6,
            halign='left',
            text_size=(200, None),
            color=(0, 0, 0, 1)
        )
        
        details_text = f"Size: {self.file_info.get('size', 'N/A')} | Type: {self.file_info['type']}"
        details_label = Label(
            text=details_text,
            size_hint_y=0.4,
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1)
        )
        
        info_layout.add_widget(name_label)
        info_layout.add_widget(details_label)
        
        # Select button
        self.select_btn = ToggleButton(
            text='Select',
            size_hint_x=None,
            width=80,
            background_color=(0.2, 0.6, 1, 1)
        )
        
        self.add_widget(icon)
        self.add_widget(info_layout)
        self.add_widget(self.select_btn)
    
    def get_icon_path(self):
        icon_map = {
            'video': 'assets/icons/video_icon.png',
            'image': 'assets/icons/image_icon.png',
            'audio': 'assets/icons/audio_icon.png',
            'document': 'assets/icons/document_icon.png',
            'other': 'assets/icons/file_icon.png'
        }
        return icon_map.get(self.file_info['type'], 'assets/icons/file_icon.png')
    
    def is_selected(self):
        return self.select_btn.state == 'down'

class ProgressWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 120
        self.padding = [10, 5]
        self.spacing = 5
        
        self.create_widgets()
    
    def create_widgets(self):
        self.progress_label = Label(
            text='تیار ہے۔ اسکین شروع کریں۔',
            size_hint_y=None,
            height=30,
            font_size='14sp'
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
            font_size='12sp',
            color=(0.5, 0.5, 0.5, 1)
        )
        
        self.time_label = Label(
            text='مقررہ وقت: --',
            size_hint_y=None,
            height=20,
            font_size='11sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        
        self.add_widget(self.progress_label)
        self.add_widget(self.progress_bar)
        self.add_widget(self.stats_label)
        self.add_widget(self.time_label)
    
    def update_progress(self, value, text=None, stats=None, time_remaining=None):
        self.progress_bar.value = value
        
        if text:
            self.progress_label.text = text
        
        if stats:
            self.stats_label.text = stats
        
        if time_remaining:
            self.time_label.text = f'مقررہ وقت: {time_remaining}'
    
    def reset(self):
        self.progress_bar.value = 0
        self.progress_label.text = 'تیار ہے۔ اسکین شروع کریں۔'
        self.stats_label.text = 'ملے ہوئے فائلز: 0'
        self.time_label.text = 'مقررہ وقت: --'

class MainScreen(BoxLayout):
    def __init__(self, app_instance, **kwargs):
        super().__init__(**kwargs)
        self.app = app_instance
        self.orientation = 'vertical'
        self.padding = [15, 15]
        self.spacing = 15
        
        self.create_ui()
    
    def create_ui(self):
        # Header
        header = self.create_header()
        self.add_widget(header)
        
        # Controls
        controls = self.create_control_buttons()
        self.add_widget(controls)
        
        # Progress
        self.add_widget(self.app.progress_widget)
        
        # Files section
        files_section = self.create_files_section()
        self.add_widget(files_section)
        
        # Actions
        actions = self.create_action_buttons()
        self.add_widget(actions)
    
    def create_header(self):
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=80
        )
        
        icon = Image(
            source='assets/icons/app_icon.png',
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
            ('فوری اسکین', (0.2, 0.6, 1, 1), self.app.quick_scan),
            ('گہری اسکین', (0.3, 0.8, 0.3, 1), self.app.deep_scan),
            ('صرف ویڈیوز', (0.9, 0.5, 0.1, 1), self.app.video_scan)
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
    
    def create_files_section(self):
        layout = BoxLayout(orientation='vertical', size_hint_y=1)
        
        section_title = Label(
            text='ملے ہوئے فائلز:',
            size_hint_y=None,
            height=30,
            bold=True,
            font_size='16sp'
        )
        layout.add_widget(section_title)
        
        self.files_grid = GridLayout(
            cols=1,
            spacing=5,
            size_hint_y=None
        )
        self.files_grid.bind(minimum_height=self.files_grid.setter('height'))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.files_grid)
        layout.add_widget(scroll_view)
        
        return layout
    
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
        self.select_all_btn.bind(on_press=self.app.select_all_files)
        
        self.recover_btn = Button(
            text='سلیکٹڈ فائلز ریکور کریں',
            background_color=(0.3, 0.8, 0.3, 1)
        )
        self.recover_btn.bind(on_press=self.app.recover_selected_files)
        
        layout.add_widget(self.select_all_btn)
        layout.add_widget(self.recover_btn)
        
        return layout
    
    def clear_files_grid(self):
        self.files_grid.clear_widgets()
    
    def add_file_card(self, file_card):
        self.files_grid.add_widget(file_card)

class MobileDataRecoveryApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scanned_files = []
        self.selected_files = []
        self.progress_widget = None
        self.main_screen = None
    
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        self.title = "Mobile Data Recovery"
        
        self.progress_widget = ProgressWidget()
        self.main_screen = MainScreen(self)
        
        return self.main_screen
    
    def quick_scan(self, instance):
        self.progress_widget.update_progress(0, "فوری اسکین شروع ہو رہی ہے...")
        self.main_screen.clear_files_grid()
        self.scanned_files = []
        
        Clock.schedule_interval(self.simulate_quick_scan, 0.1)
    
    def deep_scan(self, instance):
        self.progress_widget.update_progress(0, "گہری اسکین شروع ہو رہی ہے...")
        self.main_screen.clear_files_grid()
        self.scanned_files = []
        
        Clock.schedule_interval(self.simulate_deep_scan, 0.05)
    
    def video_scan(self, instance):
        self.progress_widget.update_progress(0, "ویڈیو اسکین شروع ہو رہی ہے...")
        self.main_screen.clear_files_grid()
        self.scanned_files = []
        
        Clock.schedule_interval(self.simulate_video_scan, 0.08)
    
    def simulate_quick_scan(self, dt):
        current_progress = self.progress_widget.progress_bar.value
        
        if current_progress < 100:
            self.progress_widget.update_progress(
                current_progress + 5,
                f"فوری اسکین ہو رہی ہے... {current_progress}%",
                f"ملے ہوئے فائلز: {len(self.scanned_files)}"
            )
            
            if current_progress % 20 == 0:
                self.add_sample_files('quick')
                
        else:
            Clock.unschedule(self.simulate_quick_scan)
            self.progress_widget.update_progress(
                100, 
                "فوری اسکین مکمل!",
                f"کل ملے ہوئے فائلز: {len(self.scanned_files)}"
            )
    
    def simulate_deep_scan(self, dt):
        current_progress = self.progress_widget.progress_bar.value
        
        if current_progress < 100:
            self.progress_widget.update_progress(
                current_progress + 2,
                f"گہری اسکین ہو رہی ہے... {current_progress}%",
                f"ملے ہوئے فائلز: {len(self.scanned_files)}",
                f"باقی وقت: {int((100-current_progress)/2)}s"
            )
            
            if current_progress % 15 == 0:
                self.add_sample_files('deep')
                
        else:
            Clock.unschedule(self.simulate_deep_scan)
            self.progress_widget.update_progress(
                100, 
                "گہری اسکین مکمل!",
                f"کل ملے ہوئے فائلز: {len(self.scanned_files)}"
            )
    
    def simulate_video_scan(self, dt):
        current_progress = self.progress_widget.progress_bar.value
        
        if current_progress < 100:
            self.progress_widget.update_progress(
                current_progress + 4,
                f"ویڈیو اسکین ہو رہی ہے... {current_progress}%",
                f"ملے ہوئے ویڈیوز: {len(self.scanned_files)}"
            )
            
            if current_progress % 25 == 0:
                self.add_sample_files('video')
                
        else:
            Clock.unschedule(self.simulate_video_scan)
            self.progress_widget.update_progress(
                100, 
                "ویڈیو اسکین مکمل!",
                f"کل ملے ہوئے ویڈیوز: {len(self.scanned_files)}"
            )
    
    def add_sample_files(self, scan_type):
        sample_files = []
        
        if scan_type == 'video':
            sample_files = [
                {'name': 'چھٹیوں کی ویڈیو.mp4', 'size': '15.2 MB', 'type': 'video'},
                {'name': 'سالگرہ پارٹی.avi', 'size': '23.7 MB', 'type': 'video'},
                {'name': 'ٹیوٹوریل ریکارڈنگ.mkv', 'size': '45.1 MB', 'type': 'video'}
            ]
        elif scan_type == 'quick':
            sample_files = [
                {'name': 'دستاویز.pdf', 'size': '2.1 MB', 'type': 'document'},
                {'name': 'پروفائل تصویر.jpg', 'size': '1.8 MB', 'type': 'image'},
                {'name': 'گانا.mp3', 'size': '3.4 MB', 'type': 'audio'}
            ]
        else:
            sample_files = [
                {'name': 'پریزنٹیشن.pptx', 'size': '5.6 MB', 'type': 'document'},
                {'name': 'اسکرین شاٹ.png', 'size': '0.9 MB', 'type': 'image'},
                {'name': 'وائس نوٹ.wav', 'size': '2.3 MB', 'type': 'audio'},
                {'name': 'فلم ٹریلر.mp4', 'size': '12.8 MB', 'type': 'video'}
            ]
        
        for file_info in sample_files:
            file_card = FileCard(file_info)
            self.main_screen.add_file_card(file_card)
            self.scanned_files.append(file_info)
    
    def select_all_files(self, instance):
        for child in self.main_screen.files_grid.children:
            if hasattr(child, 'select_btn'):
                child.select_btn.state = 'down'
    
    def recover_selected_files(self, instance):
        selected_count = sum(1 for child in self.main_screen.files_grid.children 
                           if hasattr(child, 'select_btn') and child.select_btn.state == 'down')
        
        if selected_count == 0:
            self.progress_widget.update_progress(0, "براہ کرم فائلز سلیکٹ کریں")
            return
        
        self.progress_widget.update_progress(0, f"{selected_count} فائلز ریکور ہو رہی ہیں...")
        
        Clock.schedule_interval(self.simulate_recovery, 0.1)
    
    def simulate_recovery(self, dt):
        current_progress = self.progress_widget.progress_bar.value
        
        if current_progress < 100:
            self.progress_widget.update_progress(
                current_progress + 8,
                f"فائلز ریکور ہو رہی ہیں... {current_progress}%",
                f"پروگریس: {current_progress}%"
            )
        else:
            Clock.unschedule(self.simulate_recovery)
            self.progress_widget.update_progress(
                100, 
                "ریکوری مکمل ہو گئی!",
                "تمام سلیکٹڈ فائلز ریکور ہو گئیں"
            )
    
    def show_main_screen(self):
        pass

if __name__ == '__main__':
    MobileDataRecoveryApp().run()
