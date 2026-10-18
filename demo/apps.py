from django.apps import AppConfig


class DemoAppconfig(AppConfig):
    name = "demo"

    def ready(self):
        from django.contrib import admin
        from juntagrico.entity.mailing import MailTemplate

        admin.site.unregister(MailTemplate)
