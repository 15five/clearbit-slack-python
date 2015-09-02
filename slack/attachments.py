from clearbit.slack.helpers import angellist, linkedin, twitter, field, format_number, aboutme
from clearbit.slack.helpers import facebook


class Company(object):

    def __init__(self, company_dict):
        self.company_dict = company_dict

    def as_dict(self, options=None):
        data = {
            'author_name': self.company_dict.get('name'),
            'author_icon': self.company_dict.get('logo'),
            'text': self.company_dict.get('description'),
            'color': self.color,
            'fields': self.fields
        }
        return data

    @property
    def color(self):
        return 'good'

    @property
    def fields(self):
        fields = [
            self.website,
            self.raised,
            self.location,
            self.company_type,
            self.employees,
            angellist(self.company_dict.get('angellist', {})),
            facebook(self.company_dict.get('facebook', {})),
            linkedin(self.company_dict.get('linkedin', {})),
            twitter(self.company_dict.get('twitter', {})),
        ]
        fields = [f for f in fields if f]
        return fields

    @property
    def company_type(self):
        return field('Type', self.company_dict.get('type', ''))

    @property
    def employees(self):
        metrics = self.company_dict.get('metrics', {})
        return field('Employees', format_number(metrics.get('', '')))

    @property
    def location(self):
        return field('Location', self.company_dict.get('location', ''))

    @property
    def website(self):
        return field('Website', self.company_dict.get('url', ''))

    @property
    def raised(self):
        metrics = self.company_dict.get('metrics', {})
        raised = format_number(metrics.get('raised', ''))
        return field('Raised', "${}".format(raised))


class Person(object):

    def __init__(self, person_dict):
        self.person_dict = person_dict

    def as_dict(self, options=None):
        data = {
            'color': self.color,
            'fields': self.fields
        }
        return data

    @property
    def fields(self):
        fields = [
            self.bio,
            self.email,
            self.employment_info,
            self.position,
            self.location,
            aboutme(self.person_dict.get('aboutme', {})),
            angellist(self.person_dict.get('angellist', {})),
            facebook(self.person_dict.get('facebook', {})),
            linkedin(self.person_dict.get('linkedin', {})),
            twitter(self.person_dict.get('twitter', {})),
        ]
        fields = [f for f in fields if f]
        return fields

    @property
    def bio(self):
        return field('Bio', self.person_dict.get('bio', ''), False)

    @property
    def email(self):
        return field('Email', self.person_dict.get('email', ''))

    @property
    def employment_info(self):
        employment = self.person_dict.get('employment', {})
        return field('Employment', employment.get('name', ''))

    @property
    def position(self):
        employment = self.person_dict.get('employment', {})
        return field('Position', employment.get('title', ''))

    @property
    def location(self):
        return field('Location', self.person_dict.get('location', ''))

    @property
    def color(self):
        return 'good'
