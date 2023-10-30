from django.urls import path
from .views import (CreateUserView,
                    ListUserView,
                    VerifyAPIView,
                    GetNewVerification,
                    ChangeUserInformationView,
                    )

urlpatterns = [
    path('signup', CreateUserView.as_view()),
    path('verify', VerifyAPIView.as_view()),
    path('new-verify', GetNewVerification.as_view()),
    path('change-user', ChangeUserInformationView.as_view()),
    path('list', ListUserView.as_view()),
]
