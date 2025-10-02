from android.permissions import request_permissions, Permission, check_permission

class AndroidPermissions:
    def __init__(self):
        self.required_permissions = [
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
        ]
    
    def check_and_request_permissions(self):
        """
        Permissions check aur request karta hai
        """
        missing_permissions = []
        
        for permission in self.required_permissions:
            if not check_permission(permission):
                missing_permissions.append(permission)
        
        if missing_permissions:
            request_permissions(missing_permissions)
            return False
        return True
    
    def has_all_permissions(self):
        """
        Check karta hai ke sab permissions mil gaye hain
        """
        return all(check_permission(perm) for perm in self.required_permissions)
