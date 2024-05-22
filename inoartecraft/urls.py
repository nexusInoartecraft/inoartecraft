from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path ('', views.index, name='index'),
    # ex: /polls/5/
    path("<int:id>/", views.detail ,name='detail'),
    # ex: / polls/5/results/
    #path("<int:inorte_id>/", views.results, name='results'),
    # ex: /polls/5/vote/
    #path ("<int:inoarte_id>/vote/", views.vote, name="vote"),
]
