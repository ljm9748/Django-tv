from django.urls import path
from . import views

urlpatterns = [
    path('var_route/<int:value>/', views.var_route),   # <>있어서 변수됨 url에서 string자리에 1234 있으면 string=1234로 처리됨
    path('lotto/<when>/', views.lotto),
    path('ping/',views.ping, name='ping'),       # 사용자 입력받는 곳
    path('pong/', views.pong, name='pong')       # 처리결과 보여주는 곳
]
#'https://www.themoviedb.movie/775996
