from django.contrib import admin

from membership.models import Members


class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ['timestamp', 'updated']

admin.site.register(Members, MemberAdmin)
