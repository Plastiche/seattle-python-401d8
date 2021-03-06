from django.urls import path


urlpatterns = [
    path('library/', library_view, name='library'),
    path('album/', album_view, name='album'),
    path('photo/', photo_view, name='photo'),
    path('album/<int:id>', album_detail_view, name='album_detail'),
    path('photo/<int:id>', photo_detail_view, name='photo_detail'),
]
