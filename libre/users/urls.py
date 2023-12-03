from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.login_user, name='login'),  # 'users:login'
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True,
    ),
         name='login'),
    path('logout/', views.logout_user, name='logout'),  # 'users:logout'

]
