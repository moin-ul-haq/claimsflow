from django.urls import path,include
from organization.urls import router
from .views import ChangePasswordView

urlpatterns = [
    path('',include(router.urls)),
    path('changepassword/',ChangePasswordView.as_view(),name='change_password')
]
