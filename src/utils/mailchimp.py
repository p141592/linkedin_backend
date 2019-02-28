import hashlib
import os
import requests
from requests.auth import HTTPBasicAuth

e = os.environ.get


class MailChimp:
    def __init__(self, list_id=e('MAILCHIMP_LIST_ID')):
        self.LIST_ID = list_id
        self.DC = e('MAILCHIMP_DC')
        self.tag = e('MAILCHIMP_TAG', 'directly')
        self.auth = HTTPBasicAuth(e('MAILCHIMP_USERNAME'), e('MAILCHIMP_APP_KEY'))

    def get_md5(self, email):
        return hashlib.md5(email.encode('utf-8')).hexdigest()

    def check_email(self, email):
        r = requests.get(
            f'https://{self.DC}.api.mailchimp.com/3.0/lists/{self.LIST_ID}/members/{self.get_md5(email)}',
            auth=self.auth
        )
        return r.status_code == 200

    def append(self, email, data):
        if not self.check_email(email):
            requests.post(
                f'https://{self.DC}.api.mailchimp.com/3.0/lists/{self.LIST_ID}/members/',
                json=data,
                auth=self.auth
            )

    def append_user(self, instance):
        if instance.email:
            self.append(
                instance.email,
                {
                    "email_address": instance.email,
                    'location': {
                        'country_code': instance.locale or ''
                    },
                    'tags': [self.tag],
                    "status": "subscribed",
                    "merge_fields": {
                        "FNAME": instance.first_name or '',
                        "LNAME": instance.last_name or ''
                    }
                }
            )
