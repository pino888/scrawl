from django.urls import path, include
from . import views


app_name = 'scrawl'


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/<int:pk>/following/', views.following, name='following'),
    path('create_scrawl/', views.create_scrawl, name='create_scrawl'),
    path('scrawl/<int:pk>/comments', views.comments, name='comments'),
    path('quillboard/', views.quillboard, name='quillboard'),
]
