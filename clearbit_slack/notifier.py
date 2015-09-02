import json
from slacker import Slacker
from clearbit.slack.attachments import Company, Person


class Notifier(object):
    def __init__(self, slack_token, slack_channel, attrs=None):
        self.slack_token = slack_token
        self.slack_channel = slack_channel

        attrs = attrs if attrs else {}
        self.company_dict = attrs.get('company', {})
        self.message = attrs.get('message', '')
        self.person_dict = attrs.get('person', {})
        self.given_name = attrs.get('given_name', {})
        self.family_name = attrs.get('family_name', {})
        self.email = attrs.get('email', {})

    def notify(self):
        attachments = [Person(self.person_dict).as_dict()]

        if self.company_dict:
            attachments.append(Company(self.company_dict).as_dict())

        slack = Slacker(token=self.slack_token)
        slack.chat.post_message(
            self.slack_channel,
            self.message or self.username,
            username=self.username,
            icon_url=self.icon_url,
            attachments=json.dumps(attachments)
        )

    @property
    def icon_url(self):
        return self.person_dict.get('avatar') or ''

    @property
    def username(self):
        name_dict = self.person_dict.get('name', {})

        full_name = name_dict.get('fullName')
        if full_name:
            return full_name

        given_name = name_dict.get('givenName')
        family_name = name_dict.get('familyName')
        if given_name and family_name:
            return given_name + ' ' + family_name

        return 'Unknown'
