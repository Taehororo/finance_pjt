from django.urls import path, include
from .views import CustomRegisterView

app_name = 'accounts'
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', CustomRegisterView.as_view()),
]
