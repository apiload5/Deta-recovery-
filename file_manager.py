import os
import shutil
from datetime import datetime

class FileManager:
    def __init__(self):
        self.recovery_folder = "Recovered_Files"
        
    def create_recovery_directory(self, base_path):
        try:
            recovery_path = os.path.join(base_path, self.recovery_folder)
            if not os.path.exists(recovery_path):
                os.makedirs(recovery_path)
            
            subdirs = ['Videos', 'Images', 'Audio', 'Documents', 'Others']
            for subdir in subdirs:
                subdir_path = os.path.join(recovery_path, subdir)
                if not os.path.exists(subdir_path):
                    os.makedirs(subdir_path)
            
            return recovery_path
            
        except Exception as e:
            print(f"Recovery directory creation error: {str(e)}")
            return None
    
    def copy_file_safely(self, source_path, destination_path):
        try:
            if not os.path.exists(source_path):
                return False, "Source file not found"
            
            dest_dir = os.path.dirname(destination_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            shutil.copy2(source_path, destination_path)
            
            if os.path.exists(destination_path):
                return True, "File copied successfully"
            else:
                return False, "Copy verification failed"
                
        except Exception as e:
            return False, f"Copy error: {str(e)}"
    
    def organize_recovered_files(self, recovery_path, files_list):
        results = {
            'successful': [],
            'failed': [],
            'total': len(files_list)
        }
        
        for file_info in files_list:
            try:
                file_type = file_info.get('type', 'other')
                dest_folder = self.get_destination_folder(file_type)
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                original_name = file_info['name']
                new_filename = f"recovered_{timestamp}_{original_name}"
                dest_path = os.path.join(recovery_path, dest_folder, new_filename)
                
                success, message = self.copy_file_safely(file_info['path'], dest_path)
                
                if success:
                    results['successful'].append({
                        'original': file_info['name'],
                        'recovered': new_filename,
                        'path': dest_path
                    })
                else:
                    results['failed'].append({
                        'file': file_info['name'],
                        'error': message
                    })
                    
            except Exception as e:
                results['failed'].append({
                    'file': file_info.get('name', 'unknown'),
                    'error': str(e)
                })
        
        return results
    
    def get_destination_folder(self, file_type):
        folder_map = {
            'video': 'Videos',
            'image': 'Images',
            'audio': 'Audio',
            'document': 'Documents'
        }
        return folder_map.get(file_type, 'Others')
    
    def get_file_info(self, file_path):
        try:
            stat_info = os.stat(file_path)
            
            return {
                'name': os.path.basename(file_path),
                'path': file_path,
                'size': stat_info.st_size,
                'size_formatted': self.format_size(stat_info.st_size),
                'created': datetime.fromtimestamp(stat_info.st_ctime),
                'modified': datetime.fromtimestamp(stat_info.st_mtime),
                'extension': os.path.splitext(file_path)[1].lower()
            }
        except Exception as e:
            print(f"File info error: {str(e)}")
            return None
    
    def format_size(self, size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
