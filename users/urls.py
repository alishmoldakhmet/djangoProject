from django.urls import path
from .views import UserView,Registration,Authorization,ChangePassword


urlpatterns = [
    path('user/',UserView.as_view()),
    path('registration/',Registration),
    path('authorization/',Authorization),
    path('change/password/',ChangePassword)
]