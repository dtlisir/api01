# -*- coding: utf-8 -*-
# author: dtlisir
# date: 2019/6/19

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from polls.serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from polls.models import Poll, Choice, Vote

# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:10]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)
#
# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)

# class PollList(generics.ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
#
#
# class PollDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    # queryset = Choice.objects.all()
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset
    serializer_class = ChoiceSerializer


class VoteCreate(APIView):
    # queryset = Vote.objects.all()
    # serializer_class = VoteSerializer
    def post(self, request, pk, choice_pk):
        vote_by = request.data.get('vote_by')
        data = {'choice': choice_pk, 'poll': pk, 'vote_by': vote_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
