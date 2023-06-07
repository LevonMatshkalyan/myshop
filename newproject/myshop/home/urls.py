from django.contrib import admin
from django.urls import path , include
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard/',include('dashboard.urls')),
    path('items/',include('item.urls')),
    path('', homepage , name='home_homepage'),
    path('contact/', contact , name='home_contact'),
    path('signup/', signup, name='home_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='home_login'),
    # path('logout/', logout , name = 'home_logoutuser'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='home_logoutuser'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)