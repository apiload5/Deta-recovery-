import os
import fnmatch
from datetime import datetime

class FileScanner:
    def __init__(self):
        self.video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.3gp', '.wmv']
        self.image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        self.audio_extensions = ['.mp3', '.wav', '.aac', '.flac']
        self.document_extensions = ['.pdf', '.doc', '.docx', '.xls', '.txt']
    
    def scan_directory(self, directory_path, scan_type='quick'):
        """
        Directory scan karta hai different scan types ke hisab se
        """
        found_files = []
        
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_info = self.analyze_file(file_path)
                    
                    if file_info and self.filter_file(file_info, scan_type):
                        found_files.append(file_info)
                        
        except Exception as e:
            print(f"Scanning error: {str(e)}")
        
        return found_files
    
    def analyze_file(self, file_path):
        """
        File ki complete information collect karta hai
        """
        try:
            if os.path.exists(file_path):
                stat_info = os.stat(file_path)
                
                return {
                    'name': os.path.basename(file_path),
                    'path': file_path,
                    'size': self.format_size(stat_info.st_size),
                    'size_bytes': stat_info.st_size,
                    'type': self.get_file_type(file_path),
                    'modified': datetime.fromtimestamp(stat_info.st_mtime),
                    'created': datetime.fromtimestamp(stat_info.st_ctime)
                }
        except:
            return None
    
    def get_file_type(self, file_path):
        """
        File type determine karta hai extension ke hisab se
        """
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext in self.video_extensions:
            return 'video'
        elif ext in self.image_extensions:
            return 'image'
        elif ext in self.audio_extensions:
            return 'audio'
        elif ext in self.document_extensions:
            return 'document'
        else:
            return 'other'
    
    def filter_file(self, file_info, scan_type):
        """
        Files ko filter karta hai scan type ke hisab se
        """
        if scan_type == 'video':
            return file_info['type'] == 'video'
        elif scan_type == 'quick':
            return file_info['size_bytes'] > 1024  # 1KB se bari files
        elif scan_type == 'deep':
            return True  # Sab files
        return False
    
    def format_size(self, size_bytes):
        """
        File size ko readable format mein convert karta hai
        """
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names)-1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
