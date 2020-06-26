from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'formats', views.FormatViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('member/', views.member, name='member'),
    path('diagram/<int:diagram_id>/', views.diagram_detail, name='diagram_detail'),
    path('diagram/', views.diagram, name='diagram'),

    path('react/', views.react, name='react'),
    path('tags/', views.tags, name='tags'),
    path('data_source/', views.data_source, name='data_source'),
    path('folder/', views.folder, name='folder'),
    path('tag_diagram/', views.tag_diagram, name='tag_diagram'),
    # path('comment/', views.comment, name='comment'),
    path('summary/', views.summary, name='summary'),
    path('diagram/<int:diagram_id>/bind/', views.bind, name='bind'),
    path('diagram/<int:diagram_id>/comment/', views.comment, name='comment'),
    path('test/<int:diagram_id>/', views.test, name='test'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    url('', include(router.urls)),
]