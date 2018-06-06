from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

app_name = 'product'
urlpatterns = [
    #url(r'^$', views.index(), name='index'),
    url(r'^$', views.ProductList.as_view(), name='index'),
    url(r'^login$', views.auth_login, name='login'),
    url(r'^logout$', auth_view.logout, {'next_page': '/'}, name='logout'),
    #url(r'^product/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    url(r'^product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name='detail'),
    url(r'^product/new$', views.create, name='create'),
]