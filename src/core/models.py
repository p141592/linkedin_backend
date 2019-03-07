import uuid

from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    """Компания пользователя"""
    id = models.CharField(max_length=255, default=uuid.uuid1, primary_key=True)
    user = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']


class Filter(models.Model):
    """Фильтры аудитории"""
    user = models.CharField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class Contact(models.Model):
    id = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    entityUrn = models.CharField(max_length=255)
    email = models.EmailField()


class Posts(models.Model):
    """Посты пользователей"""


class Skills(models.Model):
    """Скилы пользователей"""


class University(models.Model):
    """Университет"""


class Recommendation(models.Model):
    """Рекомендации"""


class Relationship(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    owner = models.ForeignKey(Campaign, on_delete=models.SET_NULL)
    user = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact)
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
