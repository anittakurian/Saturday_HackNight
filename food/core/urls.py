from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('game',views.game, name='game'),
    path('game2',views.game2, name='game2'),
    path('game3',views.game3, name='game3'),
    path('game4',views.game4, name='game4'),
    path('game5',views.game5, name='game5'),
    path('game6',views.game6, name='game6'),
    path('game6m',views.game6m, name='game6m'),
    path('game7',views.game7, name='game7'),
]