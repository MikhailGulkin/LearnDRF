from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionsMixin:
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]


class UserQuerySetMixin:
    user_field = 'user'
    allow_staff_view = False

    def get_queryset(self):
        user = self.request.user
        lookup_data = {self.user_field: user}
        qs = super().get_queryset()
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)
