from django import template
from ..models import Ads


register = template.Library()

@register.simple_tag
def getads():
    return Ads.objects.all()