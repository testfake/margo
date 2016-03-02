from random import randint
from blog.models import Tag
from django import template

register = template.Library()

def tags_menu():
	tags = Tag.objects.all()
	colors = ['green', 'blue', 'red']
	return {'tags': tags, 'colors': colors}

register.inclusion_tag('blog/tags/tags-menu.html')(tags_menu)