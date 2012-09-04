from django import template
from django.template.loader import render_to_string
from ..models import TalentPeople

register = template.Library()
@register.inclusion_tag('talentpool/home_mosaic.html')
def show_talent_mosaic(people_nb):
    people_nb = int(people_nb)
    return {'people' : TalentPeople.objects.order_by("?")[:people_nb]}
    