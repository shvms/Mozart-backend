from django.apps import AppConfig

class PlaylistConfig(AppConfig):
    name = 'playlist'

    def ready(self):
        import playlist.signals
        from actstream import registry
        
        registry.register(self.get_model('Song'))   # registering model for activity lookup
