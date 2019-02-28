from rest_framework import serializers

from .models import Contact, Network, MessageDistribution


class ContactS(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = (
            'date',
        )


class NetworkS(serializers.ModelSerializer):
    class Meta:
        model = Network
        exclude = (
            'date',
        )


class MessageDistributionS(serializers.ModelSerializer):
    class Meta:
        model = MessageDistribution
        fields = '__all__'
