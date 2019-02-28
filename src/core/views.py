import datetime
import os

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import Network, Contact, MessageDistribution
from .serializers import NetworkS, ContactS, MessageDistributionS


class NetworkVS(CreateModelMixin, GenericViewSet):
    serializer_class = NetworkS
    queryset = Network.objects.all()


class ContactVS(GenericViewSet):
    serializer_class = ContactS
    queryset = Contact.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            name=serializer.validated_data['name'].strip(),
            position=serializer.validated_data['position'].strip(),
            id=serializer.validated_data['id'].split('/')[-2]
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False)
    def check_progress(self, *args, **kwargs):
        return Response(str(Contact.objects.filter(date__gte=datetime.timedelta(hours=4)).count()), status=status.HTTP_200_OK)


class MessageDistributionVS(GenericViewSet):
    serializer_class = MessageDistributionS
    queryset = MessageDistribution.objects.all()
    model = MessageDistribution

    @action(methods=['GET'], detail=True)
    def check_contact(self, request, pk, contact_id):
        _object = self.model.objects.get(pk=pk)
        _contact = Contact.objects.filter(pk=contact_id)
        return Response(
            status=status.HTTP_202_ACCEPTED if _contact.exists() and _object.check_contact(_contact.first()) else status.HTTP_406_NOT_ACCEPTABLE
        )

    @action(methods=['POST'], detail=True)
    def add_contact(self, request, pk, contact_id):
        _object = self.model.objects.get(pk=pk)
        _contact_id = request.data.get('contact_id')
        _contact = Contact.objects.filter(pk=contact_id)
        if not _contact.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        _object.append_contact(_contact.first())
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def get_message(self, request, pk):
        _object = self.model.objects.get(pk=pk)
        return Response(_object.message, status.HTTP_200_OK)
