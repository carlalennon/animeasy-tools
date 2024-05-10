
from django.test import TestCase
from .models import Ticket, TicketReply
from profiles.models import UserProfile
from django.contrib.auth.models import User

class TicketModelTest(TestCase):
    def setUp(self):
        self.ticket = Ticket.objects.create(
            email='test@test.com',
            title='Test Ticket',
            content='This is a test ticket',
            status='pending'
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.email, 'test@test.com')
        self.assertEqual(self.ticket.title, 'Test Ticket')
        self.assertEqual(self.ticket.content, 'This is a test ticket')
        self.assertEqual(self.ticket.status, 'pending')

class TicketReplyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        #self.user_profile = UserProfile.objects.create(user=self.user)
        self.ticket = Ticket.objects.create(
            email='test@test.com',
            title='Test Ticket',
            content='This is a test ticket',
            status='pending'
        )
        self.user_profile = UserProfile.objects.create(user=None)  # replace with actual user
        self.ticket_reply = TicketReply.objects.create(
            ticket=self.ticket,
            admin=self.user_profile,
            reply='This is a test reply'
        )

    def test_ticket_reply_creation(self):
        self.assertEqual(self.ticket_reply.ticket, self.ticket)
        self.assertEqual(self.ticket_reply.admin, self.user_profile)
        self.assertEqual(self.ticket_reply.reply, 'This is a test reply')