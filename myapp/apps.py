from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    def ready(self):
            import myapp.signals                        # register handlers
            from myapp.backup import start_daily_scheduler
            start_daily_scheduler(hour=2, minute=0)
        
        
