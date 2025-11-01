from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import EventViewSet, RSVPViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'events', views.EventViewSet)
events_router = routers.NestedDefaultRouter(router, r'events', lookup='event')
events_router.register(r'rsvp', RSVPViewSet, basename='event-rsvp')
events_router.register(r'reviews', ReviewViewSet, basename='event-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(events_router.urls)),
]
