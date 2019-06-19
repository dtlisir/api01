# -*- coding: utf-8 -*-
# author: dtlisir
# date: 2019/6/19

from django.urls import path
# from polls import views
from polls import apiviews

urlpatterns = [
    path('polls/', apiviews.PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', apiviews.PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', apiviews.ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', apiviews.VoteCreate.as_view(), name='create_vote'),
]