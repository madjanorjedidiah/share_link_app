from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('docs', views.docs, name='docs'),
    path('try_mongo_save', views.try_mongo_save, name='try_mongo_save'),
    path('try_mongo_get', views.try_mongo_get, name='try_mongo_get'),
    path('sendlink', views.sendlink, name='sendlink'),
    # path('', views.index, name='home'),

]