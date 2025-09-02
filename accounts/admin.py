from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "username", "email", "first_name", "last_name", "user_type", "city", "state")
    list_filter = ("user_type", "city", "state")
    search_fields = ("username", "email", "first_name", "last_name", "city", "state")
    ordering = ("id",)

    # Fields shown in the user add/edit form
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "profile_picture")}),
        ("Address", {"fields": ("address_line1", "city", "state", "pincode")}),
        ("Role", {"fields": ("user_type",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields when creating a new user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "user_type", "profile_picture", "address_line1", "city", "state", "pincode"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
