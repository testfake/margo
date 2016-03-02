from random import randint
from django import template

register = template.Library()

@register.assignment_tag()
def random_pos():
    return {'top': randint(1, 5)*20, 'left': randint(0, 3)*20}