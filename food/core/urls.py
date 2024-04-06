from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('game',views.game, name='game'),
    path('game2',views.game2, name='game2'),
    path('game3',views.game3, name='game3'),
]