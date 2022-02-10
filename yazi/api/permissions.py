from email import message

from rest_framework.permissions import BasePermission


class SahibiMi(BasePermission):
    def has_permission(self, request, view):  # ilk ve her zaman çalısır
        return (
            request.user and request.user.is_authenticated
        )  # giris yapmamıs kullanıcının sayfayı görmesine engel oluyor

    message = 'Bu objenin sahibi siz olmalisiniz.'

    def has_object_permission(self, request, view, obj):  # sadece kendi görev zamanında çalısır
        return (obj.user == request.user) or request.user.is_superuser


# obj.user ile obj'nin user'ının kullanıcısı ile karşılaştırılıyor
