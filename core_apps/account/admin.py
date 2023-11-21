from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm

# from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # ordering = ["email"]
    ordering = ("-created", "-updated")
    add_form = CustomUserCreationForm
    model = User

    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "username",
        "is_staff",
        "is_active",
        "is_verified",
        "created",
        "updated",
    ]

    list_display_links = [
        "pkid",
        "id",
        "email",
        "username",
    ]

    list_filter = ["is_staff", "is_active", "is_verified"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "temp_password",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_verified",
                    "is_superuser",
                    "is_deleted",
                    "is_blocked",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ["email", "username", "first_name", "last_name", "id"]


admin.site.register(User, UserAdmin)
