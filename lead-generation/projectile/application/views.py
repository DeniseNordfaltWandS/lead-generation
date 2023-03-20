from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Position, Skill, Application
from .serializers import (PositionSerializer, SkillSerializer, ApplicationSerializer, ApplicationStatusReadUpdateSerializer,
ApplicationStatusUnreadUpdateSerializer, ApplicationStatusInterview1UpdateSerializer, ApplicationStatusInterview2UpdateSerializer,
ApplicationStatusInterview3UpdateSerializer, ApplicationStatusArchivedUpdateSerializer, ApplicationStatusRejectedUpdateSerializer,
ApplicationStatusAcceptedUpdateSerializer)

class ApplicationCreateView(CreateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationSerializer

    def get_serializer_context(self):
        return super().get_serializer_context()

class ApplicationListView(ListAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.all()

class ApplicationDetailRetrieveView(RetrieveAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusUnreadUpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusUnreadUpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusReadUpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusReadUpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusInterview1UpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusInterview1UpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusInterview2UpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusInterview2UpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusInterview3UpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusInterview3UpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusAcceptedUpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusAcceptedUpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusRejectedUpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusRejectedUpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class ApplicationStatusArchivedUpdateView(UpdateAPIView):
    queryset = Application.objects.none()
    serializer_class = ApplicationStatusArchivedUpdateSerializer
    lookup_field = 'application_id'

    def get_object(self):
        return get_object_or_404(Application, id=self.kwargs.get('application_id'))

class PositionListView(ListAPIView):
    queryset = Position.objects.none()
    serializer_class = PositionSerializer

    def get_queryset(self):
        return Position.objects.all()

class SkillListView(ListAPIView):
    queryset = Skill.objects.none()
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.all()
