from django.conf.urls import url
from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('edit/', views.edit_profile, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout')
]
