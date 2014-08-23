from django.contrib import admin

from calc.models import CalcResult


class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CalcResultAdmin(MyAdmin):
    list_display = ('result', 'message', 'time',)
    search_fields = ('result', 'message', 'time',)

admin.site.register(CalcResult, CalcResultAdmin)
