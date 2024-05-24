from django.urls import path
from . import views

app_name = 'redaksi'

urlpatterns =[
    path('masuk/',views.index, name='index'),
    path('adminpage/',views.admin, name='adminpage'),
    path('staff/', views.staff, name='staff'),
    path('login_view',views.login_view, name='login_view'),
    path('register/',views.register, name='register'),
    path('',views.TampilWeb.as_view(),name='beranda'),
    path('tambah/',views.TambahWeb.as_view(),name='tambah'),
    path('baca/<slug:slug>/',views.DetailWeb.as_view(),name='detail'),
    path('edit/<pk>/',views.UpdateWeb.as_view(),name='ubah'),
    path('delete/<pk>/',views.DeleteWeb.as_view(),name='hapus'),
    path('like_post/',views.like_post, name='like_post'),
    path('view_blogs/',views.view_blogs,name='view_blogs'),
]