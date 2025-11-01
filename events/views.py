from rest_framework import viewsets, permissions,filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, RSVP, Review
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer
from .permissions import IsOrganizerOrReadOnly,IsInvitedOrPublic
from django_filters.rest_framework import DjangoFilterBackend
from .serializers_rsvp import RSVPSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from rest_framework import serializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOrganizerOrReadOnly,IsInvitedOrPublic]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location', 'organizer__username']
    ordering_fields = ['start_time', 'created_at']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RSVP.objects.filter(event_id=self.kwargs['event_pk'])

    def perform_create(self, serializer):
        event = Event.objects.get(pk=self.kwargs['event_pk'])
        serializer.save(user=self.request.user, event=event)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(event_id=self.kwargs['event_pk'])

    def perform_create(self, serializer):
        event = Event.objects.get(pk=self.kwargs['event_pk'])
        try:
            serializer.save(user=self.request.user, event=event)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "You have already reviewed this event."}
            )