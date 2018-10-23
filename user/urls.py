from django.urls import path
from user.views import giris, kayit


urlpatterns = [
    path('giris/', giris, name="user-giris"),
    path('kayit/', kayit, name="user-kayit"),
]