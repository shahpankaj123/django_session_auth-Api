from django.urls import path
from .views import RegistrationView,ActivateUser,LoginView,LogoutVeiw,UserdetailView,ChangePasswordView,UserdeleteView,ResetpasswordView,ConformResetPasswordView

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'),
    path('activate/<id>/<token>/',ActivateUser.as_view(),name='activate'),
    path('Login/',LoginView.as_view(),name='login'),
    path('Logout/',LogoutVeiw.as_view(),name='logout'),
    path('user/',UserdetailView.as_view(),name='user'),
    path('changepassword/',ChangePasswordView.as_view()),
    path('userdelete/',UserdeleteView.as_view()),
    path('resetpassword/',ResetpasswordView.as_view()),
    path('confirmreset/<id>/<token>/',ConformResetPasswordView.as_view()),
]