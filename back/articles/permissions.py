from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        if request.method in SAFE_METHODS:
            return True
        # 요청자(request.user)가 객체(Article)의 author와 동일한지 확인
        return obj.author == request.user