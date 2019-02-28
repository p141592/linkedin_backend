import uuid

from django.db import models
from django.utils import timezone


class Network(models.Model):
    network = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.network)


class Contact(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    invite = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    mutual_contacts = models.IntegerField(default=0)
    picture = models.URLField(null=True)
    position = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pk


class MessageDistribution(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid1, max_length=255)
    send = models.ManyToManyField(Contact, blank=True)
    message = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)

    def contacts_send(self):
        return self.send.count()

    def check_contact(self, contact):
        return bool(isinstance(contact, Contact) and contact in self.send)

    def append_contact(self, contact):
        if self.check_contact(contact):
            self.send.add(contact)
