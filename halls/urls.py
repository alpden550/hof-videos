from django.urls import path

from halls import views

app_name = 'hall'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('halloffame/create/', views.HallCreateView.as_view(), name='hall-create'),
    path('halloffame/<int:pk>', views.HallDetailView.as_view(), name='hall-detail'),
    path('halloffame/<int:pk>/update/', views.HallUpdateView.as_view(), name='hall-update'),
    path('halloffame/<int:pk>/delete/', views.HallDeleteView.as_view(), name='hall-delete'),

    path('halloffame/<int:pk>/add-video/', views.add_video, name='hall-add-video'),
    path('video/search/', views.video_search, name='video_search'),
    path('video/<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video-delete'),
]
