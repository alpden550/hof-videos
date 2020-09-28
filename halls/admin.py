from django.contrib import admin

from halls.models import Hall, Video


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_editable = ('title',)
    search_fields = ('title', )
    list_filter = ('user', )
    inlines = (VideoInline, )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
