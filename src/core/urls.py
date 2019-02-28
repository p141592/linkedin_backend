from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from .views import NetworkVS, ContactVS, MessageDistributionVS

router = SimpleRouter()
router.register('contact', ContactVS, 'Contact')
router.register('network', NetworkVS, 'Network')
router.register('message', MessageDistributionVS, 'MessageDistribution')

urlpatterns = [
    url(r'^', include(router.urls))
]
