from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boardgames/', views.boardgames_index, name='index'),
    path('boardgames/<int:boardgame_id>/', views.boardgames_detail, name='detail'),
    path('boardgames/create/', views.BoardgameCreate.as_view(), name='boardgames_create'),
    path('boardgames/<int:boardgame_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
    path('boardgames/<int:pk>/update/', views.BoardgameUpdate.as_view(), name='boardgames_update'),
    path('boardgames/<int:pk>/delete/', views.BoardgameDelete.as_view(), name='boardgames_delete'),

    path('boardgames/<int:boardgame_id>/add_review/', views.add_review, name='add_review'),
]