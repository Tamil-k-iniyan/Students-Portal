from django.urls import path
from .views import upload_file
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('logout/', LogoutView.as_view(), name='logout'),
]