from django.urls import path
from blog.views import ekle, sil, guncelle, listele, detay

urlpatterns = [
    path('ekle/', ekle, name='blog-ekle'),
    path('listele/', listele, name='blog-listele'),
    path('detay/<int:pk>', detay, name='blog-detay'),
    path('sil/<int:pk>', sil),
    path('guncelle/<int:pk>', guncelle, name='blog-guncelle'),
]
