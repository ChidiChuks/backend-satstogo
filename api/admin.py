from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, SatsUser, FcmToken


class CustomUserAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model.
    list_display = ('magic_string', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    search_fields = ('magic_string',)
    readonly_fields = ('last_login', 'created_at')

    # Fieldsets define the layout of the admin pages
    fieldsets = (
        (None, {'fields': ('magic_string', 'key', 'sig')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('magic_string', 'key', 'sig', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )

    ordering = ('magic_string',)
    filter_horizontal = ()

# Register User model
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(SatsUser)
admin.site.register(FcmToken)
