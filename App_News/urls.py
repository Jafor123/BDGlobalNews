from django.urls import path
app_name = 'App_News'
from App_News import views
urlpatterns = [
    path('',views.index,name='index'),
    path('details/<str:title>/<int:id>',views.viewnews,name='viewnews'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('like/', views.newslike, name="news_like"),
    path('activate/<str:email>/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('view-author/<str:user>',views.ViewAuthorPost,name='view_author_post'),
    path('category/<str:cat>/<int:id>',views.ViewCategory,name='viewcategory'),
    path('subcategory/<int:cat_id>/<int:sub_id>/',views.ViewSubcategory,name='viewsubcategory'),
    path('search',views.Newssearch,name='news_search'),
]
