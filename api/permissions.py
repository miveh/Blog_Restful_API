from rest_framework import permissions
from rest_framework.permissions import BasePermission


# برای رست بود این
# یا صاحب پستادیت کنه یا اگه صاحب پست نبود فقط ببینه
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # متد های پست سیف هستن هیچ تغییری نمیشه داد اونا رو دسترسی میدیم
            return True
        return request.user == obj.owner

    # def has_permission(self, request, view):
    #     ip_address = request.META['REMOTE_ADDR']
    #
    # in_blacklist = Blacklist.objects.filter(ip=ip_address).exists()
    # return not in_blacklist
