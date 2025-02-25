from django.contrib.auth import get_user_model
from helpdesk.models import FollowUp, FollowUpAttachment, Ticket
from helpdesk.serializers import FollowUpAttachmentSerializer, FollowUpSerializer, TicketSerializer, UserSerializer, PublicTicketListingSerializer
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination


class ConservativePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'


class UserTicketViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A list of all the tickets submitted by the current user

    The view is paginated by default
    """
    serializer_class = PublicTicketListingSerializer
    pagination_class = ConservativePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(submitter_email=self.request.user.email).order_by('-created')


class TicketViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions to handle Ticket
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    pagination_class = ConservativePagination
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        tickets = Ticket.objects.all()
        for ticket in tickets:
            ticket.set_custom_field_values()
        return tickets

    def get_object(self):
        ticket = super().get_object()
        ticket.set_custom_field_values()
        return ticket


class FollowUpViewSet(viewsets.ModelViewSet):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer
    pagination_class = ConservativePagination
    permission_classes = [IsAdminUser]


class FollowUpAttachmentViewSet(viewsets.ModelViewSet):
    queryset = FollowUpAttachment.objects.all()
    serializer_class = FollowUpAttachmentSerializer
    pagination_class = ConservativePagination
    permission_classes = [IsAdminUser]


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
