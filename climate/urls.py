from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('member/', views.member, name='member'),
    path('diagram/<int:diagram_id>/', views.diagram_detail, name='diagram_detail'),
    path('diagram/', views.diagram, name='diagram'),
    path('tags/', views.tags, name='tags'),
    path('data_source/', views.data_source, name='data_source'),
    path('folder/', views.folder, name='folder'),
    path('tag_diagram/', views.tag_diagram, name='tag_diagram'),
    # path('comment/', views.comment, name='comment'),
    path('summary/', views.summary, name='summary'),
    path('diagram/<int:diagram_id>/bind/', views.bind, name='bind'),
    path('diagram/<int:diagram_id>/comment/', views.comment, name='comment'),
    path('test/<int:diagram_id>/', views.test, name='test'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.regist, name='regist'),
]