from django.contrib import admin

from apps.users.models import Saved, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("is_deleted",)


admin.site.register(Saved)
