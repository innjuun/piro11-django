from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size',
                    'status', 'created_at', 'updated_at']
    actions = ['make_published']

    def content_size(self, post):
        return mark_safe(("<strong>{}</strong>글자".format(len(post.content))))

    def make_published(self, request, queryset):
        updated_count =queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 published상태로 변경'
    content_size.short_description = "글자수"
    # content_size.allow_tags = True
# admin.site.register(Post, PostAdmin)
