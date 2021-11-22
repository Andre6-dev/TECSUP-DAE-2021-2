from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.serie_list),
    url('<int:pk>', views.serie_detail),
]
