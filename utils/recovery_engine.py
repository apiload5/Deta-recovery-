import os
import shutil
from datetime import datetime

class RecoveryEngine:
    def __init__(self):
        self.supported_formats = {
            'video': ['.mp4', '.avi', '.mkv', '.mov', '.3gp', '.wmv'],
            'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'audio': ['.mp3', '.wav', '.aac', '.flac'],
            'document': ['.pdf', '.doc', '.docx', '.xls', '.txt']
        }
    
    def recover_files(self, files_list, recovery_path):
        results = {
            'successful': [],
            'failed': [],
            'total': len(files_list),
            'start_time': datetime.now(),
            'end_time': None
        }
        
        for index, file_info in enumerate(files_list):
            try:
                progress = (index / len(files_list)) * 100
                
                success, recovered_info = self.recover_single_file(file_info, recovery_path)
                
                if success:
                    results['successful'].append(recovered_info)
                else:
                    results['failed'].append({
                        'file': file_info.get('name', 'unknown'),
                        'error': 'Recovery failed'
                    })
                    
            except Exception as e:
                results['failed'].append({
                    'file': file_info.get('name', 'unknown'),
                    'error': str(e)
                })
        
        results['end_time'] = datetime.now()
        results['duration'] = results['end_time'] - results['start_time']
        
        return results
    
    def recover_single_file(self, file_info, recovery_path):
        try:
            source_path = file_info['path']
            
            if not os.path.exists(source_path):
                return False, None
            
            file_type = file_info.get('type', 'other')
            dest_folder = self.get_destination_folder(file_type)
            dest_dir = os.path.join(recovery_path, dest_folder)
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            original_name = file_info['name']
            new_filename = f"recovered_{timestamp}_{original_name}"
            dest_path = os.path.join(dest_dir, new_filename)
            
            shutil.copy2(source_path, dest_path)
            
            if os.path.exists(dest_path):
                recovered_info = {
                    'original_name': original_name,
                    'recovered_name': new_filename,
                    'source_path': source_path,
                    'recovered_path': dest_path,
                    'file_type': file_type,
                    'size': os.path.getsize(dest_path),
                    'recovery_time': datetime.now()
                }
                return True, recovered_info
            else:
                return False, None
                
        except Exception as e:
            print(f"Single file recovery error: {str(e)}")
            return False, None
    
    def get_destination_folder(self, file_type):
        folder_map = {
            'video': 'Videos',
            'image': 'Images',
            'audio': 'Audio',
            'document': 'Documents',
            'other': 'Others'
        }
        return folder_map.get(file_type, 'Others')
    
    def validate_recovery(self, recovered_files):
        validation_results = []
        
        for file_info in recovered_files:
            try:
                file_path = file_info['recovered_path']
                
                is_valid = True
                issues = []
                
                if not os.path.exists(file_path):
                    is_valid = False
                    issues.append("File not found")
                
                file_size = os.path.getsize(file_path)
                if file_size == 0:
                    is_valid = False
                    issues.append("Zero file size")
                
                try:
                    with open(file_path, 'rb') as f:
                        f.read(1)
                except:
                    is_valid = False
                    issues.append("File not readable")
                
                validation_results.append({
                    'file': file_info['recovered_name'],
                    'valid': is_valid,
                    'issues': issues,
                    'size': file_size
                })
                
            except Exception as e:
                validation_results.append({
                    'file': file_info.get('recovered_name', 'unknown'),
                    'valid': False,
                    'issues': [str(e)],
                    'size': 0
                })
        
        return validation_results
    
    def get_recovery_stats(self, results):
        total_files = results['total']
        successful = len(results['successful'])
        failed = len(results['failed'])
        
        stats = {
            'total_files': total_files,
            'successful_recoveries': successful,
            'failed_recoveries': failed,
            'success_rate': (successful / total_files * 100) if total_files > 0 else 0,
            'total_size': sum(f['size'] for f in results['successful']),
            'duration': results['duration']
        }
        
        return stats
