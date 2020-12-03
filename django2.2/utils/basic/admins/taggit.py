
from django.contrib import admin


class TaggitAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        return self.list_display + ('tag_list',)

    def get_list_filter(self, request):
        return self.list_filter + ('tags',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
