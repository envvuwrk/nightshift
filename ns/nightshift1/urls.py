from django.urls import path
from . import views

app_name='nightshift1'

urlpatterns = [
    path('',views.index,name='index'),
    path('project/',views.project,name='project'),
    path('work/',views.work,name='work'),
    path('about/',views.about,name='about'),

]