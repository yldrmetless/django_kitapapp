from django.urls import path
from kitaplar.api import views as api_views

urlpatterns = [
    path('kitaplar/', api_views.KitapListCreateAPIView.as_view(), name="kitap-list-create"),
    path('kitaplar/<int:pk>/', api_views.KitapDetailAPIView.as_view(), name="kitap-detail"),
]
