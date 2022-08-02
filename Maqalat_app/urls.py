from django.urls import path
from . import views
app_name='Maqalat'
urlpatterns=[
    path('detail/<slug:slug>',views.post_detail,name='detail'),
    path('list',views.post_list,name='Article List'),
    path('category/<int:pk>',views.category_list,name='category_list'),
    path('search/',views.search,name='article_search'),
    path('contact',views.Contact_us,name='contact_us'),


]