from django.utils.html import format_html
from django.contrib import admin
from .models import User, DiaryEntry, Project, Sketch, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'tech_stack', 'created_at', 'views', 'image_thumb')
    search_fields = ('title', 'tech_stack', 'user__username')
    list_filter = ('created_at', 'tech_stack')
    readonly_fields = ('image_thumb', 'views')
    ordering = ('-created_at',)

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px; border-radius:6px;" />', obj.image.url)
        return format_html('<span style="opacity:0.6;">No image</span>')
    image_thumb.short_description = 'Thumbnail'

admin.site.register(User)
admin.site.register(DiaryEntry)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Sketch)
admin.site.register(Comment)