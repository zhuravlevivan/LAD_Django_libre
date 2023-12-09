from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),  # 'users:login'
    # path('login/', LoginView.as_view(
    #     template_name='users/login.html',
    #     redirect_authenticated_user=True,
    # ),
    #      name='login'),
    # path('logout/', views.logout_user, name='logout'),  # 'users:logout'
    path('logout/', LogoutView.as_view(), name='logout'),  # 'users:logout'
    path('register/', views.register, name='register'),

]
