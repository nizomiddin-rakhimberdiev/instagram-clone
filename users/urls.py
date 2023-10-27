from django.urls import path
from .views import CreateUserView, ListUserView, VerifyAPIView

urlpatterns = [
    path('signup', CreateUserView.as_view()),
    path('verify', VerifyAPIView.as_view()),
    path('list', ListUserView.as_view()),
]
