from django.urls import path
from .views import CreateUserView, ListUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('list/', ListUserView.as_view()),
]