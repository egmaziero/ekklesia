from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_saved$', views.form_saved, name='form_saved'),
]
