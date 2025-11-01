from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from events.models import Event, RSVP

class PrivateEventAccessTest(APITestCase):
    def setUp(self):
        # Create users
        self.organizer = User.objects.create_user(username='organizer', password='pass123')
        self.guest = User.objects.create_user(username='guest', password='pass123')
        self.stranger = User.objects.create_user(username='stranger', password='pass123')

        # Create private event
        self.event = Event.objects.create(
            title="Private Meetup",
            description="Private event for testing",
            organizer=self.organizer,
            location="Test Location",
            start_time="2025-11-01T10:00:00Z",
            end_time="2025-11-01T12:00:00Z",
            is_public=False
        )

        # Guest RSVPs (invited)
        RSVP.objects.create(event=self.event, user=self.guest, status='Going')

    def test_organizer_can_access_private_event(self):
        self.client.login(username='organizer', password='pass123')
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invited_user_can_access_private_event(self):
        self.client.login(username='guest', password='pass123')
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stranger_cannot_access_private_event(self):
        self.client.login(username='stranger', password='pass123')
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
