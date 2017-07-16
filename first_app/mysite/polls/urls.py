from django.conf.urls import url
from . import views

#-------- . means current folder

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

    #We are creating a string defined by ?P question_id and from only 0-9
    #127.0.0.0.1:8000/polls/1

    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    #127.0.0.0.1:8000/polls/1/results

    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    #127.0.0.0.1:8000/polls/1/vote

]
