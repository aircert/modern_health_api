from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ProgramSerializer, WeekSerializer, PageSerializer
from .models import Program, Week, Page

class CreateProgramView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (
        permissions.IsAuthenticated, 
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new Program."""
        serializer.save(owner=self.request.user)

class DetailsProgramView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

class CreateWeekView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Week.objects.all()
    serializer_class = WeekSerializer
    permission_classes = (
        permissions.IsAuthenticated, 
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new Week."""
        serializer.save(owner=self.request.user)

class DetailsWeekView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

class CreatePageView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (
        permissions.IsAuthenticated, 
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new Program."""
        serializer.save(owner=self.request.user)

class DetailsPageView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)