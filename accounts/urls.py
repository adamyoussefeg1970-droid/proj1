from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, HomePage

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', HomePage.as_view(), name='home'),
]