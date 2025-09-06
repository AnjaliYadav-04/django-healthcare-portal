from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, BlogPost

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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_draft', 'created_at')
    list_filter = ('category', 'is_draft', 'created_at')
    search_fields = ('title', 'summary', 'content')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_draft',)
    
   
    fieldsets = (
        (None, {"fields": ("title", "author", "category")}),
        ("Content", {"fields": ("image", "summary", "content")}),
        ("Status", {"fields": ("is_draft",)}),
        ("Dates", {"fields": ("created_at", "updated_at")}),
    )
    
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
