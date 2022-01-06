from django.urls import path
from .views import PensionUserRegister, UserActivation, LoginView, ChangePasswordView

urlpatterns = [
    path('api/register/', PensionUserRegister.as_view()),
    path('api/activation/', UserActivation.as_view(), name='user-activation'),
    path('api/user_login/', LoginView.as_view(), name='user-login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

]
