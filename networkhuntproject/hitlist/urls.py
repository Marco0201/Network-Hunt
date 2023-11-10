from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(HitlistHomeView.as_view()), name='hitlist'),
    path('hitlist/<int:pk>', login_required(HitlistDetailView.as_view()), name='hitlist_detail'),
    path('add_hitlist/', login_required(AddHitlistView.as_view()), name='add_hitlist'),
    path('hitlist/edit/<int:pk>', login_required(UpdateHitlistView.as_view()), name='update_hitlist'),
    path('hitlist/<int:pk>/remove', login_required(DeleteHitlistView.as_view()), name='delete_hitlist'),
    path('hitlist_search/', login_required(HitlistSearchView), name='hitlist_search_results'),
]
