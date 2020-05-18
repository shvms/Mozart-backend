from django.apps import AppConfig, apps

class UserManagementConfig(AppConfig):
    name = 'user_management'
    
    def ready(self):
        from actstream import registry
        registry.register(apps.get_model('auth.user'))  # registering model for activity lookup
