from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    #path('index/',views.index,name='index')
    #path('about/',views.about,name='about'),
    #path('response/',views.response,name='response')
]
