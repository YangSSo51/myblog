from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('test/',views.test,name="test"),
    path('',views.read,name="read"),
    path('notice/<int:notice_id>/',views.detail,name="detail"),
    url(r'^$', views.detail, name='detail_comment'),
    url(r'^(?P<notice_id>\d+)/comment/create/$', views.comment_create, name='comment_create'),
    path('newnotice/',views.create,name="newnotice"),
    path('update/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="delete"),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^search',views.SearchFormView.as_view(),name='search'),   #search
]