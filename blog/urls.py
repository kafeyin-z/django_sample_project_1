from django.urls import path
from blog.views import ekle, sil, guncelle, listele, detay

urlpatterns = [
    path('ekle/', ekle, name='blog-ekle'),
    path('listele/', listele, name='blog-listele'),
    path('detay/<slug:slug>', detay, name='blog-detay'),
    path('sil/<slug:slug>', sil),
    path('guncelle/<slug:slug>', guncelle, name='blog-guncelle'),
]
