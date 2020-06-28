from django.contrib import admin

from halls.models import Hall, Video


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
