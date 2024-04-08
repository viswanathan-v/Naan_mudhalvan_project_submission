from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name="home"),
    path('',views.register,name='reg'),
    path('Category_select',views.Category_select,name='Category_select'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('Trends',views.Trends,name='Trends'),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('fav',views.fav_page,name="fav"),
    path('watch_later',views.LL_page,name="watch_later"),
    path('LLviewpage',views.LLviewpage,name="LLviewpage"),
    path('search', views.search, name='search'),
    path('Trends/<str:sname>',views.Trend_views,name='Trends'),
    path('ll/<str:name>',views.llviews,name='ll'),
    path('Category_select/<str:name>',views.Category_selectviews,name='Category_select'),
    path('Category_select/<str:cname>/<str:sname>',views.song_details,name='Category_select')
    ]