from django.contrib import admin

from .models import Network, Contact, MessageDistribution


@admin.register(Network)
class NetworkA(admin.ModelAdmin):
    list_display = ('network', 'date',)
    list_filter = ('date', )
    readonly_fields = ('date', )


@admin.register(Contact)
class ContactA(admin.ModelAdmin):
    list_display = ('pk', 'name', 'position', 'mutual_contacts', 'date', )
    search_fields = ('pk', 'name', 'position', )
    list_filter = ('invite', 'date', )
    readonly_fields = ('date', 'invite', )


@admin.register(MessageDistribution)
class MessageDistributionA(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'contacts_send', )
