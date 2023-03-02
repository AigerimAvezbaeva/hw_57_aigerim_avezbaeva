from django.contrib import admin
from tracker_app.models.issues import Issue
from tracker_app.models.issues import Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'created_at')
    list_filter = ('types', 'status', 'id')
    search_fields = ('status', 'types', 'created_at')
    list_editable = ('summary', 'status')


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Type, TypeAdmin)
