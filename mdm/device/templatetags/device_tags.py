"""
Template tags to be used when showing devices.
"""

import logging

from django.utils import timezone
from django import template

register = template.Library()
logger = logging.getLogger(__name__)

@register.filter
def minutes_ago(time, minutes):
    """
    Template filter to calculate if the time is less than a number of minutes ago.
    """
    return time + timezone.timedelta(minutes=minutes) > timezone.now()

