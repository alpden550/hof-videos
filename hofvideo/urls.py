"""hofvideo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from halls import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HallMainPage.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('login/', LoginView.as_view(), name='login',),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),

    path('halloffame/create/', views.HallCreateView.as_view(), name='hall-create'),
    path('halloffame/<int:pk>', views.HallDetailView.as_view(), name='hall-detail'),
    path('halloffame/<int:pk>/update/', views.HallUpdateView.as_view(), name='hall-update'),
    path('halloffame/<int:pk>/delete/', views.HallDeleteView.as_view(), name='hall-delete'),

    path('halloffame/<int:pk>/add-video/', views.add_video, name='hall-add-video'),
    path('video/search/', views.video_search, name='video_search'),
    path('video/<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
