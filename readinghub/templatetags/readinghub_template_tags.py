from django import template
from readinghub.models import Category, Book, Event
register = template.Library()

@register.inclusion_tag('readinghub/base_event.html')
def get_event_list():
    event_list = Event.objects.all()
    return {'event_list': event_list}

